from PyQt5 import QtCore, QtGui, QtWidgets
import random
from database_recognition import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("TRAFFIC TRACK SYSTEM")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(200, 100, 500, 500))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("Resources/emergency.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        self.car = QtWidgets.QPushButton(self.centralwidget)
        self.car.setGeometry(QtCore.QRect(75, 300, 100, 75))
        self.car.setObjectName("car")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.car.clicked.connect(self.show_car)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.car.setText(_translate("MainWindow", "START"))


    def show_car(self):
        randomImage = "Resources/image" + str(random.randint(1, 4)) + ".png"
        results, plates = recognition(randomImage)
        cv2.imshow("X", results[0])
        print(plates[0][1])
        self.photo.setPixmap(QtGui.QPixmap(randomImage))