# class en:
#     a=10      # public variable
#     _b=200    # protected
#     def __init__(self):
#         print("welcome to encapisilation")
#     def oops(self,b):
#         self._c=b       # public variable
#         # print(self.b)
#         # print(en.a)
#         print(en._b)
#     def final(self):
#         print(self._c)
# class en1:
#     def __init__(self):
#         print(en.a)
#         print(en._b)
#         # print(self.b)
#     def add(self):
#         print(en.a)
#         print(en._b)
# o=en()
# o.oops("method oops")
# o.final()
# o1=en1()
# o1.add()
# # print("out ",en.a)
# print('out',en._b)


# class jeevan:
#     __a="mriet"
#     def __init__(self):
#         print(jeevan.__a)
#     def vishnu(self,b):
#         self.__b=b
#         print(self.__b)
#         print(jeevan.__a)
#     def akhil(self):
#         print(self.__b)
#         print(jeevan.__a)
# class jain:
#     def __init__(self):
#         print("name mangling",jeevan._jeevan__a)
# o=jeevan()
# o.vishnu('i am from')
# o.akhil()
# o1=jain()
# print(jeevan._jeevan__a)


# def vishnu(f):
#     def inner(a,b):
#         print("congratulations your selected")
#         f(a,b)
#         print(a,b)
#         print("your package 10lpa")
#     return inner

# @vishnu
# def name(a,b):
#     print('jeevan')
# name(10,20)

# def name():
#     print('akhil')
# name()