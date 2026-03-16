def list_prime(a):
    l=[]
    for i in a:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            l.append(i)
    return l