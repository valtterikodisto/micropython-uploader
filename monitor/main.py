import serial
from build.config import get_config

def read_serial(serial_port, baudrate):
    with serial.Serial(serial_port, baudrate) as ser:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(line)

def read_serial_loop():
    config = get_config()
    while True:
        try:
            read_serial(config.SERIAL_PORT, config.BAUDRATE)
        except OSError:
            pass
        except KeyboardInterrupt:
            break


if __name__ == '__main__':
    read_serial_loop()