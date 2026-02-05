def sifrele(acik_metin, kaydirma_sayisi):
    sifreli_metin=""
    
    for harf in acik_metin:

      if harf.isalpha():  
         if harf.isupper():
            harf_kodu=ord(harf)-65
            yeni_kod=(harf_kodu+kaydirma_sayisi)%26
            yeni_harf=chr(yeni_kod+65)
            sifreli_metin+=yeni_harf 


         else:  
           harf_kodu=ord(harf)-97
           yeni_kod=(harf_kodu+kaydirma_sayisi)%26
           yeni_harf=chr(yeni_kod+97)

           sifreli_metin+=yeni_harf 

      else:
         sifreli_metin+=harf


    return sifreli_metin

def sifre_coz(sifreli_metin, kaydirma_sayisi):
   
   cozulmus_metin = ""
    
   for harf in sifreli_metin:

     if harf.isalpha():  
         if harf.isupper():
            harf_kodu=ord(harf)-65
            yeni_kod=(harf_kodu-kaydirma_sayisi)%26
            yeni_harf=chr(yeni_kod+65)
            cozulmus_metin+=yeni_harf 


         else:  
           harf_kodu=ord(harf)-97
           yeni_kod=(harf_kodu-kaydirma_sayisi)%26
           yeni_harf=chr(yeni_kod+97)

           cozulmus_metin+=yeni_harf 

     else:
        cozulmus_metin+=harf


   return cozulmus_metin

print("-"*30)
print("SEZAR ŞİFRELEME ARACİ")
print("-"*30)

secim=input("1.Şifrele\n2. Şifre Çöz\nSeçimin (1/2):")




mesaj= input("Şifrelenecek Mesaji Gir (İngilizce karakterlerle)")
anahtar=int(input("Kaç Harf Kaydirilsin?"))


if secim == "1":
    
    sonuc = sifrele(mesaj, anahtar)
    print(f"🔒 Şifrelendi: {sonuc}")

elif secim == "2":
    
    sonuc = sifre_coz(mesaj, anahtar)
    print(f"🔓 Çözüldü: {sonuc}")

else:
    print("Hatali seçim!")


