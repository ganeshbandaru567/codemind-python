n=int(input())
lst=list(map(int,input().split()))
k=sorted(lst,reverse=True)
if lst==k:
    print("yes")
else:
    print("no")