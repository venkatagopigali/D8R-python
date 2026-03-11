# def display(a,b):
#     print(a+b)
# display(2,3)        # adding
# display("gopi",'gali') # concat

# class duck:
#     def sound(self):
#         print("quack quack")
#     def walk(self):
#         print("waking")
# class train:
#     def sound(self):
#         print("sounding")
#     def walk(self):
#         print("chasing")
# d=duck()
# d.sound()
# d.walk()
# d=train()
# d.sound()
# d.walk()
# def display(a):
#     return a.sound(),a.walk()
# print(display(duck()))
# print(display(train()))

# class overloading:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c):
#         print(a+b+c)
# o=overloading()
# # o.add(2,3)
# o.add(2,3,4)

# class overloading:
#     def add(self,*a):
#         # print(sum(a[0]))
#         s=0
#         for i in a:
#             s=s+sum(i)
#         print(s)
# o=overloading()
# o.add(1)
# o.add(1,2)
# o.add([1,2,3,4,5],[8,9,0],[5,6])
# o.add([6,7],[5,6])


# def add(*a):
#     print(a)
#     print(type(a))
# add(12,3,4)
# add([12,3,4])

# class cal:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b):
#         print(a&b)
# o=cal()
# o.add(10,5)

class cal:
    def add(self,a,b):
        print(a+b)
    def security(self):
        print('high level')
    # def add(self,a,b):
    #     print(a+b)
class cal1(cal):
    def add(self,a,b):
        print(a&b)
o=cal1()
o.add(3,4)
print(cal1.mro())
# o.security()
# print()

# o1=cal()
# o1.add(2,3)
# o1.security()