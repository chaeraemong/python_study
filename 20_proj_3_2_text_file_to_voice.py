from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '10_text.txt'
with open(file_path, 'rt', encoding='UTF8')as f:
    read_file=f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"D:\2022. Sophomore\Python Study\220730_project_1_to_4\11_hi_2.mp3")

playsound("11_hi_2.mp3")
