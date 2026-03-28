import pymysql
conn=pymysql.connect(
    host='localhost',
    user='root',
    password='gopi@1234',
    port=3306,
    database='d8r'
)
print(conn)
cur=conn.cursor()
# cur.execute("select * from dataclean")
# for i in cur:
#     print(i)
# print(cur)
while True:
    print("1.insert\n2.update\n3.delete\n4.read")
    n=int(input("enter a number : "))
    if n==1:
        s=int(input("enetr sno number : "))
        n=input("enter your name : ")
        a=int(input("enter your age : "))
        q="insert into rakesh values(%s,%s,%s)"
        cur.execute(q,(s,n,a))
        conn.commit()
        print("successfully instered")
    elif n==2:
        s=int(input("enetr sno number : "))
        new_age=int(input("enter your new age : "))
        q='update rakesh set age=%s where sno=%s'
        cur.execute(q,(new_age,s))
        conn.commit()
        print("successfully updated")
    elif n==3:
        s=int(input("enetr sno number : "))
        q='delete from rakesh where sno=%s'
        cur.execute(q,(s))
        conn.commit()
        print("successfully delete ")
    elif n==4:
        cur.execute('select * from rakesh')
        for i in cur.fetchone():
            print(i)
        conn.commit()
    else:
        print("enter valid option")