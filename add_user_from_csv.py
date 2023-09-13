import pymysql
from connectdb import connectmysql as con
import csv

# function for create user for csv


def insertusercsv():
    connection = con.connectdb()
    cursor = connection.cursor()

    with open('filedata/user.csv', 'r', encoding="UTF8") as csv_file:
        # สร้าง reader
        csv_reader = csv.reader(csv_file, delimiter=',')
        # ข้าม Header
        header = next(csv_reader)

        # วนลูป อ่านข้อมูล
        for row in csv_reader:
            sql = "INSERT INTO users (Name, Email, Mobile) VALUES (%s, %s, %s)"
            cursor.execute(sql, tuple(row))
            print("เพิ่มข้อมูลเรียบร้อย")

            connection.commit()
            connection.close()


insertusercsv()
