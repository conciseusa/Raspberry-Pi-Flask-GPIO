import RPi.GPIO as GPIO
import datetime

# simple script to test reading GPIO pins connected to the output of a
# https://www.tindie.com/products/conciseusa/24vac-isolated-interface-for-raspberry-pi-arduino
# PU (pull up) -> 3.3V, 0V (0 volts) -> Ground, O (output) -> GPIO 25 (23, 24, 26 can also be used)
# https://www.raspberrypi.com/documentation/computers/raspberry-pi.html
# https://learn.sparkfun.com/tutorials/raspberry-gpio/python-rpigpio-api

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

state = GPIO.input(25)
if state:
   print(datetime.datetime.now(), ' On')
else:
   print(datetime.datetime.now(), ' Off')

# to run once a minute and log output
# change cd to dir gpio-test.py resides
# * * * * * cd /home/your-user/Work/; python3 gpio-test.py >> gpio-test.log
