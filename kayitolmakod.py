import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from KayitOlma import Ui_kayitekrani
import sqlite3 as sql

class RegisterApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_kayitekrani()
        self.ui.setupUi(self)
        self.ui.btnRegister.clicked.connect(self.register)
        self.ui.btnLogin.clicked.connect(self.open_login_page) 

        self.conn = sql.connect('kullanicikayit.db')
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                lastname TEXT,
                username TEXT UNIQUE,
                password TEXT,
                isAdmin INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def register(self):
        name = self.ui.lneName.text()
        lastname = self.ui.lneLastName.text()
        username = self.ui.lneUsername.text()
        password = self.ui.lnePassword.text()

        if not name or not lastname or not username or not password:
            QMessageBox.warning(self, "Uyarı", "Bütün alanları doldurmak zorunludur!")
            return

        try:
            self.insert(name, lastname, username, password)
            QMessageBox.information(self, "Başarılı", "Kayıt başarıyla oluşturuldu!")
        except sql.IntegrityError:
            QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten mevcut.")
        except Exception as error:
            QMessageBox.critical(self, "Hata", f"Kayıt oluşturulurken bir hata oluştu:\n{error}")

        self.clear_fields()

    def insert(self, name, lastname, username, password):
        ekle = "INSERT INTO users (name, lastname, username, password) VALUES (?, ?, ?, ?)"
        self.cursor.execute(ekle, (name, lastname, username, password))
        self.conn.commit()

    def clear_fields(self):
        self.ui.lneName.clear()
        self.ui.lneLastName.clear()
        self.ui.lneUsername.clear()
        self.ui.lnePassword.clear()

    def open_login_page(self):
        self.hide()
        self.parent().show()

    def closeEvent(self, event):
        self.parent().show()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterApp()
    window.show()
    sys.exit(app.exec_())
