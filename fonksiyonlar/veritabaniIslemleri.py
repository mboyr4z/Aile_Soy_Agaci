import sqlite3 as sql

def vtKontrol(ui,vtKonum):

    vt = sql.connect(vtKonum)
    imlec = vt.cursor()

    yoksa_kisi_olustur = 'CREATE TABLE IF NOT EXISTS "kisi" ("id"	INTEGER NOT NULL,"ad"	TEXT NOT NULL,"soyad"	TEXT NOT NULL,"cinsiyet"	TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));'
    yoksa_baglanti_olustur = 'CREATE TABLE IF NOT EXISTS "baglantilar" ("kisiID"	INTEGER NOT NULL,"anneID"	INTEGER,"babaID"	INTEGER,"cocuklarID"	TEXT,PRIMARY KEY("kisiID" AUTOINCREMENT)); '

    imlec.execute(yoksa_kisi_olustur)
    imlec.execute(yoksa_baglanti_olustur)

    vt.commit()
    vt.close()

def kisiEkle(ui,vtKonum):

    try:
        vtKontrol(ui, vtKonum)
        ad = ui.line_Ad.text()
        soyad = ui.line_Soyad.text()
        anneID = int(ui.line_AnneID.text())
        babaID = int(ui.line_BabaID.text())
        cocuklarID = ui.line_cocuklarID.text()
        cinsiyet = ui.line_cinsiyet.text()

        vt = sql.connect(vtKonum)
        imlec = vt.cursor()
        # ---------- YOKSA EĞER TABLOLAR OLUŞTURULUR VAR SA ÖYLE KALIR --------------#
        kisi_ekle = 'INSERT INTO kisi (ad,soyad,cinsiyet) VALUES  ("' + ad + '","' + soyad + '","'+cinsiyet+'")'
        imlec.execute(kisi_ekle)

        baglantilari_ekle = "INSERT INTO baglantilar (anneID,babaID,cocuklarID) VALUES (" + str(anneID) + "," + str(
            babaID) + "," + '"' + cocuklarID + '"' + ")"

        imlec.execute(baglantilari_ekle)
        vt.commit()
        vt.close()
        ui.cikti.append(ad + " kişisi eklendi..")

        lineTemizle(ui)
    except:
        pass

def kisiSil(ui,vtKonum):


    try:
        id = int(ui.line_ID.text())
        vt = sql.connect(vtKonum)
        imlec = vt.cursor()

        imlec.execute("DELETE FROM kisi WHERE id IN("+ str(id) + ")")
        imlec.execute("DELEte FROM baglantilar WHERE kisiID IN(" + str(id) + ")")

        vt.commit()
        vt.close()


        lineTemizle()
    except:
        pass

def tabloSil(vtKonum):

    try:
        vt = sql.connect(vtKonum)
        imlec = vt.cursor()

        yoksa_kisi_olustur = 'CREATE TABLE IF NOT EXISTS "kisi" ("id"	INTEGER NOT NULL,"ad"	TEXT NOT NULL,"soyad"	TEXT NOT NULL,"cinsiyet"	TEXT NOT NULL,PRIMARY KEY("id" AUTOINCREMENT));'
        yoksa_baglanti_olustur = 'CREATE TABLE IF NOT EXISTS "baglantilar" ("kisiID"	INTEGER NOT NULL,"anneID"	INTEGER,"babaID"	INTEGER,"cocuklarID"	TEXT,PRIMARY KEY("kisiID" AUTOINCREMENT)); '

        imlec.execute(yoksa_kisi_olustur)
        imlec.execute(yoksa_baglanti_olustur)

        imlec.execute("DROP TABLE kisi")
        imlec.execute("DROP TABLE baglantilar")

        vt.commit()
        vt.close()
    except:
        pass

def kisiGuncelle(ui,vtKonum):

    try:
        id = int(ui.line_ID.text())
        ad = ui.line_Ad.text()
        soyad = ui.line_Soyad.text()
        anneID = int(ui.line_AnneID.text())
        babaID = int(ui.line_BabaID.text())
        cocuklarID = ui.line_cocuklarID.text()
        cinsiyet = ui.line_cinsiyet.text()

        vt = sql.connect(vtKonum)
        imlec = vt.cursor()

        imlec.execute("UPDATE kisi set ad = '" + ad + "' where id = " + str(id))
        imlec.execute("UPDATE kisi set soyad = '" + soyad + "' where id = " + str(id))
        imlec.execute("UPDATE kisi set cinsiyet = '" + cinsiyet+"' where id = "+ str(id))

        imlec.execute("UPDATE baglantilar set anneID = " + str(anneID) + " where kisiID = " + str(id))
        imlec.execute("UPDATE baglantilar set babaID = " + str(babaID) + " where kisiID = " + str(id))
        imlec.execute("UPDATE baglantilar set cocuklarID = '" + str(cocuklarID) + "' where kisiID = " + str(id))




        vt.commit()
        vt.close()

        lineTemizle()

    except:
        pass

def id_ile_guncelle(ui,vtKonum):

   try:

       lineTemizle(ui)

       id = int(ui.line_ID.text())

       vt = sql.connect(vtKonum)
       imlec = vt.cursor()



       donut = imlec.execute('SELECT * FROM kisi where id ='+ str(id))
       donut = donut.fetchall()[0]

       ad = donut[1]
       soyad = donut[2]
       cinsiyet = donut[3]

       donut = imlec.execute('SELECT * FROM baglantilar where kisiID ='+ str(id))
       donut = donut.fetchall()[0]

       anneID = donut[1]
       babaID = donut[2]
       cocuklarID = donut[3]

       #print(ad,soyad,anneID,babaID,cocuklarID)

       ui.line_Ad.setText(ad)
       ui.line_Soyad.setText(soyad)
       ui.line_BabaID.setText(str(babaID))
       ui.line_AnneID.setText(str(anneID))
       ui.line_cocuklarID.setText(cocuklarID)
       ui.line_cinsiyet.setText(cinsiyet)

       vt.commit()
       vt.close()



   except:
       pass

def kisileri_goster(ui,vtKonum):
    try:


        vt = sql.connect(vtKonum)
        imlec = vt.cursor()

        kisi = imlec.execute('SELECT * FROM kisi')
        kisi = kisi.fetchall()

        baglantilar = imlec.execute('SELECT * FROM baglantilar')
        baglantilar = baglantilar.fetchall()


        for i in range(len(kisi)):
            ui.cikti.append(str(kisi[i][0]) +". "+  str(kisi[i][1]) + " "+ str(kisi[i][2]) + " ** "+str(baglantilar[i][1])+ " ** "+str(baglantilar[i][2]) +" ** "+ str(baglantilar[i][3]) + " ** " + str(kisi[i][3]))




        vt.commit()
        vt.close()

        lineTemizle()

    except:
        pass

def ekraniTemizle(ui):
    lineTemizle(ui)
    ui.cikti.clear()

def lineTemizle(ui):
    ui.line_Ad.clear()
    ui.line_Soyad.clear()
    ui.line_AnneID.clear()
    ui.line_BabaID.clear()
    ui.line_cocuklarID.clear()
    ui.line_cinsiyet.clear()


