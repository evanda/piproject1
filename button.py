#!/usr/bin/python
# coding: utf-8

#
# Gotten from: https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/
# 

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 26
ButtonPin = 26

# Set all pins as input
GPIO.setup(ButtonPin,GPIO.IN)

#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
while True:

  #take a reading
  input = GPIO.input(ButtonPin)

  #if the last reading was low and this one high, print

  if ((not prev_input) and input):
    print("Button pressed")

  #update previous input
  prev_input = input

  #slight pause to debounce
  time.sleep(0.05)
