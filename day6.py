# print(2+10)
# print('2'+'10')
# print([1,2,3]+[4,5,6])

# print((2).__add__(10))
# print(('2').__add__('10'))
# print(([1,2,3].__add__([6,67,8])))

class eswar:
    def __init__(self,sql,python):
        self.a=sql
        self.b=python
    def __add__(self,e):
        print("sql marks",self.a+e.a)
        print("python ",self.b+e.b)
    def __sub__(self,e):
        print("sub method")
        # print("sql marks",self.a-e.a)
        # print("python ",self.b-e.b)
    def __mul__(self,a):
        print("multiplication")
    def __gt__(self,u):
        if self.a>u.a:
            print("True")
        else:
            print("False")
    def __lt__(self,u):
        if self.a<u.a:
            return True
        else:
            return False

st1=eswar(10,20)
st2=eswar(15,30)
# print(st1+st2)
# print(st1-st2)
# print(st1*st2)
print(st1>st2)
print(st1<st2)