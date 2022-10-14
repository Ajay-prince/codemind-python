n=list(input().split())
l=[]
def plain(n):
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
    count=0
    if str1==str2:
        count+=1
        l.append(count)
        
for i in n:
    plain(i)
print(len(l))