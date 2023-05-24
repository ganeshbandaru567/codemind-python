r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
a=0
for i in range(r):
    lst=[]
    for j in range(c):
        lst.append(mat[i][j])
    if lst==sorted(lst) or lst[::-1]==sorted(lst):
        a+=1
print(a)