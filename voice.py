import speech_recognition as sr
from time import sleep
import bozkurt
import hakn
from discord import SyncWebhook
from playsound import playsound
from os import system as yaz
import random
from unidecode import unidecode

dc = SyncWebhook.from_url("https://discord.com/api/webhooks/1173634227997245460/NiFHYw23THFc2PvaMzUdraLYYtm-3-vqzftWdmCnVUowsNDiK2taJO-XY_HFcVjdyOCJ")



def robot_kolu_hareket_et(acı):
    dc.send(acı)

def kelimesayısı(cumle):
    words = cumle.split()
    return len(words)

def çalbozkurt():
                list = ['İşte Öyle Birşey - Erol Evgin','B. Anıl Emre Daldal','Gönül İster - Duman','Mutsuz Punk - Yasemin mori','Bu Aşk Fazla Sana - Şebnem Ferah','Boş BardaK - Fettah Can','Endamın Yeter - Kıraç','Cevapsız Sorular - Manga','Nasıl Öğrendin Unutmayı - Kolpa','Gurur Benim Neyime - Kolpa','Değmesin Ellerimiz - Model','Beni Sen İnandır - Pinhai','Kendime Yalan Söyledim - Seksendört','Hayır Olamaz - Seksendört','Sigara - Müslüm Gürses','Evleniyormuşsun Bugün']
                list2 = ['Kolay Değildir - Duman','Anlamazdın - Ayla Dikmen','Deniz Üstü Köpürür - Cem Karaca','Tutamıyorum Zamanı - Müslüm Gürses', 'Sevdim Seni Bir Kere - Barış Akarsu','Yanarım Sertab Erener','Kimdir O - Barış Akarsu']
                sarki = random.choice(list)
                sleep(0.2)
                yaz("adb shell am start -n com.spotify.music/.MainActivity")
                sleep(2)
                yaz("adb shell input tap 358 1400")
                sleep(1)
                yaz("adb shell input tap 358 300")
                sleep(0.5)
                yaz(f"adb shell input text '{unidecode(sarki)}'")
                sleep(1)
                yaz("adb shell input keyevent KEYCODE_ENTER")
                sleep(0.7)
                yaz("adb shell input tap 358 320")

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



while True:
    komut = sesi_anla()


    if komut:
        komut2 = komut.lower()
        if kelimesayısı(komut2) <= int(3):
            komut3 = komut2 + " hakan" + " hakan" + " hakan"
            print(komut3)

        else:
            komut3 = komut2

        derece = str(komut3.split(' ')[0])
        yön3 = str(komut3.split(' ')[2])
        derece2 = str(90)
        if yön3:
            yön = yön3.lower()
            print(f"Derece: {derece}\nYön : {yön3}")
            if "sağ" in yön:
                yön2 = str(1)
                print(yön2 + derece)
                robot_kolu_hareket_et(yön2 + derece)
                

            elif "sol" in yön:
                yön2 = str(2)
                print(yön2 + derece)
                robot_kolu_hareket_et(yön2 + derece)
                
            #robot_kolu_hareket_et(3)
            #print(ser.read())

            elif "aşağ" in yön:
                yön2 = str(3)
                print(yön2 + derece)
                robot_kolu_hareket_et(yön2 + derece)
                            
        
            elif "yukar" in yön:
                yön2 = str(4)
                print(yön2 + derece)
                robot_kolu_hareket_et(yön2 + derece)
                
            
            elif "tut" in komut2:
                yön2 = str(6)
                robot_kolu_hareket_et(yön2 + derece2)
                
            elif "bırak" in komut2:
                yön2 = str(7)
                robot_kolu_hareket_et(yön2 + derece2)

            elif "şarkı" in komut2:
                hakn.speak("Tabi")
                çalbozkurt()

            elif "telefonu aç" in komut2:
                 yaz("adb shell input keyevent 5")


            elif "Telefonu kapat" in komut2:
                 yaz("adb shell input keyevent KEYCODE_ENDCALL")
            
            elif "mesaj gönder" in komut2:
                 yaz("adb shell service call isms 7 i32 0 s16 'null' s16 '+905315297933' s16 'null' s16 "'LALALALLALALALAL_PROFİL_FOTOĞRAFIN_EFSANE_ÖTESİ'"")


            elif "ırk" in komut2:
                file = "sesdosyasi.mp3"
                playsound(file)
            

            elif "kendini kapat" in komut2:
                break



                



#ser.close()
