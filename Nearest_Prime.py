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
            x=i
            break
    l=a+1
    while 1:
        if prime(l):
            y=l
            break
        l=l+1
    u=abs(a-x)
    v=abs(a-y)
    if u>v:
        print(y)
    else:
        print(x)
    