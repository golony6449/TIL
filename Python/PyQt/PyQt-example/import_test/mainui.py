# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TimeOut = QtWidgets.QGroupBox(self.centralwidget)
        self.TimeOut.setGeometry(QtCore.QRect(10, 10, 280, 651))
        self.TimeOut.setTitle("")
        self.TimeOut.setObjectName("TimeOut")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.TimeOut)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.TimeOut)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.TimeOutList = QtWidgets.QListView(self.TimeOut)
        self.TimeOutList.setObjectName("TimeOutList")
        self.verticalLayout_3.addWidget(self.TimeOutList)
        self.PC_group = QtWidgets.QGroupBox(self.centralwidget)
        self.PC_group.setGeometry(QtCore.QRect(290, 0, 981, 318))
        self.PC_group.setObjectName("PC_group")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.PC_group)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BTN_PC_2 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_2.sizePolicy().hasHeightForWidth())
        self.BTN_PC_2.setSizePolicy(sizePolicy)
        self.BTN_PC_2.setObjectName("BTN_PC_2")
        self.gridLayout_2.addWidget(self.BTN_PC_2, 0, 1, 1, 1)
        self.BTN_PC_10 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_10.sizePolicy().hasHeightForWidth())
        self.BTN_PC_10.setSizePolicy(sizePolicy)
        self.BTN_PC_10.setObjectName("BTN_PC_10")
        self.gridLayout_2.addWidget(self.BTN_PC_10, 0, 9, 1, 1)
        self.BTN_PC_16 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_16.sizePolicy().hasHeightForWidth())
        self.BTN_PC_16.setSizePolicy(sizePolicy)
        self.BTN_PC_16.setObjectName("BTN_PC_16")
        self.gridLayout_2.addWidget(self.BTN_PC_16, 2, 5, 1, 1)
        self.BTN_PC_11 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_11.sizePolicy().hasHeightForWidth())
        self.BTN_PC_11.setSizePolicy(sizePolicy)
        self.BTN_PC_11.setObjectName("BTN_PC_11")
        self.gridLayout_2.addWidget(self.BTN_PC_11, 2, 0, 1, 1)
        self.BTN_PC_13 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_13.sizePolicy().hasHeightForWidth())
        self.BTN_PC_13.setSizePolicy(sizePolicy)
        self.BTN_PC_13.setObjectName("BTN_PC_13")
        self.gridLayout_2.addWidget(self.BTN_PC_13, 2, 2, 1, 1)
        self.BTN_PC_12 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_12.sizePolicy().hasHeightForWidth())
        self.BTN_PC_12.setSizePolicy(sizePolicy)
        self.BTN_PC_12.setObjectName("BTN_PC_12")
        self.gridLayout_2.addWidget(self.BTN_PC_12, 2, 1, 1, 1)
        self.LEDIT_PC_15 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_15.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_15.setReadOnly(True)
        self.LEDIT_PC_15.setObjectName("LEDIT_PC_15")
        self.gridLayout_2.addWidget(self.LEDIT_PC_15, 3, 4, 1, 1)
        self.LEDIT_PC_8 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_8.setReadOnly(True)
        self.LEDIT_PC_8.setObjectName("LEDIT_PC_8")
        self.gridLayout_2.addWidget(self.LEDIT_PC_8, 1, 7, 1, 1)
        self.LEDIT_PC_9 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_9.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_9.setReadOnly(True)
        self.LEDIT_PC_9.setObjectName("LEDIT_PC_9")
        self.gridLayout_2.addWidget(self.LEDIT_PC_9, 1, 8, 1, 1)
        self.LEDIT_PC_14 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_14.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_14.setReadOnly(True)
        self.LEDIT_PC_14.setObjectName("LEDIT_PC_14")
        self.gridLayout_2.addWidget(self.LEDIT_PC_14, 3, 3, 1, 1)
        self.LEDIT_PC_10 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_10.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_10.setReadOnly(True)
        self.LEDIT_PC_10.setObjectName("LEDIT_PC_10")
        self.gridLayout_2.addWidget(self.LEDIT_PC_10, 1, 9, 1, 1)
        self.BTN_PC_18 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_18.sizePolicy().hasHeightForWidth())
        self.BTN_PC_18.setSizePolicy(sizePolicy)
        self.BTN_PC_18.setObjectName("BTN_PC_18")
        self.gridLayout_2.addWidget(self.BTN_PC_18, 2, 7, 1, 1)
        self.BTN_PC_14 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_14.sizePolicy().hasHeightForWidth())
        self.BTN_PC_14.setSizePolicy(sizePolicy)
        self.BTN_PC_14.setObjectName("BTN_PC_14")
        self.gridLayout_2.addWidget(self.BTN_PC_14, 2, 3, 1, 1)
        self.BTN_PC_15 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_15.sizePolicy().hasHeightForWidth())
        self.BTN_PC_15.setSizePolicy(sizePolicy)
        self.BTN_PC_15.setObjectName("BTN_PC_15")
        self.gridLayout_2.addWidget(self.BTN_PC_15, 2, 4, 1, 1)
        self.BTN_PC_3 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_3.sizePolicy().hasHeightForWidth())
        self.BTN_PC_3.setSizePolicy(sizePolicy)
        self.BTN_PC_3.setObjectName("BTN_PC_3")
        self.gridLayout_2.addWidget(self.BTN_PC_3, 0, 2, 1, 1)
        self.LEDIT_PC_18 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_18.setReadOnly(True)
        self.LEDIT_PC_18.setObjectName("LEDIT_PC_18")
        self.gridLayout_2.addWidget(self.LEDIT_PC_18, 3, 7, 1, 1)
        self.BTN_PC_19 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_19.sizePolicy().hasHeightForWidth())
        self.BTN_PC_19.setSizePolicy(sizePolicy)
        self.BTN_PC_19.setObjectName("BTN_PC_19")
        self.gridLayout_2.addWidget(self.BTN_PC_19, 2, 8, 1, 1)
        self.BTN_PC_17 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_17.sizePolicy().hasHeightForWidth())
        self.BTN_PC_17.setSizePolicy(sizePolicy)
        self.BTN_PC_17.setObjectName("BTN_PC_17")
        self.gridLayout_2.addWidget(self.BTN_PC_17, 2, 6, 1, 1)
        self.LEDIT_PC_11 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_11.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_11.setReadOnly(True)
        self.LEDIT_PC_11.setObjectName("LEDIT_PC_11")
        self.gridLayout_2.addWidget(self.LEDIT_PC_11, 3, 0, 1, 1)
        self.LEDIT_PC_13 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_13.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_13.setReadOnly(True)
        self.LEDIT_PC_13.setObjectName("LEDIT_PC_13")
        self.gridLayout_2.addWidget(self.LEDIT_PC_13, 3, 2, 1, 1)
        self.BTN_PC_9 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_9.sizePolicy().hasHeightForWidth())
        self.BTN_PC_9.setSizePolicy(sizePolicy)
        self.BTN_PC_9.setObjectName("BTN_PC_9")
        self.gridLayout_2.addWidget(self.BTN_PC_9, 0, 8, 1, 1)
        self.LEDIT_PC_12 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_12.setReadOnly(True)
        self.LEDIT_PC_12.setObjectName("LEDIT_PC_12")
        self.gridLayout_2.addWidget(self.LEDIT_PC_12, 3, 1, 1, 1)
        self.LEDIT_PC_6 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_6.setReadOnly(True)
        self.LEDIT_PC_6.setObjectName("LEDIT_PC_6")
        self.gridLayout_2.addWidget(self.LEDIT_PC_6, 1, 5, 1, 1)
        self.LEDIT_PC_7 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_7.setReadOnly(True)
        self.LEDIT_PC_7.setObjectName("LEDIT_PC_7")
        self.gridLayout_2.addWidget(self.LEDIT_PC_7, 1, 6, 1, 1)
        self.LEDIT_PC_1 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_1.setReadOnly(True)
        self.LEDIT_PC_1.setObjectName("LEDIT_PC_1")
        self.gridLayout_2.addWidget(self.LEDIT_PC_1, 1, 0, 1, 1)
        self.BTN_PC_1 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_1.sizePolicy().hasHeightForWidth())
        self.BTN_PC_1.setSizePolicy(sizePolicy)
        self.BTN_PC_1.setObjectName("BTN_PC_1")
        self.gridLayout_2.addWidget(self.BTN_PC_1, 0, 0, 1, 1)
        self.LEDIT_PC_16 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_16.setReadOnly(True)
        self.LEDIT_PC_16.setObjectName("LEDIT_PC_16")
        self.gridLayout_2.addWidget(self.LEDIT_PC_16, 3, 5, 1, 1)
        self.LEDIT_PC_17 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_17.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_17.setReadOnly(True)
        self.LEDIT_PC_17.setObjectName("LEDIT_PC_17")
        self.gridLayout_2.addWidget(self.LEDIT_PC_17, 3, 6, 1, 1)
        self.BTN_PC_20 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_20.sizePolicy().hasHeightForWidth())
        self.BTN_PC_20.setSizePolicy(sizePolicy)
        self.BTN_PC_20.setObjectName("BTN_PC_20")
        self.gridLayout_2.addWidget(self.BTN_PC_20, 2, 9, 1, 1)
        self.BTN_PC_4 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_4.sizePolicy().hasHeightForWidth())
        self.BTN_PC_4.setSizePolicy(sizePolicy)
        self.BTN_PC_4.setObjectName("BTN_PC_4")
        self.gridLayout_2.addWidget(self.BTN_PC_4, 0, 3, 1, 1)
        self.LEDIT_PC_5 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_5.setReadOnly(True)
        self.LEDIT_PC_5.setObjectName("LEDIT_PC_5")
        self.gridLayout_2.addWidget(self.LEDIT_PC_5, 1, 4, 1, 1)
        self.LEDIT_PC_20 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_20.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_20.setReadOnly(True)
        self.LEDIT_PC_20.setObjectName("LEDIT_PC_20")
        self.gridLayout_2.addWidget(self.LEDIT_PC_20, 3, 9, 1, 1)
        self.LEDIT_PC_4 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_4.setReadOnly(True)
        self.LEDIT_PC_4.setObjectName("LEDIT_PC_4")
        self.gridLayout_2.addWidget(self.LEDIT_PC_4, 1, 3, 1, 1)
        self.LEDIT_PC_3 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_3.setReadOnly(True)
        self.LEDIT_PC_3.setObjectName("LEDIT_PC_3")
        self.gridLayout_2.addWidget(self.LEDIT_PC_3, 1, 2, 1, 1)
        self.LEDIT_PC_2 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_2.setReadOnly(True)
        self.LEDIT_PC_2.setObjectName("LEDIT_PC_2")
        self.gridLayout_2.addWidget(self.LEDIT_PC_2, 1, 1, 1, 1)
        self.LEDIT_PC_19 = QtWidgets.QLineEdit(self.PC_group)
        self.LEDIT_PC_19.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LEDIT_PC_19.setReadOnly(True)
        self.LEDIT_PC_19.setObjectName("LEDIT_PC_19")
        self.gridLayout_2.addWidget(self.LEDIT_PC_19, 3, 8, 1, 1)
        self.BTN_PC_5 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_5.sizePolicy().hasHeightForWidth())
        self.BTN_PC_5.setSizePolicy(sizePolicy)
        self.BTN_PC_5.setObjectName("BTN_PC_5")
        self.gridLayout_2.addWidget(self.BTN_PC_5, 0, 4, 1, 1)
        self.BTN_PC_6 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_6.sizePolicy().hasHeightForWidth())
        self.BTN_PC_6.setSizePolicy(sizePolicy)
        self.BTN_PC_6.setObjectName("BTN_PC_6")
        self.gridLayout_2.addWidget(self.BTN_PC_6, 0, 5, 1, 1)
        self.BTN_PC_8 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_8.sizePolicy().hasHeightForWidth())
        self.BTN_PC_8.setSizePolicy(sizePolicy)
        self.BTN_PC_8.setObjectName("BTN_PC_8")
        self.gridLayout_2.addWidget(self.BTN_PC_8, 0, 7, 1, 1)
        self.BTN_PC_7 = QtWidgets.QPushButton(self.PC_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_PC_7.sizePolicy().hasHeightForWidth())
        self.BTN_PC_7.setSizePolicy(sizePolicy)
        self.BTN_PC_7.setObjectName("BTN_PC_7")
        self.gridLayout_2.addWidget(self.BTN_PC_7, 0, 6, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        self.Extra_group = QtWidgets.QGroupBox(self.centralwidget)
        self.Extra_group.setGeometry(QtCore.QRect(290, 320, 981, 171))
        self.Extra_group.setObjectName("Extra_group")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Extra_group)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.LEDIT_Mul_1 = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Mul_1.setObjectName("LEDIT_Mul_1")
        self.gridLayout_3.addWidget(self.LEDIT_Mul_1, 2, 0, 1, 1)
        self.LEDIT_Band = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Band.setObjectName("LEDIT_Band")
        self.gridLayout_3.addWidget(self.LEDIT_Band, 2, 5, 1, 1)
        self.LEDIT_Mul_3 = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Mul_3.setObjectName("LEDIT_Mul_3")
        self.gridLayout_3.addWidget(self.LEDIT_Mul_3, 2, 2, 1, 1)
        self.LEDIT_Ping_1 = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Ping_1.setObjectName("LEDIT_Ping_1")
        self.gridLayout_3.addWidget(self.LEDIT_Ping_1, 2, 6, 1, 1)
        self.LEDIT_Prac = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Prac.setObjectName("LEDIT_Prac")
        self.gridLayout_3.addWidget(self.LEDIT_Prac, 2, 4, 1, 1)
        self.BTN_Ping_3 = QtWidgets.QLineEdit(self.Extra_group)
        self.BTN_Ping_3.setObjectName("BTN_Ping_3")
        self.gridLayout_3.addWidget(self.BTN_Ping_3, 2, 7, 1, 1)
        self.LEDIT_Hall = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Hall.setObjectName("LEDIT_Hall")
        self.gridLayout_3.addWidget(self.LEDIT_Hall, 2, 3, 1, 1)
        self.LEDIT_Mul_2 = QtWidgets.QLineEdit(self.Extra_group)
        self.LEDIT_Mul_2.setObjectName("LEDIT_Mul_2")
        self.gridLayout_3.addWidget(self.LEDIT_Mul_2, 2, 1, 1, 1)
        self.BTN_Ping_1 = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Ping_1.sizePolicy().hasHeightForWidth())
        self.BTN_Ping_1.setSizePolicy(sizePolicy)
        self.BTN_Ping_1.setObjectName("BTN_Ping_1")
        self.gridLayout_3.addWidget(self.BTN_Ping_1, 1, 6, 1, 1)
        self.BTN_Hall = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Hall.sizePolicy().hasHeightForWidth())
        self.BTN_Hall.setSizePolicy(sizePolicy)
        self.BTN_Hall.setObjectName("BTN_Hall")
        self.gridLayout_3.addWidget(self.BTN_Hall, 1, 3, 1, 1)
        self.BTN_Mul_1 = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Mul_1.sizePolicy().hasHeightForWidth())
        self.BTN_Mul_1.setSizePolicy(sizePolicy)
        self.BTN_Mul_1.setObjectName("BTN_Mul_1")
        self.gridLayout_3.addWidget(self.BTN_Mul_1, 1, 0, 1, 1)
        self.BTN_Mul_2 = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Mul_2.sizePolicy().hasHeightForWidth())
        self.BTN_Mul_2.setSizePolicy(sizePolicy)
        self.BTN_Mul_2.setObjectName("BTN_Mul_2")
        self.gridLayout_3.addWidget(self.BTN_Mul_2, 1, 1, 1, 1)
        self.BTN_Band = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Band.sizePolicy().hasHeightForWidth())
        self.BTN_Band.setSizePolicy(sizePolicy)
        self.BTN_Band.setObjectName("BTN_Band")
        self.gridLayout_3.addWidget(self.BTN_Band, 1, 5, 1, 1)
        self.BTN_Ping_2 = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Ping_2.sizePolicy().hasHeightForWidth())
        self.BTN_Ping_2.setSizePolicy(sizePolicy)
        self.BTN_Ping_2.setObjectName("BTN_Ping_2")
        self.gridLayout_3.addWidget(self.BTN_Ping_2, 1, 7, 1, 1)
        self.BTN_Prac = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Prac.sizePolicy().hasHeightForWidth())
        self.BTN_Prac.setSizePolicy(sizePolicy)
        self.BTN_Prac.setObjectName("BTN_Prac")
        self.gridLayout_3.addWidget(self.BTN_Prac, 1, 4, 1, 1)
        self.BTN_Mul_3 = QtWidgets.QPushButton(self.Extra_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Mul_3.sizePolicy().hasHeightForWidth())
        self.BTN_Mul_3.setSizePolicy(sizePolicy)
        self.BTN_Mul_3.setObjectName("BTN_Mul_3")
        self.gridLayout_3.addWidget(self.BTN_Mul_3, 1, 2, 1, 1)
        self.Borad_group = QtWidgets.QGroupBox(self.centralwidget)
        self.Borad_group.setGeometry(QtCore.QRect(290, 490, 981, 171))
        self.Borad_group.setObjectName("Borad_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Borad_group)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LEDIT_Board_2 = QtWidgets.QLineEdit(self.Borad_group)
        self.LEDIT_Board_2.setObjectName("LEDIT_Board_2")
        self.gridLayout_4.addWidget(self.LEDIT_Board_2, 2, 1, 1, 1)
        self.LEDIT_Board_4 = QtWidgets.QLineEdit(self.Borad_group)
        self.LEDIT_Board_4.setObjectName("LEDIT_Board_4")
        self.gridLayout_4.addWidget(self.LEDIT_Board_4, 2, 3, 1, 1)
        self.LEDIT_Board_5 = QtWidgets.QLineEdit(self.Borad_group)
        self.LEDIT_Board_5.setObjectName("LEDIT_Board_5")
        self.gridLayout_4.addWidget(self.LEDIT_Board_5, 2, 4, 1, 1)
        self.BTN_Board_5 = QtWidgets.QPushButton(self.Borad_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Board_5.sizePolicy().hasHeightForWidth())
        self.BTN_Board_5.setSizePolicy(sizePolicy)
        self.BTN_Board_5.setObjectName("BTN_Board_5")
        self.gridLayout_4.addWidget(self.BTN_Board_5, 1, 4, 1, 1)
        self.LEDIT_Board_1 = QtWidgets.QLineEdit(self.Borad_group)
        self.LEDIT_Board_1.setObjectName("LEDIT_Board_1")
        self.gridLayout_4.addWidget(self.LEDIT_Board_1, 2, 0, 1, 1)
        self.BTN_Board_1 = QtWidgets.QPushButton(self.Borad_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Board_1.sizePolicy().hasHeightForWidth())
        self.BTN_Board_1.setSizePolicy(sizePolicy)
        self.BTN_Board_1.setObjectName("BTN_Board_1")
        self.gridLayout_4.addWidget(self.BTN_Board_1, 1, 0, 1, 1)
        self.BTN_Board_3 = QtWidgets.QPushButton(self.Borad_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Board_3.sizePolicy().hasHeightForWidth())
        self.BTN_Board_3.setSizePolicy(sizePolicy)
        self.BTN_Board_3.setObjectName("BTN_Board_3")
        self.gridLayout_4.addWidget(self.BTN_Board_3, 1, 2, 1, 1)
        self.BTN_Board_2 = QtWidgets.QPushButton(self.Borad_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Board_2.sizePolicy().hasHeightForWidth())
        self.BTN_Board_2.setSizePolicy(sizePolicy)
        self.BTN_Board_2.setObjectName("BTN_Board_2")
        self.gridLayout_4.addWidget(self.BTN_Board_2, 1, 1, 1, 1)
        self.BTN_Board_4 = QtWidgets.QPushButton(self.Borad_group)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BTN_Board_4.sizePolicy().hasHeightForWidth())
        self.BTN_Board_4.setSizePolicy(sizePolicy)
        self.BTN_Board_4.setObjectName("BTN_Board_4")
        self.gridLayout_4.addWidget(self.BTN_Board_4, 1, 3, 1, 1)
        self.LEDIT_Board_3 = QtWidgets.QLineEdit(self.Borad_group)
        self.LEDIT_Board_3.setObjectName("LEDIT_Board_3")
        self.gridLayout_4.addWidget(self.LEDIT_Board_3, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionstatistic = QtWidgets.QAction(MainWindow)
        self.actionstatistic.setObjectName("actionstatistic")
        self.menu.addAction(self.actionstatistic)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "거창군 청소년 문화의 집"))
        self.label.setText(_translate("MainWindow", "시간 종료"))
        self.PC_group.setTitle(_translate("MainWindow", "PC"))
        self.BTN_PC_2.setText(_translate("MainWindow", "PC02"))
        self.BTN_PC_10.setText(_translate("MainWindow", "PC10"))
        self.BTN_PC_16.setText(_translate("MainWindow", "PC16"))
        self.BTN_PC_11.setText(_translate("MainWindow", "PC11"))
        self.BTN_PC_13.setText(_translate("MainWindow", "PC13"))
        self.BTN_PC_12.setText(_translate("MainWindow", "PC12"))
        self.BTN_PC_18.setText(_translate("MainWindow", "PC18"))
        self.BTN_PC_14.setText(_translate("MainWindow", "PC14"))
        self.BTN_PC_15.setText(_translate("MainWindow", "PC15"))
        self.BTN_PC_3.setText(_translate("MainWindow", "PC03"))
        self.BTN_PC_19.setText(_translate("MainWindow", "PC19"))
        self.BTN_PC_17.setText(_translate("MainWindow", "PC17"))
        self.BTN_PC_9.setText(_translate("MainWindow", "PC09"))
        self.BTN_PC_1.setText(_translate("MainWindow", "PC01"))
        self.BTN_PC_20.setText(_translate("MainWindow", "PC20"))
        self.BTN_PC_4.setText(_translate("MainWindow", "PC04"))
        self.BTN_PC_5.setText(_translate("MainWindow", "PC05"))
        self.BTN_PC_6.setText(_translate("MainWindow", "PC06"))
        self.BTN_PC_8.setText(_translate("MainWindow", "PC08"))
        self.BTN_PC_7.setText(_translate("MainWindow", "PC07"))
        self.Extra_group.setTitle(_translate("MainWindow", "부대시설"))
        self.BTN_Ping_1.setText(_translate("MainWindow", "탁구01"))
        self.BTN_Hall.setText(_translate("MainWindow", "다목적홀"))
        self.BTN_Mul_1.setText(_translate("MainWindow", "멀티방01"))
        self.BTN_Mul_2.setText(_translate("MainWindow", "멀티방02"))
        self.BTN_Band.setText(_translate("MainWindow", "밴드연습실"))
        self.BTN_Ping_2.setText(_translate("MainWindow", "탁구02"))
        self.BTN_Prac.setText(_translate("MainWindow", "공연연습실"))
        self.BTN_Mul_3.setText(_translate("MainWindow", "멀티방03"))
        self.Borad_group.setTitle(_translate("MainWindow", "보드게임"))
        self.BTN_Board_5.setText(_translate("MainWindow", "보드게임05"))
        self.BTN_Board_1.setText(_translate("MainWindow", "보드게임01"))
        self.BTN_Board_3.setText(_translate("MainWindow", "보드게임03"))
        self.BTN_Board_2.setText(_translate("MainWindow", "보드게임02"))
        self.BTN_Board_4.setText(_translate("MainWindow", "보드게임04"))
        self.menu.setTitle(_translate("MainWindow", "통계"))
        self.actionstatistic.setText(_translate("MainWindow", "statistic"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

