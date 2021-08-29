# Importing all liraries
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import pyjokes
import wikipedia

# recognizing the microphone
listener = sr.Recognizer()
alexa= pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voices', voices[1].id)

# talking function 
def talk(text):
    alexa.say(text)
    alexa.runAndWait()

# Here user command
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening for speech.........")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                print(command)
                command = command.replace('alex', '')
    except:
        pass
    return command

# running the machine
def run_alexa():
    command = take_command()
    print(command)
# Commands
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')

# running the machine with a loop
while True:
    run_alexa()