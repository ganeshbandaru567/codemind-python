for i in range(int(input())):
    a,b=map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))
    l=[]
    for i in lst1:
        l.append(i)
    for j in lst2:
        l.append(j)
    l.sort()
    print(*l)