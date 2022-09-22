import datetime
import pyttsx3



engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def Time():
    x = datetime.datetime.now()
    hour = x.strftime("%I")
    print(hour)
    minute = x.strftime("%M")
    print(minute)
    timespan = x.strftime("%p")
    print(timespan)
    time = "it is "+hour + ":"+minute +" " +timespan
    engine.say(time)
    engine.runAndWait()
