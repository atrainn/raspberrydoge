#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import time
from getDoge import *
from btc import *
from updateValues import *

lcd = Adafruit_CharLCD()
#lcd.begin(16, 1)


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
		dogesingle = str(updateValues().updateVal('doge', dogeOldVal))
		milDoge = str(updateValues().updateVal('mildoge', milDogeOld))
		btcVal = str(updateValues().updateVal('btc', btcValOld))

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
			
			
