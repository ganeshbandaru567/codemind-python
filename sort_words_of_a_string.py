s=input().split()
x=[]
for j in s:
    #j=str(i)
    c=[]
    d=""
    for k in j:
        if k.isalpha():
            c.append(k)
    c.sort()
    m=0
    for k in j:
        if k.isalnum():
            d=d+c[m]
            m=m+1
        else:
            d=d+k
    x.append(d)
print(" ".join(x))    
    