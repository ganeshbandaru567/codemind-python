a,b=map(int,input().split())
if a>b:
    g=a
else:
    g=b
while 1:
    if (g%a==0) and (g%b==0):
        lcm=g
        break
    g+=1
print(lcm)