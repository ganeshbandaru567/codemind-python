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
    if n==k:
        return True
    else:
        return False
    
n=int(input())
x=n+1
while(1):
    if prime(x) and pal(x):
        print(x)
        break
    x=x+1

    
