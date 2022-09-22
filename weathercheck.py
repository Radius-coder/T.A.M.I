#modules needed to get JSON data, get cand change time data, import and read CSV files,
# to change text to speech and to recognise speech.
import requests
import datetime
import csv
import pyttsx3
import speech_recognition as sr

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#Keywords=======================================================================================================
weatherRequest = ["weather", "weather?", "rain", "sunny", "snow", "thunder", "temperature?", "temperature"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "today", "tomorrow"]
times = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
timeSpan = ["am", "pm"]
cities = []
#================================================================================================================

#API key and url
apik = "ef46d727cacca5bb1049ba8f64440609"
rurl = "http://api.openweathermap.org/data/2.5/forecast?"


def loadWeather(string):
 
    #Open CSV of city data and read eachline
    csvFile = open('city.csv', encoding="utf8")
    data = csvFile.read()
    #change data to lowercase
    data = data.lower()
    #remove all punctuation from CSV file.
    punctuation = '''”"?'''
    no_punc =''
    for x in data:
        if x not in punctuation:
            no_punc = no_punc + x
    #Each city name from the CSV file is added into the cities array
    cities = no_punc.split(",")
    cities.pop()
    csvFile.close()

    #Get and split user string for analysing
    userString = string
    stringLoop = userString.split()

    #Boolean initiators to check if the required data has been found
    set = False #has the weather been requested
    citySet = False
    daySet = False
    timeSet = False
    timeSpanSet = False
    wrongCity = False
    
    day = ""
    time = ""

    #Analyser
    for x in stringLoop:
        if x in weatherRequest:
            #Weather has been requested in string
            set = True
            #find matching keywords
            for x in stringLoop:
                if x in days:
                    day = x
                    daySet = True
                if x in cities:
                    city = x
                    citySet=True
                if x in times:
                    time = x
                    timeSet = True
                #checking if 'am' or 'pm' has been said
                if x in timeSpan and timeSet == True:
                    time = time+x
                    timeSpanSet = True
                    print(time)



                    
    #Checking if weather has been requested but a city has not been set    
    if set == True and citySet==False:
        

        #Speech recognition is activated to hear the city name
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1) 
            engine.say("What place would you like to know the weather?")
            engine.runAndWait()
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            string = r.recognize_google(audio)
            userString = string.lower()
            print("Google Speech Recognition thinks you said " + string)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        #Recognised speech is split and checked for a mentioned City
        stringLoop = userString.split()
        for x in stringLoop:
            if x in cities:
                city = x
                citySet = True
            else:
                engine.say("Cannot find the weather in this city, try a city inside the United Kingdom.")
                engine.runAndWait()
                wrongCity = True
                break
    if not wrongCity:            
        #If everything is done and the City is set then start gathering weather data    
        if citySet:
            url = f"{rurl}appid={apik}&q={city}&units=metric"
            r = requests.get(url)
            json_data = r.json()
            #print(day)

            #make an array for each day 
            temparr = []
            datearr = []
            dayarr = []
            descrarr = []
            timearr = []
                
            for data in json_data['list']:
                temp = data['main']['temp']
                temparr.append(temp)
                date = data['dt_txt']
                dt_tuple=tuple([int(x) for x in date[:10].split('-')])+tuple([int(x) for x in date[11:].split(':')])
                datetimeobj=datetime.datetime(*dt_tuple)
                dayarr.append(datetimeobj.strftime("%A"))
                timearr.append(datetimeobj.strftime("%I %p"))
                datearr.append(date)
                descr = data['weather'][0]['description']
                descrarr.append(descr)
            #here for debugging
            
            print(f"Date of weather check : {date}")
            #print(f"It is {descr} with a temperature of {temp}\n")

        #i have to get the current day first. if its monday and between 0 and 2 then save a value of 0 for the first day if they requested wednesday then we would need to get to 3 days later but in the array theres a value every 3 hours so it has to search the 21st value in the array. this is because there are 7 values in each day give or take as if the user requests a time at 11 then the array will start from 12 o clock leaving 3 values in the day. this can be stopped by displaying the midday time of future days or calculating the highs and lows. or datetime to show the correct temperature
        #to the user if they want the current temp or a later one
        #if we get the current date and time then we can know how many days later we will show the temp
        #remove duplicates from available days
        #dayarr = list(dict.fromkeys(dayarr))
        #print(dayarr)
        
        x = datetime.datetime.now()
        #print(x.strftime("%A"))
        #print(day)
        day = day.capitalize()
        #function to return the requested temp, takes in the day and 3 arrays
        #testing array works correctly 
        if day == "Today" or day == x.strftime("%A") or daySet==False:
            engine.say(f"Temp today: {temparr[0]} degrees celcius, at {timearr[0]}")
            engine.runAndWait()
        if day == "Tomorrow":
            engine.say(f"Temp tomorrow: {temparr[8]} degrees celcius, at {timearr[8]}")
            engine.runAndWait()
        elif day in dayarr:
            #get position of the chosen day in the dayarr and print this temperature
            i = dayarr.index(day)
            #print(i)
            engine.say(f"Temp on: {day} is {temparr[i+5]} degrees celcius, at {timearr[i+5]}")
            engine.runAndWait()
            
        engine.stop()
    else:
        engine.stop()

    


            
