ilksayi = int(input("ilk sayiyi giriniz: "))
ikincisayi = int(input("ikinci sayiyi giriniz: "))

islem = input("""Yapmak istediğiniz islemi giriniz.
(toplama: +,cikarma: -,carpma: *,bolme: /)
""")

if islem == "+":
    print("sonuc: "+str(ilksayi+ikincisayi))

elif islem == "-":
    print("sonuc: "+str(ilksayi-ikincisayi))

elif islem == "*":
    print("sonuc: "+str(ilksayi*ikincisayi))

elif islem == "/":
    print("sonuc: "+str(ilksayi/ikincisayi))

else:
    print("yanlis islem secenegi secildi!")