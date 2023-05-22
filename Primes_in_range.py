def pir(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for j in range(a,b+1):
    if (pir(j) and j!=1):
        c+=1
print(c)
        