# class certificate:
    # def __init__(self,name,age,marks,percentage,branch):
    #     self.name=name
    #     self.age=age
    #     self.marks=marks
    #     self.percentage=percentage
    #     self.branch=branch
    #     print("=====================================")
    #     print("           certificate             ")
    #     print("=====================================")
    #     print("name            :",self.name)
    #     print("age             :",self.age)
    #     print("marks           :",self.marks)
    #     print("percentage      :",self.percentage)
    #     print("branch          :",self.branch)
    # def __init__(self,a,b):
    #     print("welcome")
    # def __init__(self,a):
    #     self.a=a
    #     print(self.a)
    
# stu1=certificate("sai deepika",21,100,100,"cse")

# stu2=certificate("pranay",22,100,100,"aiml")
# onj=certificate(1,2,3)

# class constructor:
#     def __init__(self):
#         a=int(input("enter a value"))
#         b=int(input("enter sencod"))
#         print("welcome to oops")
#         print(a+b)
# obj=constructor()
# print(constructor.a)

# class house:
#     def __init__(self,kitchen,bedroom,hall):
#         print(kitchen,bedroom,hall)
# obj=house("yes",3,"yes")

class rev:
    def __init__(self,s):
        s1=""
        for i in s:
            s1=i+s1
        print(s1)
obj=rev("gopi")
obj2=rev("gali")
obj3=rev("venkata")

# "gopi" -->  "GOPI"