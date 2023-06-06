n=int(input())
p=1
s=0
while n!=0:
    k=n%10
    p*=k
    s+=k
    n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")