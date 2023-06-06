import math
for i in range(int(input())):
    n=int(input())
    k=math.sqrt(n)
    if n%k==0:
        print(True)
    else:
        print(False)