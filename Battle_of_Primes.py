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
a=int(input())
b=int(input())
for i in range(1,a+1):
    s=a+b+i
    if prime(s)==True:
        print(i)
        break