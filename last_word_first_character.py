n=list(input().split())
l1=[]
def first(s):
    for i in s:
        l1.append(i)
        break
for s in n:
    first(s)
l1.reverse()
for j in l1:
    print(j,end=' ')
    break