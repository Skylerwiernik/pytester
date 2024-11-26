from cyberonics_py import Robot, Device, DeviceProperty
import cyberonics_py.graphics as graphics

class ExampleRobot(Robot):
    def __init__(self):
        self.device1 = ExampleDevice()
        self.device2 = ExampleDevice()
        super().__init__([self.device1, self.device2])



class ExampleDevice(Device):
    def __init__(self):
        self.isEnabled = DeviceProperty(False, mutable=True)
        self.status_color = DeviceProperty(graphics.Color.DANGER, mutable=True)

        super().__init__([self.isEnabled, self.status_color], self.__make_graphic_cell())

    def __make_graphic_cell(self):
        def update_status_color(enabled):
            self.status_color.value = graphics.Color.SUCCESS if enabled else graphics.Color.DANGER

        self.isEnabled.add_listener(update_status_color)
        self.dot = graphics.StatusDot(self.status_color, alignment=graphics.Alignment.CENTER)
        self.switch = graphics.Switch(managed_property=self.isEnabled)
        return graphics.GraphicCell([self.dot, self.switch])