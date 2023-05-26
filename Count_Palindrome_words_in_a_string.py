s=input()
st=s.split()
count=0
for i in st:
    if i.lower()==i[::-1].lower():
        count+=1
print(count)