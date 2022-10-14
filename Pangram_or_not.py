n=input()
capital=['a','b','c','d','e','f'
,'g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
a=[]
for i in n:
    a.append(i.lower())

    
b=[]
for j in a:
    if j not in b:
        b.append(j)
for k in b:
    if k==' ':
        b.remove(k)

print(len(b)==26)