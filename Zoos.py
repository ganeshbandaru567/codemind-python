s=input()
c=0
cc=0
for i in s:
    if i=='z':
        c+=1
    else:
        cc+=1
if c*2==cc:
    print("Yes")
else:
    print("No")