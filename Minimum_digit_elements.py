a=int(input())
lst=list(map(str,input().split()))
n=[]
m=[]
for i in lst:
    n.append(len(i))
for j in range(a):
    if n[j]==min(n):
        m.append(lst[j])
count=0
for i in m:
    count+=1
print(count)
        