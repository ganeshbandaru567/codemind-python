n=int(input())
l=list(map(int,input().split()))
k=int(input())
total=0
count=0
for i in range(n):
    a=0
    for j in range(1,l[i]+1):
        if l[i]%j==0:
            a+=1
    if a==2:
        if l[i]<=k:
            count+=1
print(count)