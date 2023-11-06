from machine import Pin
import time
 
p25 = Pin(25,Pin.OUT)


while True:
    p25.on()
    print("ON")
    time.sleep_ms(50)
    print("OFF")
    p25.off()
    time.sleep_ms(50)
    