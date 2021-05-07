import pyttsx3
import datetime
import speech_recognition as sr
import wheel
import pyaudio
import wikipedia
import webbrowser
import os
import subprocess

dir="D:\Spotify.exe.lnk"
calcdir="C:\Windows\System32\calc.exe"
covdir="D:\COVID.exe.lnk"

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice' , voices[1].id)
print(voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! How can I help You?")
    elif hour>12 and hour<18:
        speak("Good Afternoon! How can I help You?")
    else:
        speak("Good Evening! How can I help You?")



def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognising....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")

    except Exception as e:
        # print(e)

        print("Please Say that again.....")
        return "None"
    return query


if __name__=="__main__":
    wishMe()


    #Logic for executing tasks

    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'github' in query:
            webbrowser.open("github.com")

        elif 'replit' in query:
            webbrowser.open("replit.com")

        elif 'spotify' in query:
            os.startfile(dir)
            os.system(dir)
            # subprocess.Popen([dir])
            # subprocess.call(dir)

        elif 'calculator' in query:
            speak("Opening Calculator....")
            os.startfile(calcdir)
            # os.system(calcdir)

        elif 'covid' in query:
            speak("Searching for COVID cases in Pune")
            os.system(covdir)

        elif 'notepad' in query:
            file1 = open("MyFile.txt", "a")
            speak("What do you want to write in the notepad:")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.........")
                r.pause_threshold = 0.5
                audio = r.listen(source)

            try:
                print("Recognising....")
                query = r.recognize_google(audio, language='en-in')
                file1.write(query+ " ")


            except Exception as e:
                pass



        elif 'exit' or 'quit' or 'bye' in query:
            speak("Exiting...")
            break





#pip install pipwin
#pipwin install pyaudio
