def div(n):
    c=0
    cc=0
    i=n
    while n!=0:
        k=n%10
        if k==0:
            return False
        if i%k==0:
            c+=1
        cc+=1
        n=n//10
    if c==cc:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if div(i):
        print(i,end=' ')