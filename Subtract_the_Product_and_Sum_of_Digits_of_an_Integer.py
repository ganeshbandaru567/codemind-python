n=int(input())
s=0
p=1
while n!=0:
    k=n%10
    s+=k
    p*=k
    n=n//10
print(p-s)