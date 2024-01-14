sifre = '123456'
flag = False
rakamlar = '0123456789'

for ba0 in rakamlar:
    for ba1 in rakamlar:
        for ba2 in rakamlar:
            for ba3 in rakamlar:
                for ba4 in rakamlar:
                    for ba5 in rakamlar:
                        asd = (ba0+ba1+ba2+ba3+ba4+ba5)
                        print(asd)
                        if asd == sifre:
                            print('parola: '+ asd)
                            flag = True
                            break
                    if flag == True:
                        break
                if flag == True:
                    break
            if flag == True:
                break
        if flag == True:
                break
    if flag == True:
                break

