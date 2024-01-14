import time
yanginrisk=0
pim=1
kayit=1
can=0
risk=0
yangin=0


yanginrisk=int(input("\nYANGIN RİSKİ VAR MI? (1/0): "))

if (yanginrisk==1):
    print("""
--------------------
YANGIN TÜPÜ ALINDI
--------------------""")
    pim=int(input("\nPİM AÇIK MI? (1/0): "))
    if (pim==1):
        print("""
--------------------
PİM AÇIK
--------------------""")
    else:
        pim=1
        print("""
--------------------
PİM ÇEKİLDİ
--------------------""")
    kayit=int(input("\nKAYDEDEN BİRİ VAR MI? (1/0): "))
    if (kayit==1):
        print("""
--------------------
BİRİ KAYDEDİYOR
--------------------""")
    else:
        print("""
--------------------
KİMSE KAYDETMİYOR
--------------------""")
    
    can=int(input("\nCAN RİSKİ VAR MI? (1/0): "))
    if (can==1):
        print("""
--------------------
CAN RİSKİ VAR
--------------------""")
        risk=int(input("\nKENDİNİ RİSKE DEĞER Mİ? (1/0): "))
        while can==1:
            if (risk==1):
                yangin=int(input("\nYANGIN BAŞLADI MI? (1/0): "))
                if (yangin==1):
                    print("""
--------------------
YANGIN BAŞLADI!
--------------------""")
                    yanginseviye=5
                    for i in range (5,0,-1):
                        print("\nYANGIN SEVİYESİ: "+ str(yanginseviye)+"\n\a")
                        time.sleep(5)
                        yanginseviye-=1
                    print("""
-------------------
YANGIN SÖNDÜRÜLDÜ!
-------------------""")
                else:
                    risk=int(input("\nRİSK DEVAM EDİYOR MU? (1/0): \n"))
                    if risk==0:
                        can=0
            else:
                can=0
    else:
        print("CAN RİSKİ YOK")