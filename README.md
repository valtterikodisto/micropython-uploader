## MicroPython Uploader for Arduino Nano 33 BLE

### Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
# Uploads src/ to the board
python build/main.py --port=/dev/tty --baudrate=9600

# Press reset button on the board
```

### Nano 33 BLE Sense Python Guide

https://docs.arduino.cc/tutorials/nano-33-ble-sense/ble-sense-python-api#api
