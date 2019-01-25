import connection_checker
from gtts import gTTS
import os
import random

def greet():
	fin = open('data/greetings.txt')
	line = random.choice(fin.readlines())
	print(line)
	
	tts = gTTS(line, 'en-IN')
	tts.save('audio.mp3')
	os.system("mpg123 audio.mp3")

greet()