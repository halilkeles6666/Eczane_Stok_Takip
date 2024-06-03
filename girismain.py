import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from GirisEkrani import Ui_girisekrani
from adminkod import adminPage
from userpagekod import userPage
from kayitolmakod import RegisterApp
import sqlite3 as sql

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_girisekrani()
        self.ui.setupUi(self)
        self.ui.btnLogin.clicked.connect(self.login)
        self.ui.btnRegister.clicked.connect(self.open_register_page)

        self.conn = sql.connect('kullanicikayit.db')
        self.cursor = self.conn.cursor()



    def confirm_user(self, username, password):
        self.cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        return self.cursor.fetchone()



    def login(self):
        username = self.ui.lneusername.text()
        password = self.ui.lnepassword.text()
        user_data = self.confirm_user(username, password)

        if user_data:
            QMessageBox.information(self, "Başarılı", "Giriş Başarılı")
            isAdmin = user_data[5]  
            if isAdmin == 0:
                userPage(self)
            elif isAdmin == 1:
                adminPage(self)
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı.")



    def open_register_page(self):
        self.hide()
        self.register_window = RegisterApp(self)
        self.register_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
