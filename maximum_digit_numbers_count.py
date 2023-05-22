a=int(input())
lst=list(map(str,input().split()))
n=[]
m=[]
for i in lst:
    n.append(len(i))
for j in range(a):
    if n[j]==max(n):
        m.append(lst[j])
print(*m)