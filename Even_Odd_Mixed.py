n=input()
e=[]
o=[]
for i in n:
    if int(i)%2==0:
        e.append(i)
    else:
        o.append(i)
if len(n)==len(e):
    print("Even")
elif len(n)==len(o):
    print("Odd")
else:
    print("Mixed")