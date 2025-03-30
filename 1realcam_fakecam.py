import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QGridLayout
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QThread, pyqtSignal

# Camera thật
REAL_CAMERA_ID = 0


class CameraThread(QThread):
    frame_captured = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(REAL_CAMERA_ID)
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame_captured.emit(frame)

    def stop(self):
        self.running = False
        self.cap.release()
        self.quit()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Camera Feed")
        self.setGeometry(100, 100, 1200, 800)

        layout = QGridLayout()
        self.image_labels = {}

        for cam_id in range(4):  # 1 camera thật, 3 camera giả lập
            label = QLabel(self)
            label.setFixedSize(400, 400)
            self.image_labels[cam_id] = label
            layout.addWidget(label, cam_id // 2, cam_id % 2)  # Sắp xếp 2 trên, 2 dưới

        self.setLayout(layout)

        # Khởi tạo luồng camera thật
        self.camera_thread = CameraThread()
        self.camera_thread.frame_captured.connect(self.update_frames)
        self.camera_thread.start()

    def update_frames(self, frame):
        frames = {
            0: frame,  # Camera thật
            1: cv2.flip(frame, 1),  # Lật ngang
            2: cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE),  # Xoay 90 độ
            3: cv2.GaussianBlur(frame, (15, 15), 0)  # Làm mờ
        }

        for cam_id, processed_frame in frames.items():
            height, width, channel = processed_frame.shape
            bytes_per_line = 3 * width
            qimg = QImage(processed_frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(qimg)
            self.image_labels[cam_id].setPixmap(pixmap)

    def closeEvent(self, event):
        self.camera_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
