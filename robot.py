from cyberonics_py import Robot, Target

from target import TestTarget
from motor import Motor




class Ava(Robot):
    def __init__(self):
        self.motor1 = Motor("Left Motor")
        self.motor2 = Motor("Right Motor")
        self.target = TestTarget(self)
        super().__init__([self.motor1, self.motor2], [self.target])