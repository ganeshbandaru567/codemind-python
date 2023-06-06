def pal(n):
    s=str(n)
    a=s[::-1]
    if s==a:
        return True
    else:
        return False



a=int(input())
b=int(input())
count=0
for i in range(a,b+1):
    if pal(i):
        print(i,end=' ')
