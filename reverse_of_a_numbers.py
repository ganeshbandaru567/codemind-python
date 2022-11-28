n=int(input())
rev=0
while n:
    d=n%10
    n=n//10
    rev=rev*10+d
print(rev)