import pymysql
# import oracle
# import sqlite3
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='gopi@1234',
    database='d8r'
)
cur=conn.cursor()
# cur.execute("show databases")
# for i in cur:
#     print(i)
# conn.commit()
# cur.execute("show tables")
cur.execute("select * from emp join emp as e")
for i in cur:
    print(i)
conn.commit()