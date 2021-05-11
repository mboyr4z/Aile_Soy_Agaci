from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(922, 480)

        self.lbl_Ad = QtWidgets.QLabel(self)
        self.lbl_Ad.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.lbl_Ad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_Ad = QtWidgets.QLineEdit(self)
        self.line_Ad.setGeometry(QtCore.QRect(70, 10, 131, 21))

        self.lbl_Soyad = QtWidgets.QLabel(self)
        self.lbl_Soyad.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.lbl_Soyad.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_Soyad = QtWidgets.QLineEdit(self)
        self.line_Soyad.setGeometry(QtCore.QRect(70, 40, 131, 21))

        self.lbl_AnneID = QtWidgets.QLabel(self)
        self.lbl_AnneID.setGeometry(QtCore.QRect(10, 70, 51, 16))
        self.lbl_AnneID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_AnneID = QtWidgets.QLineEdit(self)
        self.line_AnneID.setGeometry(QtCore.QRect(70, 70, 131, 21))

        self.lbl_BabaId = QtWidgets.QLabel(self)
        self.lbl_BabaId.setGeometry(QtCore.QRect(10, 100, 51, 16))
        self.lbl_BabaId.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_BabaID = QtWidgets.QLineEdit(self)
        self.line_BabaID.setGeometry(QtCore.QRect(70, 100, 131, 21))

        self.lbl_cocuklarID = QtWidgets.QLabel(self)
        self.lbl_cocuklarID.setGeometry(QtCore.QRect(10, 130, 51, 16))
        self.lbl_cocuklarID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_cocuklarID = QtWidgets.QLineEdit(self)
        self.line_cocuklarID.setGeometry(QtCore.QRect(70, 130, 131, 21))

        self.lbl_cinsiyet = QtWidgets.QLabel(self)
        self.lbl_cinsiyet.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.lbl_cinsiyet.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.line_cinsiyet = QtWidgets.QLineEdit(self)
        self.line_cinsiyet.setGeometry(QtCore.QRect(70, 160, 131, 21))


        self.btn_kaydet = QtWidgets.QPushButton(self)
        self.btn_kaydet.setGeometry(QtCore.QRect(70, 190, 131, 31))

        self.line_ID = QtWidgets.QLineEdit(self)
        self.line_ID.setGeometry(QtCore.QRect(70, 240, 131, 21))

        self.btn_taramayaBasla = QtWidgets.QPushButton(self)
        self.btn_taramayaBasla.setGeometry(QtCore.QRect(70, 270, 131, 31))

        self.lbl_ID = QtWidgets.QLabel(self)
        self.lbl_ID.setGeometry(QtCore.QRect(10, 240, 51, 16))
        self.lbl_ID.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

        self.btn_sil = QtWidgets.QPushButton(self)
        self.btn_sil.setGeometry(QtCore.QRect(70, 302, 131, 31))

        self.btn_guncelle = QtWidgets.QPushButton(self)
        self.btn_guncelle.setGeometry(QtCore.QRect(70, 334, 131, 31))

        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(40, 220, 161, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.btn_tumKisileriSil = QtWidgets.QPushButton(self)
        self.btn_tumKisileriSil.setGeometry(QtCore.QRect(70, 366, 131, 31))

        self.btn_ekraniTemizle = QtWidgets.QPushButton(self)
        self.btn_ekraniTemizle.setGeometry(QtCore.QRect(70, 400, 131, 31))

        self.btn_kisileriGoster = QtWidgets.QPushButton(self)
        self.btn_kisileriGoster.setGeometry(QtCore.QRect(70, 433, 131, 31))


        self.cikti = QtWidgets.QTextBrowser(self)
        self.cikti.setGeometry(QtCore.QRect(210, 10, 700, 454))

        self.setStyleSheet("QWidget{background:#760925;color:white;}"
                           "QLineEdit{border:1px solid;border-radius:3px; border-color:White;}"
                           "QPushButton{background:white;color:black;border:2px solid; border-radius:5px;}"
                           "QPushButton:hover{background:#760925;color:white;border:3px solid;border-color:white;}"
                           "QTextBrowser{color:black;border:2px solid; border-radius:5px; background:White;}")
        self.show()

        self.btn_tumKisileriSil.setEnabled(False)
        self.btn_sil.setEnabled(False)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_cocuklarID.setText("ÇocukID:")
        self.lbl_cinsiyet.setText("Cinsiyet:")
        self.btn_kisileriGoster.setText("Kişileri Göster")
        self.setWindowTitle(_translate("self", "Akrabalık Ağacı"))
        self.lbl_Ad.setText(_translate("self", "Ad:"))
        self.lbl_Soyad.setText(_translate("self", "Soyad:"))
        self.lbl_AnneID.setText(_translate("self", "Anne ID:"))
        self.lbl_BabaId.setText(_translate("self", "Baba ID:"))
        self.btn_kaydet.setText(_translate("self", "Kaydet"))
        self.btn_taramayaBasla.setText(_translate("self", "Çalıştır"))
        self.lbl_ID.setText(_translate("self", "ID:"))
        self.btn_sil.setText(_translate("self", "Sil"))
        self.btn_guncelle.setText(_translate("self", "Güncelle"))
        self.btn_tumKisileriSil.setText(_translate("self", "Tüm Kişileri Sil"))
        self.btn_ekraniTemizle.setText(_translate("self", "Ekranı Temizle"))



