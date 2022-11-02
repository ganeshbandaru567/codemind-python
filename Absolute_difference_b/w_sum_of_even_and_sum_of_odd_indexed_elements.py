n=int(input())
e=0
o=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2==0:
        e+=l[i]
    else:
        o+=l[i]
print(abs(e-o))
