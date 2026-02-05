import random

print("TAŞ-KAĞİT-MAKAS OYUNU :)")
print("Çikmak icin 'q' tusuna basabilirsin!")
print("Oyunda 3 puani elde eden yarişmaci oyunu kazanmiş olur.")
print("-" *30)

secenekler=['tas','kagit','makas']
bilgisayar_puani=0
kullanici_puani=0
puan_list=[]
tur_sayaci=0

kullanici_adi=input("Lütfen kullanici adinizi giriniz:")
print(f"Hoşgeldin {kullanici_adi}!")
while kullanici_puani<3 and bilgisayar_puani<3:
    tur_sayaci+=1
    kullanici_Secimi=input(f"\n {tur_sayaci}. TUR -seçiminiz:(tas,kagit,makas)").lower().strip()
    if kullanici_Secimi=='q':
        print("Bir Sonraki Oyunda Görüsmek Üzere.")
        break

    if kullanici_Secimi not in secenekler:
        print(f"Gecersiz islem yaptin {kullanici_adi}!")
        tur_sayaci-=1
        continue

    bilgisayar_Secimi= random.choice(secenekler)
    print(f"Bilgisayar secimi: {bilgisayar_Secimi}")

    if kullanici_Secimi==bilgisayar_Secimi:
        print("Berabere!")
        puan_list.append(f"{tur_sayaci}. Tur: Berabere ({kullanici_puani}-{bilgisayar_puani})")

    elif kullanici_Secimi=='tas':
        if bilgisayar_Secimi=='kagit':
            print("Kaybettin!")
            bilgisayar_puani+=1
            puan_list.append(f"{tur_sayaci}. Tur: Bilgisayar kazandi ({kullanici_puani}-{bilgisayar_puani})")
        else:
            print(f" Kazandin! Tebrikler {kullanici_adi}")
            kullanici_puani+=1
            puan_list.append(f"{tur_sayaci}. Tur: {kullanici_adi} kazandi ({kullanici_puani}-{bilgisayar_puani})")

    elif kullanici_Secimi=='kagit':
        if bilgisayar_Secimi=='makas':
             print("Kaybettin!")
             bilgisayar_puani+=1
             puan_list.append(f"{tur_sayaci}. Tur: Bilgisayar kazandi")
        else:
            print(f" Kazandin! Tebrikler {kullanici_adi}")
            kullanici_puani+=1
            puan_list.append(f"{tur_sayaci}. Tur: {kullanici_adi} kazandi ({kullanici_puani}-{bilgisayar_puani})")
    elif kullanici_Secimi=='makas':
        if bilgisayar_Secimi=='tas':
            print("Kaybettin!")
            bilgisayar_puani+=1
            puan_list.append(f"{tur_sayaci}. Tur: Bilgisayar kazandi ({kullanici_puani}-{bilgisayar_puani})")
        else:
            print(f" Kazandin! Tebrikler {kullanici_adi}")
            kullanici_puani+=1        
            puan_list.append(f"{tur_sayaci}. Tur: {kullanici_adi} kazandi ({kullanici_puani}-{bilgisayar_puani})")

    print("-"*40)   
    print(f"SKOR DURUMU: {kullanici_adi} [{kullanici_puani}] - Bilgisayar [{bilgisayar_puani}]")     
    print("-"*40)

print("MAÇ ÖZETİ:")
for kayit in puan_list:
    print(kayit)

print("-" * 30)


if kullanici_puani > bilgisayar_puani:
    print(f"🏆 TEBRİKLER ŞAMPİYON: {kullanici_adi.upper()}!")
elif bilgisayar_puani > kullanici_puani:
    print(f"🤖 KAZANAN: BİLGİSAYAR! (Bir dahaki sefere...)")
else:
    print("Oyun tamamlanmadi.")
