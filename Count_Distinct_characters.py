n=input()
a=[]
capital=['a','b','c','d','e','f'
,'g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
for u in n:
    if n.count(u)==1:
        a.append(u)
count=0
a1=[]
count1=0
       
for i in a:
    if i not in capital:
        continue
    else:
        count1+=1
a1=[]
for w in n:
    if n.count(w)!=1:
        a1.append(w)
a2=[]
for j in a1:
    if j not in a2:
         a2.append(j)
for k in a2:
    if k not in capital:
        continue
    else:
        count+=1
print(count1+count)
            
