from gtts import gTTS
from playsound import playsound
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "안녕하세요. 만나서 반갑습니다."

tts = gTTS(text=text, lang='ko')
tts.save(r"D:\2022. Sophomore\Python Study\220730_project_1_to_4\08_hi.mp3")

playsound("08_hi.mp3")
