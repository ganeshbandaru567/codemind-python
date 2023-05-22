def pal(num):
    s=str(num)
    a=s[::-1]
    if a==s:
        return True
    else:
        return False
a=int(input())
lst=list(map(int,input().split()))
count=0
for i in range(len(lst)):
    if (pal(lst[i])):
        count+=1
print(count)