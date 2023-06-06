def dig(n):
    s=0
    while n!=0:
        k=n%10
        s+=k
        n=n//10
    if len(str(s))==1:
        print(s)
    else:
        dig(s)
n=int(input())
dig(n)
