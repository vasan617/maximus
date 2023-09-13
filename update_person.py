import pymysql
from connectdb import connectmysql as con

# function for update table


def updateperson():
    connection = con.connectdb()
    cursor = connection.cursor()

  # sql แก้ไขตาราง
    sql = """ 
        UPDATE person SET fullname = 'บรรจง',age = '50'
        WHERE id = '3'
        
   """
    try:
        cursor.execute(sql)
        connection.commit()
        print("แก้ไขเรียบร้อย")
    except pymysql.error:
        print(pymysql.error)


updateperson()
