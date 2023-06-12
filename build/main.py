from .device import Arduino
from .mp_tool import MicroPythonTool
from .config import get_config
from monitor.main import read_serial_loop

def main(port, baudrate):
    mp_tool = MicroPythonTool(port)
    arduino = Arduino(port, baudrate, mp_tool)
    arduino.upload()

if __name__ == '__main__':
    config = get_config()
    print("Uploading MicroPython code to Arduino Nano 33 BLE...")
    main(config.SERIAL_PORT, config.BAUDRATE)
    print("Uploading done.")
    print("Click the reset button on the Arduino Nano 33 BLE to start the program.")
    read_serial_loop()