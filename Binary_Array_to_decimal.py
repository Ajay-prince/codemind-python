n=int(input())
l=list(map(int,input().split()))
total=0
for i in range(len(l)):
    last=l.pop()
    if last==1:
        total+=pow(2,i)
print(total)