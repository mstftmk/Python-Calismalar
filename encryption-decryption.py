# -*- coding: utf-8 -*-

import time

encodeStr = "aeioubcdfghjklmnprstvyz"
encodeint = "123456789.:-_*é^,;@€æΩ≈"

translate = str.maketrans(encodeStr,encodeint)


icerik = input("Şifrelemek istediğiniz mesajınızı giriniz.(Noktalama kullanmayınız) ")
icerik_ters = icerik[::-1]
print("Mesajınız şifreleniyor. . ", end="")
for i in range(11):
    time.sleep(.3)
    print(".", end=" ")

codedicerik = icerik_ters.lower().translate(translate)
print("\n" + codedicerik)

coz = input("Çözmek ister misiniz? Y: Evet, N: Hayır ")

if coz.upper() == "Y":
    decode = str.maketrans(encodeint,encodeStr)
    decodedicerik = codedicerik.translate(decode)
    decoded_tersduz = decodedicerik[::-1]
    print(decoded_tersduz)
elif coz.upper() == "N":
    print("Mesajınız şifreli kalmıştır.")
else:
    print("Farklı bir tuşa bastınız.")

