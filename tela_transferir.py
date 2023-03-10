from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Transferir(object):

    '''
        Classe Tela_Transferir vai representar nossa opção transferir, tendo parâmetro o objeto
                ...
                
        Logo após vai determinar proporções da tela usando parâmetros do Qt como: cor e tamanho da janela

    '''
    def setupUi(self, MainWindow):

        '''
        Configurando os parâmetros da nossa janela princial a nossa tela da opção transferir
                ...
        
        Cor da tela, tamanho da tela, tipo de fonte e icone presente na tela
        '''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 680)
        MainWindow.setMinimumSize(QtCore.QSize(650, 650))
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
        self.content.setStyleSheet("")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.register_area = QtWidgets.QFrame(self.content)
        self.register_area.setEnabled(True)
        self.register_area.setMinimumSize(QtCore.QSize(600, 600))
        self.register_area.setMaximumSize(QtCore.QSize(450, 550))
        self.register_area.setStyleSheet("border-radius: 10px;")
        self.register_area.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_area.setObjectName("register_area")
        self.pushButton_transferir = QtWidgets.QPushButton(self.register_area)
        self.pushButton_transferir.setGeometry(QtCore.QRect(160, 430, 280, 50))
        self.pushButton_transferir.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_transferir.setObjectName("pushButton_transferir")
        self.label = QtWidgets.QLabel(self.register_area)
        self.label.setGeometry(QtCore.QRect(200, 10, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.register_area)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_transf_destino = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_transf_destino.setGeometry(QtCore.QRect(180, 350, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_transf_destino.setFont(font)
        self.lineEdit_transf_destino.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_transf_destino.setMaxLength(32)
        self.lineEdit_transf_destino.setObjectName("lineEdit_transf_destino")
        self.label_3 = QtWidgets.QLabel(self.register_area)
        self.label_3.setGeometry(QtCore.QRect(240, 260, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_numero_destino = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_numero_destino.setGeometry(QtCore.QRect(180, 290, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.lineEdit_numero_destino.setFont(font)
        self.lineEdit_numero_destino.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_numero_destino.setMaxLength(32)
        self.lineEdit_numero_destino.setObjectName("lineEdit_numero_destino")
        #
        self.lineEdit_saldo = QtWidgets.QLineEdit( self.register_area )
        self.lineEdit_saldo.setGeometry( QtCore.QRect( 360, 95, 100, 30 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.lineEdit_saldo.setFont( font )

        self.lineEdit_saldo.setStyleSheet( "QLineEdit {\n"
                                           "    border: 2px solid rgb(45, 45, 45);\n"
                                           "    border-radius: 5px;\n"
                                           # "    padding: 35px;\n"
                                           "    background-color: rgb(30, 30, 30);    \n"
                                           "    color: rgb(100, 100, 100);\n"
                                           "}\n""}" )
        self.lineEdit_saldo.setObjectName( "lineEdit_saldo" )

        self.label_saldo = QtWidgets.QLabel( self.register_area )
        self.label_saldo.setGeometry( QtCore.QRect( 290, 100, 60, 16 ) )
        font = QtGui.QFont()
        font.setPointSize( 15 )
        self.label_saldo.setFont( font )
        self.label_saldo.setObjectName( "label_saldo" )

        #
        self.lineEdit_cliente = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_cliente.setGeometry(QtCore.QRect(60, 130, 113, 20))
        self.lineEdit_cliente.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_cliente.setObjectName("lineEdit_cliente")
        self.label_5 = QtWidgets.QLabel(self.register_area)
        self.label_5.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_cliente = QtWidgets.QLabel(self.register_area)
        self.label_cliente.setGeometry(QtCore.QRect(10, 130, 47, 13))
        self.label_cliente.setObjectName("label_cliente")
        self.lineEdit_numero = QtWidgets.QLineEdit(self.register_area)
        self.lineEdit_numero.setGeometry(QtCore.QRect(60, 160, 113, 20))
        self.lineEdit_numero.setStyleSheet("QLineEdit {\n"
"    border: 2px solid rgb(45, 45, 45);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30, 30, 30);    \n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55, 55, 55);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.horizontalLayout.addWidget(self.register_area)
        self.verticalLayout.addWidget(self.content)
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_bar.setStyleSheet("")
        self.top_bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_sair = QtWidgets.QPushButton(self.top_bar)
        self.pushButton_sair.setStyleSheet("QPushButton {    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {    \n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);    \n"
"    color: rgb(35, 35, 35);\n"
"}")
        self.pushButton_sair.setObjectName("pushButton_sair")
        self.horizontalLayout_2.addWidget(self.pushButton_sair)
        self.verticalLayout.addWidget(self.top_bar)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 35))
        self.bottom.setStyleSheet("background-color: rgb(15, 15, 15)")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.bottom)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        '''
        Reconfigurando a tela
                ...

        Componentes necessários para renderizar o layout do aplicativo
        sendo nossa janela principal da nossa opção de mostar a tela transferir
        logo após é inserido os labels na tela junto com os pushbotons
        cada um mostrando sua função.
        '''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Transferir"))
        self.pushButton_transferir.setText(_translate("MainWindow", "TRANSFERIR"))
        self.label.setText(_translate("MainWindow", "TRANSFERIR"))
        self.label_2.setText(_translate("MainWindow", "CONTA"))
        self.lineEdit_transf_destino.setPlaceholderText(_translate("MainWindow", "VALOR"))
        self.label_3.setText(_translate("MainWindow", "DESTINO"))
        self.lineEdit_numero_destino.setPlaceholderText(_translate("MainWindow", "NUMERO"))
        self.label_5.setText(_translate("MainWindow", "NUMERO"))
        self.label_cliente.setText(_translate("MainWindow", "CLIENTE"))
        self.pushButton_sair.setText(_translate("MainWindow", "VOLTAR"))
        self.label_saldo.setText( _translate( "MainWindow", "SALDO" ) )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Tela_Transferir()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())