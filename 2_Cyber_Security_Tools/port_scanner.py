import socket
import time
from colorama import Fore, Style, init

init(autoreset=True)

print("#"*35)
print(Fore.CYAN+"BASİT PORT TARAYICI"+ Style.RESET_ALL)
print("#"*35)


try:
    hedef_site=input("Hamgi siteyi taratayim?")
    baslangiç=int(input("Başlangiç portu ne olsun?"))
    bitiş=int(input("Bitiş portu ne olsun?"))

    hedef_ip=socket.gethostbyname(hedef_site)

    print(f"Hedef: {hedef_site}")
    print(f"Hedef Ip: {hedef_ip}")
    print(Fore.YELLOW+"Tarama başlatiliyor..."+ Style.RESET_ALL)


    for port in range(baslangiç,bitiş+1):
        soket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        sonuc=soket.connect_ex((hedef_ip,port))

        if sonuc==0:
            print(Fore.GREEN+f"PORT {port} AÇIK!"+ Style.RESET_ALL)
        else:
            pass
        soket.close()

    print("\n"+"#"*40)    
    print(Fore.CYAN+"Tarama Tamamlandi."+ Style.RESET_ALL)

except socket.gaierror:
    print(Fore.RED + "\nHATA: Belirtilen site bulunamadi veya internet yok!" + Style.RESET_ALL)
except ValueError:
    print(Fore.RED + "\nHATA: Lütfen port numaralarini SAYI olarak giriniz." + Style.RESET_ALL)
except KeyboardInterrupt:
    print(Fore.RED + "\n\nKullanici taramayi iptal etti." + Style.RESET_ALL)