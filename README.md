# micro python setup, to esp8266( ESP-WROOM-02 )

 Author  : Kouji Nakashima / kuc-arc-f.com

 date    : 2016/11/20


## setup (micro python ,firmware write)
(PC=raspberry Pi2 /raspbian-wheezy)

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

## reference
MicroPython Basics: How to Load MicroPython on a Board:

https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266

micropython:
http://micropython.org

MicroPython Wiki:
http://wiki.micropython.org/Home

mpfshell:
http://qiita.com/taka-murakami/items/25bec288d4aa1bc6f63f

