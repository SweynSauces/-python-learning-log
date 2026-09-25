stok = {
    "elma": 50,
    "armut": 30,
    "muz": 12,
    "kavun": 8,
    "çilek": 55,
    "erik": 112
}

fiyatlar = {
    "elma": 15, "armut": 20, "muz": 45, 
    "kavun": 30, "çilek": 60, "erik": 25
}

# Sonsuz döngü başlatıyoruz, kullanıcı 5'i seçene kadar program kapanmayacak
while True:
    print("\n" + "="*30)
    print("MEYVE STOK YÖNETİM SİSTEMİ")
    print("1- Stok Durumunu Listele")
    print("2- Ürün Ekle / Güncelle")
    print("3- Satış Yap (Stoktan Düş)")
    print("4- Toplam Stok Değeri Hesapla")
    print("5- Çıkış")
    print("="*30)           #menü ayrımı için kullanıldı/dekorasyon
    
    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")
    
    if secim == "1":
        print("\n--- MEVCUT STOK ---")
        for urun, miktar in stok.items():
            # Hem listeleme hem de eşik kontrolünü aynı döngüde yapıyoruz
            if miktar < 15:
                print(f"DİKKAT: {urun} stokta azalıyor! (Kalan: {miktar})")
            else:
                print(f"{urun}: {miktar} adet")
                
    elif secim == "2":
        yeni_urun = input("Eklenecek ürünün adını girin: ").lower()
        # input her zaman string (metin) verir, matematik işlemi için int() ile tam sayıya çeviriyoruz
        eklenecek_miktar = int(input("Kaç adet eklenecek: "))
        
        # 'in' operatörü ile ürünün önceden var olup olmadığını kontrol ediyoruz
        if yeni_urun in stok:
            stok[yeni_urun] += eklenecek_miktar
            print(f"Mevcut {yeni_urun} stoğu güncellendi. Yeni miktar: {stok[yeni_urun]}")
        else:
            stok[yeni_urun] = eklenecek_miktar
            print(f"Yeni ürün eklendi: {yeni_urun} ({eklenecek_miktar} adet)")
            
    elif secim == "3":
        satilan_urun = input("Satılacak ürünün adını girin: ").lower()
        
        if satilan_urun in stok:
            satilacak_miktar = int(input(f"Kaç adet {satilan_urun} satılacak: "))
            
            # İç içe if: Ürün var ama miktar yeterli mi?
            if stok[satilan_urun] >= satilacak_miktar:
                stok[satilan_urun] -= satilacak_miktar
                print(f"Satış başarılı! Kalan {satilan_urun}: {stok[satilan_urun]}")
            else:
                print(f"YETERSİZ STOK! Elinizde sadece {stok[satilan_urun]} adet {satilan_urun} var.")
        else:
            print("Hata: Böyle bir ürün stokta bulunmuyor.")
            
    elif secim == "4":
        toplam_deger = 0
        for urun, miktar in stok.items():
            # .get() metodu hayat kurtarır: Eğer sonradan eklenen yeni bir ürünün fiyatı 
            # 'fiyatlar' sözlüğünde yoksa hata vermek yerine varsayılan olarak 0 değerini alır.
            birim_fiyati = fiyatlar.get(urun, 0) 
            toplam_deger += (miktar * birim_fiyati)
            
        print(f"\nDepodaki tüm ürünlerin toplam piyasa değeri: {toplam_deger} TL")
        
    elif secim == "5":
        print("Sistemden çıkılıyor. İyi çalışmalar!")
        break # Sonsuz while döngüsünü kırar ve programı bitirir
        
    else:
        print("Geçersiz bir seçim yaptınız, lütfen 1 ile 5 arasında bir değer girin.")