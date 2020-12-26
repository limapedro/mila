
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
        google = r.recognize_google(audio)
        sphinx = r.recognize_sphinx(audio)

        print('Google: [{}]\nSphinx: {}\n\n'.format(google, sphinx))
