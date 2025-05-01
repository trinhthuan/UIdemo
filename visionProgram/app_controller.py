
# from ultralytics import YOLO
# class DummyYolo:
#     def predict(self, frame):
#         self.model = YOLO(r"D:\Python\datatrain_thuan\pythonProject\runs\detect\train\weights\best.pt")
#         results = self.model(frame)
#         return results

#####################################################


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
        time.sleep(5)  # Giả lập xử lý
        self.result_ready.emit({"status": "OK", "info": "Processed!"})



###########################################################################


from PySide6.QtCore import Qt, QObject,  QTimer, Signal
from PySide6.QtStateMachine import QStateMachine, QEventTransition, QState
import numpy as np
from camera_control import CameraThread
import cv2
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
        # Khởi tạo camera thread
        self.camera_thread = CameraThread(camera_id=0)  # Cam start
        self.camera_thread.start()
        self.camera_thread.frame_ready.connect(self.handle_frame)

    def handle_frame(self, frame):
        self.frame = frame
        if self.state_machine.configuration().pop() == self.state_waiting:
            self.window.update_image(self.frame)
            results = self.yolo.predict(self.frame)
            if len(results[0].boxes) > 0:
                for result in results:
                    for box in result.boxes:
                        x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ bounding box
                        conf = box.conf[0]  # Lấy độ tin cậy
                        cls = int(box.cls[0])  # Lấy class ID

                        # Vẽ bounding box lên ảnh
                        # label = f"{self.yolo.names[cls]} {conf:.2f}"
                        cv2.rectangle(self.frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                        # cv2.putText(self.frame, label, (x1, y2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
                        # print("###################", label)
                self.window.display_detect_result(self.frame, results)
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
        self.window.update_image(self.frame)
        results = self.yolo.predict(self.frame)
        if len(results[0].boxes) == 0:
            self.signal_manager.object_removed.emit()
        else:
            QTimer.singleShot(500, self.check_removed)

    def handle_task_result(self, result):
        self.window.display_task_result(result)
        self.signal_manager.processing_done.emit()