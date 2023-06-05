import pyttsx3
SPEAK=1
#fucntion to convert text to speech
def text_to_speech(text):
    engine = pyttsx3.init()
    #change to famale voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(text)
    engine.runAndWait()
#fucntion to call text_to_speech based on value of global variable called SPEAK
def speak(text):
    if SPEAK:
        text_to_speech(text)
