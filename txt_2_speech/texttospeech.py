from gtts import gTTS
import os

file = open("sample.txt")
text = file.read()

language = "en"

obj = gTTS(text=text,lang=language,slow=False)

obj.save("voice.mp3")

os.system("voice.mp3")