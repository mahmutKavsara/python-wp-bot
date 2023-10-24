import pywhatkit
numara = input('numarayı giriniz(ülke koduyla beraber) :')
mesaj = input("mesajınızı giriniz :")
saat = input('saati giriniz :')
dakika = input("dakika giriniz:")

pywhatkit.sendwhatmsg(numara, mesaj, saat)