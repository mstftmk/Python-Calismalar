#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:46:48 2020

@author: mustafa
"""
import pyttsx3


voice = pyttsx3.init() #Seslendirme
deneme = 0
kalanHak = 3
baslangic = 0
bulundu = False
kisiMevcut = False

kisiler = {"MUSTAFA": 99, "BATUHAN": 85, "AYŞE": 32}

isim = input("İsminiz? ")

for i in kisiler:
    if i == isim.upper():
        kisiMevcut = True
        voice.say("Hoşgeldin " + str(isim))
        voice.runAndWait()
        break
        
if kisiMevcut == True:
    while deneme <= 3 and kalanHak > 0:   
        deneme += 1
        soru = input("Şifre?")
        if kisiler[isim.upper()] == int(soru):
            print("Şifre doğru..")
            voice.say("Şifre doğru")
            voice.runAndWait()
            break
        else:
            print("Şifre yanlış..")
            voice.say("Şifre yanlış")
            voice.runAndWait()
            kalanHak -= 1
            print("Kalan hakkınız: ", kalanHak)
            
else:
    voice.say("Böyle bir isim sistemde mevcut değil")
    voice.runAndWait()
    

if kalanHak == 0:
    print("Hakkıınız bitti!")
    voice.say("Hakkınız bitti")
    voice.runAndWait()
if kisiMevcut == True:
        
    sifre_bul = input("Şifreyi çözmek ister misiniz? E veya H ")
    if sifre_bul.upper() == "E":
            
        while bulundu == False:
            if baslangic == kisiler[isim.upper()]:
                bulundu = True
                print("Şifre bulundu")
                print("Şifre", baslangic)
            else:
                print(baslangic)
                baslangic += 1                
    elif sifre_bul.upper() == "H":
        print("Şifre çözülmedi.")
    else:
        print("Hatalı tuşlama. Şifre çözülmedi.")







