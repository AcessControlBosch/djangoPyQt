# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Caderno_Verde_Atencao.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Atencao(object):
    def setupUi(self, Atencao):
        Atencao.setObjectName("Atencao")
        Atencao.resize(1290, 841)
        Atencao.setMinimumSize(QtCore.QSize(1290, 841))
        Atencao.setMaximumSize(QtCore.QSize(1290, 841))
        Atencao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Atencao)
        self.centralwidget.setObjectName("centralwidget")
        self.Label_Borda = QtWidgets.QLabel(self.centralwidget)
        self.Label_Borda.setGeometry(QtCore.QRect(0, 783, 1290, 18))
        self.Label_Borda.setText("")
        self.Label_Borda.setPixmap(QtGui.QPixmap("Imagens/Borda.png"))
        self.Label_Borda.setScaledContents(True)
        self.Label_Borda.setObjectName("Label_Borda")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1270, 760))
        self.frame.setStyleSheet("background-color: rgb(155, 228, 179);\n"
"border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:6px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Label_Seguranca = QtWidgets.QLabel(self.frame)
        self.Label_Seguranca.setGeometry(QtCore.QRect(410, 10, 451, 121))
        self.Label_Seguranca.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 65pt \"Bosch Sans Bold\";")
        self.Label_Seguranca.setObjectName("Label_Seguranca")
        self.botao_continuar = QtWidgets.QPushButton(self.frame)
        self.botao_continuar.setGeometry(QtCore.QRect(850, 570, 321, 141))
        self.botao_continuar.setStyleSheet("background-color: rgb(255, 207, 0);\n"
"border-style: outset;\n"
"border-radius: 35px;\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:4px;\n"
"\n"
"font: 75 35pt \"Bosch Sans Bold\";")
        self.botao_continuar.setObjectName("botao_continuar")
        self.Label_Seguranca_2 = QtWidgets.QLabel(self.frame)
        self.Label_Seguranca_2.setGeometry(QtCore.QRect(40, 140, 1181, 101))
        self.Label_Seguranca_2.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 25pt \"Bosch Sans Bold\";")
        self.Label_Seguranca_2.setObjectName("Label_Seguranca_2")
        self.Label_Seguranca_3 = QtWidgets.QLabel(self.frame)
        self.Label_Seguranca_3.setGeometry(QtCore.QRect(40, 300, 1201, 51))
        self.Label_Seguranca_3.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 25pt \"Bosch Sans Bold\";")
        self.Label_Seguranca_3.setText("")
        self.Label_Seguranca_3.setObjectName("Label_Seguranca_3")
        self.Label_Seguranca_4 = QtWidgets.QLabel(self.frame)
        self.Label_Seguranca_4.setGeometry(QtCore.QRect(30, 280, 661, 471))
        self.Label_Seguranca_4.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 23pt \"Bosch Sans Bold\";")
        self.Label_Seguranca_4.setObjectName("Label_Seguranca_4")
        self.Label_Seguranca_5 = QtWidgets.QLabel(self.frame)
        self.Label_Seguranca_5.setGeometry(QtCore.QRect(710, 280, 531, 231))
        self.Label_Seguranca_5.setStyleSheet("border-style: outset;\n"
"\n"
"\n"
"\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:0px;\n"
"\n"
"font: 75 23pt \"Bosch Sans Bold\";")
        self.Label_Seguranca_5.setObjectName("Label_Seguranca_5")
        self.botao_home = QtWidgets.QPushButton(self.frame)
        self.botao_home.setGeometry(QtCore.QRect(1150, 0, 120, 120))
        self.botao_home.setStyleSheet("border-style: outset;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width:5px;")
        self.botao_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagens/Home.Liberacao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botao_home.setIcon(icon)
        self.botao_home.setIconSize(QtCore.QSize(105, 105))
        self.botao_home.setObjectName("botao_home")
        Atencao.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Atencao)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1290, 21))
        self.menubar.setObjectName("menubar")
        Atencao.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Atencao)
        self.statusbar.setObjectName("statusbar")
        Atencao.setStatusBar(self.statusbar)

        self.retranslateUi(Atencao)
        QtCore.QMetaObject.connectSlotsByName(Atencao)

    def retranslateUi(self, Atencao):
        _translate = QtCore.QCoreApplication.translate
        Atencao.setWindowTitle(_translate("Atencao", "MainWindow"))
        self.Label_Seguranca.setText(_translate("Atencao", "ATENÇÃO"))
        self.botao_continuar.setText(_translate("Atencao", "CONTINUAR"))
        self.Label_Seguranca_2.setText(_translate("Atencao", "Requisitos de qualidade, segurança e meio ambiente são obrigatórios,\n"
"devendo ser revisados nas seguintes situações:"))
        self.Label_Seguranca_4.setText(_translate("Atencao", "•  Liberação de máquina / equipamento;\n"
"\n"
"\n"
"•  Após ajuste de máquina / equipamento;\n"
"\n"
"\n"
"•  Trocas de número de tipo;\n"
"\n"
"\n"
"•  Após manutenções (mecânica/elétrica/\n"
" eletrônica);\n"
""))
        self.Label_Seguranca_5.setText(_translate("Atencao", "•  Após correções de Set-up no\n"
"decorrer do processo;\n"
"\n"
"\n"
"•  No início de turnos de trabalho.\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Atencao = QtWidgets.QMainWindow()
    ui = Ui_Atencao()
    ui.setupUi(Atencao)
    Atencao.show()
    sys.exit(app.exec_())
