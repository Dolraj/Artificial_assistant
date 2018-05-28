import pyttsx
import speech_recognition as sr
import pyaudio

engine = pyttsx.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def mainfunction():
    audio = r.listen(source)
    user = r.recognize_google_cloud(audio)
    user = r.recognize_sphinx(a)
    print(user)
    
    
speak('I am captian and made by Grish Poudel')

if __name__ == "__main__":
      r = sr.Recognizer()
      with sr.Microphone() as source:
        while 1:
            mainfunction()
