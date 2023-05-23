n=int(input())
lst=list(map(int,input().split()))
k=sorted(set(lst))
if lst==k:
    print("yes")
else:
    print("no")