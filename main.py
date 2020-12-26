
# Import libraries

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import pyaudio
import json
import pyttsx3
# Import the core lib
from core import SystemInfo

# Speech Synthesis
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Speech Recognition



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
        # result is a string
        result = rec.Result()
        # convert it to a json/dictionary
        result = json.loads(result)
        text = result['text']

        if text == 'what time is' or text == 'tell me the time':
            speak(SystemInfo.get_time())
