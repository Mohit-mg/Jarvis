# # import file_filter
# # import os

# # file_filter.filefilter("C:\\Users\\mohit\\Downloads")

# # if os.path.exists("C:\\Users\\mohit\\Desktop\\jarvis\\movies"):
# #     print("already exist")
# # else:
# #     os.mkdir("C:\\Users\\mohit\\Desktop\\jarvis\\movies")
# import tiktekto
# tiktekto.play_game()

import pyttsx3
import speech_recognition as sr

Engine=pyttsx3.init('sapi5')
voices=Engine.getProperty('voices')
# print(voices[0])
Engine.setProperty("voice",voices[0].id)

def speak(audio):
    Engine.say(audio)
    Engine.runAndWait()

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

if __name__ == "__main__":
    query=take_command().lower()
    speak(query)
    