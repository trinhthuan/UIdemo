# serial_port.py
import serial
import serial.tools.list_ports


class SerialPort:
    def __init__(self, baudrate=9600, timeout=0.1):
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def list_ports(self):
        """Liệt kê các cổng serial đang khả dụng."""
        return [port.device for port in serial.tools.list_ports.comports()]

    def connect(self, port_name):
        """Kết nối tới cổng serial."""
        if self.serial and self.serial.is_open:
            self.serial.close()
        try:
            self.serial = serial.Serial(port_name, self.baudrate, timeout=self.timeout)
            print(f"✅ Connected to {port_name}")
            return True
        except serial.SerialException as e:
            print(f"❌ Serial connection error: {e}")
            return False

    def disconnect(self):
        """Ngắt kết nối khỏi cổng serial."""
        if self.serial and self.serial.is_open:
            self.serial.close()
            print("🔌 Disconnected.")

    def is_connected(self) -> bool:
        """Kiểm tra trạng thái kết nối."""
        return self.serial is not None and self.serial.is_open

    def read_line(self) -> str:
        """Đọc một dòng dữ liệu nếu có."""
        if self.is_connected() and self.serial.in_waiting > 0:  # in_waiting Số byte đang chờ để được đọc trong buffer đầu vào của cổng serial.
            try:
                return self.serial.readline().decode(errors='ignore').strip()
            except Exception as e:
                print(f"⚠️ Error reading from serial: {e}")
        return ""

    def write(self, data: str):
        """Gửi dữ liệu ra cổng serial."""
        if self.is_connected():
            try:
                self.serial.write(data.encode())
            except Exception as e:
                print(f"⚠️ Error sending data: {e}")
