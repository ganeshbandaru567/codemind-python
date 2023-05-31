s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
s3 = s1.intersection(s2)
f=0
k=[]
for i in s3:
    if i.isalpha():
        k.append(i)
        k.sort()
        f+=1
if f==0:
    print("-1")
else:
    for i in k:
        print(i,end='')

