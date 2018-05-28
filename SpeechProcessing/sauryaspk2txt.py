import speech_recognition as sr
from subprocess import call
import math
from pygame import mixer
import pyaudio
from google import search
import bs4 as bs
import urllib.request
import time
import pywapi
import os



r = sr.Recognizer()
mixer.init()  #initialize the mixer
x = 0
y = 0
extra = ""
recognised = ""
recengine = "google"
mode = 0
Name = ''
call(["espeak", "Adjusting for background noise"])



def Record():
     with sr.Microphone() as source:
          call(['espeak', Request])
          audio = r.listen(source)

     try:
          recognized = r.recognize_google(audio)
          call(['espeak', 'You said' + recognized])
          print(recognized)

     except:
          recognized = r.recognize_sphinx(audio)
          call(['espeak', 'You said' + recognized])
          print('sphinx' + recognized)

     return recognized

def Speak(Result):
    call(['espeak', Result])

def Request():
    Speak('Please Say Something.')

Speak('Adjusting Background Noise')
def Background():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)






Recorded = Record("Say something. I will say it back")
Speak("You just said" + Recorded)
Speak('Please Say something. I will try to understand.')




while True:

    Background()
    Recorded = Record()





    if 'your name' in Recorded:
        if 'what is' in Recorded:
            NameObj = open('Name','r' )
            Name = NameObj.read()
            NameObj.close()
            Speak('My name is' + Name)
            Request()


        elif 'change' in Recorded:
            Speak('What name do you want me to call?')
            Name = Record()
            Speak('Ok My name is' + Name + 'What else can I do for you?')

            NameObj = open('Name', 'r+')
            #Name = NameObj.read()
            #Name = re.sub('foobar', 'bar', text)
            NameObj.seek(0)
            NameObj.write(Name)
            NameObj.truncate()
            NameObj.close()

            Request()

    elif 'hello' in Recorded:

        NameObj = open('Name', 'r')
        Name = NameObj.read()
        NameObj.close()
        Called = Recorded[6:]

        if Name in Recorded:
            Speak('Hello Surya Prasad Bhandari')

        else:
            Speak('I am not' + '  ' + Called + '  ' + 'You are out of your mind.')

        Request()






    elif 'Google search' in Recorded:
        Speak('Search for what?')
        SearchFor = Record()

        for url in search(SearchFor, tld='com', lang='en', num=1, start=0, stop=1, pause=2.0):
            print(url)
            sauce = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(sauce, 'lxml')
            body = soup.p.text


            print(body)
            Speak(body)

            Request()


    elif 'time' in Recorded:
        if 'what' in Recorded or 'tell me' in Recorded:

            TimeNow = time.localtime()
            TimeH = TimeNow.tm_hour
            TimeM = TimeNow.tm_min

            if TimeH > 12:
                TimeH = TimeH - 12
                AP = "PM"
            else:
                AP = "AM"

            ex = ' '

            Speak('The time is' + str(TimeH) + ex + str(TimeM) + ex + AP)
            Request()

    elif 'set alarm' in Recorded:
        Speak('Tell me the time')
        hr = Record()

        timeas = str(123)

        if len(timeas) == 4:

            hr = int(timeas[:2])
            print(hr)
            min = int(timeas[2:])
            print(min)

        elif len(timeas) == 3:

            hr = int(timeas[:1])
            print(hr)
            min = int(timeas[1:])
            print(min)




            







    elif 'go to hell' in Recorded:
        Speak('No I will go to heaven. You will go to hell instead. Goodbye')
        break

    elif 'stop' in Recorded or 'shut down' in Recorded:
        Speak('Ok! I am off now')
        break

    else:
        Speak('Sorry I didn\'t understand' + Recorded + 'Please Say Something.')












