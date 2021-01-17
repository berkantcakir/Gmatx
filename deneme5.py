import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.select import Select
import string
from random import *
import random
from PyQt5 import QtWidgets
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gha import Ui_MainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel, QWidget, QAction, QTabWidget, QVBoxLayout)
from PyQt5 import QtCore, QtWidgets
from lisans import Ui_Lisans
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
class EmbTerminal(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(EmbTerminal, self).__init__(parent)
        self.process = QtCore.QProcess(self)

        self.terminal = QtWidgets.QWidget(self)

        layout = QtWidgets.QVBoxLayout(self)

        layout.addWidget(self.terminal)

        # Works also with urxvt:

        self.process.start('urxvt',['-embed', str(int(self.winId()))])

        self.setFixedSize(640, 480)

class Licance(QtWidgets.QMainWindow):
   
    def __init__(self):
        super(Licance, self).__init__()
        self.li = Ui_Lisans()
        self.li.setupUi(self)
        self.li.lisansonay.clicked.connect(self.getDetail)


    def getDetail(self):
        try:
            global mysqldizi
            global myidnumber
            global myanahtar
            global myislemsayisi

            mySQLConnection = mysql.connector.connect(host='localhost',
                                                database='gmatx',
                                                user='root',
                                                password='')

            cursor = mySQLConnection.cursor(buffered=True)
            sql_select_query = """SELECT * FROM `key` where anahtar = %s"""
            cursor.execute(sql_select_query, (self.li.anahtarkontrol.text(),))
            record = cursor.fetchall()

            mysqldizi = record
            myidnumber = mysqldizi[0][0]
            myanahtar = mysqldizi[0][1]
            myislemsayisi = int(mysqldizi[0][2])
            global newislem2
            newislem2 = myislemsayisi

            print(f"{myislemsayisi} İşlem Başarılı")
            self.w = myApp()
            self.w.show()
            self.hide()          
        except :
            msg = QMessageBox()
            msg.setWindowTitle("Gmatx | Lisans")
            msg.setText("Yanlış Lisans Girdiniz ! \nLütfen Doğru Lisans Girin!                     ")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)

            x = msg.exec_()

        
class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.baslat.clicked.connect(self.hesap)


        self.kullanislem_txt2 = QLabel(f'Kalan İşlem Sayınız: {myislemsayisi}',self)
        self.kullanislem_txt2.move(390,20)
        self.kullanislem_txt2.resize(500,50)

        self.ui.tabWidget.addTab(EmbTerminal(),"Deneme")
        self.ui.tabWidget.addTab(QtWidgets.QMdiArea(), "QMdiArea")


        def install_update():
            win32api.ShellExecute(0, 'open', f'tmp\\{_AppName_}.msi', None, None, 10)
            parent.destroy()

        def start_update_manager():
            with requests.get('https://github.com/vsantiago113/Tkinter-MyTestApp/raw/master/'
                              'updates/MyTestApp.msi?raw=true', stream=True) as r:
                self.progressbar['maximum'] = int(r.headers.get('Content-Length'))
                r.raise_for_status()
                with open(f'./tmp/{_AppName_}.msi', 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            self.progressbar['value'] += 4096
            self.ui.button1.config(text='Install', state=self.ui.NORMAL)

        self.progressbar = self.ui.Progressbar(self,
                                           orient='horizontal',
                                           length=200,
                                           mode='determinate',
                                           value=0,
                                           maximum=0)
        self.progressbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.button1 = self.ui.Button(self, text='Wait!', state=tk.DISABLED, command=install_update)
        self.button1.place(x=-83, relx=1.0, y=-33, rely=1.0)

        self.t1 = threading.Thread(target=start_update_manager)
        self.t1.start()



    def hesap(self):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmatx',
                                                user='root',
                                                password='')
            cursor = connection.cursor()
            # Update single record now
            global newislem
            print(myanahtar) #deneme
            global newislem2
            newislem2 = newislem2 - 1
            print(newislem2)
            sql_update_query = f"""UPDATE `key` SET islemsayisi ={newislem2} WHERE id ={myidnumber}"""
            cursor.execute(sql_update_query)
            print(sql_update_query)
            print("Mysql Güncellendi.")

            self.kullanislem_txt2.setText(f'Kalan İşlem Sayınız: {newislem2}')

                       
            # sql_select_query = f"""SELECT * FROM `key` where anahtar = {myanahtar}"""
            # cursor.execute(sql_select_query)
            # record = cursor.fetchall()

            # mysqldizi = record
            # myidnumber = mysqldizi[0][0]
            # myanahtar = mysqldizi[0][1]
            # myislemsayisi = mysqldizi[0][2]
            
            sayi = int(self.ui.sayial.text())
            print(sayi)
            # proxyip = []
            proxydizi = self.ui.proxylist.toPlainText().split("\n")
            sayi = 0
            proxysayi = 0
            islemtekrari = 0 
            # 50d510c8-b67b-4dfb-b64b-a47ca6372d31
            while int(self.ui.urethesapsayisi.text()) > islemtekrari:
                PROXY = f"{proxydizi[proxysayi]}" # IP:PORT or HOST:PORTS
                print(proxydizi)
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--proxy-server=%s' % PROXY)

                chrome = webdriver.Chrome(options=chrome_options)
                chrome.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

                time.sleep(2)
                ad = chrome.find_element_by_xpath("//*[@id='firstName']")
                soyad = chrome.find_element_by_xpath("//*[@id='lastName']")

                # BEAUTİLFULSHOUP #
                url = "https://huseyindemirtas.net/kullanici-adi-listesi-ad-soyad-listesi/"

                html = requests.get(url).content
                soup = BeautifulSoup(html,'html.parser')
                dizi = []

                liste = soup.find_all('tr')
                for i in liste:
                    karisik = i.text.strip()

                    name = karisik.split("\n")
                            
                    dizi.append(name)

                isim = dizi[sayi][0]
                soyisim = dizi[sayi][1]


                # GÖNDERME İŞLEMİ #


                ad.send_keys(isim)
                time.sleep(2)
                soyad.send_keys(soyisim)
                time.sleep(7)

                sifre1 = chrome.find_element_by_xpath("//*[@id='passwd']/div[1]/div/div[1]/input")
                sifre2 = chrome.find_element_by_xpath("//*[@id='confirm-passwd']/div[1]/div/div[1]/input")

                characters = string.ascii_letters + string.digits
                password =  "".join(choice(characters) for x in range(randint(8, 14)))

                sifre1.send_keys(password)
                sifre2.send_keys(password)

                time.sleep(2)

                mailAdresi = chrome.find_element_by_xpath("//*[@id='username']")
                # mailAdresi.send_keys(Keys.CONTROL, 'a')
                # kopya = mailAdresi.send_keys(Keys.CONTROL, 'c') #copy

                # chrome.find_element_by_xpath("//*[@id='username']").clear()
                # mailAdresi.clear()

                # mailAdresi.send_keys(Keys.CONTROL, 'v')


                # accountList.append(mailAdresi)
                # accountList.append(sifre1)
                # passw = chrome.find_elements_by_id("username")
                value = mailAdresi.get_attribute('data-initial-value')

                with open("AccountList.txt","a",encoding="UTF-8") as file:
                    file.write(f"{value}@gmail.com:{password}\n")


                ileri = chrome.find_element_by_xpath("//*[@id='accountDetailsNext']/span/span")

                ileri.click()   


                def numaraAl():
                    git2 = f"https://sms-activate.ru/stubs/handler_api.php?api_key={self.ui.api_key.text()}&action=getNumber&service=go&country=0"
                    print("Sms siparişi verildi!")
                    html = requests.get(git2).content
                    soup = BeautifulSoup(html,'html.parser').text
                    dizi2 = []
                    print(soup)

                    ekle = soup.split(":")

                    dizi2.append(ekle)
                    print(dizi2)
                    global idnumber
                    global number

                    idnumber = dizi2[0][1]
                    number = dizi2[0][2]
                    time.sleep(3)
                    print("Sipariş Başarılı! idnumber: ",idnumber,"number: ",number)

                    phoneNumber = chrome.find_element_by_xpath("//*[@id='phoneNumberId']")
                    phoneNumber.clear()
                    phoneNumber.send_keys(f"+{number}")

                    time.sleep(2)
                    ileri2 = chrome.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                    ileri2.click()
                    time.sleep(5)
                numaraAl()

                def hata():
                    url = (f"https://sms-activate.ru/stubs/handler_api.php?api_key={self.ui.api_key.text()}&action=setStatus&status=8&id={idnumber}")
                    print(url)
                    html = requests.get(url).content
                    soup = BeautifulSoup(html,'html.parser')
                    print("Numara İptal Edildi. Yeni Numara Alınıyor...")
                    time.sleep(5)
                    numaraAl()

                while True:
                    try:
                        elem = chrome.find_element_by_xpath("//*[@id='code']")
                        if elem.is_displayed():
                            print("Numara Kullanılıyor")

                            time.sleep(2)

                            dogrula = chrome.find_element_by_xpath('//*[@id="code"]')

                            time.sleep(2)

                            print("Sms almaya Gidiliyor!")
                            # number = git[0]["phone"]["number"]
                            # idnumber = git[0]["phone"]["id"]

                            print("30 saniye bekleniyor...")
                            time.sleep(30)

                            git4 = (f"https://sms-activate.ru/stubs/handler_api.php?api_key={self.ui.api_key.text()}&action=getStatus&id={idnumber}")
                            
                            html = requests.get(git4).content
                            soup = BeautifulSoup(html,'html.parser').text
                            dizi3 = []
                            print(soup)

                            ekle2 = soup.split(":")

                            dizi3.append(ekle2)
                            print(dizi3)

                            message = dizi3[0][1]

                            time.sleep(2)

                            print("SMS KODU ALINDI ! SMS KODU: ",message)

                            dogrula2 = chrome.find_element_by_xpath('//*[@id="code"]')

                            dogrula2.send_keys(message)

                            ileri3 = chrome.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")

                            ileri3.click()
                            time.sleep(3)

                            day = chrome.find_element_by_xpath('//*[@id="day"]')

                            day.send_keys(random.randint(1, 28))
                            time.sleep(2)
                            year = chrome.find_element_by_xpath('//*[@id="year"]')

                            year.send_keys("2000")
                            
                            select_fr = Select(chrome.find_element_by_xpath('//*[@id="month"]')) 
                            time.sleep(2)
                            select_fr.select_by_index(random.randint(0, 11))

                            # //*[@id="gender"]
                            # //*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]
                            # //*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]
                            # //*[@id="termsofserviceNext"]/span/span
                            time.sleep(2)
                            cinsiyet = Select(chrome.find_element_by_xpath('//*[@id="gender"]'))
                            
                            cinsiyet.select_by_index(random.randint(1, 3))
                            time.sleep(2)
                            ileri4 = chrome.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
                            ileri4.click()
                            time.sleep(2)

                            atla = chrome.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div/button/div[2]')
                            atla.click()
                            time.sleep(2)
                            kabul = chrome.find_element_by_xpath('//*[@id="termsofserviceNext"]/span/span')

                            kabul.click()

                            time.sleep(9)

                            print("Herşey Başarılı!")
                            print("Gmail Oluşturuldu ve Chrome Kapanıp Açılacak!")
                            sayi += 1
                            newmyislem = myislemsayisi - 1
                            time.sleep(1)
                            proxysayi += 1
                            # message = git2[0]["values"]["0"]["text"]

                            # time.sleep(1)

                            # dogrula.send_keys(message)

                            # time.sleep(2)
                            # ileri3 = chrome.find_element_by_xpath("//*[@id='view_container'']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
                            # ileri3.click()

                            # print(f"id: {idnumber}")
                            # print(f"no: {number}")
                            # print(f"message: {message}")

                            # chrome.get("http://code8.ml/")

                            # driver = webdriver.Chrome()
                            # url = "http://code8.ml"
                            # driver.get(url)
                        break

                    except NoSuchElementException:
                        if elem.is_displayed():
                            pass
                        else:
                            print("Numara Kullanılmıyor")
                            time.sleep(2)
                            print("Numara İptal Ediliyor..")
                            time.sleep(4)
                            hata()
                        

                print("İşlem bitti")
        except:
            pass

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())


def licance():
    lica = QtWidgets.QApplication(sys.argv)
    lican = Licance()
    lican.show()
    sys.exit(lica.exec_())

licance()
