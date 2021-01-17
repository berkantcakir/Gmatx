import mysql.connector
from mysql.connector import Error

anahtarkontrol = "50d510c8-b67b-4dfb-b64b-a47ca6372d31"

global mysqldizi
global myidnumber
global myanahtar
global myislemsayisi

mySQLConnection = mysql.connector.connect(host='sql7.freemysqlhosting.net',
                                    database='sql7372698',
                                    user='sql7372698',
                                    password='wxDk4ZxbB4')


cursor = mySQLConnection.cursor(buffered=True)

sql_select_query = """SELECT * FROM `key` where anahtar = %s"""
cursor.execute(sql_select_query, (anahtarkontrol))
record = cursor
mysqldizi = record
print("sa")
myidnumber = mysqldizi[0][0]
myanahtar = mysqldizi[0][1]
myislemsayisi = int(mysqldizi[0][2])
global newislem2
newislem2 = myislemsayisi

print(f"{myislemsayisi} İşlem Başarılı")
