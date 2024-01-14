print('Telefon numaranizi sadece rakam olarak girin bende yaziyla cikti veriyim')
telno = input('Tel No: ')
rakamlar = ('sifir','bir','iki','uc','dort','bes','alti','yedi','sekiz','dokuz')
yaziyla = []
for rakam in telno:
    yaziyla.append(rakamlar[int(rakam)])
print(yaziyla)