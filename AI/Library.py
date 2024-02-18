from pyttsx3 import speak
import datetime
import speech_recognition as sr
import json
import subprocess

def LoadMemory(FilePath: str) -> dict:
  with open(FilePath, 'r') as file:
     data: dict = json.load(file)
  return data

def save_memory(FilePath: str, data: dict):
   with open(FilePath, 'w') as file:
      json.dump(data, file, indent=2)

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("please say that again")
            return "None"
        return statement

def checkDetails(whatYouNeed: str):
    Memory: dict = LoadMemory('data.json')
    Name = Memory["Details"][1]["Name"]
    MyName = Memory["Details"][1]["MyName"]
    speakable = Memory["Details"][1]["speakable"]
    printable = Memory["Details"][1]["printable"]
    if whatYouNeed == "Name":
        return Name
    elif whatYouNeed == "MyName":
        return MyName
    elif whatYouNeed == "speakable":
        return speakable
    elif whatYouNeed == "printable":
        return printable
    else:
        pass