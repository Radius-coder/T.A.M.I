#Music will be a new program as the user should still be able to do other things during music
from pynput.keyboard import Key, Controller
#time is used to assist keyboard controll
import time
import numpy
#used to open the default web browser
import webbrowser
import os
import pyttsx3


#Initiate Text to Speech
speak = pyttsx3.init()
rate = speak.getProperty('rate')
speak.setProperty('rate', rate-20)
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)

#the triggers that are longer than 1 word go at the start so characters dont get taken out the string
#e.g. play will be removed from start playing if play is compared first.
music = numpy.array(["put on the song called", "put on the song", "start playing", "can you play", "play the song", "play", "music", "song", "put on"])

def changeWindow():
    
    keyboard = Controller()
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    time.sleep(1)               
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)

def startMusic(string):
    keyboard = Controller()
    string = string
    string  = string.lower()

    #if a trigger word is found then remove it from the string
    #the remaining string should be the search query
    for x in music:
        if x in string:
            print("True")
            string = string.replace(x, '')
            break
        
    print(string)
    if  not len(string.split()) < 1: 

        #check to see if music is already playing before continue
        file = open('musicplaying.txt', 'r')
        state = file.readline()
        file.close()
        if state == "1":
            changeWindow()
            keyboard.press(Key.ctrl)
            keyboard.press('w')
            time.sleep(1)
            keyboard.release('w')
            keyboard.release(Key.ctrl)

            #change file to let music property changer close
            file = open('musicplaying.txt', 'w')
            file.write("0")
            file.close()
            
            
        speak.say(f"Searching for {string}")
        speak.runAndWait()
        speak.stop()
        #first open YouTube and search the user's string
        webbrowser.open("https://youtube.com/results?search_query=" + string)
        #initiate keyboard controller
       

        #go to search bar of youtube
        time.sleep(8)
        print("TAB")
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)


        time.sleep(2)
        print("ENTER")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        print("FIN")
        os.startfile("G:\Programming\TAMI\TAMI\musicController.py")
        file = open('musicplaying.txt', 'w')
        file.write("1")
        file.close()

