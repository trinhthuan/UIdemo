'''
demo_app/
│
├── main.py
├── app_controller.py
├── ui_mainwindow.py
├── dummy_yolo.py
└── task_thread.py
'''


###1️⃣ ui_mainwindow.py – giao diện + log + khung ảnh

from PySide6.QtWidgets import QMainWindow, QLabel, QTextEdit, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt
from PySide6.QtStateMachine import QStateMachine, QEventTransition, QState
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Vision State Machine Demo")
        self.image_label = QLabel()
        self.image_label.setFixedSize(640, 480)
        self.image_label.setStyleSheet("background-color: black;")

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.log_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def display_frame(self, frame: np.ndarray):
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)

    def display_detect_result(self, frame, result):
        self.log("✅ Object Detected!")
        self.display_frame(frame)

    def display_task_result(self, result):
        self.log(f"🛠 Task Done: {result}")

    def log(self, text: str):
        self.log_text.append(text)



###2️⃣ dummy_yolo.py – mô phỏng YOLO phát hiện ngẫu nhiên
import random
import numpy as np

class DummyYolo:
    def predict(self, frame):
        # 1/4 xác suất giả lập có vật thể
        return [("object", 100, 100, 200, 200)] if random.random() < 0.25 else []



###3️⃣ task_thread.py – giả lập xử lý tác vụ

from PySide6.QtCore import QThread, Signal
import time

class TaskThread(QThread):
    result_ready = Signal(object)

    def __init__(self):
        super().__init__()
        self._frame = None

    def process_frame(self, frame):
        self._frame = frame
        self.start()

    def run(self):
        time.sleep(1)  # Giả lập xử lý
        self.result_ready.emit({"status": "OK", "info": "Processed!"})



###4️⃣ app_controller.py – QStateMachine và xử lý

from PySide6.QtCore import Qt, QObject,  QTimer, Signal
from PySide6.QtStateMachine import QStateMachine, QEventTransition

import numpy as np

class SignalManager(QObject):
    object_detected = Signal()
    processing_done = Signal()
    object_removed = Signal()

class AppController(QObject):
    def __init__(self, window, yolo_model):
        super().__init__()
        self.window = window
        self.yolo = yolo_model
        self.task_thread = TaskThread()
        self.signal_manager = SignalManager()
        self.state_machine = QStateMachine()
        self.init_states()
        self.connect_signals()
        self.frame = None

    def start(self):
        self.state_machine.start()
        self.simulate_camera()

    def init_states(self):
        self.state_waiting = QState()
        self.state_processing = QState()
        self.state_wait_to_reset = QState()

        self.state_waiting.entered.connect(self.on_waiting)
        self.state_processing.entered.connect(self.on_processing)
        self.state_wait_to_reset.entered.connect(self.on_wait_to_reset)

        # thiết lập để khi object_detected được phát ra, state machine sẽ tự động chuyển từ state_waiting sang state_processing.
        self.state_waiting.addTransition(self.signal_manager.object_detected, self.state_processing)
        self.state_processing.addTransition(self.signal_manager.processing_done, self.state_wait_to_reset)
        self.state_wait_to_reset.addTransition(self.signal_manager.object_removed, self.state_waiting)

        self.state_machine.addState(self.state_waiting)
        self.state_machine.addState(self.state_processing)
        self.state_machine.addState(self.state_wait_to_reset)
        self.state_machine.setInitialState(self.state_waiting)

    def connect_signals(self):
        self.task_thread.result_ready.connect(self.handle_task_result)

    def simulate_camera(self):
        # Camera giả lập – mỗi 300ms chụp một frame
        self.timer = QTimer()
        self.timer.timeout.connect(self.handle_frame)
        self.timer.start(300)

    def handle_frame(self):
        self.frame = np.ones((480, 640, 3), dtype=np.uint8) * 255  # Frame trắng
        self.window.display_frame(self.frame)

        if self.state_machine.configuration().pop() == self.state_waiting:
            result = self.yolo.predict(self.frame)
            if len(result) > 0:
                self.window.display_detect_result(self.frame, result)
                self.signal_manager.object_detected.emit()

    def on_waiting(self):
        self.window.log("🔁 State: WAITING")

    def on_processing(self):
        self.window.log("🔁 State: PROCESSING")
        self.task_thread.process_frame(self.frame)

    def on_wait_to_reset(self):
        self.window.log("🔁 State: WAIT_TO_RESET")
        QTimer.singleShot(1000, self.check_removed)

    def check_removed(self):
        if len(self.yolo.predict(self.frame)) == 0:
            self.signal_manager.object_removed.emit()
        else:
            QTimer.singleShot(500, self.check_removed)

    def handle_task_result(self, result):
        self.window.display_task_result(result)
        self.signal_manager.processing_done.emit()


###5️⃣ main.py
import sys
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    controller = AppController(window, DummyYolo())
    controller.start()
    window.show()
    sys.exit(app.exec())
