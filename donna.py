import speech_recognition as sr
from gtts import gTTS
import os
import subprocess

def speak(text):
	""" Convert the 'text' in audio, stores it in s'ound/audio.mp3'
	and plays it through terminal. """
	tts = gTTS(text, 'en-IN')
	tts.save('sound/audio.mp3')
	os.system("mpg123 sound/audio.mp3")

def listen():
	''' Captures voice input from the Microphone and returns
	it in Str data type. '''
	r = sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		speak("What can I do for you?")
		r.pause_Threshold = 2
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)

	return r.recognize_google(audio)

def appointment():
	''' Opens 'data/appointments.txt' using gedit to let users to set the appointments manually.
	Also displays the previous appointments. '''
	proc = subprocess.Popen(['gedit', 'data/appointments.txt'])

# Looks sloppy! requires refinement
def read_appointment():
	''' Reads the appointments line by line from appointments.txt '''
	if(os.stat("data/appointments.txt").st_size == 0):
		speak("You don't have any appointments.")
	else:
		with open('data/appointments.txt') as f:
			no_of_tasks = sum(1 for _ in f)
			speak("You have "+str(no_of_tasks)+ " appointments.")
		file = open("data/appointments.txt", "r")
		for line in file:
			speak(line)

def set_alarm():
	speak("I am not programmed to set alarms yet. Sorry!")


def process(command):
	if (command.find("appointment") != -1 or command.find("task") != -1):
		appointment()
	elif(command.find("read")):
		read_appointment()
	elif(command.find("alarm") != -1):
		set_alarm()
	else:
		speak("I don't understand you.")


# test_command = listen()
# process(test_command)
read_appointment()