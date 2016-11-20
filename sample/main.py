import machine
import time

pin=  machine.Pin(4, machine.Pin.OUT)
pin.low()

while True:
  pin.high()
  time.sleep(0.5)
  pin.low()
  time.sleep(2.0)
  print ('Blinking LED-[ma-3]')


