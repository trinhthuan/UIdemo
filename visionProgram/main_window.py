import sys
import os

from PySide6.QtCore import QTime, QTimer
from PySide6.QtWidgets import QWidget, QGridLayout, QApplication, QMessageBox, QFileDialog, QMainWindow
from PySide6.QtSvg import QtSvg
from my_ui_main_window import Ui_MainWindow
# from dut_widget import DUTWidget
from DUTwidget import DUTWidget
import json
from config_manager import ConfigManager
from serial_port import SerialPort
import socket

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
def get_local_ip():
    try:
        # Tạo socket tạm để lấy IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # kết nối giả tới Google DNS
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        return f"Lỗi: {e}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.num_duts = load_config()

        self.config = ConfigManager()

        self.dut_widgets = []
        # Initialize DUTs
        self.init_duts()

        # Connect button
        self.ui.autoTabBtn.clicked.connect(self.switch_to_tab_testing)
        self.ui.dataTabBtn.clicked.connect(self.switch_to_tab_data)
        self.ui.settingTabBtn.clicked.connect(self.switch_to_tab_setting)
        self.ui.saveConfigBtn.clicked.connect(self.save_config)
        self.ui.restartBtn.clicked.connect(self.restart_app)

        # Connect button
        self.ui.manualBtn.clicked.connect(self.start_all_duts)
        self.ui.uploadBtn.clicked.connect(self.stop_all_duts)

        ip_address = get_local_ip()
        self.ui.ipInfo.setText(f"• IP: {ip_address}")

        # Tạo timer cập nhật mỗi giây
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # 1000 ms = 1 giây

        self.update_time()  # cập nhật ngay lúc khởi động

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.ui.timeInfo.setText("• Time: " + current_time)

    def start_all_duts(self):
        for dut in self.dut_widgets:
            dut.start = True
            dut.start_loop()

    def stop_all_duts(self):
        for dut in self.dut_widgets:
            dut.stop_detection()

    def init_duts(self):
        for widget in self.dut_widgets:
            widget.setParent(None)
        self.dut_widgets.clear()

        for i in range(self.num_duts):
            dut_widget = DUTWidget(f"DUT_{i}", i)
            self.dut_widgets.append(dut_widget)
            row = i // 2  #Chia lấy nguyên
            col = i % 2   #Chia lấy dư
            self.ui.dutGridLayout.addWidget(dut_widget, row, col)

    def save_config(self):
        try:
            new_num = int(self.ui.dutNumber.text())
            if new_num < 1:
                raise ValueError
            save_config(new_num)
            QMessageBox.information(self, "Saved", "Config saved! Press 'Restart App' to apply changes.")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number (>0)!")

    def restart_app(self):
        # Ghi config trước khi restart
        self.save_config()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def closeEvent(self, event):
        for dut_widget in self.dut_widgets:
            dut_widget.close()
            event.accept()
        super().closeEvent(event)

        # # Loading config file
        # self.config = ConfigManager()
        #
        # # Khoi tao serial port
        # self.serial_handler = SerialPort(115200, 0.1)
        # self.refresh_ports()
        # # Timer for reading serial
        # self.timer = QTimer()
        # # self.timer.timeout.connect(self.read_serial)
        #
        # # self.toggle_connection()
        #
        # # Tab data, load file
        # self.folder_mdl_path = self.config.get("model_file")  # Biến lưu path folder được chọn
        # self.ui.modelFileLine.setText(self.folder_mdl_path)
        # self.file_feature_path = self.config.get("feature_file")  # Biến lưu path file được chọn
        # self.ui.fetureFileLine.setText(self.file_feature_path)
        # self.ui.selectModelBtn.clicked.connect(self.select_folder)
        # self.ui.selectFeatureBtn.clicked.connect(self.select_file)
        # self.ui.comboBox.currentTextChanged.connect(self.save_selected_option)
        # self.comport = self.config.get("serial_port")
        # self.ui.comboBox.setCurrentText(self.comport)








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
            self.config.set("model_file", self.folder_mdl_path)
            self.config.save_config()

    def select_file(self):
        file, _ = QFileDialog.getOpenFileName(self, "Chọn file", "", "Tất cả tệp (*.*)")
        if file:
            self.file_feature_path = file  # Lưu vào biến
            self.ui.fetureFileLine.setText(os.path.basename(file))  # Hiển thị tên thư mục
            print(f"📁 Đã chọn: {self.file_feature_path}")  # In ra để kiểm tra
            self.config.set("feature_file", self.file_feature_path)
            self.config.save_config()

    def refresh_ports(self):
        ports = self.serial_handler.list_ports()
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(ports)













if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())



