import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir")

    else:
        speak("Good Evening! Sir")

    speak("My name is JETT and I am Your Personal Voice Assistant. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'how are you' in query:
            speak('I am Fine! how are you !. Tell Me how may I help You Sir !')

        elif 'about yourself' in query:
            speak('Hi ! i am JETT , your personal assistant. my version is 1.o . I can do several things for you ,such as '
                  'getting information from wikipedia,opening websites,playing music for you ,telling current weather conditions ,'
                  'searching places nearby you and many more ! Thank You ')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            speak("Tell me Which Song You Want to listen ! ")
            song = takeCommand().lower()
            if song != 'none':
                print(f"Now Playing.....\n {song}")
                webbrowser.open(f"https://gaana.com/song/{song}")


            # music_dir = "E:\\Music"
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open brave ' in query:
            brave = "C:\\ProgramData\\Microsoft\\Windows\Start Menu\\Programs\\Brave.lnk"
            os.startfile(brave)

        elif 'weather' in query:
            webbrowser.open("current weather")

        elif 'near me' in query:
            webbrowser.open(query)

        elif 'news' in query:
            webbrowser.open(query)


        elif 'stop' in query:
            exit()