from cyberonics_py import Robot, Device, DeviceProperty
import cyberonics_py.graphics as graphics
from devices.example_device import ExampleDevice
from targets.ExampleTarget import ExampleTarget


class ExampleRobot(Robot):
    def __init__(self):
        self.device1 = ExampleDevice()
        self.device2 = ExampleDevice()
        self.targets = [ExampleTarget(self)]
        super().__init__([self.device1, self.device2], self.targets)

