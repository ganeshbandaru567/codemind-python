a=input()
lst=[]
m=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                c+=1
    if c==0:
        print(i)
        m=1
        break
if m==0:
    print("-1")
            
            