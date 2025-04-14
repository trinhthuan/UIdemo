import sys
import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QThread, pyqtSignal

# Danh sách các camera ID (thay đổi theo thiết bị cụ thể)
CAMERA_IDS = [0, 1, 2, 3]


class CameraThread(QThread):
    frame_captured = pyqtSignal(np.ndarray, int) # Tín hiệu truyền ảnh và ID camera

    def __init__(self, camera_id):
        super().__init__()
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(self.camera_id)
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if ret:
                self.frame_captured.emit(frame, self.camera_id)  # Phát tín hiệu

    def stop(self):
        self.running = False
        self.cap.release()
        self.quit()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live Camera Feed")
        self.setGeometry(100, 100, 1200, 800)

        layout = QHBoxLayout()
        self.image_labels = {}
        self.threads = {}

        for cam_id in CAMERA_IDS:
            label = QLabel(self)
            label.setFixedSize(600, 400)
            self.image_labels[cam_id] = label
            layout.addWidget(label)

            thread = CameraThread(cam_id)
            thread.frame_captured.connect(self.update_frame) #Kết nối tín hiệu frame_captured của CameraThread với phương thức self.update_frame để xử lý và hiển thị hình ảnh.
            thread.start()
            self.threads[cam_id] = thread

        self.setLayout(layout)

    def update_frame(self, frame, cam_id):
        frame = self.process_frame(frame)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        qimg = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.image_labels[cam_id].setPixmap(pixmap)

    def process_frame(self, frame):
        # Chuyển sang grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:  # Lọc bỏ nhiễu nhỏ
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = f"{w}x{h} pixels"
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def closeEvent(self, event):
        for thread in self.threads.values():
            thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
