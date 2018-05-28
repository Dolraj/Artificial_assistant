import pyttsx
import speech_recognition as sr
import pocketsphinx
import pyaudio
import random
import os

engine = pyttsx.init()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        a = r.listen(source)

        try:
                return r.recognize_sphinx(a)
            
        except sr.UnknownValueError:
            print('could not understand audio')
            
        except sr.RequestError as e:
                print("Recog Error; (0)".format(e))
                
        return ""    
        
        
def media():
    speak('ok sir')
    speak('startingrequired application')
    speak('what do you want me to play for you')
    k = listen()
    speak('ok sir playing' + k + 'for you')
    os.startfile('C:\Users\Grishma\Music\Free YouTube Downloader'+k+'.mp3')

def shutdown():
    speak('understood sir')
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')

def gooffline():
    speak('ok sir')
    speak('closing all system')
    speak('disconnecting to servers')
    speak('going offline')
    quit()
    
def speak(text):
    engine.say(text)
    engine.runAndWait()
def online():
    speak('Hello sir')
    speak('starting all system application')
    speak('installing all drivers')
    speak('every driver is installed')
    speak('now i am online sir')
def mainfunction():
    a = r.listen(source)
    user = r.recognize_google(a)
    print(user)

    if user == "A":
        online()
        
    elif user == "B":
        media()
    
    elif user == "down":
        goofline()
        
    elif user == "shutdown":
        shutdown()
    elif user in['hi','hey','whatsup','sup','good']:
        d = random.choice(['hey','hi','sub'])
        speak(d)
    
speak('HEllo')

if __name__ == "__main__":
      r = sr.Recognizer()
      with sr.Microphone() as source:
        while 1:
            mainfunction()
