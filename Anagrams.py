s1=input()
s2=input()
n1=[]
n2=[]
for i in s1:
    n1.append(i.lower())
for j in s2:
    n2.append(j.lower())
n1.sort()
n2.sort()
str1=''
str2=''
for k in n1:
    str1+=k
for e in n2:
    str2+=e
print(str1==str2)