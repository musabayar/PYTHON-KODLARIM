def ebob_bul(sayi1, sayi2):
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

def ekok_bul(sayi1, sayi2):
    ebob = ebob_bul(sayi1, sayi2)
    return sayi1 * sayi2 // ebob

# Kullanıcıdan input alma
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))

# EKOK'u bulma
ekok = ekok_bul(sayi1, sayi2)
print(f"{sayi1} ile {sayi2} sayılarının EKOK'u: {ekok}")

ebob = ebob_bul(sayi1, sayi2)
print(f"{sayi1} ile {sayi2} sayılarının EBOB'u: {ebob}")

