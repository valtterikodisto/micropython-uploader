from device import Arduino
from mp_tool import MicroPythonTool
import argparse

def main(port, baudrate):
    mp_tool = MicroPythonTool(port)
    arduino = Arduino(port, baudrate, mp_tool)
    arduino.upload()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Upload MicroPython code to Arduino Nano 33 BLE')
    parser.add_argument('-p', '--port', type=str, help='Serial port')
    parser.add_argument('-b', '--baudrate', type=int, default=9600, help='Baudrate')

    args = parser.parse_args()
    main(args.port, args.baudrate)