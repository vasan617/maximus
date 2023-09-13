import pymysql
from connectdb import connectmysql as con

# function for create table


def addperson():
    connection = con.connectdb()
    cursor = connection.cursor()

  # sql สร้างตาราง
    sql = """ 
     INSERT INTO person (fullname, email, age)
     VALUES ('มานพ', 'manop@email.com', '66')
        
   """
    try:
        cursor.execute(sql)
        connection.commit()
        print("เพิ่มข้อมูลเรียบร้อย")
    except pymysql.error:
        print(pymysql.error)


addperson()
