import pymysql
import pandas as pd
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='gopi@1234',
    port=3306,
    database='d8r'
)
data=pd.read_sql("select * from dataclean",conn)
print(data.to_string())