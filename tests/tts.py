import pyttsx3
engine = pyttsx3.init()

engine.say("I will speak this text")
engine.runAndWait()

voices = engine.getProperty('voices')

#print(voices)