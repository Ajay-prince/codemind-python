n=list(input().split())
l1=[]
l2=[]
for _ in range(len(n)):
    a=''
    a=n.pop()
    l1.append(a)
l1.reverse()
for i in l1:
    
    l2.append(len(i))
print(max(l2))