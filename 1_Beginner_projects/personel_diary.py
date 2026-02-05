print("*"*30)
print("Yapilacaklar Listesi")
print("+"*30)

yapilacaklar=[]

try:
    with open("ajanda.txt","r",encoding="utf-8") as dosya:
      for satir in dosya:
          yapilacaklar.append(satir.strip())
        
except FileNotFoundError:
    pass

while True:
    print("Ne Yapmak İstersin?")
    print("1. Görev Ekle")
    print("2. Görev Sil")
    print("3. Listeyi Göster")
    print("4. Çikiş (q)")
    
    secim= input("Seçimin: ").strip()

    if secim=="1":
        gorev= input("Eklenecek GÖrev Nedir: ")
        yapilacaklar.append(gorev)
        print("Eklendi..")

    elif secim=="2":
        silinecek= input("Silinecek görev nedir: ")
        if silinecek in yapilacaklar:
            yapilacaklar.remove(silinecek)
            print("Silindi..")
        else:
            print("Böyle bir görev listede yok!!")


    elif secim=="3":
        print("\n ----LİSTENİZ----") 

        for isimiz in yapilacaklar:
            print("✰ "+isimiz)


    elif secim=="4" or secim=="q":
        print("İyi Günler Dilerim ✮⋆")
        with open("ajanda.txt","w",encoding="utf-8") as dosya:
            for gorev in yapilacaklar:
                dosya.write(gorev + "\n")
 
        break
    

    else:
        print("Hatali secim yaptin!")