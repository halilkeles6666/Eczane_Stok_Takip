from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from UserPage import Ui_MainWindow
import sqlite3

class UserPageApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("urunler.db")
        self.cursor = self.conn.cursor()

        self.ui.pushButton_2.clicked.connect(self.kayit_listele)
        self.ui.pushButton.clicked.connect(self.kategoriye_gore_listele)
        self.ui.lineEdit.textChanged.connect(self.metin_ile_ara)
        self.ui.btnBack.clicked.connect(self.go_back)

        self.kayit_listele()

    def go_back(self):
        self.parent().show()
        self.close()

    def kayit_listele(self):
        self.ui.tblListe.clear()
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        sorgu = "SELECT * FROM urun"
        self.cursor.execute(sorgu)
        self.ui.tblListe.setRowCount(0)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kategoriye_gore_listele(self):
        listelenecek_kategori = self.ui.cmbListele.currentText()
        sorgu = "SELECT * FROM urun WHERE kategori = ?"
        self.cursor.execute(sorgu, (listelenecek_kategori,))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def metin_ile_ara(self):
        aranan_metin = self.ui.lineEdit.text()
        sorgu = "SELECT * FROM urun WHERE urunAdi LIKE ? OR urunAciklamasi LIKE ? OR marka LIKE ? OR kategori LIKE ?"
        self.cursor.execute(sorgu, (f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%'))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

def userPage(parent_window):
    user_window = MainWindow(parent=parent_window)
    user_window.show()
    parent_window.hide()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("urunler.db")
        self.cursor = self.conn.cursor()
        self.ui.pushButton_2.clicked.connect(self.kayit_listele)
        self.ui.pushButton.clicked.connect(self.kategoriye_gore_listele)
        self.ui.lineEdit.textChanged.connect(self.metin_ile_ara)
        self.ui.btnBack.clicked.connect(self.go_back)

        self.kayit_listele()

    def go_back(self):
        self.parent().show()
        self.close()

    def kayit_listele(self):
        self.ui.tblListe.clear()
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        sorgu = "SELECT * FROM urun"
        self.cursor.execute(sorgu)
        self.ui.tblListe.setRowCount(0)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kategoriye_gore_listele(self):
        listelenecek_kategori = self.ui.comboBox.currentText()
        sorgu = "SELECT * FROM urun WHERE kategori = ?"
        self.cursor.execute(sorgu, (listelenecek_kategori,))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def metin_ile_ara(self):
        aranan_metin = self.ui.lineEdit.text()
        sorgu = "SELECT * FROM urun WHERE urunAdi LIKE ? OR urunAciklamasi LIKE ? OR marka LIKE ? OR kategori LIKE ?"
        self.cursor.execute(sorgu, (f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%'))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(
            ("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi")
        )
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))
