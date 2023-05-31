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
def pal(n):
    temp=n
    t=str(temp)
    k=int(t[::-1])
    return k
n=int(input())
x=pal(n)
if prime(n) and prime(x):
    print('circular prime')
elif prime(n)==True and prime(x)==False:
    print('prime but not a circular prime')
else:
    print('not prime')
