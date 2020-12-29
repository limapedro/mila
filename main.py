
# Import libraries

#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import os
import subprocess
import pyaudio
import json
import pyttsx3
# Import the core lib
from core import SystemInfo
from core.system import Runner

# Import NLU classifier
from nlu.classifier import classify

# Runner
runner = Runner()

# Speech Synthesis
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def evaluale(text):
    output = classify(text)

    entity = output['entity']
    conf = output['conf']

    print('You said: {}  Confidence: {}', text, conf)
    
    if entity == 'time\\getTime':
         speak(SystemInfo.get_time())
    if entity == 'time\\getDate':
        speak(SystemInfo.get_date())
    elif entity == 'time\\getYear':
        speak(SystemInfo.get_year())
    elif entity == 'open\\notepad':
        speak('ok, opening notepad')
        os.system('notepad.exe')
    elif entity == 'open\\chrome':
        speak('ok, opening google chrome')
        os.system('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
    elif entity == 'open\\mpc':
        speak('ok, opening media player classic')
        os.system('"C:\Program Files\MPC-HC\mpc-hc64.exe"')
    elif entity == 'open\\vlc':
        speak('ok, opening vlc')
        os.system('"C:\Program Files\VideoLAN\VLC\vlc.exe"')


    else:
        pass

# Speech Recognition

model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # result is a string
        result = rec.Result()
        # convert it to a json/dictionary
        result = json.loads(result)
        text = result['text']
        evaluale(text)
        
        