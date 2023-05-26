s1=input().lower().split()
s2=input().lower().split()
count=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j]:
            count+=1
print(count)