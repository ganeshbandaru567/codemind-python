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
    if prime(i):
        l.append(i)
d=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]*l[j]==n:
            print(l[i],end=' ')
            print(l[j])
            d+=1
            break
if d==0:
    print("-1")
        