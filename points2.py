# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'points.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pointWindow(object):
        def __init__(self) -> None:
            pass
        def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(501, 235)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(0, 0, 500, 230))
            self.label_2.setStyleSheet("\n"
    "background-color: rgb(57, 125, 84);")
            self.label_2.setFrameShape(QtWidgets.QFrame.Box)
            self.label_2.setLineWidth(5)
            self.label_2.setText("")
            self.label_2.setObjectName("label_2")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(30, 30, 241, 31))
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            self.label_4.setFont(font)
            self.label_4.setObjectName("label_4")
            self.you_points = QtWidgets.QPlainTextEdit(self.centralwidget)
            self.you_points.setGeometry(QtCore.QRect(40, 100, 431, 51))
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(18)
            font.setBold(True)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(75)
            self.you_points.setFont(font)
            self.you_points.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.you_points.setStyleSheet("background-color: rgb(153, 184, 152);")
            self.you_points.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.you_points.setLineWidth(1)
            self.you_points.setTabStopWidth(0)
            self.you_points.setObjectName("you_points")
            MainWindow.setCentralWidget(self.centralwidget)

            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
            
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.label_4.setText(_translate("MainWindow", "You Points "))
            self.you_points.setPlainText(_translate("MainWindow", str(self.points)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_pointWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
