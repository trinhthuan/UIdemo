import json
import os
import sys
import time
import cv2
import numpy as np
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QMessageBox
)
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QPixmap, QImage

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("num_duts", 4)
    return 4

def save_config(num_duts):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"num_duts": num_duts}, f, indent=4)


# Camera thread - nhận thâm số truyền vào cam-index
class CameraThread(QThread):
    frameCaptured = Signal(np.ndarray)  # frame được dùng làm signal truyền về main thread
    statusChanged = Signal(str) # status được dùng làm signal truyền về main thread

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self.running = False

    def run(self):
        cap = cv2.VideoCapture(self.camera_index)
        if not cap.isOpened():
            self.statusChanged.emit("Camera Error")
            return

        self.running = True
        self.statusChanged.emit("Running")  #truyền signal về main thread

        while self.running:
            ret, frame = cap.read()
            if ret:
                self.frameCaptured.emit(frame) #truyền signal về main thread
            time.sleep(0.03)

        cap.release()
        self.statusChanged.emit("Stopped")

    def stop(self):
        self.running = False


#Class DUT - Thể hiện đầy đủ các phần của 1 DUT
class DUTWidget(QWidget):
    def __init__(self, dut_name, camera_index):
        super().__init__()
        self.dut_name = dut_name
        self.camera_index = camera_index
        self.camera_thread = None

        self.layout = QVBoxLayout()  #Khởi tạo Box chứa toàn bo các đối tượng của DUT, sắp xếp dạng Vertical layout

        self.title = QLabel(f"{self.dut_name}")
        self.title.setAlignment(Qt.AlignCenter)
        self.status_label = QLabel("Status: Idle")
        self.image_label = QLabel()
        self.image_label.setFixedSize(320, 240)
        self.image_label.setStyleSheet("background-color: black;")

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")

        self.layout.addWidget(self.title)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)

        self.setLayout(self.layout) #gán cái layout bạn vừa xây dựng vào widget cha (ở đây self là cửa sổ hoặc widget của bạn).

        self.start_button.clicked.connect(self.start_camera)
        self.stop_button.clicked.connect(self.stop_camera)

    def start_camera(self):
        if self.camera_thread is None:
            self.camera_thread = CameraThread(self.camera_index)
            self.camera_thread.frameCaptured.connect(self.update_image)
            self.camera_thread.statusChanged.connect(self.update_status)
            self.camera_thread.start()

    def stop_camera(self):
        if self.camera_thread is not None:
            self.camera_thread.stop()
            self.camera_thread.wait()
            self.camera_thread = None

    @Slot(np.ndarray)
    def update_image(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img).scaled(320, 240, Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)

    @Slot(str) #đăng ký hàm update_status là một slot. slot này chỉ nhận kiểu dữ liệu str — việc này giúp kiểm tra kiểu an toàn, tối ưu hiệu suất và giúp cơ chế signal-slot chạy nhanh hơn.
    def update_status(self, status):
        self.status_label.setText(f"Status: {status}")

    def closeEvent(self, event):
        self.stop_camera()
        super().closeEvent(event)


#Giao diện chính
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multi-DUT Camera Manager")

        self.num_duts = load_config()

        self.main_layout = QVBoxLayout() #Layout vertical chính
        self.grid_layout = QGridLayout() #Layout Grid dùng để chưa các DUT

        self.control_layout = QHBoxLayout() #Layout horizontal chứa label và texbox chọn config
        self.num_duts_input = QLineEdit(str(self.num_duts))
        self.save_config_button = QPushButton("Save Config")
        self.restart_button = QPushButton("Restart App")
        self.control_layout.addWidget(QLabel("Number of DUTs:"))  # Sắp xếp các đối tượng vào layout control
        self.control_layout.addWidget(self.num_duts_input)
        self.control_layout.addWidget(self.save_config_button)
        self.control_layout.addWidget(self.restart_button)

        self.main_layout.addLayout(self.control_layout)  #Sắp xếp control vào main
        self.main_layout.addLayout(self.grid_layout) #Sắp xếp grid DUT vào main

        self.setLayout(self.main_layout)  #Hiển thị tất cả vào Widget - đóng gói tất cả widget con vào widget cha và Qt sẽ tự tính toán việc sắp xếp, co giãn, v.v.

        self.dut_widgets = []

        self.init_duts()

        self.save_config_button.clicked.connect(self.save_config)
        self.restart_button.clicked.connect(self.restart_app)

    def init_duts(self):
        for widget in self.dut_widgets:
            widget.setParent(None)
        self.dut_widgets.clear()

        for i in range(self.num_duts):
            dut_widget = DUTWidget(f"DUT_{i}", i)
            self.dut_widgets.append(dut_widget)
            row = i // 2
            col = i % 2
            self.grid_layout.addWidget(dut_widget, row, col)

    def save_config(self):
        try:
            new_num = int(self.num_duts_input.text())
            if new_num < 1:
                raise ValueError
            save_config(new_num)
            QMessageBox.information(self, "Saved", "Config saved! Press 'Restart App' to apply changes.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number (>0)!")

    def restart_app(self):
        # Lệnh chạy lại chính chương trình
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def closeEvent(self, event):
        for dut_widget in self.dut_widgets:
            dut_widget.stop_camera()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
