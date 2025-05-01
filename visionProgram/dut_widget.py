import time

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal, Slot, QObject
from PySide6.QtGui import QImage, QPixmap, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from my_ui_dut_widget import Ui_Form

# Camera thread - nhận thâm số truyền vào cam-index
class CameraThread(QObject):
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


#########################################################################################

class DUTWidget(QWidget):
    def __init__(self, dut_name: str, camera_id: int):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.dut_name = dut_name
        self.camera_id = camera_id
        self.camera_thread = None

        # Gán tên DUT
        self.ui.dutNameLabel.setText(self.dut_name)






    def start_camera(self):
        if self.camera_thread is None:
            self.camera_thread = CameraThread(self.camera_id)
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
        #
        self.ui.dutImageLabel.setPixmap(pixmap)

    @Slot(str) #đăng ký hàm update_status là một slot. slot này chỉ nhận kiểu dữ liệu str — việc này giúp kiểm tra kiểu an toàn, tối ưu hiệu suất và giúp cơ chế signal-slot chạy nhanh hơn.
    def update_status(self, status):
        self.ui.dutStatusLabel.setText(f"Status: {status}")

    def closeEvent(self, event):
        self.stop_camera()
        super().closeEvent(event)
