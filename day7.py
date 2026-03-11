# class ins:
    # def __init__(self):
    #     print("welcome")
    # def add(self,a,b):
    #     self.a=a
    #     self.b=b
    #     if self.a>self.b:
    #         print("a is big")
    #     else:
    #         print("b is big")
    # def sub(self):
    #     if self.a>self.b:
    #         print("a is big value")
    #     else:
    #         print("b is big value")
    # def sum(self,c,d):
    #     c=10
    #     d=10
    #     print(c+d)
    # def mul(self):
    #     print(c*d)
    # print(self.a)
    # @staticmethod
    # def hello(a,b):
    #     print("hi")
    #     print(a+b)
#     pass
# o=ins()
# o.add(3,4)
# o.sub()
# o.hello(5,6)
# o.sum()
# def hello():
#     print("hi")
# hello()


# class cl:
#     bank='SBI'
#     IFSCCODE='SBI0007'

#     @classmethod
#     def change(cls,b):
        # print(cl.bank,"\n",cl.IFSCCODE)
        # bank1='hello'
        # cls.bank=b
        # print(cls.bank)
        # print(cls.b)
    # def change1(self,bank):
    #     print(cl.bank)
    #     self.bank=bank
    #     print(self.bank)
        # self.bank='union'
    # def new(self):
    #     print(self.bank)
    # print(bank)
#     pass
# o=cl()
# o.change('axis')
# o.change1('union')
# o.new()


# class hello:
#     def __init__(self):
#         print('welcome')
#     def display1(self):
#         # super().__init__()
#         print("10000coders")
# class b(hello):
#     def __init__(self):
#         super().__init__()
#         print("hello word")
# o=hello()
# # o.display()
# o.display1()
# o=b()


# class father:
#     def __init__(self):
#         print('i am father')
# class mother:
#     def __init__(self):
#         print('i am mother')
# class child(father,mother):
#     def __init__(self):
#         super().__init__()
#         print('i am child')
# o=child()
# print(child.__mro__)