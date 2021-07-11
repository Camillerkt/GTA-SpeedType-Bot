# GTA SAMP SpeedType bot made by Camille Rakotoarisoa (https://camillerakoto.fr)

# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
#pip install pytesseract et télécharger Tesseract
import pytesseract
# importing OpenCV : pip install opencv-python
import cv2
from PIL import ImageGrab
import re
import platform
#pip install pynput
from pynput.keyboard import Key, Controller
keyboard = Controller()

class Bot:
	def __init__(self, kbrd_keys, coords, tesseract_path):
		self.kbrd_keys = kbrd_keys
		self.coords = coords
		self.tesseract_path = tesseract_path

	def recordScreen(self):
		pytesseract.pytesseract.tesseract_cmd = self.tesseract_path
		cap = ImageGrab.grab(bbox =(self.coords['top'], self.coords['left'], self.coords['height'], self.coords['width']))

		tesstr = pytesseract.image_to_string(
				cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
				lang ='eng')

		return tesstr

	def getTheCode(self, screen):
		all_strings_on_screen = screen.split(' ')
		for string in all_strings_on_screen:
			if code_begin in string:
				return string

	def enterTheCodeInChat(self, code):
		keyboard.press(self.kbrd_keys['tchat_key'])
		keyboard.release(self.kbrd_keys['tchat_key'])

		for char in code:
			keyboard.press(char)
			keyboard.release(char)


#Keyboard keys, Screen Resolution, Tesseract path
bot = Bot({ 'tchat_key': 't' }, {'top':0, 'left':0, 'height':1366, 'width':768}, r'/usr/local/bin/tesseract')
code_begin = 'N/A'
continue_record = True

while continue_record:
	screen = bot.recordScreen()
	code = bot.getTheCode(screen)
	if code != None:
		bot.enterTheCodeInChat(code)
		continue_record = False