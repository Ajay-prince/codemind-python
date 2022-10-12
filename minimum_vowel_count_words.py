n=list(input().split())
vowel=['a','e','i','o','u','A','E','I','O','U']
l1=[]
def vowel2(s):
    c=0
    for i in s:
        
        if i in vowel:
            c+=1
    l1.append(c)

for s in n:
    vowel2(s)
d=min(l1)
c1=0
for i in l1:
    if i==d:
        c1+=1
print(c1)

            
