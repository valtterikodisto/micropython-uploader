import serial
import time
import os
from mp_tool import MicroPythonTool

class Arduino:
    def __init__(self, port: str, baudrate: int, mp_tool: MicroPythonTool):
        self.port = port
        self.baudrate = baudrate
        self.mp_tool = mp_tool

    def stop(self):
        """
        Stop the running script on the Arduino.
        This is needed when you need to interact with the board.
        """
        with serial.Serial(self.port, self.baudrate) as ser:
            # Send Ctrl+C to stop the running script
            ser.write(b'\x03')
            time.sleep(0.1)
            ser.write(b'\x03')

    def upload(self):
        """
        Upload src/ directory to the Arduino /flash directory.
        The entry point is `src/main.py`.
        """

        self.stop()
        self.clean()
        src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
        self.mp_tool.put(src_path, "/flash")

    def clean(self):
        """
        Remove all files and directories in /flash.
        """

        cleaner_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cleaner.py'))
        self.mp_tool.run(cleaner_path)