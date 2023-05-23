r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sv=0
so=0
for i in range(len(mat)):
    if i%2==0:
        sv+=sum(mat[i])
    else:
        so+=sum(mat[i])
print(sv,so)
        
    