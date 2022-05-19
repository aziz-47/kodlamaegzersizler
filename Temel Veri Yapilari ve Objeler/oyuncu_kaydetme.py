print("Oyuncu Kaydetme Programi")

ad = input("Oyuncunun adi:")
soyad= input("Oyuncuunun soyadi:")
takim= input("Oyuncunun Takimi:")

bilgiler = [ad,soyad,takim]
print("Bilgiler Kaydediliyor...")

print("Oyuncu Adi: {}\nOyunucu Soyadi: {}\nOyuncu Takimi:{}\n".format(bilgiler[0],
                                                                    bilgiler[1],
                                                                    bilgiler[2]))

print("Bilgiler Kaydedildi...")