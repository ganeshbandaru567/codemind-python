n=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
mat1=[list(map(int,input().split())) for i in range(n)]
s=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(abs(mat[i][j]-mat1[i][j]))
        #print(s,end=' ')
    #print()
    s.append(a)
for i in s:
    print(*i)