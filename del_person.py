import pymysql
from connectdb import connectmysql as con

# function for update table


def delperson():
    connection = con.connectdb()
    cursor = connection.cursor()

  # sql ลบตาราง
    sql = """ 
        delete from person
        WHERE id = '3'
        
   """
    try:
        cursor.execute(sql)
        connection.commit()
        print("ลบเรียบร้อย")
    except pymysql.error:
        print(pymysql.error)


delperson()
