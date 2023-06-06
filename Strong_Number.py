t=int(input())
n=t

s=0
while n!=0:
    k=n%10
    fc=1
    for i in range(1,k+1):
        fc*=i
    s+=fc
    n=n//10
if s==t:
    print(f'The number {t} is a strong number')
else:
    print(f'The number {t} is not a strong number')