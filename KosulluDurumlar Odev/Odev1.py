print("""************
Lutfen Boy ve Kilonuzu Giriniz....
************
""")

kilo= int(input("Kilo:"))
boy= float(input("Boy:"))

BKI= kilo/(boy**2)
print("BKI {}\n".format(BKI))

if (BKI<18.5):
    print("------>zayif")
elif(BKI>=18.5 and BKI<25):
    print("------>Normal")
elif(BKI>=25 and BKI<30):
    print("------>Fazla Kilolu")
elif(BKI>30):
    print("------>Obez")
else:
    print("Lutfen secimi dogru giriniz...")
