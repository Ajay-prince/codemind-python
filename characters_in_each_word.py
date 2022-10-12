n=list(input().split())
l1=[]
for _ in range(len(n)):
    a=''
    a=n.pop()
    l1.append(a)
l1.reverse()
for i in l1:
    
    print(len(i),end=' ')