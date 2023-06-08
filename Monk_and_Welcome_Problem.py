n=int(input())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
l=[]
for i in range(n):
    l.append(lst1[i]+lst2[i])
print(*l)