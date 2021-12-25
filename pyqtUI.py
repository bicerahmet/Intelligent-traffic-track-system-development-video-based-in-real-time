from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *

from database_recognition import recognition
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TRAFFIC TRACK SYSTEM")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.car = QtWidgets.QPushButton(self.centralwidget)
        self.car.setGeometry(QtCore.QRect(30, 150, 100, 75))
        self.car.setObjectName("car")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(200, 150, 500, 500))
        self.photo.setPixmap(QtGui.QPixmap("Resources/welcome.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("ARACIN FOTOĞRAFI")
        self.label.move(400, 100)
        self.label.setFont(QFont('Arial', 10))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("ARACIN PLAKASI")
        self.label.move(750, 100)
        self.label.setFont(QFont('Arial', 10))

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setText("....")
        self.label1.move(750, 150)
        self.label1.resize(200, 50)
        self.label1.setFont(QFont('Arial', 10))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("ARACIN DURUMU")
        self.label.move(750, 400)
        self.label.setFont(QFont('Arial', 10))

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setText("....")
        self.label2.move(750, 450)
        self.label2.resize(200, 50)
        self.label2.setFont(QFont('Arial', 10))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.car.clicked.connect(self.show_car)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.car.setText(_translate("MainWindow", "START"))

    def show_car(self):
        randomImage = "Resources/image" + str(random.randint(1, 4)) + ".jpg"
        results, plates = recognition(randomImage)
        self.label1.setText(plates[0][1])
        self.label2.setText(plates[0][-1])
        self.photo.setPixmap(QtGui.QPixmap(randomImage))