# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayüz.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(578, 523)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 420, 531, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.sonuc = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.sonuc.setContentsMargins(0, 0, 0, 0)
        self.sonuc.setObjectName("sonuc")
        self.label_sonuc_maxdizi = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sonuc_maxdizi.setObjectName("label_sonuc_maxdizi")
        self.sonuc.addWidget(self.label_sonuc_maxdizi, 0, 0, 1, 1)
        self.label_sonuc_mindizi = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_sonuc_mindizi.setObjectName("label_sonuc_mindizi")
        self.sonuc.addWidget(self.label_sonuc_mindizi, 0, 1, 1, 1)
        self.label_evirici_max = QtWidgets.QLabel(self.centralwidget)
        self.label_evirici_max.setGeometry(QtCore.QRect(30, 343, 221, 16))
        self.label_evirici_max.setObjectName("label_evirici_max")
        self.label_evirici_min = QtWidgets.QLabel(self.centralwidget)
        self.label_evirici_min.setGeometry(QtCore.QRect(30, 390, 231, 16))
        self.label_evirici_min.setObjectName("label_evirici_min")
        self.pushButton_max_dizi_hesapla = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_max_dizi_hesapla.setGeometry(QtCore.QRect(390, 370, 131, 41))
        self.pushButton_max_dizi_hesapla.setObjectName("pushButton_max_dizi_hesapla")
        self.lineEdit_evirici_max = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_evirici_max.setGeometry(QtCore.QRect(250, 340, 113, 31))
        self.lineEdit_evirici_max.setObjectName("lineEdit_evirici_max")
        self.lineEdit_evirici_min = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_evirici_min.setGeometry(QtCore.QRect(250, 380, 113, 31))
        self.lineEdit_evirici_min.setObjectName("lineEdit_evirici_min")
        self.pushButton_Selcity = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Selcity.setGeometry(QtCore.QRect(330, 40, 211, 31))
        self.pushButton_Selcity.setObjectName("pushButton_Selcity")
        self.label_maxtemp = QtWidgets.QLabel(self.centralwidget)
        self.label_maxtemp.setGeometry(QtCore.QRect(30, 124, 581, 17))
        self.label_maxtemp.setObjectName("label_maxtemp")
        self.comboBox_Country = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Country.setGeometry(QtCore.QRect(30, 16, 291, 20))
        self.comboBox_Country.setObjectName("comboBox_Country")
        self.comboBox_Country.addItem("")
        self.label_selectcountry = QtWidgets.QLabel(self.centralwidget)
        self.label_selectcountry.setGeometry(QtCore.QRect(30, 76, 581, 18))
        self.label_selectcountry.setObjectName("label_selectcountry")
        self.label_mintemp = QtWidgets.QLabel(self.centralwidget)
        self.label_mintemp.setGeometry(QtCore.QRect(30, 147, 581, 18))
        self.label_mintemp.setObjectName("label_mintemp")
        self.pushButton_Selcountry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Selcountry.setGeometry(QtCore.QRect(330, 10, 211, 31))
        self.pushButton_Selcountry.setObjectName("pushButton_Selcountry")
        self.comboBox_City = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_City.setGeometry(QtCore.QRect(30, 50, 291, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_City.sizePolicy().hasHeightForWidth())
        self.comboBox_City.setSizePolicy(sizePolicy)
        self.comboBox_City.setObjectName("comboBox_City")
        self.comboBox_City.addItem("")
        self.label_selectcity = QtWidgets.QLabel(self.centralwidget)
        self.label_selectcity.setGeometry(QtCore.QRect(30, 100, 581, 18))
        self.label_selectcity.setObjectName("label_selectcity")
        self.comboBox_Panelbrand = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Panelbrand.setGeometry(QtCore.QRect(30, 180, 261, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_Panelbrand.sizePolicy().hasHeightForWidth())
        self.comboBox_Panelbrand.setSizePolicy(sizePolicy)
        self.comboBox_Panelbrand.setObjectName("comboBox_Panelbrand")
        self.comboBox_Panelbrand.addItem("")
        self.label_Voc = QtWidgets.QLabel(self.centralwidget)
        self.label_Voc.setGeometry(QtCore.QRect(30, 301, 581, 16))
        self.label_Voc.setObjectName("label_Voc")
        self.pushButton_selmodel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selmodel.setGeometry(QtCore.QRect(330, 202, 221, 31))
        self.pushButton_selmodel.setObjectName("pushButton_selmodel")
        self.comboBox_Panelmodel = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_Panelmodel.setGeometry(QtCore.QRect(30, 210, 261, 20))
        self.comboBox_Panelmodel.setObjectName("comboBox_Panelmodel")
        self.comboBox_Panelmodel.addItem("")
        self.label_Selectmodel = QtWidgets.QLabel(self.centralwidget)
        self.label_Selectmodel.setGeometry(QtCore.QRect(30, 259, 581, 16))
        self.label_Selectmodel.setObjectName("label_Selectmodel")
        self.label_BVoc = QtWidgets.QLabel(self.centralwidget)
        self.label_BVoc.setGeometry(QtCore.QRect(30, 322, 581, 16))
        self.label_BVoc.setObjectName("label_BVoc")
        self.label_Selectpanel = QtWidgets.QLabel(self.centralwidget)
        self.label_Selectpanel.setGeometry(QtCore.QRect(30, 238, 581, 16))
        self.label_Selectpanel.setObjectName("label_Selectpanel")
        self.label_Power = QtWidgets.QLabel(self.centralwidget)
        self.label_Power.setGeometry(QtCore.QRect(30, 280, 581, 16))
        self.label_Power.setObjectName("label_Power")
        self.pushButton_selbrand = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_selbrand.setGeometry(QtCore.QRect(330, 172, 221, 31))
        self.pushButton_selbrand.setObjectName("pushButton_selbrand")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(350, 270, 75, 23))
        self.pushButton_clear.setObjectName("pushButton_clear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_sonuc_maxdizi.setText(_translate("MainWindow", "Maximum Dizi Sayısı :"))
        self.label_sonuc_mindizi.setText(_translate("MainWindow", "Minumum Dizi Sayısı"))
        self.label_evirici_max.setText(_translate("MainWindow", "Eviricinin maximumum gerilim değerini giriniz :"))
        self.label_evirici_min.setText(_translate("MainWindow", "Eviricinin minumum gerilim değerini giriniz :"))
        self.pushButton_max_dizi_hesapla.setText(_translate("MainWindow", "Dizi Sayılarını Hesaplat"))
        self.pushButton_Selcity.setText(_translate("MainWindow", "Select City"))
        self.label_maxtemp.setText(_translate("MainWindow", "Max Sıcaklık :"))
        self.comboBox_Country.setItemText(0, _translate("MainWindow", "Country Select"))
        self.label_selectcountry.setText(_translate("MainWindow", "Seçilen Ülke :"))
        self.label_mintemp.setText(_translate("MainWindow", "Min Sıcaklık :"))
        self.pushButton_Selcountry.setText(_translate("MainWindow", "Select Country"))
        self.comboBox_City.setItemText(0, _translate("MainWindow", "City Select"))
        self.label_selectcity.setText(_translate("MainWindow", "Seçilen Şehir :"))
        self.comboBox_Panelbrand.setItemText(0, _translate("MainWindow", "Panel Brand"))
        self.label_Voc.setText(_translate("MainWindow", "Voc :"))
        self.pushButton_selmodel.setText(_translate("MainWindow", "Select Model"))
        self.comboBox_Panelmodel.setItemText(0, _translate("MainWindow", "Panel Model"))
        self.label_Selectmodel.setText(_translate("MainWindow", "Seçilen Model :"))
        self.label_BVoc.setText(_translate("MainWindow", "BVoc :"))
        self.label_Selectpanel.setText(_translate("MainWindow", "Seçilen Panel :"))
        self.label_Power.setText(_translate("MainWindow", "Power :"))
        self.pushButton_selbrand.setText(_translate("MainWindow", "Select Brand"))
        self.pushButton_clear.setText(_translate("MainWindow", "CLEAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
