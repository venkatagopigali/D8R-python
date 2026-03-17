# from new_fn import max_number,hight_prime
# a=[11,1,2,3,4,5,6,12]
# print(max(a))
# print(max_number(a))
# print(hight_prime(a))

# from new_pack import practice,mod1
# a=[11,1,2,3,4,5,6,12]
# print(practice.list_prime(a))
# mod1.arm(1534)
# o=mod1.example()
# print(o.display(1,2))

from new_pack.practice import list_prime
from new_pack.mod1 import example,arm
o=example()
print(o.display(10,40))
print(arm(153))