# ATM-Program-
print("""*****************************************
Atm Programına Hoşgeldiniz...
*****************************************
İşlemler;
Bakiye Sorgulama İçin:(1)
Para Yatırma İçin:(2)
Para Çekmek İçin:(3)
Kredi Kartı Nakit Avans İçin:(4)
YKS Sınav Ücreti Yatırmak İçin(5)
Motorlu Taşıtlar Sınav Ücreti Yatırmak İçin(6)
MEB Açıköğretim Sınav Ücreti Yatırmak İçin(7)
KYK Yurt Ücreti Yatırmak İçin(8)
Ana Menüye Dönmek İçin 'A' ya basın
Kart İade İçin 'q' ya basın
""")
bakiye=1000
kredi=15000
yks=230
ehliyet=130
meb=75
kyk=850
while True:
    işlem=input("İşlem Seçiniz")
    if (işlem == "A"):
        print("""
                   İşlemler;
               Bakiye Sorgulama İçin:(1)
               Para Yatırma İçin:(2)
               Para Çekmek İçin:(3)
               Kredi Kartı Nakit Avans İçin:(4)
               YKS Sınav Ücreti Yatırmak İçin(5)
               Motorlu Taşıtlar Sınav Ücreti Yatırmak İçin(6)
               MEB Açıköğretim Sınav Ücreti Yatırmak İçin(7)
               KYK Yurt Ücreti Yatırmak İçin(8)
               Kart İade İçin 'q' ya basın
               """)
        continue

    elif(işlem=="q"):
        print("İyi Günler Yine Bekleriz")
        break
    elif(işlem=="1"):
        print("Bakiyeniz: {} TL'dir".format(bakiye))

    elif(işlem=="2"):
        miktar=int(input("Miktarı giriniz:"))
        bakiye+=miktar

    elif(işlem=="3"):
        miktar = int(input("Miktarı giriniz:"))
        if(bakiye<miktar):
            print("Bakiye Yetersiz!!")
            continue
        bakiye-=miktar


    elif(işlem=="4"):
        miktar=int(input("Miktarı Giriniz:"))
        if (kredi < miktar):
             print("Bakiye Yetersiz!!")
             continue
        kredi-=miktar
    elif(işlem=="5"):
        print("YKS 2023 Sınav Ücreti 2 Oturum: {} TL'dir,Lütfen Sadece {} TL yatırınız".format(yks,yks))
        miktar = int(input("Miktarı Giriniz:"))
        yks-=miktar
    elif(işlem=="6"):
        print("Motorlu Taşıtlar 2022/Ağustos Sınav Ücreti:{} TL'dir,Lütfen sadece 130 TL yatırınız".format(ehliyet))
        miktar = int(input("Miktarı Giriniz:"))
        ehliyet-=miktar
    elif(işlem=="7"):
        print("2022/Ağustos MEB Açıköğretim Sınav Ücreti:{} TL'dir,Lütfen sadece 75 TL yatırınız".format(meb))
        miktar = int(input("Miktarı Giriniz:"))
        meb-=miktar
    elif(işlem=="8"):
        print("KYK 2022 Ekim Ayı Yurt Ücreti:{} TL'dir ,Lütfen sadece 850 TL yatırınız".format(kyk))
        miktar = int(input("Miktarı Giriniz:"))
        kyk -= miktar
    else:
        print("Geçersiz İşlem")






