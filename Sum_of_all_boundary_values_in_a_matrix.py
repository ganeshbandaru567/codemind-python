n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
s=sum(mat[0])+sum(mat[-1])
for i in range(1,len(mat)-1):
    s+=(mat[i][0])
    s+=(mat[i][-1])
print(s)