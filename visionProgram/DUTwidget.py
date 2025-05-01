import os
import time
from datetime import datetime

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal, Slot, QObject
from PySide6.QtGui import QImage, QPixmap, Qt, QColor
from PySide6.QtStateMachine import QStateMachine, QState
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidgetItem
from my_ui_dut_widget import Ui_Form

# camera_worker.py
from PySide6.QtCore import QObject, Signal
# import cv2
# import time
from ultralytics import YOLO

model = YOLO(r"D:\Python\datatrain_thuan\pythonProject\runs\detect\train\weights\best.pt")


class CameraWorker(QObject):
    object_detected = Signal()
    frame_ready = Signal(object)  # Ảnh live
    detected_frame_ready = Signal(object)  # Ảnh có bounding box
    object_cleared = Signal()

    def __init__(self, camera_index):
        super().__init__()
        self.camera_index = camera_index
        self.running = False
        self.last_detected_frame = None
        self.cap = None
        self._stop_flag = False
        self.missed_counter = 0
        self._object_present = False

    def run(self):
        self.cap = cv2.VideoCapture(self.camera_index)  # Hoặc CAP_MSMF nếu cần
        if not self.cap.isOpened():
            print(f"❌ Cannot open camera index {self.camera_index}")
            return

        frame_couter = 0
        while not self._stop_flag:
            if not self.running:
                time.sleep(0.1)
                continue

            ret, frame = self.cap.read()
            if not ret:
                continue
            frame_couter += 1

            if frame_couter >= 10:
                frame_couter = 0
                detection = self.detect_object(frame.copy())
                if detection is not None:
                    if not self._object_present:
                        self._object_present = True
                        self.last_detected_frame = frame.copy()
                        self.detected_frame_ready.emit(detection)
                        self.object_detected.emit()
                        self.running = False  # stop loop until next start
                        self.missed_counter = 0  # reset
                else:
                    # self.frame_ready.emit(frame)
                    if self._object_present:
                        self.missed_counter += 1
                        if self.missed_counter >= 5:
                            self._object_present = False
                            self.object_cleared.emit()
                            self.frame_ready.emit(frame)
                            # self.missed_counter = 0  # reset
            else:
                if not self._object_present:
                    self.frame_ready.emit(frame)

            time.sleep(0.1)

    def detect_object(self, frame):
        results = model(frame)
        if len(results[0].boxes) > 0:
            for result in results:
                for box in result.boxes:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ bounding box
                    conf = box.conf[0]  # Lấy độ tin cậy
                    cls = int(box.cls[0])  # Lấy class ID

                    # Vẽ bounding box lên ảnh
                    label = f"{model.names[cls]} {conf:.2f}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y2 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            return frame
        else:
            return None

    def start_detection(self):
        self.running = True

    def stop(self):
        self._stop_flag = True
        if self.cap and self.cap.isOpened():
            self.cap.release()


###########################################################################################

# processor_worker.py
from PySide6.QtCore import QObject, Signal
import time
import cv2


class ProcessorWorker(QObject):
    processing_done = Signal()
    result_ready = Signal(object)
    start_processing = Signal(object)  #


    def __init__(self):
        super().__init__()
        self.start_processing.connect(self.process_frame)  #Nhận tín hiệu từ Main thread

    def run(self):
        pass  # No loop needed

    def process_frame(self, frame):
        # Simulate processing by drawing rectangle on detected frame
        h, w, _ = frame.shape
        result = frame.copy()
        cv2.rectangle(result, (10, 10), (w - 10, h - 10), (0, 0, 255), 2)
        time.sleep(3)  # Simulate processing delay
        self.result_ready.emit(result)
        self.processing_done.emit()


#############################################################################################

class DUTWidget(QWidget):
    # Start Signal
    start_signal = Signal()
    processing_done_signal = Signal()

    def __init__(self, dut_name: str, camera_id: int):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.dut_name = dut_name
        self.camera_id = camera_id
        self.start = False

        # Gán tên DUT
        self.ui.dutNameLabel.setText(self.dut_name)

        # Threads & workers
        self.camera_thread = QThread()
        self.camera_worker = CameraWorker(self.camera_id)
        self.camera_worker.moveToThread(self.camera_thread)
        self.camera_thread.started.connect(self.camera_worker.run)

        self.processor_thread = QThread()
        self.processor_worker = ProcessorWorker()
        self.processor_worker.moveToThread(self.processor_thread)
        self.processor_thread.started.connect(self.processor_worker.run)

        # State Machine
        self.machine = QStateMachine(self)

        self.state_idle = QState()
        self.state_detecting = QState()
        self.state_processing = QState()
        self.state_done = QState()
        self.state_waiting_clear = QState()

        self.state_idle.addTransition(self.start_signal, self.state_detecting)
        self.state_detecting.addTransition(self.camera_worker.object_detected, self.state_processing)
        self.state_processing.addTransition(self.processor_worker.processing_done, self.state_done)
        self.state_done.addTransition(self.processing_done_signal, self.state_waiting_clear)
        self.state_waiting_clear.addTransition(self.camera_worker.object_cleared, self.state_idle)

        self.state_idle.entered.connect(self.start_loop)
        self.state_detecting.entered.connect(self.start_detection)
        self.state_processing.entered.connect(self.start_processing)
        self.state_done.entered.connect(self.processing_done)
        self.state_waiting_clear.entered.connect(self.wait_for_clear)

        self.machine.addState(self.state_idle)
        self.machine.addState(self.state_detecting)
        self.machine.addState(self.state_processing)
        self.machine.addState(self.state_done)
        self.machine.addState(self.state_waiting_clear)
        self.machine.setInitialState(self.state_idle)
        self.machine.start()

        self.camera_worker.frame_ready.connect(self.update_image)
        self.processor_worker.result_ready.connect(self.update_result_image)
        self.camera_worker.detected_frame_ready.connect(self.update_image)  # hiển thị ảnh có bounding box

        self.camera_thread.start()
        self.processor_thread.start()

    def start_loop(self):
        self.update_status("Idle...")
        if self.start:
            self.start_signal.emit()
  

    def start_detection(self):
        self.update_status("Detecting...")
        # ✅ Gửi tín hiệu khởi động lại camera thread
        if self.camera_thread.isRunning():
            self.camera_worker.start_detection()
        else:
            self.camera_thread.start()

    def stop_detection(self):
        self.camera_worker.stop()
        self.update_status("Stopped")

    def start_processing(self):
        self.update_status("Processing...")
        frame = self.camera_worker.last_detected_frame
        # self.update_image(frame)  # Hiển thị ảnh detect tạm thời
        self.processor_worker.start_processing.emit(frame)  # Gửi frame để xử lý ở thread riêng

    def processing_done(self):
        self.update_status("Processing done")
        logger = TestLoggerCSV(dut_name="DUT0", version="v1.2.3", ip_address="123.123")
        test_data = [
            {"item": "Voltage", "measure": "3.29", "result": "PASS", "lsl": "3.20", "usl": "3.40"},
            {"item": "Current", "measure": "1.01", "result": "PASS", "lsl": "0.95", "usl": "1.05"},
            {"item": "Temp", "measure": "41.2", "result": "FAIL", "lsl": "30.0", "usl": "40.0"}
        ]

        logger.write_test_log(test_data, test_result="FAIL")
        self.display_test_result_on_table(self.ui.tableWidget, test_data)
        self.processing_done_signal.emit()

    def wait_for_clear(self):
        self.update_status("Waiting for clear...")
        # ✅ Gửi tín hiệu khởi động lại camera thread
        if self.camera_thread.isRunning():
            self.camera_worker.start_detection()
        else:
            self.camera_thread.start()

    def update_result_image(self, result_frame):
        rgb_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img).scaled(320, 240, Qt.KeepAspectRatio)
        self.ui.dutImageLabel.setPixmap(pixmap)



    # @Slot(np.ndarray)
    def update_image(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_frame.shape
        bytes_per_line = ch * w
        qt_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_img).scaled(320, 240, Qt.KeepAspectRatio)
        self.ui.dutImageLabel.setPixmap(pixmap)

    # @Slot(str)  # đăng ký hàm update_status là một slot. slot này chỉ nhận kiểu dữ liệu str — việc này giúp kiểm tra kiểu an toàn, tối ưu hiệu suất và giúp cơ chế signal-slot chạy nhanh hơn.
    def update_status(self, status):
        self.ui.dutStatusLabel.setText(f"Status: {status}")
        self.stage_log(status)

    def closeEvent(self, event):
        # Stop camera worker
        self.camera_worker.stop()
        if hasattr(self.camera_worker, 'cap') and self.camera_worker.cap.isOpened():
            self.camera_worker.cap.release()

        self.camera_thread.quit()
        self.camera_thread.wait()

        self.processor_thread.quit()
        self.processor_thread.wait()
        event.accept()


    ##Ghi Stage log
    def stage_log(self, text: str):
        timestamp = datetime.now()
        time_str = timestamp.strftime("[%Y-%m-%d %H:%M:%S]")
        log_entry = f"{self.dut_name} {time_str} {text}"

        # Hiển thị lên GUI
        self.ui.state_textBrowser.append(log_entry)

        # Tạo tên file theo ngày và DUT number
        log_filename = timestamp.strftime(f"log_{self.dut_name}_%Y-%m-%d.txt")

        # Nếu file chưa tồn tại, tạo và ghi tiêu đề (nếu muốn)
        if not os.path.exists(log_filename):
            with open(log_filename, "w", encoding="utf-8") as f:
                f.write(log_entry + "\n")

        # Ghi log vào file theo ngày
        with open(log_filename, "a", encoding="utf-8") as f:
            f.write(log_entry + "\n")

    ##Hiển thị log lên giao diện
    def display_test_result_on_table(self,table_widget, test_items: list):
        table_widget.clearContents()
        table_widget.setRowCount(len(test_items))
        table_widget.setColumnCount(5)
        table_widget.setHorizontalHeaderLabels(["Item", "Measure", "LSL", "USL", "Result"])

        for row, item in enumerate(test_items):
            for col, key in enumerate(["item", "measure", "lsl", "usl", "result"]):
                value = str(item[key])
                cell = QTableWidgetItem(value)

                # Tô màu theo kết quả PASS/FAIL
                if key == "result":
                    if value.upper() == "PASS":
                        cell.setBackground(QColor("lightgreen"))
                    elif value.upper() == "FAIL":
                        cell.setBackground(QColor("red"))
                        cell.setForeground(QColor("black"))
                table_widget.setItem(row, col, cell)

        table_widget.resizeColumnsToContents()


#####################################################################################
##Class Ghi log CSV
import os
import csv
from datetime import datetime

class TestLoggerCSV:
    def __init__(self, dut_name: str, version: str, ip_address: str):
        self.dut_name = dut_name
        self.version = version
        self.ip_address = ip_address

    def get_log_filename(self):
        date_str = datetime.now().strftime("%Y-%m-%d")
        return f"log_test_{self.dut_name}_{date_str}.csv"

    def write_test_log(self, test_items: list, test_result: str):
        """
        test_items: List[dict] with keys: item, measure, result, lsl, usl
        test_result: "PASS" | "FAIL"
        """
        timestamp = datetime.now()
        date_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        time_str = timestamp.strftime("%H:%M:%S")
        filename = self.get_log_filename()

        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)

            # === MỞ ĐẦU ===
            writer.writerow(["===>>> TEST START <<<==="])
            writer.writerow(["IP", self.ip_address])
            writer.writerow(["Version", self.version])
            writer.writerow(["DUT", self.dut_name])
            writer.writerow(["Date", date_str])
            writer.writerow([])

            # === BODY ===
            writer.writerow(["Item", "Measure", "Result", "LSL", "USL"])
            for item in test_items:
                writer.writerow([
                    item["item"],
                    item["measure"],
                    item["result"],
                    item["lsl"],
                    item["usl"]
                ])
            writer.writerow([])

            # === KẾT THÚC ===
            writer.writerow(["Final Result", test_result])
            writer.writerow(["Test Time", time_str])
            writer.writerow(["===>>> TEST END <<<==="])
            writer.writerow([])  # Dòng trắng cách giữa các log


