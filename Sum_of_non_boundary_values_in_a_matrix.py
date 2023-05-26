n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
    for j in range(m):
        if i!=0 and j!=0 and i!=n-1 and j!=m-1:
            s+=mat[i][j]
print(s)