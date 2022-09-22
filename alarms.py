import speech_recognition as sr
import pyttsx3
# OS used for launching other programs
import os

#file initiator
file = ""


#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#Trigger words=============================================================================================
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "tommorow", "days"]
hours = range(1,13, 1)
minutes = range(61,0,-1)
timespans = ['am', 'pm', "p.m.", "a.m."]
#==========================================================================================================

#Timetype holds what kind of alarm the user wants
Timetype = ""

def Alarms(string):
    timeSet = False
    if ":" in string:
        string = string.replace(":", " ")
    #seperate words spoken and find what type of alarm they want.
    #if the user says a time with the alarm then a Boolean is set to true
    #so some steps can be skipped later
    string = string.split()
    
    for x in string:
        if x == "alarm":
            Timetype = x
            for y in string:
                print(y)
                for z in hours:
                    if str(z) == y:
                        timeSet = True
        elif x == "stopwatch":
            Timetype = x
        elif x == "timer":
            Timetype = x
        
            
        
            
    print(Timetype)
    if Timetype == "alarm":

        #initiate key variables
        requested_time = ""
        hour =""
        minute=""
        day=""
        timespan = ""
        
        #If the user has not said a time already then get that here
        if timeSet == False:
                #Speech recognition is activated to hear the time
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1) 
                    engine.say("When do you want to set an alarm")
                    engine.runAndWait()
                    audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    newstring = r.recognize_google(audio)
                    requested_time = newstring.lower()
                    print("Google Speech Recognition thinks you said " + newstring)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("alarm.wavm Google Speech Recognition service; {0}".format(e))

        #user will say a time and day this must be saved and another program will wait for it to reach that time and sound the alarm
                requested_time = requested_time.replace(":", " ")
                requested_time = requested_time.split()
                
        else:
            requested_time = string

        print(requested_time)
        #analyse input for a time and day
        for x in requested_time:
            if x in days:
                print(x)
                day = x
            for y in hours:
                if str(y) == x:
                    print(x)
                    hour = x
                    break
            for y in minutes:
                if str(y) == x:
                    print(x)
                    minute = x
            for y in timespans:
                if y == x:
                    timespan = x
                    if timespan == "a.m.":
                        timespan = "am"
                    elif timespan == "p.m.":
                        timespan = "pm"
                    print(timespan)

        #Validation
        if not day:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) 
                engine.say("What day would you like to set the alarm?")
                engine.runAndWait()
                audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    newstring = r.recognize_google(audio)
                    requested_time = newstring.lower()
                    print("Google Speech Recognition thinks you said " + newstring)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("alarm.wavm Google Speech Recognition service; {0}".format(e))
            day = requested_time

        if not hour:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1) 
                engine.say("On what hour would you like to set the alarm?")
                engine.runAndWait()
                audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    newstring = r.recognize_google(audio)
                    requested_time = newstring.lower()
                    print("Google Speech Recognition thinks you said " + newstring)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("alarm.wavm Google Speech Recognition service; {0}".format(e))

            hour = requested_time
        if not minute:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                engine.say("What minute would you like to set the alarm?")
                engine.runAndWait()
                audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    newstring = r.recognize_google(audio)
                    requested_time = newstring.lower()
                    print("Google Speech Recognition thinks you said " + newstring)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("alarm.wavm Google Speech Recognition service; {0}".format(e))
            minute = requested_time

        if not timespan:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                engine.say("Would you like to set the alarm in the morning or the afternoon?")
                engine.runAndWait()
                audio = r.listen(source)

                # recognize speech using Google Speech Recognition
                try:
                    newstring = r.recognize_google(audio)
                    requested_time = newstring.lower()
                    print("Google Speech Recognition thinks you said " + newstring)
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print("alarm.wavm Google Speech Recognition service; {0}".format(e))
            timespan = requested_time
            if timespan == "a.m." or "morning":
                timespan = "am"
            elif timespan == "p.m." or "afternoon":
                timespan = "pm"

        #If enough information has been set then it will open a file and save the time and day
        #of the alarm
        if hour and minute and day:
            if int(minute) < 10:
                minute = '0' + minute
            alarm_time = hour+","+minute+','+timespan
            speak = "Setting an alarm for "+ str(alarm_time) + " on "+ str(day)
            engine.say(speak)
            engine.runAndWait()
            f = open("alarms.txt", 'a')
            f.write(day)
            f.write('\n')
            f.write(alarm_time)
            f.write('\n')
            f.close()
            os.startfile("Alarm checker.py")
                
            
    elif Timetype == "stopwatch":
        y = 0
        #set state of stopwtach to true and save in file for other programs to see.
        file = open('stopwatch.txt', 'w')
        file.write("1")
        file.close()
        
        #start stopwatch
        engine.say("Starting stopwatch. Say stop when done.")
        engine.runAndWait()
        os.startfile("stopwatch.py")
        os.startfile("stop.py")

        
        
    elif Timetype == "timer":
        #set a timer
        #check for time in words spoken
        for x in string:
            print(x)
            if x.isdigit():
                print("Found digit...")
                counter = int(x)
                num = int(x)
                break
            
        #check for units in words spoken
        #if unit found save this to a file for the timer program to use
        f = open('timer.txt', 'w')
        if "minutes" in string:
            speak = "Okay, setting a timer for "+ str(num)+ " minutes"
            engine.say(speak)
            engine.runAndWait()
            counter *= 60
            f.write(str(counter))
        elif "seconds" in string:
            speak = "Okay, setting a timer for " + str(num) + " seconds"
            engine.say(speak)
            engine.runAndWait()
            f.write(str(counter))
        elif "hours" in string:
            speak = "Okay, setting a timer for " + str(num) + " hours"
            engine.say(speak)
            engine.runAndWait()
            counter *=120
            f.write(str(counter))
        else:
            f.write(str(counter))

        f.close()
        #save file and start timer
        os.startfile("timer.py")
        


    engine.stop()
    

