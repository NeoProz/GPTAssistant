import speech_recognition as sr
import os
import openai
import pyttsx3


openai.api_key = "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"

r = sr.Recognizer()
engine = pyttsx3.init()

def gr(p):
    completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[{"role": "user", "content": p}]
)
    return completion.choices[0].message.content

while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    x =  r.recognize_google(audio)
    print("You: "+x)
    engine.say(gr(x))
    print("Assistant: "+gr(x))
    engine.runAndWait()