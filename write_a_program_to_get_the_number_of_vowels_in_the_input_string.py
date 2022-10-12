n=input()

vowel=['a','e','i','o','u','A','E','I','O','U']
l=[]
for i in n:
    if i in vowel:
        l.append((i))
    
if len(l)!=0:
    print(len(l))
else:
    print(0)