import os
import argparse
import sys
import glob
import serial
from typing import NamedTuple
from dotenv import load_dotenv

class Config(NamedTuple):
    SERIAL_PORT: str
    BAUDRATE: int

def get_config() -> Config:
    load_dotenv()

    env_serial_port = os.getenv('SERIAL_PORT')
    env_baudrate = os.getenv('BAUDRATE')

    parser = argparse.ArgumentParser(description='Upload MicroPython code to Arduino Nano 33 BLE')
    if env_serial_port:
        parser.set_defaults(serialport=env_serial_port)
    if env_baudrate:
        parser.set_defaults(baudrate=env_baudrate)

    parser.add_argument('-p', '--serialport', type=str, help='Serial port')
    parser.add_argument('-b', '--baudrate', type=int, help='Baudrate')
    parser.add_argument('-l', '--list', action='store_true', help='List available serial ports')

    args = parser.parse_args()

    if args.list:
        print("Available serial ports:")
        for port in available_serial_ports():
            print(f"\t{port}")
        sys.exit(0)
    if not args.serialport:
        raise Exception('Serial port not specified')
    if not args.baudrate:
        raise Exception('Baudrate not specified')

    return Config(args.serialport, args.baudrate)


def available_serial_ports() -> list[str]:
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result: list[str] = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result