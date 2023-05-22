n=int(input())
l=list(map(int,input().split()))
m=set(l)
c=0
for i in m:
    if l.count(i)==i:
        c+=1
print(c)
        