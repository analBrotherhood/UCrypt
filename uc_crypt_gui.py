# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uc_crypt_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UCrypt(object):
    def setupUi(self, UCrypt):
        UCrypt.setObjectName("UCrypt")
        UCrypt.setEnabled(True)
        UCrypt.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(UCrypt)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(10, 10, 781, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.txt_encrypt = QtWidgets.QLabel(self.centralwidget)
        self.txt_encrypt.setGeometry(QtCore.QRect(10, 100, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txt_encrypt.setFont(font)
        self.txt_encrypt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txt_encrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_encrypt.setObjectName("txt_encrypt")
        self.txt_decrypt = QtWidgets.QLabel(self.centralwidget)
        self.txt_decrypt.setGeometry(QtCore.QRect(410, 100, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.txt_decrypt.setFont(font)
        self.txt_decrypt.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.txt_decrypt.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_decrypt.setObjectName("txt_decrypt")
        self.msg_encrypted = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_encrypted.setGeometry(QtCore.QRect(10, 390, 381, 161))
        self.msg_encrypted.setObjectName("msg_encrypted")
        self.msg_decrypted = QtWidgets.QTextBrowser(self.centralwidget)
        self.msg_decrypted.setGeometry(QtCore.QRect(410, 390, 381, 161))
        self.msg_decrypted.setObjectName("msg_decrypted")
        self.msg_to_encrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.msg_to_encrypt.setGeometry(QtCore.QRect(10, 150, 381, 181))
        self.msg_to_encrypt.setObjectName("msg_to_encrypt")
        self.msg_encrypt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.msg_encrypt_key.setGeometry(QtCore.QRect(10, 340, 261, 41))
        self.msg_encrypt_key.setObjectName("msg_encrypt_key")
        self.msg_to_decrypt = QtWidgets.QTextEdit(self.centralwidget)
        self.msg_to_decrypt.setGeometry(QtCore.QRect(410, 150, 381, 181))
        self.msg_to_decrypt.setObjectName("msg_to_decrypt")
        self.msg_decrypt_key = QtWidgets.QTextEdit(self.centralwidget)
        self.msg_decrypt_key.setGeometry(QtCore.QRect(410, 340, 261, 41))
        self.msg_decrypt_key.setObjectName("msg_decrypt_key")
        self.button_encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.button_encrypt.setGeometry(QtCore.QRect(280, 340, 111, 41))
        self.button_encrypt.setObjectName("button_encrypt")
        self.button_decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.button_decrypt.setGeometry(QtCore.QRect(680, 340, 111, 41))
        self.button_decrypt.setObjectName("button_decrypt")
        UCrypt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UCrypt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        UCrypt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UCrypt)
        self.statusbar.setObjectName("statusbar")
        UCrypt.setStatusBar(self.statusbar)

        self.retranslateUi(UCrypt)
        QtCore.QMetaObject.connectSlotsByName(UCrypt)

    def retranslateUi(self, UCrypt):
        _translate = QtCore.QCoreApplication.translate
        UCrypt.setWindowTitle(_translate("UCrypt", "UCrypt by Usu4lC0d3r S0ftw4r3"))
        self.title.setText(_translate("UCrypt", "UCrypt by Usu4lC0d3r S0ftw4r3"))
        self.txt_encrypt.setText(_translate("UCrypt", "Encrypt message"))
        self.txt_decrypt.setText(_translate("UCrypt", "Decrypt message"))
        self.msg_to_encrypt.setPlaceholderText(_translate("UCrypt", "Type message for encrypt"))
        self.msg_to_decrypt.setPlaceholderText(_translate("UCrypt", "Type message for decrypt"))
        self.msg_encrypt_key.setPlaceholderText(_translate("UCrypt", "8-digits sercet key"))
        self.msg_decrypt_key.setPlaceholderText(_translate("UCrypt", "8-digits sercet key"))
        self.msg_encrypted.setPlaceholderText(_translate("UCrypt", "Encrypted message will be shown here :3"))
        self.msg_decrypted.setPlaceholderText(_translate("UCrypt", "Decrypted message will be shown here :D"))
        self.button_encrypt.setText(_translate("UCrypt", "ENCRYPT!"))
        self.button_decrypt.setText(_translate("UCrypt", "DECRYPT!"))
