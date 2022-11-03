n=int(input())
lst=list(map(int,input().split()))
x=[lst[i] for i in range(n)]
print("%0.2f"%(sum(x)/n))