a = int(input("Bir sayı giriniz"))
b = int(input("Bir sayı giriniz"))
sonuchesabı=input("Hangi işlemi yapmak istersiniz? (*,/,+,-)")
if(a<b):
  çıkarma = b-a
else:
  çıkarma = a-b

toplama = a+b
çarpma = a*b
if(a>b):
    bölme = a / b
else:
    bölme = b / a
if('+' == sonuchesabı):
    print("toplama Sonucu = ", toplama)
if('/' == sonuchesabı):
    print("bölme Sonucu = ", bölme)
if ('-' == sonuchesabı):
    print("çıkarma Sonucu = ", çıkarma)
if ('*' == sonuchesabı):
    print("çarpma Sonucu = ", çarpma)

