
class DinoControl:
    def __init__(self):
        self.exposure = 0
    def set_exposure(self,value):
        self.exposure = value
        print(f"[DinoLite] Exposure set to: {value}")

class LightControl:
    def __init__(self):
        self.lightLevel = 0
    def set_light_level(self,value):
        self.lightLevel = value
        print(f"[Light] Light set to: {value}")