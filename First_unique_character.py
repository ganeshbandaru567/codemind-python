s=input().lower()
s=list(s)
c=0
for i in s:
    if i==' ':
        continue
    elif s.count(i)==1:
        print(i)
        c=1
        break
if c==0:
    print("-1")
    