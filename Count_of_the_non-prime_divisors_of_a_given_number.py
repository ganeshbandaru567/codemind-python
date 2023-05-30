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
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
c=0
for i in l:
    if prime(i)==False:
        c+=1
print(c)