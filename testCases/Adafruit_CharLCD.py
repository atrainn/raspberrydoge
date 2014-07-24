#!/usr/bin/python

#
# based on code from lrvick and LiquidCrystal
# lrvic - https://github.com/lrvick/raspi-hd44780/blob/master/hd44780.py
# LiquidCrystal - https://github.com/arduino/Arduino/blob/master/libraries/LiquidCrystal/LiquidCrystal.cpp
#

from time import sleep


class Adafruit_CharLCD(object):

    def clear(self):
        print "\nCleared LCD\n"
        
    def message(self, text):
        """ Send string to LCD. Newline wraps to second line"""
        print text


if __name__ == '__main__':
    lcd = Adafruit_CharLCD()
    lcd.clear()
    lcd.message("  Adafruit 16x2\n  Standard LCD")
