n=input()
n1=[]
for i in n:
    n1.append(i.lower())
n2=n1
str1=''
for i in n2:
    str1+=i

n1.reverse()
str2=''
for j in n1:
    str2+=j
print(str2==str1)
