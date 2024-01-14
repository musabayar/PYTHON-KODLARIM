sayi1=int(input("1.sayiyi giriniz: "))
sayi2=int(input("2.sayiyi giriniz: "))
islem = input("yapmak istediğinz işlemi yaziniz(toplama/cikarma/carpma/bolme): ")

if islem == "toplama":
    print(sayi1 + sayi2)

if islem == "cikarma":
    print(sayi1 - sayi2)

if islem == "carpma":
    print("sayi1 * sayi2")

if islem == "bolme":
    print(sayi1 // sayi2)
