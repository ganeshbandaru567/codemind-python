n=int(input())
a=0
b=1
print(a,end=' ')
print(b,end=' ')
for i in range(2,n):
    k=a+b
    print(k,end=' ')
    a,b=b,k
    