kardes1 = "Anne -> Oğul"
kardes2 = "Anne -> Kız"
kardes3 = "Baba -> Oğul"
kardes4 = "Baba -> Kız"

dede1 = "Anne -> Baba"
dede2 = "Baba -> Baba"

nene1 = "Anne -> Anne"
nene2 = "Baba -> Anne"

dayi1 = "Anne -> Baba -> Oğul"
dayi2 = "Anne -> Anne -> Oğul"

teyze1 = dede1 + " -> Kız"
teyze2 = nene1 + " -> Kız"

hala1 = dede2 + " -> Kız"
hala2 = nene2 + " -> Kız"

amca1 = dede2 + " -> Oğul"
amca2 = nene2 + " -> Oğul"



def kisalt(bilgi):

    kopya = str(bilgi)


    #DAYILAR
    if dayi1 in bilgi:
        bilgi = bilgi.replace(dayi1,"Dayı")
    if dayi2 in bilgi:
        bilgi = bilgi.replace(dayi2,"Dayı")

    if hala1 in bilgi:
        bilgi = bilgi.replace(hala1,"Hala")
    if hala2 in bilgi:
        bilgi = bilgi.replace(hala2,"Hala")

    if amca1 in bilgi:
        bilgi = bilgi.replace(amca1,"Amca")
    if amca2 in bilgi:
        bilgi = bilgi.replace(amca2,"Amca")



    if nene1 in bilgi:
        bilgi = bilgi.replace(nene1, "Nine")
    if nene2 in bilgi:
        bilgi = bilgi.replace(nene2, "Nine")


    if teyze1 in bilgi:
        bilgi = bilgi.replace(teyze1,"Teyze")
    elif teyze2 in bilgi:
        bilgi = bilgi.replace(teyze2,"Teyze")

    if dede1 in bilgi:
        bilgi = bilgi.replace(dede1,"Dede")
    if dede2 in bilgi:
        bilgi = bilgi.replace(dede2,"Dede")

    if kardes1 in bilgi:
        bilgi = bilgi.replace(kardes1, "Kardeş")
    if kardes2 in bilgi:
        bilgi = bilgi.replace(kardes2, "Kardeş")
    if kardes3 in bilgi:
        bilgi = bilgi.replace(kardes3, "Kardeş")
    if kardes4 in bilgi:
        bilgi = bilgi.replace(kardes4, "Kardeş")

    return bilgi, kopya
