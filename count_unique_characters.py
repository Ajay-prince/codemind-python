n=input()
a=[]
capital=['a','b','c','d','e','f'
,'g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
for i in n:
    if n.count(i)==1:
        a.append(i)
a.sort()
count=0
for i in a:
    if i not in capital:
        continue
    else:
        count+=1
print(count)