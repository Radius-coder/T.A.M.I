import pyttsx3
import time

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
y = 0
while True:
    time.sleep(1)
    y+=1
    engine.say(y)
    engine.runAndWait()

    #check for stop
    file = open('stopwatch.txt', 'r')
    state = file.readline()
    file.close()
    if state == '0':
        engine.stop()
        exit()
