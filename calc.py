import pyttsx3

#Initiate Text to Speech
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#KEY WORDS++++++++++++++++++++++++++++++++++++++++++++++++++
add = ['add', 'plus', '+']
minus = ['minus', 'subtract', '-']
divide = ['divide', 'divided by', '/']
multiply = [ 'multiply', 'times', '*', "x"]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



def Calculate(string):

    #initiate sum variables
    num1 = 0
    num2 = 0
    op = ""
    answer = 0
    digit1 = False    
   
    for x in string.split():
        #if number is found
        if x.isdigit():
            #and the number hasnt already been found
            if digit1 == False:
                num1 = int(x)
                digit1 = True
            else:
                num2 = int(x)
                break
        #look for operator and convert into a form that python understands    
        if x in add:
            op = "+"
        elif x in minus:
            op = "-"
        elif x in divide:
            op = "/"
        elif x in multiply:
            op = "*"


    #do calculation
    if op=="+":
        answer = num1+num2
    elif op=="-":
        answer = num1-num2
    elif op=="*":
        answer = num1*num2
    elif op=="/":
        if num1 == 0 | num2 == 0:
            engine.say("cannot divide by 0")
            engine.runAndWait()
        else:
            answer = num1/num2
    else:
        engine.say("Please calculate a valid sum")
        engine.runAndWait()

    #convert these symbols back to plain english for the output
    if op == "/":
        op = "divided by"
    elif op == "-":
        op = "minus"

    answerstring = (num1, op, num2, "=", answer)
    engine.say(answerstring)
    engine.runAndWait()
    engine.stop()

