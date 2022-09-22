import datetime
import pyttsx3
import speech_recognition as sr
#spell checker will be used as getting the correctly spelt days and event names are crucuial
from spellchecker import SpellChecker
spell = SpellChecker()

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Trigger words===========================================================================================================
events = ["meeting", "birthday", "shopping", "nails", "test", "exam", "doctors", "appointment"]
denominator = ["the", "for", "at", "on", "in", "my" ]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "today", "tomorrow"]
times = ["12","11","10","9","8","7","6","5","4","3","2","1"]
minutes = range(60,0, -1)

timeSpan = ["am", "pm", "a.m.", "p.m.", "morning", "afternoon", "evening"]
sched = ["schedule", "set reminder", "calendar", "reminder", "remind me"]
remin = ["once a week", "everyday"]
#=========================================================================================================================


def Schedule(string):
    splitstring = string.split()
    r = sr.Recognizer()
    #Initiate time storers
    day = ""
    time = ""
    timespan = ""
    minute = ""

    setOften = False
        #get current time
    currentTime = datetime.datetime.now()

        #look for words that arent related and delete them from string
    for x in sched:
        if x in string:
            string = string.replace(x, "")

    #look to see if theyve already said how often
    for x in remin:
        if x in string:
            day = x
            setOften = True
            string = string.replace(day, "")
        #Look for a day in the string and store it in the day variable, Then remove it from the original string.        
    for x in splitstring:
        if x in days:
            day = x
            string = string.replace(day, "")
        #Do the same for hours
    for x in times:
        if x in string:
            time = x
            string = string.replace(time, "", 1)
            break

    for x in minutes:
        if str(x) in string:
            minute = str(x)
            print(minute)
            break

    string = string.replace(minute, "")
        #And because is 12 hour we must find if its in the morning or afternoon
    for x in timeSpan:
        if x in string:
            timespan = x
            string = string.replace(timespan, "")
            if timespan == "a.m." or timespan == "morning":
                timespan = "am"
            elif timespan == "p.m." or timespan == "afternoon":
                timespan = "pm"
    #In this function will will remove denominators from the string.
    #these are certain words that are used in a sentencce like the.
    for x in splitstring:
        if x in denominator:
            string = string.replace(x, "")

    if not day:
       
        #Speech recognition is activated to hear the day
 
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            engine.say("What day is this on?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            newstring = r.recognize_google(audio)
            day = newstring.lower()
            print("Google Speech Recognition thinks you said " + newstring)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        

    if not time:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            engine.say("What hour is this on?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            newstring = r.recognize_google(audio)
            time = newstring.lower()
            print("Google Speech Recognition thinks you said " + newstring)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        for x in timeSpan:
            if x in time:
                timespan = x
                time = time.replace(x, "")
                break

    if not minute and day:
        minute = "00"
        #If the user has not said if its in the morning or afternoon then TAMI will ask for this. 
    if not timespan:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            engine.say("Is this in the morning or afternoon?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            newstring = r.recognize_google(audio)
            timespan = newstring.lower()
            print("Google Speech Recognition thinks you said " + newstring)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        if timespan == 'morning':
            timespan = 'am'
        elif timespan == 'afternoon':
            timespan = 'pm'
        
    #remove spaces from the left and right of the string
    string = string.lstrip()
    string = string.rstrip()
    #Validate if this is correct with the user



    event = "On," + day + ",at," + time + "," + minute + ',' + timespan + ",you have," + string

    print(time)
    time = int(time)
    time = time - 1
    print(time)
    time = str(time)

    #converting time to an interger to be changed to an hour before and then
    #converting it back to a string so i can make a variable for the reminder time
    reminder = day + ',' + time + ',' + minute + ',' + timespan
    print(reminder)
    if not setOften:
        #If so they can select how often or what date and time they want to be reminded.
        #months/twelvth/yearsb
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            engine.say("When or how often would you like to be reminded?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            newstring = r.recognize_google(audio)
            reminder = newstring.lower()
            print("Google Speech Recognition thinks you said " + newstring)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))


        splitstring = reminder.split()


        #if the user says a day then store it here
        for x in splitstring:
            if x in days:
                day = x
        #if they dont say a day then check if they said how often and store it
        for x in remin:
            if x in reminder:
                day = x
         #if hte user says morning or afternoon then store that here       
        for x in timeSpan:
            if x in reminder:
                timespan = x
                if timespan == "p.m." or timespan == "afternoon":
                    timespan = "pm"
                elif timespan == "a.m." or timespan == "morning":
                    timespan = "am"
        #if user mentioned a time store it here and remove the time from the user's string
        for x in times:
            if x in reminder:
                time = x
                reminder = reminder.replace(time, "", 1) #1 is how many occurences of time i want to remove so it doesnt delete part of the minutes
                print(reminder)
                break

        #if user says the minutes store that here      
        for x in minutes:
            if str(x) in reminder:
                minute = str(x)
                print(minute)
                break

        
                
        if day == "once" or day == "never":
            pass    #SET no reminder


        reminder = day + ',' + time + ',' + minute + ',' + timespan


    #save event and reminder to file for another program to check reminders
    f = open("reminders.txt", 'a')
    f.write(event)
    f.write('\n')
    f.write(reminder)
    f.write('\n')
    f.close()

    print(event)
    print(reminder)
    engine.stop()

    #check to see if reminder reader is open
    #if not then open it
    f = open("reminderSet.txt", 'r')
    state = f.readline()
    f.close()
    if state == '0':
        os.startfile("calchecker.py")


#test inputs:
#schedule a meeting on monday at 10pm
#remind me everyday to take my medicine
#remind me everyday to take my medicine at 10 am on monday
