﻿# micro python setup, to esp8266( ESP-WROOM-02 )

 Author  : Kouji Nakashima / kuc-arc-f.com

 date    : 2016/11/20


## setup (micro python ,firmware write)
(PC=raspberry Pi2 /raspbian-wheezy)

download: http://micropython.org/download#esp8266


bin= esp8266-20160809-v1.8.3.bin

    sudo pip install esptool

erase_flash (if port= /dev/ttyUSB0 )

    esptool.py --port  /dev/ttyUSB0 erase_flash

write_flash

    esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=8m 0 esp8266-20160809-v1.8.3.bin


## file transfer shell ( tool )
mpfshell: https://github.com/wendlers/mpfshell

pip install:


    $ sudo pip install pyserial

    $ sudo pip install colorama

    $ sudo pip install websocket_client


setup:

    $ sudo python setup.py install

[Test]

    $ mpfshell

    mpfs [/]> open ttyUSB0

    mpfs [/]> ls

main.py copy:

    mpfs [/]> put main.py

REPL:

    mpfs [/]> repl


*1) CTR+D = reboot, microPython.

*2) exit, Ctrl+]

## Sample ,LED Blink

sample/main.py

## youtube (sample LED) 
https://youtu.be/1tXvscYFnC0

### related:
MicroPython Basics: How to Load MicroPython on a Board:

https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266

micropython:
http://micropython.org

MicroPython Wiki:
http://wiki.micropython.org/Home

mpfshell:
http://qiita.com/taka-murakami/items/25bec288d4aa1bc6f63f

***
## related (GitHub)
* MicroPython Tutorial #1, dht11 Sensor etc

https://gist.github.com/kuc-arc-f/bcf773bd7fd6f5d6f23cf5cda3a89afe

* MicroPython Tutorial #2, OLED( SSD1306 )  

https://gist.github.com/kuc-arc-f/a3f4f7c3ad501d2040ac6f1e5660a2fe

***