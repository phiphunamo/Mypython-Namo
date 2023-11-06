from machine import Pin
import time
 
p2 = Pin(2,Pin.OUT)
p3 = Pin(3,Pin.OUT)
p4 = Pin(4,Pin.OUT)
p25 = Pin(25,Pin.OUT)
while True:
    p2.on()
    print("ON")
    time.sleep_ms(50)
    print("OFF")
    p2.off()
    time.sleep_ms(50)
    p3.on()
    time.sleep_ms(50)
    p3.off()
    time.sleep_ms(50)
    p4.on()
    time.sleep_ms(50)
    p4.off()
    time.sleep_ms(50)
    p25.on()
    time.sleep_ms(50)
    p25.off()
    time.sleep_ms(50)
    