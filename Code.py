import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit

listener = sr.Recognizer()
cortana = pyttsx3.init()
# voices = cortana.getProperty('voices')
# cortana.setProperty('voice', voices[1].id)

def talk(text):
    cortana.say(text)
    cortana.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cortana' in command:
                command = command.replace('cortana', '')

    except:
        pass
    return command

def run_cortana():
    command = take_command()
# Knowing_time
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

run_cortana()