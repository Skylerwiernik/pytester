from cyberonics_py import Robot
from devices.example_device import ExampleDevice


class ExampleRobot(Robot):
    def __init__(self):
        self.device1 = ExampleDevice()
        self.device2 = ExampleDevice()
        super().__init__([self.device1, self.device2])