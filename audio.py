from gtts import gTTS #google text to speech tanslator
import os
f=open('1.txt') #opening  a text file which we want to convert into speech
x=f.read() #read that file and store into x
language='en' #language is english wich we want to convert
audio=gTTS(text=x,lang=language,slow=False) #gtts convert our txt file into
audio.save('1.wav')                          #into audio using prameters text =x wich contains our text lang we want to convert
os.system('1.wav' )    #save audio in wav format cnly gtts only convert into wav format