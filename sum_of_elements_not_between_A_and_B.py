n=int(input())
lst=list(map(int,input().split()))
m,n=map(int,input().split())
sum=0
for i in lst:
    if i<m or i>n:
        sum+=i
print(sum)
