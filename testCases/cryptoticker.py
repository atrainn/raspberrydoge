#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import time
from dogemethod import *
from btc import *

lcd = Adafruit_CharLCD()
#lcd.begin(16, 1)

def updateVal(coins):
	obj = 0
	
	if coins == 'doge':
		try:
			obj = str(getdoge().singledoge())
		except Exception:
			sys.exec_clear()
	elif coins == 'mildoge':
		try:
			obj = (float(dogesingle)*1000000)
		except Exception:
			sys.exec_clear()
	elif coins == 'btc':
		try:
			obj = str(getbtc().FifteenVal())
		except Exception:
			sys.exec_clear()
	return obj
		

if __name__ == "__main__":
	while 1:
		lcd.clear()
		lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
		lcd.message("Updating...")
		dogesingle = str(updateVal('doge'))
		mildoge = str(updateVal('mildoge'))
		btcval = str(updateVal('btc'))

		x = 0
		while x < 10:
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("1D: $" + dogesingle)
			time.sleep(10)
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("1MD: $" + str(mildoge))
			time.sleep(10)
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("BTC: $" + btcval)
			time.sleep(10)
			x += 1
			
			
#For use on Pi comment out print statements and uncomment lcd. statements!
#Every 10 seconds it will switch between 1 doge and 1million doge
#Updates values every five minutes
	