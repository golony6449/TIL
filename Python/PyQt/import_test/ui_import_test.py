import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from basic.mainui import  *

__author__ = "Deokyu Lim <hong18s@gmail.com>"


class Form(QMainWindow,Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        #self.ui=Ui_MainWindow()
        self.setupUi(self)
        print("test")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    exit(app.exec_())
