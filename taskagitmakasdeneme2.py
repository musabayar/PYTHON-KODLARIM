import random
secenek=["tas","kagit","makas"]
tas=secenek[0]
kagit=secenek[1]
makas=secenek[2]
print("Tas,Kagit,Makas oyunu")
while True:
    secim = input("Tas mi kagit mi makas mi? ")
    bil_secim = random.choice(secenek)
    if secim==tas:
        if bil_secim==tas:
            print("Bilgisayarin secimi: Tas Sonuc: Berabere")
        elif bil_secim==kagit:
            print("Bilgisayarin secimi: Kagit Sonuc: Kaybettiniz")
        else:
            print("Bilgisayarin secimi: makas Sonuc: Kazandiniz")
    if secim==kagit:
        if bil_secim==taş:
            print("Bilgisayarin secimi: Taş Sonuc: Kazandiniz")
        elif bil_secim==kagit:
            print("Bilgisayarin secimi: Kagit Sonuc: Berabere")
        else:
            print("Bilgisayarin secimi: makas Sonuc: Kaybettiniz")
    if secim==makas:
        if bil_secim==tas:
            print("Bilgisayarin secimi: Tas Sonuc: Kaybettiniz")
        elif bil_secim==kagit:
            print("Bilgisayarin secimi: Kagit Sonuc: Kazandiniz")
        else:
            print("Bilgisayarin secimi: makas Sonuc: Berabere")