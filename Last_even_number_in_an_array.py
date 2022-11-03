n=int(input())
lst=list(map(int,input().split()))
x=[lst[i] for i in range(n) if lst[i]%2==0]
print(x[-1])