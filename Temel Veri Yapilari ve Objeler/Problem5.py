a= int(input("a:"))
b= int(input("b:"))

print("Degistirilmeden Once Degerler\na: {} b: {}\n".format(a,b))

a,b= b,a

print("Degistirildikten Sonraki Degerler\na: {} b: {}\n".format(a,b))