from machine import Pin
from utime import sleep

print("Hello, ESP32!")

led = Pin(12, Pin.OUT)
while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)

