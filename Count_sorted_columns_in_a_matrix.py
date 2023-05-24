r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
sum=0

for i in range(c):
    lst=[]
    for j in range(r):
        lst.append(mat[j][i])
    if (lst==sorted(lst) or lst[::-1]==sorted(lst)):
        
        sum+=1
print(sum)
'''
r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
k=0
for i in range(c):
    d=[]
    for j in range(r):
        d.append(m[j][i])
    if(d==sorted(d) or d[::-1]==sorted(d)):
        k=k+1
print(k)        
        '''