import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'spanish')
def hear_me():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Grabando...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="es-ES")
        except:
            text = ""
    return text

def say_me(text):

    engine.say(text)
    engine.runAndWait()
    engine.stop()
    return text

def save_mp3(text):
    engine.save_to_file(text, "speech.mp3")
    engine.runAndWait()
