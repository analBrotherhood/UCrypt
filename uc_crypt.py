from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import uc_crypt_gui
import time
import sys
import os

class App(QMainWindow, uc_crypt_gui.Ui_UCrypt):
    def __init__(self):
        super().__init__()
        self.ui = uc_crypt_gui.Ui_UCrypt()
        self.ui.setupUi(self)
        self.ui.button_encrypt.clicked.connect(self.button_encrypt_clicked)
        self.ui.button_decrypt.clicked.connect(self.button_decrypt_clicked)
        
    def button_encrypt_clicked(self):
        key_to_encrypt = self.ui.msg_encrypt_key.toPlainText()
        key_to_encrypt = int(key_to_encrypt)
        msg_for_encrypt = self.ui.msg_to_encrypt.toPlainText()
        alphabet = '=>?@[\\]678hiVWlmABCDEpqrsjkJKL01234RюБжэяЩРтшЦМйu&UмоПtлС5хКцvЧёgчwSещFTвНZ#ОькТЖЯЁфбГъуЗиргШЪ$ЮХыЫIXHЕ!ВДG"Фа%АYсЙЬИздЛoxyz<MNOPQnУЭпн9abcdef^_`{|}~ \'()*+,-./:;'
        length = len(alphabet)
        res = ''

        for c in msg_for_encrypt:
            if c in alphabet:
                s1 = alphabet.find(c)
                s1 = (s1 + key_to_encrypt) % length
                res += alphabet[s1]
            else:
                res += c
    
        self.ui.msg_encrypted.setText(res)

    def button_decrypt_clicked(self):
        key_to_decrypt = self.ui.msg_decrypt_key.toPlainText()
        key_to_decrypt = int(key_to_decrypt)
        msg_for_decrypt = self.ui.msg_to_decrypt.toPlainText()
        alphabet = '=>?@[\\]678hiVWlmABCDEpqrsjkJKL01234RюБжэяЩРтшЦМйu&UмоПtлС5хКцvЧёgчwSещFTвНZ#ОькТЖЯЁфбГъуЗиргШЪ$ЮХыЫIXHЕ!ВДG"Фа%АYсЙЬИздЛoxyz<MNOPQnУЭпн9abcdef^_`{|}~ \'()*+,-./:;'
        length = len(alphabet)
        res = ''
        
        for c in msg_for_decrypt:
            if c in alphabet:
                s1 = alphabet.find(c)
                s1 = (s1 - key_to_decrypt) % length
                res += alphabet[s1]
            else:
                res += c
        self.ui.msg_decrypted.setText(res)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.setWindowIcon(QIcon('favicon.ico'))
    window.show()
    app.exec()
