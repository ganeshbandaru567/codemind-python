r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sv=0
so=0
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            sv+=mat[i][j]
        else:
            so+=mat[i][j]
print(sv,so)