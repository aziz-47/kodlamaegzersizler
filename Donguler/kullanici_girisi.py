print("""
************
Kullanici Girisi Programi
************

""")


sys_kullanici_adi= "aaziz"
sys_parola= "12345"
gris_hakki= 3


while True:
    kullanici_adi = input("Kullanici Adi:")
    paola= input("Parola:")

    if(sys_kullanici_adi!=kullanici_adi and sys_parola==paola):
        print("Kullanici adi hatali...")
        gris_hakki-=1
    elif(sys_kullanici_adi==kullanici_adi and sys_parola!=paola):
        print("Parola Hatali...")
        gris_hakki-=1
    elif(sys_kullanici_adi!=kullanici_adi and sys_parola!=paola):
        print("Kullancii adi ve Parola Hatali...")
        gris_hakki-=1
    else:
        print("Sisteme basariyla Girildi...")
        break

    if(gris_hakki==0):
        print("Giris Hakkiniz Bitmistir...")
        break


