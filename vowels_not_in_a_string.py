n=input()
vowel=['a','e','i','o','u']
l=[]
for i in vowel:
    if i not in n:
        l.append((i))
    
if len(l)!=0:
    for j in l:
        print(j,end=' ')
else:
    print(0)