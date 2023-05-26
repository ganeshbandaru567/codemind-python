s=input()
l=input()
for i in l.split():
    for j in s.split():
        if(i.lower()==j.lower()):
            print(j.lower(),end=" ")
            