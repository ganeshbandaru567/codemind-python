import math
n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(len(lst)):
    k=math.sqrt(lst[i])
    if lst[i]%k==0:
        l.append(lst[i])
print(sum(l))
