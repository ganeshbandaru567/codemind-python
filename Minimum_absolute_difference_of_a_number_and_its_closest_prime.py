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
if prime(n):
    print("0")
    exit()
for i in range(n-1,1,-1):
    if prime(i):
        k=i
        break
a=n+1
while 1:
    if prime(a):
        l=a
        break
    a+=1
r1=n-k
r2=l-n
if r1<r2:
    print(r1)
elif r1==r2:
    print(r1)
else:
    print(r2)