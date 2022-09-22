from playsound import playsound
import time
f = open('timer.txt', 'r')
counter = f.readline()
time.sleep(int(counter))
playsound("alarm.wav")
print("end")
