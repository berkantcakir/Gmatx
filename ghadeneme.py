# import requests
# import json
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import NoSuchElementException
# import time
# from selenium.webdriver.support.select import Select
# import string
# from random import *
# import random
# from PyQt5 import QtWidgets
# import sys
# from gha import Ui_MainWindow

# class myApp(QtWidgets.QMainWindow):

#     def __init__(self):
#         super(myApp, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.ui.guncelle(self.)

#     def yukle(self):
#         pass
      




# def app():
#     app = QtWidgets.QApplication(sys.argv)
#     win = myApp()
#     win.show()
#     sys.exit(app.exec_())

# app()


import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
import mysql.connector
from mysql.connector import Error

# class Window2(QMainWindow):                           # <===
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Window22222")

# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.title = "First Window"
#         self.top = 100
#         self.left = 100
#         self.width = 680
#         self.height = 500

#         self.pushButton = QPushButton("Start", self)
#         self.pushButton.move(275, 200)
#         self.pushButton.setToolTip("<h3>Start the Session</h3>")

#         self.pushButton.clicked.connect(self.window2)              # <===

#         self.main_window()

#     def main_window(self):
#         self.label = QLabel("Manager", self)
#         self.label.move(285, 175)
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.top, self.left, self.width, self.height)
#         self.show()

#     def window2(self):                                             # <===
#         self.w = Window2()
#         self.w.show()
#         self.hide()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     sys.exit(app.exec())

import mysql.connector
from mysql.connector import Error 
# anahtar = "50d510c8-b67b-4dfb-b64b-a47ca6372d31"
# anahtar = "50d510c8-b67b-4dfb-b64b-a47ca6372d31"
# mySQLConnection = mysql.connector.connect(host='localhost',
#                                     database='gmatx',
#                                     user='root',
#                                     password='')

# cursor = mySQLConnection.cursor(buffered=True)
# sql_select_query = """SELECT * FROM `key` where anahtar = %s"""
# cursor.execute(sql_select_query, (anahtar,))
# global record
# global mysqldizi
# global myidnumber
# global myanahtar
# global myislemsayisi

# record = cursor.fetchall()
# mysqldizi = record
# myidnumber = mysqldizi[0][0]
# myanahtar = mysqldizi[0][1]
# myislemsayisi = mysqldizi[0][2]

# myislemsayisi -= 1
# print(myislemsayisi)
# id = 1 

    def getDetail(myislemsayisi2):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='gmatx',
                                                user='root',
                                                password='')

            cursor = connection.cursor()
            # Update single record now
            sql_update_query = f"""UPDATE `key` SET islemsayisi ={myislemsayisi2} WHERE id ={id}"""
            cursor.execute(sql_update_query) 
            print("Mysql Güncellendi.")

        except:
            print("hata oluştu.")
# getDetail(myislemsayisi)


def getMysql(self):
connection = mysql.connector.connect(host='localhost',
                                    database='gmatx',
                                    user='root',
                                    password='')

cursor = connection.cursor()
# Update single record now
print(myislemsayisi)
print(myanahtar)
myislemsayisi =- 1
sql_update_query = f"""UPDATE `key` SET islemsayisi ={myislemsayisi} WHERE id ={myidnumber}"""
cursor.execute(sql_update_query)
print(sql_update_query)
print("Mysql Güncellendi.")
self.kullanislem_txt2.setText(f'Kalan İşlem Sayınız: {myislemsayisi}',self)

