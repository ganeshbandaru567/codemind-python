n=int(input())
lst=list(map(int,input().split()))
e=0
for i in range(len(lst)):
    if i%2==0:
        e+=lst[i]
print(e)