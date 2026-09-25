#IF / ELIF / ELSE VE MANTIKSAL OPERATÖRLER UYGULAMA PROJESİ
#KONU: Hayatta Kalma/Korku Oyunu İçin Karakter ve Çevre Kontrol Sistemi

karakter_can = 10
karakter_enerji = 10
fener_pil = 20                 # Yüzde üzerinden değerlendirilen pil durumu
fener_durumu = False           # Fenerin açık veya kapalı olduğunu belirten durum
anahtar_var_mi = False        # Anahtarın karakterde olup olmadığını belirten durum
canavar_yakinda_mi = True     # Canavarın karaktere yakın olup olmadığını belirten durum

print("---- KARAKTER DURUMU ----")

#Karakter sağlığını kontrol eden karar mekanizması

if karakter_can <=0:
    #Eğer karakterimizin canı 0 veya altına düştüyse, karakter ölmüş demektir ve oyunu kaybetmiş oluruz.    
    print("Karakter öldü! Oyunu kaybettiniz.")

elif karakter_can > 0 and karakter_can <= 30:
    #and operatörü; hem canıı 0'dan büyük hem de 30 veya 30'dan küçükse kodu çalıştırır.
    print("Karakter ağır yaralı. Sağlık çantası bulman gerekiyor.")

elif karakter_can > 30 and karakter_can <= 70:
    print("Karakter yaralandı.")

else:
    #Yukarıdaki koşulların hiçbiri sağlanmazsa yani karakter canı 70'den büyükse bu kod çalışır.
    print("Karakter durumu stabil")

print("\n--- EYLEM VE ÇEVRE KONTROLÜ ---")

# or ve not operatörlerinin kullanımı.
# Karakterin kaçma yeteneğini ve çevresel faktörleri değerlendiriyoruz.

if canavar_yakinda_mi:
    print("SİSTEM UYARISI: Yakınlarda bir tehdit var!")
    
    # Canavar yakındayken karakterin kaçıp kaçamayacağını stamina ve can ile ölçüyoruz.
    # or operatörü: Şartlardan BİRİ BİLE doğruysa blok çalışır.
    
    if karakter_enerji < 20 or karakter_can < 20:
        print("-> KAÇAMAZSIN! Yeterli enerjin veya canın yok. Saklanacak bir yer bul!")
    
    else:
        print("-> Hızlıca koşarak uzaklaşabilirsin!")
        
else:
    # not operatörü: Bir durumun tersini alır. 
    # Eğer "canavar yakında değilse" ve "anahtarımız yoksa" arama yapmaya devam etmeliyiz.
    
    if not anahtar_var_mi:
        print("Etraf güvenli. Çıkış kapısı için anahtarı aramaya devam et.")


print("\n--- ENVANTER VE EŞYA KONTROLÜ ---")

# Fenerin çalışma durumunu kontrol eden basit bir yapı.

if fener_durumu and fener_pil > 0:
    
    if fener_pil <= 10:
        print("Işık titriyor... Fener pili bitmek üzere!")

    elif fener_pil <=0:
        print("Pil yüzdesi 0'dan küçük olamaz. ")
        
    else:
        print("Fener yolu aydınlatıyor.")
        
elif fener_durumu and fener_pil == 0:
    print("Fenerin açık ancak pili bitti. Karanlıktasın.")
    
else:
    print("Fener kapalı. Gizlenmek için iyi bir fırsat.")