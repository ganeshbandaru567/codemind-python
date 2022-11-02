n = int(input())
arr = list(map(int,input().split()))
m=int(input())
for i in range(len(arr)):
    if arr[i]==m:
       print(True)
       break
else:
    print(False)