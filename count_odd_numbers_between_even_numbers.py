n=int(input())
l=list(map(int,input().split()))
index=[]
for i in range(len(l)):
    if l[i]%2==0:
        index.append(i+1)
index.reverse()
sum=0
for i in range(len(index)-1):
    sum+=(index[i]-index[i+1])-1
print(sum)