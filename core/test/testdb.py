from PySide6.QtSql import QSqlDatabase, QSqlDriver
import mysql.connector

db = QSqlDatabase.addDatabase("QSQLITE")
db.setHostName("localhost")
db.setDatabaseName("myQtdb")
db.setUserName("root")
db.setPassword("Laky@689393")
ok = db.open()
if ok:
    print("Ok")
print(ok, db.lastError())

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Laky@689393",
 auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)