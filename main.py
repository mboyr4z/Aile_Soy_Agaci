from PyQt5 import QtWidgets

from Proje_Akrabalik.fonksiyonlar.searching import aramayaBasla
from Proje_Akrabalik.tasarim.tasarim import Ui_Form
from Proje_Akrabalik.fonksiyonlar.veritabaniIslemleri import *
from Proje_Akrabalik.fonksiyonlar.searching import *
import sys


if __name__ == "__main__":
    import os

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()

    vtKonum = "veritabani.db"


    ui.btn_kaydet.clicked.connect(lambda : kisiEkle(ui,vtKonum))
    ui.btn_tumKisileriSil.clicked.connect(lambda : tabloSil(vtKonum))
    ui.btn_sil.clicked.connect(lambda : kisiSil(ui,vtKonum))
    ui.line_ID.textChanged.connect(lambda : id_ile_guncelle(ui,vtKonum))
    ui.btn_kisileriGoster.clicked.connect(lambda : kisileri_goster(ui,vtKonum))
    ui.btn_ekraniTemizle.clicked.connect(lambda : ekraniTemizle(ui))
    ui.btn_guncelle.clicked.connect(lambda : kisiGuncelle(ui,vtKonum))

    ui.btn_taramayaBasla.clicked.connect(lambda : aramayaBasla(ui,vtKonum))

    sys.exit(app.exec_())

