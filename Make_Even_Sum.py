n=int(input())
lst=list(map(int,input().split()))
sum=0
for i in lst:
    sum+=i
if sum%2==0:
    print(1)
else:
    print(0)