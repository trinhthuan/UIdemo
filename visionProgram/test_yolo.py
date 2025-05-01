import cv2
from ultralytics import YOLO

# Load mô hình YOLOv8 đã huấn luyện
model = YOLO(r"D:\Python\datatrain_thuan\pythonProject\runs\detect\train\weights\best.pt")  # Đổi path nếu cần

# Mở webcam (0 là webcam mặc định, nếu có nhiều camera thì đổi thành 1, 2,...)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Dừng nếu không nhận được frame từ webcam

    # Chạy mô hình YOLO trên frame hiện tại
    results = model(frame)

    # Vẽ bounding box lên ảnh
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lấy tọa độ bounding box
            conf = box.conf[0]  # Lấy độ tin cậy
            cls = int(box.cls[0])  # Lấy class ID

            # Vẽ bounding box lên ảnh
            label = f"{model.names[cls]} {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y2-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Hiển thị ảnh với kết quả YOLO
    cv2.imshow("YOLOv8 Webcam", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
