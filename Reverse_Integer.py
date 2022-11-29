n=int(input())
count=0
if n<0:
    count=1
else:
    pass
string=str(abs(n))
reverse=string[::-1]
if(count==1):
    print(-1*(int(reverse)))
else:
    print(int(reverse))
    