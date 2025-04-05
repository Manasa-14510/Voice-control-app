import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()

def alexa_command():
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            listener.adjust_for_ambient_noise(source)  # Adjusts to background noise levels
            print("Listening...")
            voice = listener.listen(source)  # Listen for audio
            command = listener.recognize_google(voice)  # Recognize speech using Google API
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa","")
                print(command)

            
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return command
def run_alexa():
    command=alexa_command()
    print(command)
    if "play" in command:
        song=command.replace("Play","")
        talk("Playing" +song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M")
        print("time")
        talk("Current time is"+time)
    elif "superstar" in command:
        person=command.replace("superstar","")
        info=wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif "joke" in command:
        person=command.replace("superstar","")
        info=wikipedia.summary(person,2)
        print(info)
        talk(pyjokes.get_joke())


run_alexa()
