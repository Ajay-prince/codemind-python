n=int(input())
l=map(int,input().split())
count=0
for i in l:
    j=str(i)
    if len(j)%2==0:
        count+=1
print(count)