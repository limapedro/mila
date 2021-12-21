
# Import libraries

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
<<<<<<< Updated upstream
=======
import json
import pyttsx3
# Import the core lib
from core import SystemInfo

# Import NLU classifier
from nlu.classifier import classify

# Speech Synthesis
engine = pyttsx3.init()

a = 2

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition
>>>>>>> Stashed changes

model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())