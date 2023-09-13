import pymysql
from connectdb import connectmysql as con
from tabulate import tabulate

# function for create table


def readperson():
    connection = con.connectdb()
    cursor = connection.cursor()

  # sql อ่านข้อมูล
    sql = """ 
     SELECT * FROM person
        
   """
    try:
        cursor.execute(sql)
        connection.commit()
        # # ดึงข้อมูล แบบธรรมดา
        # result = cursor.fetchall()
        # for row in result:
        #     print(row)

# ดึงข้อมูลแบบ library tabulate
        # print(tabulate(cursor, tablefmt="pretty"))  # not header (tablefmt plain,pretty,simple,githyb)

        headers = {
            "id": "ID", "fullname": "FULLNAME", "email": "EMAIL", "age": "AGE"
        }
        print(tabulate(cursor, headers=headers, tablefmt="pretty"))

    except pymysql.Error:
        print(pymysql.Error)


readperson()
