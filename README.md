## MicroPython Uploader for Arduino Nano 33 BLE

### Install

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage

```bash
# Set up .env and edit it
cp .env.example .env

# Uploads src/ to the board (python -m build.main -h for help)
# Run python -m build.main -l to list available serial ports
python -m build.main

# Press reset button on the board once the upload is complete
```

### Nano 33 BLE Sense Python Guide

https://docs.arduino.cc/tutorials/nano-33-ble-sense/ble-sense-python-api#api
