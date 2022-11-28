n=int(input())
x=0
y=1
print(x,y,end=" ")
for i in range(1,n-1):
    z=x+y
    x=y
    y=z
    print(z,end=" ")