r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
temp=[]
s=0
for i in range(r):
    for  j in range(c):
        if (i==j or i+j==len(mat)-1) and [i,j] not in temp:
            temp.append([i,j])
            s+=mat[i][j]
print(s)