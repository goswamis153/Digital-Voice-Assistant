import pyttsx3
import datetime
import os
import webbrowser
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning!')
    elif hour>=12 and hour<18:
        speak('Good afternoon!')
    else:
        speak('Good evening')
    
    speak('i am zira How may i help you')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        # r.energy_threshold = 20
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()
    

if __name__=="__main__":
    wishMe()
    i = 10
    while i>1:
        query = takeCommand()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            
            music_dir = "D:\\sound"
            songs = os.listdir(music_dir)
            print(songs)
            speak('playing music') 
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'who are you' or 'what can you do for me' in query:
            speak("Hello  I am zira your virtual voice assistant i can do certain task for you like playing music opening google,youtube and gather information from wikipedia ")

        elif 'quit' in query :
            speak('terminating the program signing off')
            exit()
        
        query = ''

        i-=1