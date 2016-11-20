 micro python setup, to esp8266( ESP-WROOM-02 )

 Author  : Kouji Nakashima / kuc-arc-f.com

 date    : 2016/11/20


# setup (micro python ,firmware write)
(PC=raspberry Pi2 /raspbian-wheezy)

    sudo pip install esptool

erase_flash (if port= /dev/ttyUSB0 )

    esptool.py --port  /dev/ttyUSB0 erase_flash

write_flash

    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=8m 0 esp8266-20160809-v1.8.3.bin


# file transfer shell ( tool )


# youtube (sample LED) 
https://youtu.be/1tXvscYFnC0

# reference
MicroPython Basics: How to Load MicroPython on a Board:

https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266

micropython:
http://micropython.org

MicroPython Wiki:
http://wiki.micropython.org/Home

