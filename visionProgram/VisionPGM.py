import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtCore import Qt

from interface_ui import *

# from Custom_Widgets.Widgets import *

from PySide6.QtCore import QTimer
#import file serial_port
from serial_port import SerialPort
#import config_manager file
from config_manager import ConfigManager

import cv2
from ultralytics import YOLO
from camera_control import CameraThread
from AI_yolo_process import YoloThread


model = YOLO(r"D:\Python\datatrain_thuan\pythonProject\runs\detect\train\weights\best.pt")


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # loadJsonStyle(self, self.ui)
        self.show()

        #Loading config file
        self.config = ConfigManager()



        #Khoi tao serial port
        self.serial_handler = SerialPort(115200, 0.1)
        self.refresh_ports()
        # Timer for reading serial
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_serial)

        self.toggle_connection()

        # Khởi tạo camera thread
        # self.camera_thread = CameraThread(camera_id=0)
        # self.camera_thread.frame_ready.connect(self.update_image)

        self.camera_thread = CameraThread(camera_id=0)   #Cam start
        self.camera_thread.frame_ready.connect(self.handle_raw_frame) #Nhận frame từ luồng camera gọi xử lý(gọi luồng AI)

        self.yolo_thread = YoloThread(model) #luồng AI process
        self.yolo_thread.result_ready.connect(self.handle_yolo_result) # sau khi xử lý sẽ trả kết quả v luồng chính


        #Tab data, load file
        self.folder_mdl_path = self.config.get("model_file") # Biến lưu path folder được chọn
        self.ui.modelFileLine.setText(self.folder_mdl_path)
        self.file_feature_path = self.config.get("feature_file") # Biến lưu path file được chọn
        self.ui.fetureFileLine.setText(self.file_feature_path)
        self.ui.selectModelBtn.clicked.connect(self.select_folder)
        self.ui.selectFeatureBtn.clicked.connect(self.select_file)
        self.ui.comboBox.currentTextChanged.connect(self.save_selected_option)
        self.comport = self.config.get("serial_port")
        self.ui.comboBox.setCurrentText(self.comport)


        # Gắn sự kiện (event) cho nút bấm chuyển Tab
        self.ui.autoTabBtn.clicked.connect(self.switch_to_tab_testing)
        self.ui.dataTabBtn.clicked.connect(self.switch_to_tab_data)
        self.ui.settingTabBtn.clicked.connect(self.switch_to_tab_setting)

        self.ui.manualBtn.clicked.connect(self.start_live)
        self.ui.uploadBtn.clicked.connect(self.stop_live)

    def stop_live(self):
        self.camera_thread.stop()
    def start_live(self):
        self.camera_thread.start()
    def switch_to_tab_setting(self):
        self.ui.tabWidget.setCurrentIndex(2)  # Chuyển sang Tab 3

    def switch_to_tab_data(self):
        self.ui.tabWidget.setCurrentIndex(1)  # Chuyển sang Tab 2

    def switch_to_tab_testing(self):
        self.ui.tabWidget.setCurrentIndex(0)  # Chuyển về Tab 1

    def save_selected_option(self, index):
        """Lưu giá trị chọn vào config."""
        selected_option = self.ui.comboBox.currentText()
        self.config.set("serial_port", selected_option)
        self.config.save_config()
        print(f"Đã lưu giá trị chọn: {selected_option}")

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Chọn thư mục")
        if folder:
            self.folder_mdl_path = folder  # Lưu vào biến
            self.ui.modelFileLine.setText(os.path.basename(folder))  # Hiển thị tên thư mục
            print(f"📁 Đã chọn: {self.folder_mdl_path}")  # In ra để kiểm tra
            self.config.set("model_file",self.folder_mdl_path)
            self.config.save_config()
    def select_file(self):
        file,_ = QFileDialog.getOpenFileName(self, "Chọn file","", "Tất cả tệp (*.*)")
        if file:
            self.file_feature_path = file  # Lưu vào biến
            self.ui.fetureFileLine.setText(os.path.basename(file))  # Hiển thị tên thư mục
            print(f"📁 Đã chọn: {self.file_feature_path}")  # In ra để kiểm tra
            self.config.set("feature_file", self.file_feature_path )
            self.config.save_config()
    def refresh_ports(self):
        ports = self.serial_handler.list_ports()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(ports)
    def toggle_connection(self):
        if self.serial_handler.is_connected():
            self.serial_handler.disconnect()
            self.timer.stop()
            self.ui.textBrowser.append(f"{self.ui.comboBox.currentText()} Disconnected")
        else:
            port = self.ui.comboBox.currentText()
            if self.serial_handler.connect(port):
                self.timer.start(100)
                self.ui.textBrowser.append(f"{port} {self.serial_handler.baudrate} Connected")
                # self.config.set("serial_port", port)
                # self.config.save_config()
            else:
                self.ui.textBrowser.append("❌ Failed to connect.")

    def read_serial(self):
        line = self.serial_handler.read_line()
        if line:
            self.ui.textBrowser.append(line)

    # Khi nhận frame từ camera
    def handle_raw_frame(self, frame):
        if not self.yolo_thread.isRunning():
            self.yolo_thread.start()
        self.yolo_thread.set_frame(frame)

    # Khi nhận frame sau YOLO
    def handle_yolo_result(self, frame):
        self.update_image(frame)

    def update_image(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)

        self.ui.viewSettingLabel.setPixmap(pixmap)
        self.ui.image1Label.setPixmap(pixmap)
        self.ui.image2Label.setPixmap(pixmap)
        self.ui.image3Label.setPixmap(pixmap)
        self.ui.image4Label.setPixmap(pixmap)



    def closeEvent(self, event):
        self.camera_thread.stop()
        self.yolo_thread.stop()
        super().closeEvent(event)







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
(.venv) PS D:\Python\GiaoDienSample> cd D:\Python\GiaoDienSample\visionProgram
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-uic interface.ui -o interface_ui.py
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-rcc resources.qrc -o resources_rc.py

##QCustom
https://pypi.org/project/QT-PyQt-PySide-Custom-Widgets/

##JSON Style
https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-slide-menu-widgets
'''