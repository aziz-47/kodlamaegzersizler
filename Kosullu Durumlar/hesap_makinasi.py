print("""*******************************
Hesap Makinasi Programi

islemler;

1.Toplama islemi

2. Cikarma ilsemi

3. Carpma islmei

4. Bolme islmi
*******************************
"""
)

a= int(input("Birinic Sayi:"))
b= int(input("Ikinici Sayi:"))

islem= input("Islemi Giriniz:")

if islem =="1":
    print("{} ile {} in toplami {} dir".format(a,b, a+b))
elif islem =="2":
    print("{} ile {} in farki {} dir".format(a,b, a-b))
elif islem =="3":
    print("{} ile {} in carpimi {} dir".format(a,b, a*b))
elif islem =="4":
    print("{} ile {} in bolumu {} dir".format(a,b, a/b))
else:
    print("Gecersiz islem girildi!..")
