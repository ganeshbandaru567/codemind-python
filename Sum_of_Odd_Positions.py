n=int(input())
lst=list(map(int,input().split()))
o=0
for i in range(len(lst)):
    if i%2!=0:
        o+=lst[i]
print(abs(o))