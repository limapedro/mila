
# Import libraries

import speech_recognition as sr
import datetime


r = sr.Recognizer()

# Get the default microphone
with sr.Microphone() as source:
    # Listens to a command, using 
    
    while True:
        audio = r.listen(source)

        # Recognizes speech using Google as a service: online
        text = r.recognize_google(audio)

        if str(text).lower() == 'what time is':
            print(datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))