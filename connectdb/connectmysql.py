import pymysql

# create func connect db


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# ทดสอบเรียก connection
# print(connectdb())
