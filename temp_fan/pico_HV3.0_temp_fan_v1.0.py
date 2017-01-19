#!/usr/bin/python

import logging
import smbus
from time import sleep

logging.basicConfig(filename='/home/pi/PiModules/temp_fan/error.log',level=logging.INFO)

# Set your desired temperature symbol
# C = Celsius
# F = Fahrenheit
degrees = "C"

pico = smbus.SMBus(1)

# function to get temperature from TO92 sensor
def to92_temp():
        data = pico.read_byte_data(0x69, 0x1C)
        data = format(data,"02x")
        if (degrees == "C"):
                return float(data)
        elif (degrees == "F"):
                return (float(data) * 9 / 5) + 32

# function to set the fan speed
def set_fan_speed(speed):
        logging.info("setting fan speed: %s",speed)
        pico.write_byte_data(0x6b, 0x11, 0x00) # turn fan off
        pico.write_byte_data(0x6b, 0x12, speed) # set speed
        pico.write_byte_data(0x6b, 0x11, 0x01) # turn fan on

prev_temp = 0

while True:
        try:
                logging.info("checking temp")
                temp = to92_temp()
                logging.info("current temperature: %s",temp)
                if temp != prev_temp: # check if temp has changed, no need to make unnecessary i2c calls
                        prev_temp = temp # update prev_temp variable to current temp to compare next time

# setup temperature thresholds to set the fan at different speeds

                        if temp <= 30:
                                set_fan_speed(0)
                        if temp > 30:
                                set_fan_speed(25)
                        if temp > 60:
                                set_fan_speed(50)
                        if temp > 70:
                                set_fan_speed(75)
                        if temp > 80:
                                set_fan_speed(100)
        except:
                logging.exception("Exception message:")
        sleep(900) # wait 15 minutes


