def pal(n):
    s=str(n)
    l=s[::-1]
    return int(l)
n=int(input())
for i in range(n):
    n=n+pal(n)
    if n==pal(n):
        print(n)
        break