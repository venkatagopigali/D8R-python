class example:
    def __init__(self):
        print("welcome packages")
    def display(self,a,b):
        return a+b
def arm(a):
    b=a
    l=len(str(a))
    res=0
    while a>0:
        r=a%10
        res=res+r**l
        a//=10
    if b==res:
        print(b , "is arm strong")
    else: 
        print(b , "not arm strong")
