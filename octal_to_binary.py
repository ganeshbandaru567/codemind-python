n=int(input())
dn=0
i=0
while(n!=0):
    d=n%10
    dn=dn+d*pow(8,i)
    n=n//10
    i=i+1
temp=dn    
bn=0
j=0
while(dn!=0):
    k=dn%2
    bn=bn+k*pow(10,j)
    dn=dn//2
    j=j+1
print(bn)  