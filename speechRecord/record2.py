import attachment
from array import *
import speech_recognition as sr
print(sr.__version__)
r = sr.Recognizer()

file_audio = sr.AudioFile('hello.wav')

with file_audio as source:
   audio_text = r.record(source)

print(type(audio_text))
file = open("record.txt","w")
file.write(r.recognize_google(audio_text))
file.close()

f1 = open("record.txt", 'r')
f2 = open("Badwords.txt", 'r')
output = open("output.txt", 'w')

file1 = set(f1)
file2 = set(f2)
#file(word,freq)
words1 = f1.read().split()
words2 = f2.read().split()
words = ('u',['kill','hello'])
for line in f1:
    word, freq = line.split()
    if words1 in words:
        output.write("Both files have the following words: " + file1.intersection(words))
f1.close()
f2.close()
f=open("output.txt",'r+')
print(f.read())
output.close()
"""
for i in words:
    if words1 == words[i]:
        print(words[i])"""
#print(r.recognize_google(audio_text))