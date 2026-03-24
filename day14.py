import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='gopi@1234',
    database='cur'
)
# print(conn)
cur=conn.cursor()  # to write the commands
print("1.insert student\n2.update")
a=int(input("enter your option"))
if a==1:
    sno=int(input("enter a number"))
    name=input("enter your name")
    ph=int(input("enter mobile number "))
    email=input("enter your email")
    q="insert into eswar(sno,phone) values(%s,%s)"
    cur.execute(q,(sno,ph))
# cur.execute("create database cur")
# cur.execute("create table eswar(sno int,name varchar(100),phone bigint)")
elif a==2:
    sno=int(input("enter a number"))
    name=input("enter your name")
    cur.execute("update eswar set name=%s where sno=%s",(name,sno))
else:
    s=int(input("enter sno number"))
    cur.execute("delete from eswar where sno=%s",(s))
# for i in cur:
#     print(i)
conn.commit()
