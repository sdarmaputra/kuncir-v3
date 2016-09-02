#!/usr/bin/python


import RPi.GPIO as GPIO
import time

class Servo:
	def __init__(self):
		self.initiate()

	def initiate(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(40,GPIO.OUT)
		self.pwm = GPIO.PWM(40,50)
		self.pwm.start(7.5)

	def cleanup(self):
		GPIO.cleanup()

	def turn0Degree(self):
		self.pwm.ChangeDutyCycle(7.5)
		time.sleep(0.8)

	def turn90Degree(self):
		self.pwm.ChangeDutyCycle(5)
		time.sleep(0.8)
