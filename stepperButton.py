#!/usr/bin/python
# coding: utf-8

#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#    Stepper Motor Test
#
# A simple script to control
# a stepper motor.
#
# Author : Matt Hawkins
# Date   : 28/09/2015
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [4,17,22,27]

# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)


# Define GPIO signals to use
ButtonPin = 26

# Set all pins as input
GPIO.setup(ButtonPin,GPIO.IN)


# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

# above is backward of the 8 step.
#8 Step : A – AB – B – BC – C – CD – D – DA
# 4 Step : AB – BC – CD – DA (Usual application)
# below is forward of the 4 step
#Seq = [[1,1,0,0],
       #[0,1,1,0],
       #[0,0,1,1],
       #[1,0,0,1]]

       
StepCount = len(Seq)
StepDir = -1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0
prev_input = 0

# Start main loop
while True:

  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0, 4):
    xpin = StepPins[pin]
    if Seq[StepCounter][pin]!=0:
      print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir


  #take a reading
  input = GPIO.input(ButtonPin)

  #if the last reading was low and this one high, print
  if ((not prev_input) and input):
    print("Button pressed")
    StepDir = -1 * StepDir

  #update previous input
  prev_input = input


  # Wait before moving on
  time.sleep(WaitTime)
