#pythonda ucgen yapimi musa

ucgen_kati = int(input('ucgen kac katli olsun efendim?: '))

for k in range(ucgen_kati):
    print(' ' * (ucgen_kati - 1-k), end='')
    for i in range(k*2 + 1):
        print('*', end='')
    print()

print('\nucgen cizilmistir!')