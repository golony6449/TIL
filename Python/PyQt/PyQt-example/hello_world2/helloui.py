# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hello.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QLineEdit(Dialog)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BTN_1st = QtWidgets.QPushButton(Dialog)
        self.BTN_1st.setObjectName("BTN_1st")
        self.horizontalLayout.addWidget(self.BTN_1st)
        self.BTN_2nd = QtWidgets.QPushButton(Dialog)
        self.BTN_2nd.setObjectName("BTN_2nd")
        self.horizontalLayout.addWidget(self.BTN_2nd)
        self.BTN_3rd = QtWidgets.QPushButton(Dialog)
        self.BTN_3rd.setObjectName("BTN_3rd")
        self.horizontalLayout.addWidget(self.BTN_3rd)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.BTN_1st.clicked.connect(Dialog.slot_1st)
        self.BTN_2nd.clicked.connect(Dialog.slot_2nd)
        self.BTN_3rd.clicked.connect(Dialog.slot_3rd)
        self.line.textChanged['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "여기에 입력 됩니다요"))
        self.line.setText(_translate("Dialog", "Hello World"))
        self.BTN_1st.setText(_translate("Dialog", "첫번째"))
        self.BTN_2nd.setText(_translate("Dialog", "두번째"))
        self.BTN_3rd.setText(_translate("Dialog", "세번째"))

