import numpy as np
from PySide6.QtCore import QThread, Signal
import cv2


class YoloThread(QThread):
    result_ready = Signal(np.ndarray)

    def __init__(self, model):
        super().__init__()
        self.model = model
        self._running = True
        self.input_frame = None

    def run(self):
        while self._running:
            if self.input_frame is not None:
                result = self.process_frame(self.input_frame)
                self.result_ready.emit(result)
                self.input_frame = None  # reset để chờ frame mới
            self.msleep(10)

    def stop(self):
        self._running = False
        self.quit()
        self.wait()

    def set_frame(self, frame):
        self.input_frame = frame.copy()

    def process_frame(self, frame):
        results = self.model(frame)

        # Vẽ bounding box lên ảnh
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ bounding box
                conf = box.conf[0]  # Lấy độ tin cậy
                cls = int(box.cls[0])  # Lấy class ID

                # Vẽ bounding box lên ảnh
                label = f"{self.model.names[cls]} {conf:.2f}"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                cv2.putText(frame, label, (x1, y2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return frame  # frame đã xử lý