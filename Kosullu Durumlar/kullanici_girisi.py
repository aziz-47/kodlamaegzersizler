print("""******************
Kullanici Girisi
******************
""")

sys_kullanici_adi= "Aziz"
sys_parola= "12345"

kullanici_adi = input("Kullanici Adi:")
parola= input(("Parola:"))

if(kullanici_adi==sys_kullanici_adi and parola!=sys_parola):
    print("Parola Hatali...")
elif(kullanici_adi!=sys_kullanici_adi and parola==sys_parola):
    print("Kullanici Adi Hatali...")
elif(kullanici_adi!=sys_kullanici_adi and parola!=sys_parola):
    print(("Kullanici adi ve Parola Hatali..."))
else:
    print("Sisteme Girisi Basariyla Yapildi...")