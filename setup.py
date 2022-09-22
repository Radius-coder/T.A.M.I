import subprocess

def install(name):
    subprocess.call(['pip', 'install', name])
    
if __name__ == "__main__":
    print("Installing dictionary API")
    install('python-freeDictionaryAPI')
    print("Installing speech recognition API")
    install('SpeechRecognition')
    print("Installing text to speech API")
    install('pyttsx3')
    print("Installing playsound")
    install('playsound')
    print("Installing auto-correct API")
    install('pyspellchecker')
    print("Installing keyboard controller API")
    install('pynput')

