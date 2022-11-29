n=int(input())
num=len(str(n))
sq=n**2
ld = sq%pow(10,num)  
if ld == n:  
  print("Automorphic Number")  
else:  
  print("Not an Automorphic Number")  
  