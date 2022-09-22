#using numpy for faster array checking
import numpy as np
#module used to translate text to speech
import pyttsx3

#importing all functions
import weathercheck as wc
import conversation as conversation
import dic as dc
import tim as tc
import cal as cc
import lig as lc
import music as mc
import alarms as ac
import calc as calc

#initialse text to speech engine
speak = pyttsx3.init()
#get and change the rate of the voice
rate = speak.getProperty('rate')
speak.setProperty('rate', rate-20)
#get and set the voice of TAMI to the system's default
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)

#Trigger words-----------------------------------------------------------------------------------------------------------------------------------
greetings = np.array(["hi","hello","hiya","hey", "howdy", "yo", "how are you", "how's it going", "how you feeling", "whats up", "you good"])
thank = np.array(["thanks", "thank you", "cheers", "great"])
time = np.array(["time", "whats the time"])
weather = np.array(["weather", "weather?", "temperature", "temperature?", "temp", "raining", "sunny", "snowing"])
dictionary = np.array(["what is the meaning of", "what is", "what's the meaning of", "what's the meaning", "what is the", "definition",  "define", "dictionary", "what's"])
light = np.array(["light", "lights", "lightbulb"])
bt = np.array(["connect", "bluetooth"])
sched = np.array(["schedule", "set reminder", "calendar", "reminder", "remind me"])
name = np.array(["name", "what's your name", "what is your name", "what are you called", "who are you"])
changeName = np.array(["change name","change your name", "rename", "new name",])
shop = np.array(["order", "can you order", "want food", "buy"]) 
affirm = np.array(["yes", "okay", "yes please", "please do", "yeah", "ye", "hell yeah", "of course", "mhm", "sure", "ok"])
good = np.array(["good", "cool", "nice", "lovely", "very well"])
music = np.array(["put on the song called", "put on the song", "start playing", "can you play", "play the song", "play", "music", "song", "put on"])
alarm = np.array(["alarm", "stopwatch", "timer"])
calculator = np.array(["+", "-", "x", "/", "plus", "add", "subtract", "minus", "divide", "times", "multiplied", "equal"]) 
tami = "TAMI"
#------------------------------------------------------------------------------------------------------------------------------------------------
nameSaid = False


#Analyse function
def CheckString(string):
    global tami
    global nameSaid
    if tami in string or "tammy" in string:
        
        string.replace(tami, "")
        string.replace("tammy", "")
        #Checking if a trigger has been activated. I will do these at the start of the loop
        #so after a command has been completed they will reset
        musicSet = False
        reminderSet = False
        weatherSet = False
        alarmSet = False
        calcSet = False
        timeSet = False
        change = False
        #import TAMI's name. This can change so it must be a global variable


        #split the user's input into an array of words
        splitstring = string.split()

        #Loop Through Trigger words in natural speaking order to find matches
        #If a match is found, that trigger will take the string and activate it's respected functions

        #Conversation
        for x in greetings:
            if x in string:
                conversation.Feeling(string)
                break
            
        #Calculator    
        for x in calculator:
            if x in string:
                calc.Calculate(string)
                calcSet = True
                break
            
        #setting an alarm, timer or stopwatch
        for x in alarm:
            if x in string:
                ac.Alarms(string)
                alarmSet = True
                break
                
        #Music playing
        for x in music:
            if x in string:
                mc.startMusic(string)
                musicSet = True
                break
        if not alarmSet:
            #Time request
            for z in time:
                if z in string:
                    tc.Time()
                    timeSet = True
                    break
        #Calender events    
        for x in sched:
            if x in string:
                cc.Schedule(string)
                reminderSet = True
                break
        #Basic reply to affirmations    
        for x in splitstring:
            if x in good:
                speak.say("Indeed")
                speak.runAndWait()
        #Weather request     
        for x in splitstring:
            if x in weather:
                wc.loadWeather(string)
                weatherSet = True
                break
                
        #Recognise Name being said   
        for x in splitstring:
            if x in tami:
                speak.say("How can I help?")
                speak.runAndWait()
                break

        if musicSet or reminderSet or weatherSet or alarmSet or calcSet or timeSet:
            print("DO NOT DEFINE")
        else:
            #Dictionary definitions    
            for z in dictionary:
                if z in string:
                    dc.Define(string)
                    break
        """Smart light control (Uses a private API key)
        for x in splitstring:
            if x in light:
                lc.Lights(string)
                break"""
        
        #What TAMI does when it hears its name
        for z in splitstring:
            if nameSaid == True:
                #Changing TAMI's name
                if z in affirm:
                    speak.say("What shall i answer to now?")
                    speak.runAndWait()
                    tami = input()
                    nameSaid = not nameSaid
                    break
                else:
                    nameSaid = False
            else:
                for z in splitstring:
                    if z in affirm:
                        speak.say("How can I help?")
                        speak.runAndWait()
                        break
                break
        #################
        for z in name:
            if z in string:
                #check if change is also included
                for y in changeName:
                    if y in string:
                        change = True
                        break
                    else:
                
                        #engine.say
                        speak.say(f"I am {tami} the talking and moving intelligence but you can change my name if you want")
                        speak.runAndWait()
                        nameSaid = True
                        break
                    break
                break
                
        ################                  
        for z in changeName:
            if z in string:
                speak.say("What shall i answer to now?")
                speak.runAndWait()
                tami = input()
                break
            if change == True:
                speak.say("What shall i answer to now?")
                speak.runAndWait()
                tami = input()
                change = False
                break
        ##################

       
        #User says a thank you
        for z in thank:
            if z in string:
                speak.say("No worries")
                speak.runAndWait()
                break
            
        #Recording input for debugging    
        with open('usersmessages.txt', 'a') as file:
            string = string + "\n"
            file.write(string)
            file.close()
            
        #stop the text to speech engine from running.        
        speak.stop()
