import connection_checker as cc
from gtts import gTTS
import os
import listener
import random


def greet():
	'''This function gets random greeting from data/greetings.txt in form of strings
		converts it into audio and paly it directly. It always runs at the start of
		the application to greet the user.'''

	fin = open('data/greetings.txt')
	line = random.choice(fin.readlines()) # randomly selects a line from greetings.txt
	print(line)
	
	tts = gTTS(line, 'en-IN')	# converts the text-to-speech 
	tts.save('audio.mp3')
	os.system("mpg123 audio.mp3")	# audio is played by the mpg123 lib

if(cc.check_internet_connection()):
	greet()
	command = listener.commands()
	print(listener.command_processor(command))
else:
	print("Sorry I can't feel my brains. A decent Internet connection might help.")
