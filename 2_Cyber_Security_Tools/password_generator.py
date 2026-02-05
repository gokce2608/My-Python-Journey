import random
import string
import datetime 

print("-" * 30)
print("🏦  ŞİFRE KASASI VE OLUŞTURUCU")
print("-" * 30)

def sifre_uret(uzunluk):
    tum_karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ""
    for i in range(uzunluk):
        sifre += random.choice(tum_karakterler)
    return sifre

try:
   
    hesap_adi = input("Bu şifre hangi hesap için? (Örn: Instagram): ")
    hane_sayisi = int(input("Kaç haneli olsun? (Örn: 16): "))
    
    
    yeni_sifre = sifre_uret(hane_sayisi)
    
    print(f"\n✅ Oluşturulan Şifre: {yeni_sifre}")
    
    
    with open("sifrelerim.txt", "a", encoding="utf-8") as dosya:
        
        bugun = datetime.date.today()
        
        
        dosya.write(f"[{bugun}] {hesap_adi}: {yeni_sifre}\n")
        
    print(f"💾 Şifreniz 'sifrelerim.txt' dosyasına eklendi!")
    print("-" * 30)

except ValueError:
    print("❌ Lütfen şifre uzunluğunu sayı olarak girin!")