import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from pyqtdesigner_ui import Ui_MainWindow  # Import UI đã chuyển từ Qt Designer

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Gắn sự kiện (event) cho nút bấm
        self.ui.btn_tab_testing.clicked.connect(self.switch_to_tab_testing)
        self.ui.btn_tab_data.clicked.connect(self.switch_to_tab_data)
        self.ui.btn_tab_setting.clicked.connect(self.switch_to_tab_setting)



    def switch_to_tab_setting(self):
        self.ui.tab_data.setCurrentIndex(2)  # Chuyển sang Tab 3

    def switch_to_tab_data(self):
        self.ui.tab_data.setCurrentIndex(1)  # Chuyển sang Tab 2

    def switch_to_tab_testing(self):
        self.ui.tab_data.setCurrentIndex(0)  # Chuyển về Tab 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
