import speech_recognition as sr
import pyttsx

speech_engine = pyttsx.init()
speech_engine.setProperty('rate', 150)
def speak(text):
    speech_engine.say(text)
    speech_engine.runAndWait()

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    speak("Say something!")
    audio = r.listen(source)
try:
    audio = r.listen(source)
    a = r.recognize_google(audio)
    print ("you speak" + a)
except sr.UnknownValueError:
    speak("I could not understand audio")
except sr.RequestError as e:
    speak("Could not request results from Google Speech Recognition service; {0}" .format(e))


