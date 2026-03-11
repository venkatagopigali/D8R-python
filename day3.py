# class phone:
#     def __init__(self):
#         print("constructor")
#     def files(self):
#         print("movies,pics")
#     def downloads(self):
#         print("movies")
# class laptop(phone):
#     def desktop(self):
#         print("floader")
#     def cdrive(self):
#         print("storage")
# obj=phone()
# obj.files()
# obj.downloads()
# obj.desktop()
# obj2=laptop()
# obj2.cdrive()
# obj2.files()

# class parent:
#     def color(self):
#         print("white")
#     def height(self):
#         print("5.5")
#     def weight(self):
#         print("70")
# class child(parent):
#     def hobbies(self):
#         print("reading books")
# o=child()
# o.hobbies()
# o.color()




# class grandfather:
#     def height(self):
#         print("5.8")
#     def color(self):
#         print("black")
#     def age(self):
#         print(70)
# class father(grandfather):
#     def color(self):
#         print("white")
#     def weight(self):
#         print("70")
# class child(father):
#     def hobbies(self):
#         print("cricket")
# obj=child()
# obj.color()
# obj.weight()

# p=father()
# p.hobbies()
# p.color()
# p.height()


class father:
    def height(self):
        print("5.8")
    def color(self):
        print("black")
    def age(self):
        print(70)
class mother:
    def color(self):
        print("white")
    def weight(self):
        print("70")
class child(father,mother):
    def hobbies(self):
        print("cricket")
# obj=child()
# obj.color()
print(child.__mro__)