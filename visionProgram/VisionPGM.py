import sys
import os
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from interface_ui import *

# from Custom_Widgets.Widgets import *

from PySide6.QtCore import QTimer
#import file serial_port
from serial_port import SerialPort
#import config_manager file
from config_manager import ConfigManager




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







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


'''
(.venv) PS D:\Python\GiaoDienSample> cd D:\Python\GiaoDienSample\dashboard
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-uic interface.ui -o interface.py
(.venv) PS D:\Python\GiaoDienSample\dashboard> pyside6-rcc resources.qrc -o resources_rc.py

##QCustom
https://pypi.org/project/QT-PyQt-PySide-Custom-Widgets/

##JSON Style
https://khamisikibet.github.io/Docs-QT-PyQt-PySide-Custom-Widgets/docs/widgets/custom-slide-menu-widgets
'''