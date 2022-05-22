import random
import time

print("""***************************
Sayi Tahmin Oyunu

1 ile 40 arasinda sayiyi tahmin edin

******************************

""")

rastegele_sayi = random.randint(1,40)
tahmin_hakki= 7
while True:

    tahmin= int(input("Tahminiz:"))

    if(tahmin<rastegele_sayi):
        print("Bilgiler sorgulaniyor....")
        time.sleep(1)


        print("Daha yuksek bir sayi soyleyin...")

        tahmin_hakki-=1
    elif(tahmin>rastegele_sayi):
        print("Bilgiler sorgulaniyor...")
        time.sleep(1)

        print("Daha dusuk bir sayi soyleyin....")

        tahmin_hakki-=1
    else:
        print("Bilgiler Sorgulaniyor...")
        time.sleep(1)
        print("Tebrikler! Sayimiz:",rastegele_sayi)
        break
    if(tahmin_hakki==0):
        print("Tahmin hakkiniz bitti...")
        print("Sayimiz:", rastegele_sayi)
        break