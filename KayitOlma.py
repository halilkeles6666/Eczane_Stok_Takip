# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kayitolma.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_kayitekrani(object):
    def setupUi(self, kayitekrani):
        kayitekrani.setObjectName("kayitekrani")
        kayitekrani.resize(805, 611)
        self.centralwidget = QtWidgets.QWidget(kayitekrani)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(250, 40, 281, 111))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 180, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 280, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 230, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 330, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lneName = QtWidgets.QLineEdit(self.centralwidget)
        self.lneName.setGeometry(QtCore.QRect(310, 190, 191, 31))
        self.lneName.setObjectName("lneName")
        self.lneLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lneLastName.setGeometry(QtCore.QRect(310, 240, 191, 31))
        self.lneLastName.setObjectName("lneLastName")
        self.lneUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lneUsername.setGeometry(QtCore.QRect(310, 290, 191, 31))
        self.lneUsername.setObjectName("lneUsername")
        self.lnePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lnePassword.setGeometry(QtCore.QRect(310, 350, 191, 31))
        self.lnePassword.setObjectName("lnePassword")
        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(340, 400, 101, 41))
        self.btnRegister.setObjectName("btnRegister")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 470, 221, 16))
        self.label_6.setObjectName("label_6")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(340, 460, 101, 41))
        self.btnLogin.setObjectName("btnLogin")
        kayitekrani.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(kayitekrani)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 26))
        self.menubar.setObjectName("menubar")
        kayitekrani.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(kayitekrani)
        self.statusbar.setObjectName("statusbar")
        kayitekrani.setStatusBar(self.statusbar)

        self.retranslateUi(kayitekrani)
        QtCore.QMetaObject.connectSlotsByName(kayitekrani)

    def retranslateUi(self, kayitekrani):
        _translate = QtCore.QCoreApplication.translate
        kayitekrani.setWindowTitle(_translate("kayitekrani", "MainWindow"))
        self.textBrowser.setHtml(_translate("kayitekrani", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Kayıt Ol</span></p></body></html>"))
        self.label.setText(_translate("kayitekrani", "Ad"))
        self.label_2.setText(_translate("kayitekrani", "Kullanıcı Adı"))
        self.label_3.setText(_translate("kayitekrani", "Soyad"))
        self.label_4.setText(_translate("kayitekrani", "Şifre"))
        self.btnRegister.setText(_translate("kayitekrani", "Kayıt Ol"))
        self.label_6.setText(_translate("kayitekrani", "Halihazırda hesabın var mı? Giriş Yap!"))
        self.btnLogin.setText(_translate("kayitekrani", "Giriş Yap"))
