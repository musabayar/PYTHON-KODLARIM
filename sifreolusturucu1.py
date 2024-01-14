import random
import string

rakamlar = '0123456789'
semboller = string.punctuation
kucukharf = string.ascii_lowercase
buyukharf = string.ascii_uppercase
cuval = [rakamlar,semboller,kucukharf,buyukharf]

sifre=''
for j in range(4):
    for i in range(2):
        sifre += cuval[j][random.randint(0, 9)]

sifre = list(sifre)
random.shuffle(sifre)
yenisifre = ''
yenisifre = yenisifre.join(sifre)

print(yenisifre)