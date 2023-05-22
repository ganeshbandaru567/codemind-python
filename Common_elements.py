a,b=map(int,input().split())
lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
lst=[]
for i in lst1:
    if i in lst2:
        if i not in lst:
            lst.append(i)
print(*lst)