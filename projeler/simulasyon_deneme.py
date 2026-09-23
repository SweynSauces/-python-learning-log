import time
import random

# --- NESNE KALIBI (CLASS) ---
class Karakter:
    def __init__(self, isim, can, saldiri_gucu):
        self.isim = isim
        self.can = can
        self.saldiri_gucu = saldiri_gucu
        
    def saldir(self, hedef):
        print(f"> {self.isim}, {hedef.isim}'e {self.saldiri_gucu} hasar vurdu!")
        hedef.can -= self.saldiri_gucu
        
        if hedef.can <= 0:
            hedef.can = 0
            print(f"☠️  {hedef.isim} yok edildi!\n")
        else:
            print(f"❤️  {hedef.isim} Kalan Can: {hedef.can}\n")

    def hayatta_mi(self):
        return self.can > 0

# --- SAVAŞ MEKANİĞİ ---
def savas(oyuncu, dusman):
    print(f"\n⚔️  SAVAŞ BAŞLADI: {dusman.isim} (Can: {dusman.can}, Saldırı: {dusman.saldiri_gucu})")
    time.sleep(1)
    
    # İkisinden biri ölene kadar sırayla birbirlerine vururlar
    while oyuncu.hayatta_mi() and dusman.hayatta_mi():
        oyuncu.saldir(dusman)
        time.sleep(1)
        
        if dusman.hayatta_mi():
            dusman.saldir(oyuncu)
            time.sleep(1)

# --- GANİMET SEÇİM MEKANİĞİ ---
def ganimet_sec(oyuncu):
    print("🎉 Düşmanı alt ettin! Karşına iki seçenek çıktı:")
    print(" [1] Can Bonusu  : +20 Can")
    print(" [2] Saldırı Bonusu: +5 Saldırı Gücü")
    print(" [3] Şans Kutusu  : (Büyük ödüller veya can kaybı içerir!)")
    
    while True:
        secim = input("\nSeçimin nedir? (1, 2 veya 3 yazıp Enter'a bas): ")
        
        if secim == "1":
            oyuncu.can += 20
            print(f"\n✨ Can bonusunu seçtin! Yeni Can: {oyuncu.can}\n")
            break

        elif secim == "2":
                    # Şans kutusu havuzu (Senin belirlediğin oranlar)
                    oyuncu.saldiri_gucu += 5
                    print(f"\n✨ Saldırı bonusunu seçtin! Yeni Saldırı Gücü: {oyuncu.saldiri_gucu}\n")
                    

        elif secim == "3":
            # Şans kutusu havuzu (Senin belirlediğin oranlar)
            havuz = [
                ("can", 5), ("can", 10), ("can", 25), 
                ("saldiri", 20), ("saldiri", 25), ("saldiri", 30), 
                ("can", -5), ("can", -15)
            ]
            odul_tipi, miktar = random.choice(havuz)
            
            print("\n🎁 Şans Kutusu açılıyor...")
            time.sleep(1.5)
            
            if odul_tipi == "can":
                oyuncu.can += miktar
                if miktar > 0:
                    print(f"🌟 Şanslısın! +{miktar} Can kazandın.")
                else:
                    print(f"💀 Kötü şans! Kutudan çıkan zehir {miktar} Can kaybettirdi.")
            elif odul_tipi == "saldiri":
                oyuncu.saldiri_gucu += miktar
                print(f"⚔️ Efsanevi güç! +{miktar} Saldırı Gücü kazandın.")
                
            print(f"Güncel Durum -> Can: {oyuncu.can}, Saldırı Gücü: {oyuncu.saldiri_gucu}\n")
            break
        else:
            print("❌ Hatalı giriş! Lütfen sadece 1, 2 veya 3 yaz.")

# ==========================================
# OYUN HİKAYESİ VE AKIŞI BURADA BAŞLIYOR
# ==========================================

# Karakterlerimizi oluşturuyoruz
oyuncu = Karakter("Sercan", can=100, saldiri_gucu=25)
dusman1 = Karakter("Şanslı İblis", can=60, saldiri_gucu=15)

print("--- KARANLIK ORMAN MACERASI BAŞLIYOR ---\n")

# 1. Aşama: Şanslı İblis ile savaş
savas(oyuncu, dusman1)

if oyuncu.hayatta_mi():
    # 2. Aşama: Ganimet Seçimi (Klavye girdisi bekler)
    ganimet_sec(oyuncu)
    time.sleep(2)
    
    # 3. Aşama: Kadim Ejderha Boss Savaşı
    dusman2 = Karakter("Kadim Ejderha", can=100, saldiri_gucu=33)
    print("🔥 Yerin sarsıldığını hissediyorsun... Gökyüzü karardı!")
    time.sleep(1.5)
    savas(oyuncu, dusman2)
    
    # Oyun Sonu Kontrolü
    if oyuncu.hayatta_mi():
        print("🏆 İNANILMAZ! Kadim Ejderha'yı yendin ve ormandan sağ çıktın. Sen bir efsanesin!")
    else:
        print("💀 Kadim Ejderha'nın alevleri arasında kül oldun. Oyun Bitti.")
else:
    print("💀 Şanslı İblis seni alt etti. Oyun Bitti.")