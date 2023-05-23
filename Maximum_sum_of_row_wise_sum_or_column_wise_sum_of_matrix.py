r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
lst=[]
for i in range(len(mat)):
    lst.append(sum(mat[i]))
print(max(lst))
        