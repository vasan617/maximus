import pymysql
from curdmysql.connectdb import connectmysql as con

# function for create table


def createtable():
    connection = con.connectdb()
    cursor = connection.cursor()

  # sql สร้างตาราง
    sql = """ 
     CREATE TABLE person(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        fullname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age int NOT NULL
        )
   """
    try:
        cursor.execute(sql)
        connection.commit()
        print("สร้างตารางแล้ว")
    except pymysql.error:
        print(pymysql.error)


createtable()
