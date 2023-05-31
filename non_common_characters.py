s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
b=[]
s3 = s1.symmetric_difference(s2)
for i in s3:
    if i!=' ' and i.isalpha():
        b.append(i)
        b.sort()
for i in b:
    print(i,end='')