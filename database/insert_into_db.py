import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

connection = pymysql.connect(
    host = host,
    user = user,
    password = password,
    database = database,
)

cursor = connection.cursor()

sql = "INSERT INTO orders (name, address, phone, courier, status) VALUES (%s, %s)"
val = [
("Linda", "12a peterborough road LONDON HA1 2BQ", "0793837563", "3", "preparing"),
("Johnny", "38 Hindes road LONDON NW10 6HJ", "0734875949", "2", "preparing"),
("Sammy", "166 exeter road, LONDON, HA2 0HJ", "07568564726", "1", "preparing"),
("Danni", "143 stonefield way NW10 9PK", "07568324726", "4", "preparing")
]

cursor.executemany(sql, val)
connection.commit()
print(cursor.rowcount, "record was inserted")


#cursor.close()
#connection.close()

