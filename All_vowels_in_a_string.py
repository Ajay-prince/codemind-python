n=list(input().split())
vowel=['a','e','i','o','u']
vowel1=['A','E','I','O','U']
lower=[]
upper=[]
def vowel2(s):
    for i in s:
        if i in vowel:
            lower.append(i)
def vowel3(s):
    for j in s:
        if j in vowel1:
            upper.append(j)
    
for s in n:
    
    vowel2(s)
    vowel3(s)
lower1=[]
upper1=[]
for u in lower:
    if u not in lower1:
        lower1.append(u)
for h in upper:
    if h not in upper1:
        upper1.append(h)
if len(lower1)==5 or  len(upper1)==5:
    print(True)
else:
    print(False)
    