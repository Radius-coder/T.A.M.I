from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi.errors import DictionaryApiError
from spellchecker import SpellChecker
import pyttsx3

spell = SpellChecker()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-20)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

dictionaryarr = ["what is the meaning of", "what is the definition", "what's the meaning of", "what's the meaning", "what is", "what", "is", "of", "definition",  "define", "dictionary", "what's", "a"]
greetings = ["hi","hello","hiya","hey", "howdy", "yo", "how are you", "hows it going", "how you feeling", "whats up", "you good"]

def Define(string):
    for word in dictionaryarr:
        if word in string:
            string = string.replace(word, "", 1)
            print(string)
    for word in greetings:
        if word in string:
            string = string.replace(word, "")
            print(string)

    if string != "":    
        string = spell.correction(string)
        print(string)

    #Open connection to dictionary databse, sending our request
    #if word doesnt exist then let user know
    with DictionaryApiClient() as client:
        try:
            parser = client.fetch_parser(string)
        except DictionaryApiError:
            print("Word not found buddy")
            engine.say("I could not find the word you were looking for.")
            engine.runAndWait()
        else:
            definitionsarr = parser.get_all_definitions()

            for x in definitionsarr:
                print(x)
                engine.say(x)
                engine.runAndWait()

    engine.stop()


    #sensor to detect people nearby
    #
