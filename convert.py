from PyQt5 import uic
with open("AdminPage.py","w" ,encoding="utf-8") as fout:
    uic.compileUi("adminPage.ui",fout)