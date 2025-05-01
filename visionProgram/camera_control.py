import numpy as np
from PySide6.QtCore import QThread, Signal
import cv2

class CameraThread(QThread):
    frame_ready = Signal(np.ndarray)

    def __init__(self, camera_id=0, parent=None):
        super().__init__(parent)
        self.camera_id = camera_id
        self._running = False

    def run(self):
        cap = cv2.VideoCapture(self.camera_id)
        self._running = True
        while self._running:
            ret, frame = cap.read()
            if ret:
                self.frame_ready.emit(frame)
            self.msleep(100)  # ~33fps

        cap.release()

    def stop(self):
        self._running = False
        self.quit()
        self.wait()