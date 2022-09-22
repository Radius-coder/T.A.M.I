from playsound import playsound
import datetime
import time
i = 0
alarm = ""
while True:
    current_time = datetime.datetime.now()
    current_day = current_time.strftime("%A").lower()
    current_hour = current_time.strftime("%I")
    current_minute = current_time.strftime("%M")
    current_timespan = current_time.strftime('%p').lower()

    #turn the numbers into the correct format
    current_time = current_day + ' ' + str(current_hour)+ " " + str(current_minute) + ' ' + current_timespan


    with open('alarms.txt') as f:
        for line in f:
            if (i % 2) == 0:
               alarm_day = line
               print(alarm_day)
               alarm_day = alarm_day.strip()
               i += 1
            else:
               alarm_time = line
               alarm_time = alarm_time.split(',')
               print(alarm_time)
               hour = alarm_time[0]
               print(hour)
               minute = alarm_time[1]
               print(minute)
               timespan = alarm_time[2]
               timespan = timespan.replace('\n', '')
               print(timespan)
               alarm = alarm_day + ' ' + hour + ' ' + minute + ' ' + timespan
               alarm = alarm.strip()
               i += 1
               print(alarm)
               print(current_time)

            
            
            if alarm and current_time == alarm:
                print("Found set alarm.")
                counter = 0
                while counter<=30:
                    #sound alarm
                    playsound("alarm.wav")
                    f = open("alarmTriggered.txt", 'w')
                    f.write('1')
                    f.close()
                    f = open("alarmTriggered.txt", 'r')
                    alarm_triggered = f.readline()
                    f.close()
                    time.sleep(1)
                    if alarm_triggered == '0':
                        alarm = ""
                        break
                    else:
                        counter +=1
                    if counter == 29:
                        f = open("alarmTriggered.txt", 'w')
                        f.write('0')
                        f.close()
                        

