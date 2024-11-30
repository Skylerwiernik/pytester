from asyncio import sleep

from cyberonics_py import Target
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..robot import ExampleRobot

class ExampleTarget(Target):
    def __init__(self, robot: ExampleRobot):
        self.robot = robot
        self.is_running = False
        super().__init__(robot, shutdown_timeout=0.5)

    async def run(self):
        self.is_running = True
        while self.is_running:
            self.robot.device1.isEnabled.value = True
            self.robot.device2.isEnabled.value = True
            await sleep(1)
            self.robot.device1.isEnabled.value = False
            self.robot.device2.isEnabled.value = False
            await sleep(1)

    async def shutdown(self, beat):
        self.is_running = False
        while self.robot.device1.isEnabled.value or self.robot.device2.isEnabled.value:
            beat()
            await sleep(0.25)
