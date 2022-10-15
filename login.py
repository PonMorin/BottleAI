# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_MainWindow


class Ui_loginWindow(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton#Login_Button{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(35, 93, 58);\n"
"    border-radius: 15px;\n"
"    \n"
"    border-left:1px solid rgb(116, 146, 122);\n"
"    border-right:1px solid rgb(116, 146, 122);\n"
"    border-bottom:5px solid rgb(116, 146, 122);\n"
"}\n"
"QPushButton#Login_Button:hover{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-bottom:5px solid rgb(128,128,128);\n"
"}\n"
"QPushButton#Login_Button:pressed{\n"
"    background-color:rgb(192,192,192);\n"
"    color:rgb(0,0,0);\n"
"    border-left:1px solid rgb(128,128,128);\n"
"    border-right:1px solid rgb(128,128,128);\n"
"    border-top:5px solid rgb(128,128,128);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 500, 230))
        self.label_2.setStyleSheet("\n"
"background-color: rgb(115, 192, 136);")
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(5)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 160, 191, 191))
        self.label_3.setStyleSheet("border-image: url(:/pic/kisspng-clip-art-water-bottles-portable-network-graphics-o-water-bottle-png-clipart-vector-clipart-psd-pe-5ce4d4e4a08179.5023082315585005806574-removebg-preview.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 90, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.student_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.student_ID.setGeometry(QtCore.QRect(110, 210, 211, 41))
        self.student_ID.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.student_ID.setObjectName("student_ID")
        self.student_Pass = QtWidgets.QLineEdit(self.centralwidget)
        self.student_Pass.setGeometry(QtCore.QRect(110, 260, 211, 41))
        self.student_Pass.setStyleSheet("background-color: rgba(0, 0, 0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.student_Pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.student_Pass.setObjectName("student_Pass")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(130, 320, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Login_Button.setFont(font)
        self.Login_Button.setObjectName("Login_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Login_Button.clicked.connect(self.openWindow)
        self.Login_Button.clicked.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Log In"))
        self.student_ID.setPlaceholderText(_translate("MainWindow", "Student ID"))
        self.student_Pass.setPlaceholderText(_translate("MainWindow", "Password"))
        self.Login_Button.setText(_translate("MainWindow", "L o g I n"))
import RES_01_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())