#!/usr/bin/env python
from RPi import GPIO
from time import sleep

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_UP)

clkLastState = GPIO.input(clk)

def my_callback(channel):
    global clkLastState
    global counter
    try:
                clkState = GPIO.input(clk)
                if clkState != clkLastState:
                        dtState = GPIO.input(dt)
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                print counter
                clkLastState = clkState
                sleep(0.01)
    finally:
                print "Ending"

counter = 0
clkLastState = GPIO.input(clk)
GPIO.add_event_detect(17, GPIO.FALLING  , callback=my_callback, bouncetime=300)
raw_input("Enter anything :")
GPIO.cleanup()
