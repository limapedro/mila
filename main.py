
# Import libraries

import speech_recognition as sr

r = sr.Recognizer()

# Get the default microphone
with sr.Microphone() as source:
    # Listens to a command, using 
    
    while True:
        audio = r.listen(source)

        text = r.recognize_google(audio)

        print(text)