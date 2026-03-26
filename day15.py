import pymysql
conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='gopi@1234',
    database='datascience'
)
cur=conn.cursor()

def add_student():
    name=input("enter student name :")
    email=input("enter student email :")
    password=input("enter student password :")
    course=input("enter student course :")
    branch=input("enter student branch :")
    passout=int(input("enter student passout year :"))
    phone=int(input("enter student phone :"))
    q="insert into student(name,email,password,course,branch,passout_year,phone) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(q,(name,email,password,course,branch,passout,phone))
    conn.commit()
    print("successfully add a student")

def update_student():
    col_name=input("enter your column : ")
    sno=int(input("enter sno of student : "))
    new_data=input("enter your data : ")
    a='%s'
    q=f"update student set {col_name}={a} where sno={a}"
    cur.execute(q,(new_data,sno))
    conn.commit()
    print("successfully updated")

def delete_student():
    sno=int(input("enter sno of student to delete : "))
    q='delete from student where sno=%s'
    cur.execute(q,(sno))
    conn.commit()
    print("successfully deleted")

def add_trainer():
    name=input("enter trainer name :")
    email=input("enter trainer email : ")
    password=input("enter trainer password : ")
    phone=int(input("enter trainer phone number : "))
    q='insert into trainer(name,email,password,phone) values(%s,%s,%s,%s)'
    cur.execute(q,(name,email,password,phone))
    conn.commit()
    print("trainer added successfully")

def view_trainer(email):
    q='select * from trainer where email=%s'
    cur.execute(q,(email))
    for i in cur:
        # print(i)
        print("sno :",  i[0])
        print("name :",  i[1])
        print("email :",  i[2])
        print("password :",  i[3])
        print("phone :",  i[4])
    conn.commit()


while True:
    print("============================================")
    print("               10000coders                  ")
    print("============================================")
    print("1.admin\n2.trainer\n3.pm\n4.student")
    try:
        op=int(input("choose who are you : "))
        if op==1:
            print("============================================")
            print("               WELCOME TO ADMIN PORTAL      ")
            print("============================================")
            email=input("enter your emailid   :")
            password=input("enter your password : ")
            cur.execute("select * from admin")
            for i in cur:
                # print(i[2],i[3])
                if email==i[2] and password==i[3]:
                    print("1.add admin\n2.add trainer\n3.delete trainer\n4.update trainer\n5.add pm\n6.update pm\n7.delete pm\n8.add student\n9.update student\n10.delete student")
                    op=int(input("choose your option : "))
                    if op==1:
                        pass
                    elif op==2:
                        add_trainer()
                    elif op==3:
                        pass
                    elif op==4:
                        pass
                    elif op==5:
                        pass
                    elif op==6:
                        pass
                    elif op==7:
                        pass
                    elif op==8:
                        add_student()
                    elif op==9:
                        update_student()
                    elif op==10:
                        delete_student()
                    else:
                        print("choose correct option")
                else:
                    print("invalid credentials")
            conn.commit()
        elif op==2:
            print("============================================")
            print("              WELCOME TRAINER PORTAL        ")
            print("============================================")
            email=input("enter your email : ")
            password=input("enter your password : ")
            cur.execute('select * from trainer')
            for i in cur:
                if i[2]==email and i[3]==password:
                    print("1.add student\n2.update student\n 3.delete student\n4.view details\n5.update details")
                    op=int(input("choose your option : "))
                    if op==1:
                        add_student()
                    elif op==2:
                        update_student()
                    elif op==3:
                        delete_student()
                    elif op==4:
                        view_trainer(email)
                    elif op==5:
                        pass
                    else:
                        print("choose correct option")
                else:
                    print("invalid credentials")
            conn.commit()
        elif op==3:
            print("welcome to pm")
        elif op==4:
            print("welcome to student")
            email=input("enter your emailid   :")
            password=input("enter your password : ")
            cur.execute("select * from student")
            for i in cur:
                if email==i[2] and password==i[3]:
                    print(f"login successfull {i[1]}")

                else:
                    print("not a student")
        else:
            print("choose correct option")
    except Exception as e:
        print(e)


print('ok')