import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import re
import file_filter
import tiktekto

Engine=pyttsx3.init('sapi5')
voices=Engine.getProperty('voices')
# print(voices[0])
Engine.setProperty("voice",voices[0].id)



def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()


def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir! ")
    else:
        speak("good evening sir!")
    speak(" I am jarvis please tell me how can i help you")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("listning....")
        # r.energy_threshold=250
        r.pause_threshold =1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said:{query}\n")
    
    except Exception :
        speak("soryy..")
        print("say that again please...")
        return "none"
    return query


def add(*args):
    total=0
    for arg in args:
        for i in arg:
            total=total+i
    return total




if __name__=="__main__":
   wish_me()
   start=True
   while start:
        query=take_command().lower()
        #logics for command:
        if "wikipedia"in query:
            speak("searching wikipedia.....")
            query=query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open email" in query:
            webbrowser.open("gmail.com")

        elif "open whats app" in query:
            webbrowser.open("whatsapp.com")

        elif"play music" in query:
            pass       
        elif"quit" in query:
            start=False
        elif "who are you" in query:
            speak("I am jarvis your friend.")
        elif "add" in query:
            num=re.compile("[0-9]"+"[0-9]")
            output=num.findall(query)
            new=[]
            for i in output:
                new.append(int(i))
            print(new)

            total=add(new)
            print(f"your sum is {total}")
        elif "python file" in query:
            speak("ok sir")
            os.startfile("D:\python")
        elif "filter" in query:
            speak("Enter path of the folder")
            folder_path=input("Enter Folder path here:")
            file_filter.filefilter(folder_path)
        elif "play game" in query:
            speak("You want to play tiktek to")
            query=take_command().lower()
            if "yes" in query:
                tiktekto.play_game()
            else:
                pass

            
            


#Still in Developing period  
            
            





