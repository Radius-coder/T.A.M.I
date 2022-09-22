#this program will read the file for reminder times to see if it
#should activate

#the commas in each 2 lines will allow me to split each line into an array
#where i can access the value i need by index number
import pyttsx3
import datetime
import time
#get current day in letters, and hour in 12 hour format
#and minutes as a number between 00 and 60

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


  
i = 0

f = open("reminderSet.txt", 'w')
f.write('1')
f.close()

while True:
    current_time = datetime.datetime.now()
    current_day = current_time.strftime("%A").lower()
    current_hour = current_time.strftime("%I")
    current_minute = current_time.strftime("%M")
    current_timespan = current_time.strftime('%p').lower()

    with open('reminders.txt') as f:
       for line in f:
           if (i % 2) == 0:
               event = line
               print(event)
               i += 1   
           else:
               reminder = line
               print(reminder)
               reminder = reminder.split(',')
               print(reminder)
               
               day = reminder[0]
               if day == 'today':
                   day = current_day
               hour = reminder[1]
               inthour = int(hour)
               if inthour < 10:
                   hour = '0' + str(hour)
               minute = reminder[2]
               if int(minute) < 10:
                   minute = '0' + minute
               timespan = reminder[3]
               timespan = timespan.replace('\n', '')
               remintime = (day + ' ' + hour + ' ' + minute +' ' + timespan)
               currtime = (current_day + ' ' +  current_hour + ' ' + current_minute + ' ' + current_timespan)
               print(remintime)
               print(currtime)
               i += 1    
               #if a reminder is triggered it will read the event related to it         
               if remintime == currtime:
                   event = event.replace(',', ' ')
                   engine.say(event)
                   engine.runAndWait()
                   time.sleep(20)
                   break 
                   #if everyday is not set then remove event from file afterwards

engine.stop()
    
                 

