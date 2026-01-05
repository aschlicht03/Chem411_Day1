from time import sleep_ms
from machine import Pin

led=Pin(2,Pin.OUT) #create LED object from pin2,Set Pin2 to output
while True:
        led.value(1)
        sleep_ms(500) #Set led turn on
        led.value(0)
        sleep_ms(100) #Set led turn off