import time
from board import LED

led_red = LED(1)

while True:
    led_red.on()
    time.sleep_ms(1000)
    led_red.off()
    time.sleep_ms(1000)