import time
from board import LED
from ubluepy import Service, Characteristic, UUID, Peripheral, constants

device_name = "Nano BLE"
led_red, led_green, led_blue = LED(1), LED(2), LED(3)

led_red.off()
led_green.off()
led_blue.off()

try:
    def event_handler(id, handle, data):
        global periph
        global service
        global led_green
        global led_blue

        if id == constants.EVT_GAP_CONNECTED:
            led_blue.on()
        elif id == constants.EVT_GAP_DISCONNECTED:
            # restart advertising
            periph.advertise(device_name=device_name, services=[service])
            led_blue.on()
            time.sleep_ms(1000)
            led_blue.off()
            time.sleep_ms(1000)
        elif id == constants.EVT_GATTS_WRITE:
            data_decimal = int.from_bytes(data, 'big') if len(data) > 0 else 0
            if data_decimal == 1:
                led_green.on()
            elif data_decimal == 0:
                led_green.off()

    notif_enabled = False
    uuid_service = UUID("87FA6B32-8CDE-4391-BC6B-B2BEC6761558")
    uuid_char = UUID("A3EA49C8-87C4-47C9-84D6-14EDAE739E2B")

    service = Service(uuid_service)
    char = Characteristic(uuid_char, props=Characteristic.PROP_WRITE)
    service.addCharacteristic(char)

    periph = Peripheral()
    periph.addService(service)
    periph.setConnectionHandler(event_handler)
    periph.advertise(device_name=device_name, services=[service])

    while True:
        time.sleep_ms(500)
except Exception as e:
    while True:
        led_red.on()
        time.sleep_ms(100)
        led_red.off()
        time.sleep_ms(100)
        print(e.value)