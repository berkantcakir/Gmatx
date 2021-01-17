# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lisans.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Lisans(object):
    def setupUi(self, Lisans):
        Lisans.setObjectName("Lisans")
        Lisans.resize(476, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Lisans.setWindowIcon(icon)
        Lisans.setStyleSheet("border-image: url(C:/Users/hp/Desktop/Berkant/Diğer/gha/background.jpg) 0 0 0 0 stretch stretch;\n"
"")
        self.centralwidget = QtWidgets.QWidget(Lisans)
        self.centralwidget.setStyleSheet("border-image: ur(lC:/Users/hp/Desktop/Berkant/Diğer/gha/background1.jpg) 0 0 0 0 stretch stretch;\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.anahtarkontrol = QtWidgets.QLineEdit(self.centralwidget)
        self.anahtarkontrol.setGeometry(QtCore.QRect(40, 190, 391, 20))
        self.anahtarkontrol.setInputMask("")
        self.anahtarkontrol.setText("")
        self.anahtarkontrol.setObjectName("anahtarkontrol")
        self.lisansonay = QtWidgets.QPushButton(self.centralwidget)
        self.lisansonay.setGeometry(QtCore.QRect(280, 250, 151, 23))
        self.lisansonay.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.lisansonay.setObjectName("lisansonay")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 0, 241, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("licence.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.anahtarkontrol.raise_()
        self.lisansonay.raise_()
        Lisans.setCentralWidget(self.centralwidget)

        self.retranslateUi(Lisans)
        QtCore.QMetaObject.connectSlotsByName(Lisans)

    def retranslateUi(self, Lisans):
        _translate = QtCore.QCoreApplication.translate
        Lisans.setWindowTitle(_translate("Lisans", "Gmatix | Lisans"))
        self.lisansonay.setText(_translate("Lisans", "Onayla"))
