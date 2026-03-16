def max_number(a):
    m=a[0]
    for i in a:
        if m<i:
            m=i
    return m

def hight_prime(a):
    m=2
    for i in a:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            if m<i:
                m=i
    return m