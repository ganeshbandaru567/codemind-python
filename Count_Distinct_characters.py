s=input().lower()
s=list(s)
lst=[]
for i in range(len(s)):
    if s[i]!=' ':
        lst.append(s[i])
lst=set(lst)
print(len(lst))
    