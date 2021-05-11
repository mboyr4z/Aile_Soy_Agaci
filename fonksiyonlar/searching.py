import sqlite3 as sql

from Proje_Akrabalik.fonksiyonlar.akrabaTespit import kisalt


def aramayaBasla(ui,vtKonum):
    try:

        id = int(ui.line_ID.text())

        vt = sql.connect(vtKonum)
        imlec = vt.cursor()

        search(id,ui,imlec , "" , [])

        vt.commit()
        vt.close()

    except:
        print("patladı")

def search(id,ui,imlec,bilgi, gezilmisler):
    anneID = imlec.execute("SELECT anneID from baglantilar where kisiID = " + str(id)).fetchall()[0][0]
    babaID = imlec.execute("SELECT babaID from baglantilar where kisiID = " + str(id)).fetchall()[0][0]
    cocuklarID = imlec.execute("SELECT cocuklarID from baglantilar where kisiID = " + str(id)).fetchall()[0][0]

    kisi = imlec.execute("SELECT ad,soyad from kisi where id = " + str(id)).fetchall()[0]
    kisiAd = kisi[0]
    kisiSoyad = kisi[1]

    bilgi, kopya = kisalt(bilgi)
    tumBilgi = bilgi +" " +kisiAd +" "+ kisiSoyad



    # print(tumBilgi)

    ui.cikti.append(bilgi + kisiAd +" "+ kisiSoyad)
    #print(bilgi + kisiAd +" "+ kisiSoyad)
    gezilmisler.append(id)

    if anneID != -1 and anneID not in gezilmisler:
        anneAd = imlec.execute("SELECT ad from kisi where id = " + str(anneID)).fetchall()[0][0]
        ek = kopya + " Anne ->"
        search(anneID,ui,imlec,ek,gezilmisler)

    if babaID != -1 and babaID not in gezilmisler:
        babaAd = imlec.execute("SELECT ad from kisi where id = " + str(babaID)).fetchall()[0][0]
        ek = kopya +  " Baba ->"
        search(babaID, ui, imlec,ek,gezilmisler)

    if cocuklarID != "-1":
        idler = cocuklarID.split(",")
        for cocukID in idler:
            if int(cocukID) not in gezilmisler:
                cocukAd = imlec.execute("SELECT ad from kisi where id = " + str(cocukID)).fetchall()[0][0]
                cocukCinsiyet = imlec.execute("SELECT cinsiyet from kisi where id = " + str(cocukID)).fetchall()[0][0]

                if cocukCinsiyet == "KADIN" or cocukCinsiyet == "kadın":
                    ek = kopya + " Kız -> "
                else:
                    ek = kopya + " Oğul -> "

                search(int(cocukID),ui,imlec,ek,gezilmisler)




    #x = txt.replace(giden,gelen)

