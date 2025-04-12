from cyberonics_py import Robot

from target import TestTarget, SecondTarget
from motor import Motor




class Ava(Robot):
    def __init__(self):
        self.motor1 = Motor("Left Motor")
        self.motor2 = Motor("Right Motor")
        self.target = TestTarget(self)
        self.target2 = SecondTarget(self)
        super().__init__([self.motor1, self.motor2], [self.target, self.target2])