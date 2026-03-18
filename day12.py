# try:
#     a=int(input("enter value :- "))
#     b=int(input("enter second values :- "))
#     print(a/b)
# except ValueError:
#     print("enter int values")
# except ZeroDivisionError:
#     print("cannot divided with zero")


# try:
#     # a=int(input("enter value :- "))
#     # b=int(input("enter second values :- "))
#     # print(a/b)
#     # l=[1,2,3,4]
#     # print(l[10])
#     dict={'name':'akhil'}
#     print(dict['name'])
# except Exception as e:
#     print(e)

# else:
#     print("congratulations")
# finally:
#     print('please give values carefully')

# print("block of code")

# mysql.connector , pymysql

import pymysql 
conn=pymysql.connect(
    host='localhost',
    user='root',
    port=3306,
    password='gopi@1234',
    database='d8r'
)
cur=conn.cursor()
# cur.execute("select * from emp")
# for i in cur.fetchall():
#     print(i)
# conn.commit()
name=input("enter a your name:")
age=int(input("enter your age:"))
branch=input("enter your branch ")
college=input("enter your college")
q="insert into pr_py(name,age,branch,college) values(%s,%s,%s,%s)"
cur.execute(q,(name,age,branch,college))
conn.commit()