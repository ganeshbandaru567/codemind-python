n=int(input())
l=list(map(int,input().split()))
a=int(input())
lst=[]
count=0
for i in range(n):
    h=0
    for j in range(n):
        if l[i]==l[j]:
            h+=1
    if h==a:
        print(l[i],end=' ')
        count+=1
        l[i]=0
if count==0:
    print('-1')
            