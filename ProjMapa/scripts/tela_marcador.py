# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\blite\Desktop\tela_visu_mapa_addMarc.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_marcador(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(431, 362)
        MainWindow.setMinimumSize(QtCore.QSize(431, 362))
        MainWindow.setMaximumSize(QtCore.QSize(431, 362))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/Images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("color: rgb(200, 200, 200);\n"
"background-color: rgb(10, 10, 10);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMinimumSize(QtCore.QSize(0, 0))
        self.content.setMaximumSize(QtCore.QSize(431, 359))
        self.content.setAutoFillBackground(False)
        self.content.setStyleSheet("background-color: rgb(101, 255, 111)")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_area = QtWidgets.QFrame(self.content)
        self.login_area.setMaximumSize(QtCore.QSize(450, 550))
        self.login_area.setStyleSheet("border-radius: 10px;")
        self.login_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_area.setObjectName("login_area")
        self.lineEdit_titu = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_titu.setGeometry(QtCore.QRect(90, 200, 221, 31))
        self.lineEdit_titu.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_titu.setObjectName("lineEdit_titu")
        self.label_titu = QtWidgets.QLabel(self.login_area)
        self.label_titu.setGeometry(QtCore.QRect(50, 210, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_titu.setFont(font)
        self.label_titu.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_titu.setObjectName("label_titu")
        self.label = QtWidgets.QLabel(self.login_area)
        self.label.setGeometry(QtCore.QRect(90, 40, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"")
        self.label.setObjectName("label")
        self.pushButton_addTitu = QtWidgets.QPushButton(self.login_area)
        self.pushButton_addTitu.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.pushButton_addTitu.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"")
        self.pushButton_addTitu.setObjectName("pushButton_addTitu")
        self.pushButton_voltar = QtWidgets.QPushButton(self.login_area)
        self.pushButton_voltar.setGeometry(QtCore.QRect(330, 270, 75, 23))
        self.pushButton_voltar.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"")
        self.pushButton_voltar.setObjectName("pushButton_voltar")
        self.label_lon = QtWidgets.QLabel(self.login_area)
        self.label_lon.setGeometry(QtCore.QRect(80, 150, 57, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lon.setFont(font)
        self.label_lon.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lon.setObjectName("label_lon")
        self.label_lat = QtWidgets.QLabel(self.login_area)
        self.label_lat.setGeometry(QtCore.QRect(90, 120, 44, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_lat.setFont(font)
        self.label_lat.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_lat.setObjectName("label_lat")
        self.lineEdit_lon = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_lon.setGeometry(QtCore.QRect(140, 150, 113, 20))
        self.lineEdit_lon.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_lon.setObjectName("lineEdit_lon")
        self.lineEdit_lat = QtWidgets.QLineEdit(self.login_area)
        self.lineEdit_lat.setGeometry(QtCore.QRect(140, 120, 113, 20))
        self.lineEdit_lat.setStyleSheet("    background-color: rgb(0, 0, 0);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"\n"
"")
        self.lineEdit_lat.setObjectName("lineEdit_lat")
        self.horizontalLayout.addWidget(self.login_area)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adicionar Marcador"))
        self.label_titu.setText(_translate("MainWindow", "Titulo"))
        self.label.setText(_translate("MainWindow", "Add Marcador"))
        self.pushButton_addTitu.setText(_translate("MainWindow", "Adicionar"))
        self.pushButton_voltar.setText(_translate("MainWindow", "Voltar"))
        self.label_lon.setText(_translate("MainWindow", "Longitude"))
        self.label_lat.setText(_translate("MainWindow", "Latitude"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_marcador()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
