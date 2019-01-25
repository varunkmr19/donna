import speech_recognition as sr
import connection_checker as cc

def commands():
	if(cc.check_internet_connection()):
		r = sr.Recognizer()
		mic = sr.Microphone()
		with mic as source:
			print("I am ready for your next command")
			r.pause_Threshold = 1
			r.adjust_for_ambient_noise(source)
			audio = r.listen(source)

		return r.recognize_google(audio)

def command_processor(text):
	if(text.find("hello") != -1):
		return "Hi"
