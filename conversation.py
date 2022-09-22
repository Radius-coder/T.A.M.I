import numpy as np
import random 
import pyttsx3


#check for negative words like not these do the opposite
#not good is bad and not bad is good


#human inputs
good = np.array(["good", "amazing", "perfect", "fine", "great", "lovely", "bless"])

bad = np.array(["bad", "sad", "angry", "mad", "unhappy", "upset", "terrible", "shit", "crap"])

no = np.array(["not", "no", "un", "negative", "too"])

cpuCheck = np.array(["how are you", "hows it going", "how you feeling", "whats up", "and you", "you good"])

#computer replies

hi = np.array(["hi","hello","hiya","hey", "howdy", "yo"])

wellbeingcheck = np.array(["how are you", "hows it going", "how you feeling", "whats up"])

def Feeling(string):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    neg = False
    chck = False
       
    replies = []
    replyone = string
    replies = replyone.split()

    for x in replies:
        if replyone == "exit":
            break
        #if they say no
        if x in no:
            #print("negative used...")
            neg = True
        #could have user lists and computer lists for appropriate but random replies
        
            
        elif neg==False:        
            if x in good:
                print("Thats "+random.choice(good))
            elif x in bad:
                print("Thats "+random.choice(bad))
                    
        elif neg==True:
            if x in bad:
                print("Thats good")
                neg = False
            if x in good:
                print("Thats bad")
                neg = False
            neg = False
        if x in hi:
            engine.say(random.choice(hi))
            engine.runAndWait()
        #for every reply in CPUcheck check if the user said one
        #then stop loop
        if chck == False:
            for z in cpuCheck:
                if z in replyone:
                    chck = True
    if chck == True:
        engine.say("I am doing "+random.choice(good)+" thanks")
        engine.runAndWait()
        chck = False
    engine.stop()

#csv file of replies and questions then studies data of conversations to see which replies are said to what questions. then based on the data and the plot it will predict a reply to a users question by finding the one with the highest relationship rating (correlation)
