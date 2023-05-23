r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sum=0
for i in range(r):
    for j in range(c):
        sum+=mat[i][j]
print(sum)