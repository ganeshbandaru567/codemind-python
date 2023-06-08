lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))
l1=0
l2=0
for i in range(len(lst1)):
    if lst1[i]>lst2[i]:
        l1+=1
    elif lst1[i]==lst2[i]:
        continue
    else:
        l2+=1
print(l1,l2)