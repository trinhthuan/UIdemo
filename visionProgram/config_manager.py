import json
import os


class ConfigManager:
    def __init__(self,  config_file="config.json"):
        self.config_file = config_file
        self.config = {
            "model_file": "",
            "feature_file": "",
            "serial_port": ""
        }
        self.load_config()

    def load_config(self):
        """Tải config từ file nếu có, nếu không thì tạo file mặc định."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, "r") as f:
                    data = json.load(f)  #Đọc và chuyển nội dung JSON thành dict.
                    if isinstance(data, dict): #isinstance(data, dict) kiểm tra xem biến data có phải là kiểu dictionary hay không.
                        self.config.update(data)
                    else:
                        print("⚠️ File config không đúng định dạng, dùng cấu hình mặc định.")
            except Exception as e:
                print(f"❌ Lỗi khi load config: {e}")
        else:
            print("ℹ️ Không tìm thấy config, tạo file mới.")
            self.save_config()  # Tạo file mới từ config mặc định

    def save_config(self):
        """Lưu config hiện tại vào file."""
        try:
            with open(self.config_file, "w") as f:
                json.dump(self.config, f, indent=4)
        except Exception as e:
            print(f"❌ Lỗi khi lưu config: {e}")

    def get(self, key):
        return self.config.get(key, "")

    def set(self, key, value):
        self.config[key] = value
