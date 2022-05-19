print("""*************************
ATM Makinasina HosGeldiniz

Islemler;
1.Bakiye Sorgulama

2.Para Yatirma 

3.Para Cekme

Programdan Cikmak Icin "q" a basin
""")

bakiye = 1000

while True:
    islem=input("Lutfen Yapmak Istedginiz Islemi seciniz:")

    if(islem=="q"):
        input("Tesekkur ederiz... Yine Bekleriz...")
        break
    elif(islem=="1"):
        print("Bakiyeniz {} tl'dir".format(bakiye))
    elif(islem=="2"):
        miktar= int(input("Miktari giriniz:"))
        bakiye+=miktar
    elif(islem=="3"):
        miktar= int(input("Miktari Giriniz:"))

        if(bakiye-miktar<0):
            print("Boyle Bir Mikatar Cekemezsiniz")
            continue
        bakiye-=miktar
    else:
        print("Gecersiz Islem...")
