import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginButton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        if username == "ira" and password == "123":
            self.gotopage()
        else:
            self.show_popup()

    def gotopage(self):
        loginsuccess = Loginsuccess()
        widget.addWidget(loginsuccess)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Login Failed")
        msg.setText("Login Failed")
        x = msg.exec_()


class Loginsuccess(QDialog):
    def __init__(self):
        super(Loginsuccess,self).__init__()
        loadUi("loginSuccess.ui",self)

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(620)
widget.setFixedWidth(500)
widget.show()
app.exec_()