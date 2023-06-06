import math
def prime(n):
    if n==1:
        return False
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            return False
    else:
        return True
for i in range(int(input())):
    a=int(input())
    for i in range(a,1,-1):
        if prime(i):
            k=i
            break
    s=a+1
    while 1:
        if prime(s):
            l=s
            break
        s+=1
    x=a-k
    y=l-a
    if x<y:
        print(k)
    elif x==y:
        print(k)
    else:
        print(l)
        