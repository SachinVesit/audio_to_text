import comparee
from array import *
import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

file_audio = sr.AudioFile('u.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
file = open("record.txt","w")
file.write(r.recognize_google(audio_text))
file.close()

#attachment
print(r.recognize_google(audio_text))
comparee.term