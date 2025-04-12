from cyberonics_py import Target, Robot
from multiprocessing import Process
import time


class TestTarget(Target):
    def __init__(self, robot: 'Robot'):
        self.process = None
        super().__init__("Test target", robot)
    def _run(self):
        def run_process():
            while True:
                print("hello")
                time.sleep(2)

        self.process = Process(target=run_process)
        self.process.start()
        return self.process

    def _shutdown(self, watchdog):
        self.process.terminate()
