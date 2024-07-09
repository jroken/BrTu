import speech_recognition as sr
import os
from playsound import playsound
from gtts import gTTS



def sesi_anla():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Sesinizi bekliyorum...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:

        print("Ses anlaşılıyor...")
        komut = recognizer.recognize_google(audio, language="tr-TR")
        print("Anlaşılan komut:", komut)
        return komut
    except sr.UnknownValueError:
        print("Üzgünüm, ses anlaşılamadı.")
        return None
    except sr.RequestError as e:
        print(f"Ses tanıma servisine erişim sağlanamadı; {e}")
        return None

import random
def speak(string):
    tts = gTTS(text=string, lang='tr', slow=False)
    rand = random.randint(1, 30)
    sayi = 1 + rand
    file = f"answer{sayi}.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)