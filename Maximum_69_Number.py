n=int(input())
k=list(str(n))
for i in range(len(k)):
    if(k[i]=="6"):
        k[i]="9"
        break
for i in range(len(k)):
    print(k[i],end="")