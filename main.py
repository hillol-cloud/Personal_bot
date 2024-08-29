import datetime
import wikipedia
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
from tkinter import *
import threading

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google_cloud(voice)
            command = command.lower()
            if 'Ace' in command:
                command = command.replace('Ace', '')
                print(command)
    except:
        pass
    return command

def run_Ace():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif ' joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again.')


def start_assistant():
    """Start the assistant when the button is pressed"""
    threading.Thread(target=take_command).start()

root = Tk()
root.title("Personal Assistant")
root.geometry("300x200")

# Add a button to start the assistant
start_button = Button(root, text="Start Assistant", command=start_assistant)
start_button.pack(pady=20)

root.mainloop()