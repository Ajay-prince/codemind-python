for _ in range(int(input())):
    n=int(input())
    s=input()
    l3=[]
    for u in s:
        l3.append(u)
    l=[]
    for i in l3:
        if i not in l:
            l.append(i)
    l2=[]
    for j in l:
        if l3.count(j)==1:
            l2.append(j)
    if len(l2)==0:
        print(-1)
    else:
        for k in l2:
            print(k)
            break
    