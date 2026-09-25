# GÜN 4: DÖNGÜLER (LOOPS) - FOR, WHILE VE SÖZLÜKLERDE GEZİNME

print("--- 1. FOR DÖNGÜSÜ İLE TOPLAMA ---")
# Amaç: 1'den 100'e kadar olan sayıları toplamak.
# Döngü başlamadan önce sepetimiz boş olduğu için değerini 0 yapıyoruz.
toplam_for = 0

# range(1, 101) fonksiyonu 1'den başlar ve 101'e kadar sayıları sırasıyla verir. range() fonksiyonu son elemanı dahil etmez.
for sayi in range(1, 101):
    # toplam_for += sayi ifadesi, "toplam_for = toplam_for + sayi" işleminin kısa yazımıdır.
    toplam_for += sayi

print(f"For döngüsü ile 1'den 100'e kadar toplam: {toplam_for}")


print("\n--- 2. WHILE DÖNGÜSÜ İLE TOPLAMA ---")
# 'while' döngüsü, belirli bir koşul doğru (True) olduğu sürece çalışmaya devam eder.

toplam_while = 0
sayac = 1  # Manuel olarak kendi sayacımızı başlatıyoruz.

while sayac <= 100:
    toplam_while += sayac  
    
    # EN ÖNEMLİ ADIM: Sayacı her turda 1 artırmalıyız. 
    # Eğer bu satırı yazmazsak, sayac hep 1 kalır ve döngü asla bitmez (Sonsuz Döngü).
    sayac += 1

print(f"While döngüsü ile 1'den 100'e kadar toplam: {toplam_while}")


print("\n--- 3. SÖZLÜKLERDE (DICTIONARY) GEZİNME VE TUPLE UNPACKING ---")
# Daha önce öğrendiğimiz gibi anahtar-değer (key-value) tutan bir sözlük oluşturuyoruz.
karakter_istatistikleri = {
    "isim": "Sercan",
    "sinif": "4.sınıf",
    "deneyim_puani": 850,
    "hayatta_mi": True
}

# .items() metodu, sözlükteki her bir elemanı bize bir Tuple (Demet) çifti olarak döndürür.
# Örneğin ilk turda ('isim', 'Sercan') tuple'ı gelir.
# "for anahtar, deger in ..." yazarak, gelen bu tuple'ın içindeki 2 elemanı 
# anında iki ayrı değişkene (anahtar ve deger) atıyoruz. Buna 'Tuple Unpacking' denir.

for anahtar, deger in karakter_istatistikleri.items():
    # Burada hem anahtarı hem de karşılık gelen değeri aynı anda kullanabiliyoruz.
    print(f"Karakterin {anahtar} bilgisi: {deger}")