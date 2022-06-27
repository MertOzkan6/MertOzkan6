from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from arayüz import Ui_MainWindow
import math 

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.selected_country = ''
        self.selected_city = ''
        self.selected_panel_brands = ''
        self.selected_panel_models = ''
        self.max_temp = '' 
        self.min_temp = '' 
        self.voc = ''
        self.bvoc = ''
        self.power = ''
        self.deltat1 = ''
        self.deltat2 = ''
        self.y2 = ''
        self.y1 = ''

        self.panels = list(panels_dictionary.keys())
        self.countries = list(countries_dictionary.keys())

        self.combo_country = self.ui.comboBox_Country
        self.combo_country.addItems(self.countries)
        self.ui.pushButton_Selcountry.clicked.connect(self.SelCount)
        
        self.combo_city = self.ui.comboBox_City
        self.ui.pushButton_Selcity.clicked.connect(self.SelCity)
      
        self.combo_panel_brand = self.ui.comboBox_Panelbrand
        self.combo_panel_brand.addItems(self.panels)
        self.ui.pushButton_selbrand.clicked.connect(self.SelBrand)

        self.combo_panel_model = self.ui.comboBox_Panelmodel
        self.ui.pushButton_selmodel.clicked.connect(self.SelModel)
        
        self.ui.pushButton_max_dizi_hesapla.clicked.connect(self.hesapla)
        self.ui.pushButton_clear.clicked.connect(self.combo_city.clear)       
        self.ui.pushButton_clear.clicked.connect(self.combo_panel_model.clear)
        self.ui.pushButton_clear.clicked.connect(self.ui.lineEdit_evirici_max.clear) 
        self.ui.pushButton_clear.clicked.connect(self.ui.lineEdit_evirici_min.clear) 
#######################################################################################
#######################################################################################
#ComboBox da ülke seçimi için tanımlama
    def SelCount(self):
        # self.ui.comboBox_Country.addItems(countries)
        self.selected_country = str(self.combo_country.currentText())
        self.ui.label_selectcountry.setText('Seçilen  Ülke :' + self.selected_country)
        cities = list(countries_dictionary[self.selected_country].keys())
        self.combo_city.addItems(cities)
#######################################################################################
#######################################################################################  
#ComboBox da seçilen ülkü için şehir seçimi tanımlama  
    def SelCity(self):
        self.selected_city = str(self.ui.comboBox_City.currentText())
        self.ui.label_selectcity.setText('Seçilen Şehir :' + self.selected_city)
        self.max_temp = countries_dictionary[self.selected_country][self.selected_city]['max']
        self.min_temp = countries_dictionary[self.selected_country][self.selected_city]['min']
        self.ui.label_maxtemp.setText('Max temp :' + self.max_temp)
        self.ui.label_mintemp.setText('Min temp :' + self.min_temp)
#######################################################################################
#######################################################################################
#ComboBox da panel markası seçimi için tanımlama
    def SelBrand(self):
        self.selected_panel_brands = str(self.combo_panel_brand.currentText())
        self.ui.label_Selectpanel.setText('Seçilen Panel :' + self.selected_panel_brands)
        models = list(panels_dictionary[self.selected_panel_brands].keys())
        self.combo_panel_model.addItems(models)
#######################################################################################
#######################################################################################
#ComboBox da seçilen panel markası için panel modeli seçimi tanımlama
    def SelModel(self):
        self.selected_panel_models = str(self.ui.comboBox_Panelmodel.currentText())
        self.ui.label_Selectmodel.setText('Seçilen model :' + self.selected_panel_models)
        self.voc = panels_dictionary[self.selected_panel_brands][self.selected_panel_models]['voc']
        self.bvoc = panels_dictionary[self.selected_panel_brands][self.selected_panel_models]['bvoc']
        self.power = panels_dictionary[self.selected_panel_brands][self.selected_panel_models]['power']
        self.ui.label_Power.setText('Power :' + self.power)
        self.ui.label_Voc.setText('Voc :' + self.voc)
        self.ui.label_BVoc.setText('BVoc :' + self.bvoc)
#######################################################################################
####################################################################################### 
# Max ve Min dizi sayısı hesaplamak için tanımlama       
    def hesapla(self):
        
        self.deltat1 = int(self.max_temp) - 25 #deltat1 max sıcaklıkdan 25 derece çıkarımı
        self.deltat2 = int(self.min_temp) - 25 #deltat2 min sıcaklıkdan 25 derece çıkarımı
        
        self.y2  = ((int(self.deltat2) * float(self.bvoc) * float(float(self.voc)/100)) + float(self.voc))
        
        self.y1  = ((int(self.deltat1) * float(self.bvoc) * float(float(self.voc)/100)) + float(self.voc))
        
        m = (int(self.ui.lineEdit_evirici_max.text()) / (float(self.y2))) #max dizi sayısını bulmak için yapılan işlem
        u = (int(self.ui.lineEdit_evirici_min.text()) / (float(self.y1))) #min dizi sayısını bulmak için yapılan işlem

        self.ui.label_sonuc_maxdizi.setText('Max Dizi Sayısı : ' + str(math.floor(m))) 
        self.ui.label_sonuc_mindizi.setText('Min Dizi Sayısı : ' + str(math.ceil(u)))
    
#######################################################################################
#######################################################################################
#oluşturduğumuz databaseden ülke,şehir ,max sıcaklık ve min sıcaklık değerini çekmek
countries_dictionary = {}
file = open('country.txt.ini', 'r', encoding='utf8')
for line in file.readlines():
    items = line.split() #oluşturduğumuz data base i split ederek indexlere parçalıyoruz
    country = items[0]  # sıfırıncı index ülke bilgileri
    city = items[1]     #birinci index şehir bilgileri
    max_temp = items[2] #ikinci index max sıcaklık bilgileri
    min_temp = items[3] #üçüncü index min sıcaklık bilgileri
    if country in countries_dictionary:
        countries_dictionary[country][city] = {'max': max_temp, 'min': min_temp}
    else:
        countries_dictionary[country] = {city: {'max': max_temp, 'min': min_temp}} 
#######################################################################################
#######################################################################################
#oluşturduğumuz databaseden panel marka ,model , güç , Voc ve BVoc  değerini çekmek
panels_dictionary = {}
panels_file = open('panels.txt', 'r', encoding='utf8')
for line in panels_file.readlines():
    items = line.rstrip('\n').rstrip('\r\n').split(',') #oluşturduğumuz data base i strip ederek indexlere parçalıyoruz
    if len(items) != 5:
        continue
    brand = items[0] # sıfırıncı index panel marka bilgileri
    model = items[1] # birinci index seçilen panelin marka ve model bilgileri 
    power = items[2] # ikinci index seçilen panel marka ve modelin güç bilgileri
    voc = items[3]   # üçüncü index seçilen panel marka ve modelin voc bilgileri
    bvoc = items[4]  # dördüncü index seçilen panel marka ve modelin bvoc bilgileri
    if brand in panels_dictionary:
        panels_dictionary[brand][model] = {'power': power, 'voc': voc, 'bvoc': bvoc}
    else:
        panels_dictionary[brand] = {model: {'power': power, 'voc': voc, 'bvoc': bvoc}}


app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())