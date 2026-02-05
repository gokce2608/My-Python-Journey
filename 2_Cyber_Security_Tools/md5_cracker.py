import time
import hashlib

print("*"*50)
print("MD5 HASH KIRICI (DICTIONARY ATTACK)")
print("*"*50)

hedef_hash = "0192023a7bbd73250516f069df18b500"
print(f"Hedef Hash: {hedef_hash}")
print("Saldiri başlatiliyor...\n")

try:
    with open("Sifreler.txt","r",encoding="utf-8") as dosya:
        

        for satir in dosya:

            kelime=satir.strip()
            olusan_hash=hashlib.md5(kelime.encode("utf-8")).hexdigest()

            print(f"Deneniyor: {kelime} -> {olusan_hash}")

            
            time .sleep(0.05)

            if olusan_hash==hedef_hash:
                print("\n" + "⭐"*20)
                print(f" ŞİFRE BULUNDU!")
                print(f"Hash: {hedef_hash}")
                print(f"Gerçek Şifre: {kelime}")
                print("⭐"*20)
                break
        else:
                print("\n❌ Şifre bu listede yok.")   
except FileNotFoundError:
    print("HATA: 'sifreler.txt' dosyasi bulunamadi!")
    print("Lütfen python dosyanla ayni klasörde olduğundan emin ol.")
