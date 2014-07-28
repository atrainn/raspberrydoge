from getDoge import *
from Adafruit_CharLCD import Adafruit_CharLCD
from btc import *

class updateValues:
    def updateVal(coins, oldVal):
    
    	if coins == 'doge':
    		try:
    			value = str(getDoge().singleDoge())
    		except:
    			try:
    				value = str(getDoge2().singleDoge())
    			except:
    				lcd.clear()
    				lcd.message("Could Not Update\n" + coins)
    			time.sleep(2)
    			if value == '0':
    				value = oldVal
    				
    				
    	elif coins == 'mildoge':
    		try:
    			value = float(getDoge().dogeMil())
    		except:
    			try:
    				value = str(getDoge2().dogeMil())
    			except:
    				lcd.clear()
    				lcd.message("Could Not Update\n" + coins)
    			time.sleep(2)
    			if value == '0':
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
    	