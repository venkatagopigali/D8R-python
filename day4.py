# class father:
#     def weight(self):
#         print("70")
#     def color(self):
#         print("black")
# class mother:
#     def color(self):
#         print("white")
#     def height(self):
#         print("5.5")
# class child(father,mother):
#     def hobbies(self):
#         print("playing game")
# c=child()
# c.color()
# c.height()
# o=father()
# o.color()
# o.hobbies()

# class main_software:
#     def cam(self):
#         print("50px")
#     def security(self):
#         print("ios")
#     # def battery(self):
#     #     print("5000")
# class phone1(main_software):
#     def color(self):
#         print("blue")
#     def battery(self):
#         print("6000")
# class phone2(main_software):
#     def color(self):
#         print("red")
# class phone3(main_software):
#     def color(self):
#         print("white")
#     def cam(self):
#         print("100px")
# ph1=phone1()
# ph1.battery()
# ph1.security()
# ph1.color()

# ph2=phone2()
# ph2.security()
# ph2.battery()
# ph3=phone3()
# ph3.security()
# ph3.cam()
# ph3.battery()


class a:
    def color(self):
        print("green")
    def size(self):
        print("16:9")
class b(a):
    def proffession(self):
        print("data analyst")
class c(a):
    def company(self):
        print("10000coders")
class d(b,c):
    def salary(self):
        print("16lpa")
    def address(self):
        print("kphb")
# obj=d()
# obj.salary()
# obj.company()
# obj.proffession()
# obj.color()
# obj.size()

# obj1=b()
# obj1.color()
# obj1.proffession()
# print(c.__mro__)