n=int(input())
lst=list(map(int,input().split()))
m=int(input())
c=0

for i in range(n):
    if m==lst[i]:
        print(i,end=' ')
        c+=1
        break
for i in range(n-1,-1,-1):
    if m==lst[i]:
        print(i,end=' ')
        c+=1
        break
if c==0:
    print("-1 -1")
        