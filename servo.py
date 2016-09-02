#!/usr/bin/python

from handlers.servoHandler import Servo
import time
import sys
import json
import requests
import getch

motor = None

def initiate():
	global motor
	motor = Servo()
	motor.cleanup()
	return

def motorTo0Degree():
	global motor
	motor.initiate()
	motor.turn0Degree()
	motor.cleanup()
	return

def motorTo90Degree():
	global motor
	motor.initiate()
	motor.turn90Degree()
	motor.cleanup()
	return


if __name__ == '__main__':
	initiate()
	if len(sys.argv) > 1:
		option = sys.argv[1]
		if option == 'open':
			motorTo0Degree()
		elif option == 'close':
			motorTo90Degree()
		else:
			print "Wrong option"
	else:
		print "usage: servo.py [option]"

	sys.exit()

