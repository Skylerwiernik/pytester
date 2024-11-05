from cyberonics_py import Robot, Device, DeviceProperty
import cyberonics_py.graphics as graphics

class Motor(Device):
    def __init__(self, name: str):
        self.speed = DeviceProperty(0., mutable=True)
        header = graphics.HeaderText(name)
        slider = graphics.Slider(managed_property=self.speed, min_value=0., max_value=1., step=0.1)
        self.speed.add_listener(lambda speed: self.set_speed(speed))
        self.device_cell = graphics.GraphicCell([header, slider])
        super().__init__([self.speed], self.device_cell)

    def set_speed(self, speed: DeviceProperty[float]):
        print(f"Setting motor speed to", speed.value)
        # TODO: Implement motor speed control logic here


class Ava(Robot):
    def __init__(self):
        self.motor1 = Motor("Motor 1")
        self.motor2 = Motor("Motor 2")
        super().__init__([self.motor1, self.motor2])