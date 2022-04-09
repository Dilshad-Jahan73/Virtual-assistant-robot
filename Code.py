import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
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
            print(command)
            if 'cortana' in command:
                command = command.replace('cortana', ' ')
                #print(command)

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
# play_song_on_youtube
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
#tell_me_about_info_from_wikipedia
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', ' ')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
#tell_me_joke
    elif 'joke' in command:
        jokes = pyjokes.get_joke()
        print(jokes)
        talk(jokes)
#when_did_not_understand
    else:
        talk('Sorry, I can not hear you but i can search it for you')
        pywhatkit.search(command)

while True:
    run_cortana()