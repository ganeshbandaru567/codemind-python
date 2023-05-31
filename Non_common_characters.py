s1=input().lower()
s2=input().lower()
s1=set(s1)
s2=set(s2)
s3 = s1.symmetric_difference(s2)

k=[]
for i in s3:
    if i!=' ' and i.isalpha():
        k.append(i)
print(len(k))
