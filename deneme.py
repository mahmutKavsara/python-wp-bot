import pywhatkit
numara = input('Numarayı giriniz(ülke koduyla beraber) :')
mesaj = input("Mesajınızı giriniz :")
saat = input('Saati giriniz :')
dakika = input("Dakika giriniz :")

pywhatkit.sendwhatmsg(numara, mesaj, saat)