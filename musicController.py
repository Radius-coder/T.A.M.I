from pynput.keyboard import Key, Controller
import time
import speech_recognition as sr

keyboard = Controller()
 
def changeWindow():
    keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    time.sleep(1)               
    keyboard.release(Key.tab)
    keyboard.release(Key.alt)
    
while True:
    #checks if user is requesting anohter song or just continuing their current song
    file = open('musicplaying.txt', 'r')
    state = file.readline()
    file.close()
    if state == "0":
        exit()


    #Speech recognition is activated to hear the city name
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Say something!")
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


    choice = userString
    count = choice.split()
  
    if len(count) <= 1:
          if choice == "pause":
              changeWindow()
              time.sleep(1)
              keyboard.press(Key.space)
              keyboard.release(Key.space)
              changeWindow()
          elif choice == "play" or choice == "resume":
              changeWindow()
              time.sleep(1)
              keyboard.press(Key.space)
              keyboard.release(Key.space)
              changeWindow()
          elif choice == "replay" or choice == "restart":
              changeWindow()
              time.sleep(2)
              keyboard.press(Key.f5)
              keyboard.release(Key.f5)
              time.sleep(5)
              keyboard.press(Key.space)
              keyboard.release(
                  Key.space)
              changeWindow()
          elif choice == "stop":
              changeWindow()
              keyboard.press(Key.ctrl)
              keyboard.press('w')
              time.sleep(1)
              keyboard.release('w')
              keyboard.release(Key.ctrl)
              #change a file so the analyser can see if music is already
              #playing before it searches another one#
              file = open('musicplaying.txt', 'w')
              file.write("0")
              file.close()
              exit()
