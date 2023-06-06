n=int(input())
a=0
b=1
k=0
while 1:
    k=a+b
    a,b=b,k
    if k<n:
        mi=k
    else:
        ma=k
        break
r1=n-mi
r2=ma-n
if r1<r2:
    print(mi)
elif r1==r2:
    print(mi,ma)
else:
    print(ma)