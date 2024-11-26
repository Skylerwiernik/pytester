from cyberonics_py import Robot, Device, DeviceProperty
import cyberonics_py.graphics as graphics
from cyberonics_py.graphics import Color, Alignment


class Motor(Device):
    def __init__(self, name: str):
        self.speed = DeviceProperty(0., mutable=True)
        self.isEnabled = DeviceProperty(False, mutable=True)
        self.status_color = DeviceProperty(Color.DANGER, mutable=True)

        self.speed.add_listener(lambda speed: print("Speed set to ", speed.value))
        self.isEnabled.add_listener(self.__update_status_color)
        self.status_color.add_listener(lambda color: print("Color set to ", color.value))

        super().__init__(f"{self.__class__.__name__}--{name}", [self.speed, self.isEnabled, self.status_color], self.__make_device_cell(name))

    def __update_status_color(self, enabled: DeviceProperty):
        self.status_color.value = Color.SUCCESS if enabled.value else Color.DANGER

    def __on_button(self):
        print("Button pressed!")
        self.dot.flash()

    def __make_device_cell(self, name):
        self.dot = graphics.StatusDot(self.status_color, alignment=graphics.Alignment.RIGHT)
        header = graphics.HeaderText(name)
        bodyText = graphics.BodyText("Motor", color=graphics.Color.SECONDARY)
        switch = graphics.Switch(managed_property=self.isEnabled)
        button = graphics.Button("Flash", self.__on_button, text_color=graphics.Color.hex("#f542a7"))
        slider = graphics.Slider(managed_property=self.speed, min_value=0., max_value=1., step=0.1)
        subText = graphics.SubText("Speed", color=graphics.Color.SECONDARY, alignment=Alignment.CENTER)
        return graphics.GraphicCell([self.dot, header, bodyText, switch, button, slider, subText])




class Ava(Robot):
    def __init__(self):
        self.motor1 = Motor("Left Motor")
        self.motor2 = Motor("Right Motor")
        super().__init__([self.motor1, self.motor2])