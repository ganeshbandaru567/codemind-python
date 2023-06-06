def pal(n):
    s=str(n)
    l=s[::-1]
    if s==l:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if pal(i):
        print(i,end=' ')