from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QHeaderView
from AdminPage import Ui_adminpanel
import sqlite3

def adminPage(parent_window):
    admin_window = MainWindow(parent=parent_window)
    admin_window.show()
    parent_window.hide()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_adminpanel()
        self.ui.setupUi(self)

        self.conn = sqlite3.connect("urunler.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS urun (
                urunKodu INTEGER PRIMARY KEY,
                urunAdi TEXT,
                birimFiyati INTEGER,
                stokMiktari INTEGER,
                urunAciklamasi TEXT,
                marka TEXT,
                kategori TEXT
            )
        """)
        self.conn.commit()

        self.ui.btnEkle.clicked.connect(self.kayit_ekle)
        self.ui.btnListele.clicked.connect(self.kayit_listele)
        self.ui.btnKategoriListele.clicked.connect(self.kategoriye_gore_listele)
        self.ui.tblListe.itemSelectionChanged.connect(self.tabloya_tikla)
        self.ui.btnSil.clicked.connect(self.kayit_sil)
        self.ui.btnGuncelleme.clicked.connect(self.kayit_guncelle)
        self.ui.lneArama.textChanged.connect(self.metin_ile_ara)
        self.ui.btngeri.clicked.connect(self.go_back)

        self.kayit_listele()

    def go_back(self):
        self.parent().show()
        self.close()

    def kayit_ekle(self):
        try:
            UrunKodu = int(self.ui.lneUrunKodu.text())
            UrunAdi = self.ui.lneUrunAdi.text()
            BirimFiyati = int(self.ui.lneBirimFiyati.text())
            StokMiktari = int(self.ui.lneStokMiktari.text())
            UrunAciklamasi = self.ui.lneUrunAciklama.text()
            Marka = self.ui.cmbMarka.currentText()
            Kategori = self.ui.cmbKategori.currentText()

            ekle = "INSERT INTO urun (urunKodu, urunAdi, birimFiyati, stokMiktari, urunAciklamasi, marka, kategori) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(ekle, (UrunKodu, UrunAdi, BirimFiyati, StokMiktari, UrunAciklamasi, Marka, Kategori))
            self.conn.commit()
            self.ui.statusbar.showMessage("Kayıt Ekleme İşlemi Başarılı", 10000)
            self.kayit_listele()
            self.clear_fields()
        except Exception as error:
            self.ui.statusbar.showMessage("Kayıt Eklenemedi Hata Çıktı: " + str(error))

    def kayit_listele(self):
        
        self.ui.tblListe.clear()
        self.ui.tblListe.setHorizontalHeaderLabels(("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi"))
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        sorgu = "SELECT * FROM urun"
        self.cursor.execute(sorgu)
        self.ui.tblListe.setRowCount(0)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def clear_fields(self):
        self.ui.lneUrunKodu.clear()
        self.ui.lneUrunAciklama.clear()
        self.ui.lneUrunAdi.clear()
        self.ui.lneBirimFiyati.clear()
        self.ui.lneStokMiktari.clear()
        self.ui.cmbMarka.clear()
        self.ui.cmbKategori.clear()
    
    
    def kategoriye_gore_listele(self):
        
        listelenecek_kategori = self.ui.cmbListele.currentText()
        sorgu = "SELECT * FROM urun WHERE kategori = ?"
        self.cursor.execute(sorgu, (listelenecek_kategori,))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi"))
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def tabloya_tikla(self):
        
        secilen = self.ui.tblListe.selectedItems()
        if secilen:
            UrunKodu = secilen[0].text()
            sorgu = "SELECT * FROM urun WHERE urunKodu = ?"
            self.cursor.execute(sorgu, (UrunKodu,))
            kayit = self.cursor.fetchone()

            if kayit:
                self.ui.lneUrunKodu.setText(str(kayit[0]))
                self.ui.lneUrunAdi.setText(kayit[1])
                self.ui.lneBirimFiyati.setText(str(kayit[2]))
                self.ui.lneStokMiktari.setText(str(kayit[3]))
                self.ui.lneUrunAciklama.setText(kayit[4])
                self.ui.cmbMarka.setCurrentText(kayit[5])
                self.ui.cmbKategori.setCurrentText(kayit[6])

    def metin_ile_ara(self):
        aranan_metin = self.ui.lneArama.text()
        sorgu = "SELECT * FROM urun WHERE urunAdi LIKE ? OR urunAciklamasi LIKE ? OR marka LIKE ? OR kategori LIKE ?"
        self.cursor.execute(sorgu, (f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%', f'%{aranan_metin}%'))
        self.ui.tblListe.clear()
        self.ui.tblListe.setRowCount(0)
        self.ui.tblListe.setHorizontalHeaderLabels(("Ürün Kodu", "Ürün Adı", "Birim Fiyati", "Stok Miktari", "Ürün Açıklama", "Ürün Markası", "Ürün Kategorisi"))
        self.ui.tblListe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for indexSatir, kayitNumarasi in enumerate(self.cursor.fetchall()):
            self.ui.tblListe.insertRow(indexSatir)
            for indexSutun, kayitSutun in enumerate(kayitNumarasi):
                self.ui.tblListe.setItem(indexSatir, indexSutun, QTableWidgetItem(str(kayitSutun)))

    def kayit_sil(self):
        self.clear_fields()
        sil_mesaj = QMessageBox.question(self, "Silme Onayı", "Silmek İstediğinize Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)
        if sil_mesaj == QMessageBox.Yes:
            secilenkayit = self.ui.tblListe.selectedItems()
            if secilenkayit:
                silinecekkayit = secilenkayit[0].text()
                sorgu = "DELETE FROM urun WHERE urunKodu = ?"
                try:
                    self.cursor.execute(sorgu, (silinecekkayit,))
                    self.conn.commit()
                    self.ui.statusbar.showMessage("Kayıt Başarıyla Silindi!", 2000)
                    self.kayit_listele()
                except Exception as error:
                    self.ui.statusbar.showMessage("Kayıt Silinirken Hata Oluştu: " + str(error))
            else:
                self.ui.statusbar.showMessage("Lütfen silmek istediğiniz kaydı seçin!")
        else:
            self.ui.statusbar.showMessage("Silme İşlemi İptal Edildi!")

    def kayit_guncelle(self):
        
        güncelle_mesaj = QMessageBox.question(self, "Güncelleme Onayı", "Güncellemek İstediğinize Emin Misiniz?", QMessageBox.Yes | QMessageBox.No)
        if güncelle_mesaj == QMessageBox.Yes:
            try:
                UrunKodu = self.ui.lneUrunKodu.text()
                UrunAdi = self.ui.lneUrunAdi.text()
                BirimFiyati = self.ui.lneBirimFiyati.text()
                StokMiktari = self.ui.lneStokMiktari.text()
                UrunAciklama = self.ui.lneUrunAciklama.text()
                Marka = self.ui.cmbMarka.currentText()
                Kategori = self.ui.cmbKategori.currentText()

                self.cursor.execute("""
                    UPDATE urun 
                    SET urunAdi = ?, birimFiyati = ?, stokMiktari = ?, urunAciklamasi = ?, marka = ?, kategori = ?
                    WHERE urunKodu = ?
                """, (UrunAdi, BirimFiyati, StokMiktari, UrunAciklama, Marka, Kategori, UrunKodu))
                self.conn.commit()
                self.kayit_listele()
                self.ui.statusbar.showMessage("Kayıt Başarıyla Güncellendi!")
            except Exception as error:
                self.ui.statusbar.showMessage("Güncellemede Hata Oluştu: " + str(error))
        else:
            self.ui.statusbar.showMessage("Güncelleme İptal Edildi!")
