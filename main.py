import analyse as analyse

#Speech recognition API
import speech_recognition as sr

import subprocess

import pyttsx3

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def install(name):
    subprocess.call(['pip', 'install', name])

count = 0

#Setup extensions
print("Installing dictionary API")
install('python-freeDictionaryAPI')
print("Installing speech recognition API")
install('SpeechRecognition')
print("Installing text to speech API")
install('pyttsx3')
print("Installing playsound")
install('playsound')
print("Installing auto-correct API")
install('pyspellchecker')
print("Installing keyboard controller API")
install('pynput')

#Introduce self to user
engine.say("""Hello, I am TAMI, but you can change my name if you want.
I am here to assist you. I can tell you the weather in your city,
play any song you request, set reminders on each day of the week,
I can process calculations, I can set a timer, stopwatch or alarm and
I can even find the meaning of any word""")
engine.runAndWait()
engine.stop()
while True:
    #string stores user's input
    string = ""
    #initiate the Speech recognition API setttings
    r = sr.Recognizer()
    #Level of sound there has to be for the microphone to recognise speech
    #setting it high will mean aautomatic adustments will account for ambient noises
   # r.energy_threshold = 200
    #pause threshold is how long the silence has to be to register the end of a phrase
    r.pause_threshold = 0.5      


    #activate microphone and record
    with sr.Microphone() as source:
        #automatically changes the energy threshold
        #duration is how long it waits before the microphone listens
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        #recognize_google can take a key but for development I will use the default API
        string = r.recognize_google(audio)
        string = string.lower()
        print("Google Speech Recognition thinks you said " + string)
        count = 0
    except sr.UnknownValueError:
        if not count == 1:
            print("Google Speech Recognition could not understand audio")
            count += 1
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #CheckString Is where the inputs are analysed for keywords
    analyse.CheckString(string)
