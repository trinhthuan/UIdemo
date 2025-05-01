import os
import sys

# các đối tượng trên giao diện
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QTableWidget, \
    QTableWidgetItem, QLabel, QCheckBox, QProgressBar, QMessageBox, QHeaderView

#Chạy mutil thread
from PyQt6.QtCore import QThread, pyqtSignal, Qt



#### === Class giao diện
class PyQty_UI_Demo(QWidget):
    ### Hàm constructor, thực thi khi classdduowcjc gọi
    def __init__(self):
        super().__init__()
        self.initUI()

        ## Khởi tạo các biến của Class...



### Hàm thực hien thiết kế giao diện
    def initUI(self):

        #### Style cho các đối tượng giao diên
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover {
                background-color: #69a049;
            }
        """)

        # Kích hoạt kéo thả
        self.setAcceptDrops(True)

        # Thiết lập vị trí và kích thước cửa sổ.
        self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle("TrinhThuan")

    # Tạo layout
        layout = QVBoxLayout()

    # Tạo nút bấm
        self.button = QPushButton("Nhấn tôi!")
        self.button.clicked.connect(self.show_message)  # Kết nối sự kiện
        layout.addWidget(self.button)
    #Tạo Label
        self.label = QLabel("Chọn thư mục để kiểm tra dung lượng các file")
        self.label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(self.label)





        self.setLayout(layout)




    '''Sự kiện khi kéo file vào'''
    def dragEnterEvent(self, event):
        """ Khi người dùng kéo một thư mục vào giao diện """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        """ Khi người dùng thả thư mục vào giao diện """
        urls = event.mimeData().urls()
        if urls:
            folder_path = urls[0].toLocalFile()
            if os.path.isdir(folder_path):  # Kiểm tra xem có phải thư mục không
                self.label.setText(f"Thư mục đã chọn: {folder_path}")






####=== Các Function trong Class của giao diện
    def show_message(self):
        QMessageBox.information(self, "Thông báo", "Bạn đã nhấn nút!")

####=== Hàm Main
if __name__ == "__main__":
    app = QApplication(sys.argv)  #Quản lý vòng đời của ứng dụng.
    window = PyQty_UI_Demo()
    window.show()
    sys.exit(app.exec())  #Chạy vòng lặp sự kiện của ứng dụng.
