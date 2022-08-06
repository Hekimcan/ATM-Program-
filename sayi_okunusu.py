#Girilen İki Basamaklı Sayının Türkçe okunuşunu döndüren Program
print("""************************

Sayının Okunuşunu Bulan Program

************************""")


def okunus(sayi):


    onlar_bas=((sayi%100-sayi%10)/10)
    birler_bas=sayi%10
    okunus2=" "
    if onlar_bas==1:
         okunus1="on"
    elif onlar_bas==2:
        okunus1="yirmi"
    elif onlar_bas==3:
        okunus1="otuz"
    elif onlar_bas==4:
        okunus1="kırk"
    elif onlar_bas==5:
        okunus1="elli"
    elif onlar_bas==6:
        okunus1="altmış"
    elif onlar_bas==7:
        okunus1="yetmiş"
    elif onlar_bas==8:
        okunus1="seksen"
    elif onlar_bas==9:
        okunus1="doksan"
    if birler_bas==0:
        if onlar_bas==1:
            okunus="on"
        elif onlar_bas==2:
            okunus="yirmi"
        elif onlar_bas==3:
            okunus="otuz"
        elif onlar_bas==4:
            okunus = "kırk"
        elif onlar_bas==5:
            okunus="elli"
        elif onlar_bas==6:
            okunus="altmış"
        elif onlar_bas==7:
            okunus="yetmiş"
        elif onlar_bas==8:
            okunus="seksen"
        elif onlar_bas==9:
            okunus="doksan"

    if birler_bas==1:
        okunus2="bir"
    elif birler_bas==2:
        okunus2="iki"
    elif birler_bas==3:
        okunus2="üç"
    elif birler_bas==4:
        okunus2="dört"
    elif birler_bas==5:
        okunus2="beş"
    elif birler_bas==6:
        okunus2="altı"
    elif birler_bas==7:
        okunus2="yedi"
    elif birler_bas==8:
        okunus2="sekiz"
    elif birler_bas==9:
        okunus2="dokuz"
    okunus=okunus1+okunus2
    print("{} sayısının okunuşu:{} 'dir".format(sayi,okunus))
sayi=int(input("İki basamaklı bir sayı giriniz:"))
okunus(sayi)
