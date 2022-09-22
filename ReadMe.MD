# Prerequistes:
'main.py' will automatically run the installation process on start up.
Plugged in microphone,
Connected to internet,
Microsoft's Windows operating system,

# How to run:
Launch main.py to run this program. 

## What is it?
TAMI is a voice controleld assistant

## Why is it?
I always liked the idea of voice-controlled systems like Iron Man’s Jarvis, but it was not until I watched Artificial Intelligence by Steven Spielberg[1]  when I was really inspired. In this movie is an intelligent, walking and talking teddy bear that was used by the kids to play with. It was also from this I produced the name TAMI, standing for Talking and Moving Intelligence. I liked the idea of bringing a fantasy creature to life whether it is a teddy bear or something from a movie or game like a dragon. 
I would like to see my project be used in the health sector as I believe it can help patients with social anxiety or disabilities like dementia. My computer will remind them of things they need to do such as taking medicine, completing a task, writing a list as well as assisting the user with any queries such as what restaurants are open nearby, sending an email or playing music. 
The computer can also be modified to aim at children as an educational toy as my computer could provide answers to many questions using the internet or used to teach math. 

## How to add functions
All functions are ran through 'analyse.py'.'analyze.py' checks the user's input and if a trigger word (the word to activate a function) is said then the appropriate function is activated. When creating a function you must allow it to take a string. The string is what is sent to  'analyze.py' after the user has said something into the mic. From there, you can do anything with that function and make it output any voice (or not) using the pyttsx3 engine.

### Example of a function I made
[This function uses Tuya's API to connect to my smart light.](https://www.youtube.com/shorts/Pj2tcwc5rWc) This opens up a lot of doors as a voice assitant because you can control any smart device with it. You can create schedules on them or combine devices for a better effect. For example you could have an alarm that turns on the lights and plays a song at the same time. If the user has the right equipment you could even boil their kettle or start the hoovering. 

## Future of this project
I have already put this program onto a raspberyy Pi and safely contained with in a teddy bear. I was happy with the results but I would like to see simple movement in the body and a custom voice so it suits the teddy bear. I would also like to have a personliased experience. I want TAMI to take in when for example, the user sets an alarm. It will study the time they created the alarm and the time they set it for and how many times they set that exact one. If it hits so many times then TAMI will automcatically say at that time something like 'Would you like to set an alarm for 6.30am on Monday *user's name*  ?' and if the user says yes then the function reccomendation stays otherwise, a counter will go down to show it is not as used. When it's low enough then it wont recommend that function. This concept can be used for things like timers, playing music. turning on and off lights etc.

Feel free to ask me any questions.
