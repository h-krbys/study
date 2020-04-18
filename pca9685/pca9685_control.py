#!/usr/bin/python
# -*- coding: utf-8 -*-

import Adafruit_PCA9685
import time

# Initialise the PCA9685 using desired address and/or bus:
pwm = Adafruit_PCA9685.PCA9685(address = 0x40, busnum = 1)

# Number of servo
servo_num = 12

# Set frequency to 60[Hz]
pwm.set_pwm_freq(60)

while True:
    pos = input('Enter servo position (150-600): ')
    for i in range(servo_num):
        pwm.set_pwm(i, 0, pos)
    time.sleep(2)