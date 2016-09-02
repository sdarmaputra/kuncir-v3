#!/usr/bin/python

from handlers.servoHandler import Servo
from handlers.lcdHandler import Screen
import time
import sys
import json
import requests
import getch
import os

lcd = None

def initiate():
	global lcd
	lcd = Screen()
	lcd.cleanup()
	return

def rewriteScreen(message):
	global lcd
	lcd.initiate()
	lcd.message(message)
	lcd.cleanup()
	return


if __name__ == '__main__':
	#while True:
#		input = getch.getch()
#		print input
	initiate()
	os.system("python servo.py close")
	while True:
		string = ' Selamat datang :)\nMasukkan NRP!'
		rewriteScreen(string)
		print string
		nrp = input()
		string = ' ' + str(nrp) + '\nMasukkan PIN!'
		rewriteScreen(string)
		print string
		pin= input()
		data = {'nrp': nrp, 'pin': pin}
		req = requests.post('http://10.151.36.23:8080/pinjam_kunci', data = data)
		res = json.loads(req.text)
		if res['status'] == 'success':
			string = ' @' + str(nrp) + '\nKembali: tekan 0'
			rewriteScreen(string)
			print string
			time.sleep(1)
			os.system("python servo.py open")
			time.sleep(1)
			os.system("python servo.py close")
			while True:
				option = input()
				if (option == 0):
					break
		else:
			string = ' Gagal!\n Coba lagi :)'
			rewriteScreen(string)
			print string
			time.sleep(1)
