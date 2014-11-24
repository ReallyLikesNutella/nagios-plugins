#!/usr/bin/python
# Sample program for reading digital temperature sensor data using I2C - Modified to work as a Nagios check script
# Program uses SMBus Python library for I2C interface.
# pimpmipi.com, modifications by Dan Cottam
import smbus
import time
import datetime
import sys

bus = smbus.SMBus(1)
warntemp = 25
crittemp = 30

#Device address
device_add = 72 # CHANGE THIS TO YOUR DEVICE ADDRESS

# Index of the register on the TCN75A which contains the configurable
# resolution settings (temp_res)
config_reg = 1

# Temperature resolution
# Possible values are 0, 32, 64, and 96, where
# 0 is lowest resolution and 96 is the highest.
# 96 = 0.01625C steps
# 0 = 0.5C steps (default)
temp_res = 96

# Index of register where current temperature is stored
temp_reg = 0

try:
# Configure sensor resolution (optional)
    bus.write_byte_data(device_add, config_reg, temp_res)
    bus.write_byte(device_add, temp_reg)
# Read 2 bytes from temperature register
    temperature_bytes = bus.read_i2c_block_data(device_add, temp_reg, 2)

# Byte 0 contains integer part of temperature value
# Byte 1 contains decimal part which is 1/256 of a degrees celsius
# Values 1-127 are positive and values greater than 127 are negative
# following shows temperature values based on received bytes:
# [1][0]=1C,[0][16]=0.062C, [0][0]=0C, [255][240]=-0.062 C,[255][0]=-1C

    temperature = temperature_bytes[0] + temperature_bytes[1]/256.000;

    strtemperature = str(temperature) #convert temperature to a string for printing output

    if temperature >= crittemp:
        print ("Temperature is " + strtemperature + " degrees celcius")
        sys.exit(2)
    elif temperature >= warntemp:
        print ("Temperature is " + strtemperature + " degrees celcius")
        sys.exit(1)
    elif temperature < warntemp:
        print ("Temperature is " + strtemperature + " degrees celcius")
        sys.exit(0)
    else:
        print ("Error, script output: " + strtemperature)
        sys.exit(3)

except IOError as (errno, strerror):
     print "I/O error({0}): {1}".format(errno, strerror)
