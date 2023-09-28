import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='Kesiana1999!@'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS CRM_DB")
print("All done!")