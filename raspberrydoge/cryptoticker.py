#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import time
from getDoge import *
from btc import *

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

def updateVal(coins, oldVal):

	if coins == 'doge':
		try:
			value = str(getDoge().singleDoge())
		except:
			lcd.clear()
			lcd.message("Error updating\n" + coins)
			time.sleep(2)
			value = oldVal
	elif coins == 'mildoge':
		try:
			value = float(getDoge().dogeMil())
		except:
			lcd.clear()
			lcd.message("Error updating\n" + coins)
			time.sleep(2)
			value = oldVal
	elif coins == 'btc':
		try:
			value = str(getBTC().FifteenVal())
		except:
			lcd.clear()
			lcd.message("Error updating\n" + coins)
			time.sleep(2)
			value = oldVal
			
	return value
	
#Sets the new value to the old value if there's an issue updating
	

if __name__ == "__main__":
	#Define Backup Vals
	dogesingle = 0
	dogeOldVal = dogesingle
	milDoge = 0
	milDogeOld = milDoge
	btcVal = 0
	btcValOld = btcVal
	#Define Backup Vals
	
	
	
	while True:
		lcd.clear()
		lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
		lcd.message("Updating...")
		dogesingle = str(updateVal('doge', dogeOldVal))
		milDoge = str(updateVal('mildoge', milDogeOld))
		btcVal = str(updateVal('btc', btcValOld))

		x = 0
		while x < 10:
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("1D: $" + dogesingle)
			time.sleep(10)
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("1MD: $" + str(milDoge))
			time.sleep(10)
			lcd.clear()
			lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
			lcd.message("BTC: $" + btcVal)
			time.sleep(10)
			x += 1
			
			

#used for testing. Adafruit_CharLCD has been edited to output to console	
#uncomment lcd begins