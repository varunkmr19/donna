import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
from alarm import run_alarm


def speak(text):
    """ Converts the 'text' in audio, stores it in 'sound/audio.mp3'
    and plays it through terminal. """
    print("Donna: "+text)
    tts = gTTS(text, 'en-IN')
    tts.save('sound/audio.mp3')
    # q attributes hides the messages by mpg123
    os.system("mpg123 -q sound/audio.mp3")


def listen():
    ''' Captures voice input from the Microphone and returns
    it in Str data type. '''

    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.pause_Threshold = 2
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    text = r.recognize_google(audio)  # Converts audio into text.
    print("User: " + text)

    return text


def appointment():
    ''' Opens 'data/appointments.txt' using gedit to let users to set the appointments manually.
    Also displays the previous appointments. '''

    proc = subprocess.Popen(['gedit', 'data/appointments.txt'])
    proc.wait()

# Looks sloppy! requires refinement


def read_appointment():
    ''' Reads the appointments line by line from appointments.txt '''

    if(os.stat("data/appointments.txt").st_size == 0):
        speak("You don't have any appointments.")
    else:
        with open('data/appointments.txt') as f:
            no_of_tasks = sum(1 for _ in f)
            speak("You have "+str(no_of_tasks) + " appointments.")
        file = open("data/appointments.txt", "r")
        for line in file:
            speak(line)


def set_alarm():
    speak("Sure, when's the alarm for?")
    user_input = listen()
    # print(user_input)
    speak("Alright, your alarm is set for " + user_input)
    run_alarm(user_input)


# Find a better way to process these. If-statements seems repetitive.
def process(command):
    if (command.find("appointment") != -1 or command.find("task") != -1):
        appointment()
    elif(command.find("read") != -1):
        read_appointment()
    elif(command.find("alarm") != -1):
        set_alarm()
    else:
        speak("I don't understand you.")


speak("Hi, I'm donna. What can I do for you?")
# set_alarm()
test_command = listen()
process(test_command)
