n=int(input())
lst=list(map(int,input().split()))
num=0
for i in range(n):
    num=num*10+lst[i]
arr=[]
num+=1
s=0
while num!=0:
    d=num%10
    arr.append(d)
    s+=1
    num=num//10
for i in range(s-1,-1,-1):
    print(arr[i],end=' ')