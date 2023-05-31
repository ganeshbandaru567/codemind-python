n=input().split()
p=[]
for i in n:
    k=[]
    c=0
    s=''
    for j in i:
        if j in 'AEIOUaeiou':
            pass
        else:
            k.append(j)
    k.sort()
    for j in i:
        if j in 'AEIOUaeiou':
            s+=j
        else:
            s+=k[c]
            c+=1
    p.append(s)
print(*p)
            