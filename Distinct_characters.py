s=input().lower()

lst='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'
for i in s:
    if i==' ':
        continue
    else:
        if s.count(i)==1:
            lst+=i
k=sorted(lst)
print(''.join(k))
