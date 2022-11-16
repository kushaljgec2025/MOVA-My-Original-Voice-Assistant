import pyttsx3

import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0],id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    speak("Hey!")
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=10 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Afternoon!")  
    speak(" I am MOVA , How can i help u? ")      
def takeCommand():
    # it takes microphone input and string return
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Litsening.........")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing........")
        query=r.recognize_google(audio,  language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e :
        # print(e)
        print(" Sorry !Say That Again Plaese! Sir")
        return "None"
    return query
if __name__== "__main__":
    wishMe()
    if 1:
        query=takeCommand().lower()


        if 'wikipedia' in query:
           query=query.replace("wikipedia","")
           speak("Serching in  wikipedia")
           result=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           print(result)
           speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time now' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Time is  { strTime} ")
        elif 'open code' in query:
            codePath="C:\\Users\\91891\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

