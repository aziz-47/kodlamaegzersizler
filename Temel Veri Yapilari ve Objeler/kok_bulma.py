"""
2. dereceden bir bilinmyeneli denklem bulma
Denklem: ax^2+ bx +c
Deltayi Hesaplama: b**2-4*a*c

Birinic Kok: (-b-delta**0.5)/(2*a)
Ikinic Kok : (-b+delta**0.5)/(2*a)
"""

a=int(input("a:"))
b= int(input("b:"))
c= int(input("c:"))

delta= b**2-4*a*c
x1= (-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)

print("Birinci kok: {}\nIkinci Kok: {}\n".format(x1,x2))