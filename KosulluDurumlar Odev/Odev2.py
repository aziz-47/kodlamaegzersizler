print("""************
Lutfen Uc Tane Sayi Giriniz.....
************
""")

a= int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))

if(a>b and b>c):
    print("En buyuk sayi:\n",a)
elif(a<b and b>c):
    print("En buyuk sayi:\n",b)
elif(a<b and b<c):
    print("En buyuk sayi:\n",c)
else:
    print("Lutfen bir sayi girniz")
