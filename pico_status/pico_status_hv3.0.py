#!/usr/bin/python

#####################################################################################
# pico_status_hv3.0.py
# updated: 20-01-2017
# Script to show you some statistics pulled from your UPS PIco HV3.0A

#####################################################################################
# SETTINGS
#####################################################################################

# Set your desired temperature symbol
# C = Celsius
# F = Fahrenheit
degrees = "C"

#####################################################################################
# It's not necessary to edit anything below this line unless your knowing what to do!
#####################################################################################

import smbus
import time
import datetime

i2c = smbus.SMBus(1)

def fw_version():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x26)
   data = format(data,"02x")
   return data

def boot_version():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x25)
   data = format(data,"02x")
   return data

def pcb_version():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x24)
   data = format(data,"02x")
   return data

def pwr_mode():
   data = i2c.read_byte_data(0x69, 0x00)
   data = data & ~(1 << 7)
   if (data == 1):
      return "RPi POWERED"
   elif (data == 2):
      return "BAT POWERED"
   else:
      return "ERROR"

def bat_version():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x07)
   if (data == 0x46):
      return "LiFePO4 (ASCII : F)"
   elif (data == 0x51):
      return "LiFePO4 (ASCII : Q)"
   elif (data == 0x53):
      return "LiPO (ASCII: S)"
   elif (data == 0x50):
      return "LiPO (ASCII: P)"
   else:
      return "ERROR"

def bat_runtime():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x01) + 1
   if (data == 0x100):
      return "TIMER DISABLED"
   elif (data == 0xff):
      return "TIMER DISABLED"
   else:
      data = str(data)+ " MIN"
      return data

def bat_level():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x08)
   data = format(data,"02x")
   return (float(data) / 100)

def bat_percentage():
   time.sleep(0.1)
   datavolts = bat_level()
   databattery = bat_version()
   if (databattery == "LiFePO4 (ASCII : F)") or (databattery == "LiFePO4 (ASCII : Q)"):
      datapercentage = ((datavolts-2.9)/1.25)*100

   elif (databattery == "LiPO (ASCII: S)") or (databattery == "LiPO (ASCII: P)"):
      datapercentage = ((datavolts-3.4)/0.75)*100
   return datapercentage

def rpi_level():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x0a)
   data = format(data,"02x")
   return (float(data) / 100)

def ntc1_temp():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x1b)
   data = format(data,"02x")
   if (degrees == "C"):
      return data
   elif (degrees == "F"):
      return (float(data) * 9 / 5) + 32

def to92_temp():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x69, 0x1C)
   data = format(data,"02x")
   if (degrees == "C"):
      return data
   elif (degrees == "F"):
      return (float(data) * 9 / 5) + 32

def epr_read():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x0c)
   data = format(data,"02x")
   return (float(data) / 100)

def ad2_read():
   time.sleep(0.1)
   data = i2c.read_word_data(0x69, 0x14)
   data = format(data,"02x")
   return (float(data) / 100)
   
def fan_mode():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x11)
   data = data & ~(1 << 2)
   if (data == 1):
      return "ENABLED"
   elif (data == 0):
      return "DISABLED"
   else:
      return "ERROR"

def fan_state():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x13)
   data = data & ~(1 << 2)
   if (data == 1):
      return "ON"
   elif (data == 0):
      return "OFF"
   else:
      return "ERROR"

def fan_speed():
   time.sleep(0.1)
   data = i2c.read_word_data(0x6b, 0x12)
   data = format(data,"02x")
   return (float(data) * 10)

def r232_state():
   time.sleep(0.1)
   data = i2c.read_byte_data(0x6b, 0x02)
   if (data == 0x00):
      return "OFF"
   elif (data == 0x01):
      return "ON @ 4800 pbs"
   elif (data == 0x02):
      return "ON @ 9600 pbs"
   elif (data == 0x03):
      return "ON @ 19200 pbs"
   elif (data == 0x04):
      return "ON @ 34600 pbs"
   elif (data == 0x05):
      return "ON @ 57600 pbs"
   elif (data == 0x0f):
      return "ON @ 115200 pbs"
   else:
      return "ERROR"

print " "
print "***********************************"
print "      UPS PIco HV3.0A Status       "
print "***********************************"
print " "
print " ","UPS PIco Firmware.....:",fw_version()
print " ","UPS PIco Bootloader...:",boot_version()
print " ","UPS PIco PCB Version..:",pcb_version()
print " ","UPS PIco BAT Version..:",bat_version()
print " ","UPS PIco BAT Runtime..:",bat_runtime()
print " ","UPS PIco r232 State...:",r232_state()
print " "
print " ","Powering Mode.........:",pwr_mode()
print " ","BAT Percentage........:",bat_percentage(),"%"
print " ","BAT Voltage...........:",bat_level(),"V"
print " ","RPi Voltage...........:",rpi_level(),"V"

if (degrees == "C"):
   print " ","NTC1 Temperature......:",ntc1_temp(),"C"
   print " ","TO-92 Temperature.....:",to92_temp(),"C"
elif (degrees == "F"):
   print " ","NTC1 Temperature......:",ntc1_temp(),"F"
   print " ","TO-92 Temperature.....:",to92_temp(),"F"
else:
   print " ","NTC1 Temperature......: please set your desired temperature symbol!"
   print " ","TO-92 Temperature.....: please set your desired temperature symbol!"

print " ","Extended Voltage......:",epr_read(),"V"
print " ","A/D2 Voltage..........:",ad2_read(),"V"
print " "
print " ","PIco FAN Mode.........:",fan_mode()
print " ","PIco FAN State........:",fan_state()
print " ","PIco FAN Speed........:",fan_speed(),"RPM"
print " "
print "***********************************"
print "         Powered by PiCo           "
print "***********************************"
print " "