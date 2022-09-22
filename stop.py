import speech_recognition as sr
from playsound import playsound
import time

while True:
    r = sr.Recognizer()
    r.pause_threshold = 0.5      

    #Check there is a microphone

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            string = r.recognize_google(audio)
            string = string.lower()
            print("Google Speech Recognition thinks you said " + string)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            continue
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    #Check for stop
    string = string.split()
    for x in string:
        if x == "stop":
            file = open('stopwatch.txt', 'w')
            file.write("0")
            file.close()
            exit()
                
