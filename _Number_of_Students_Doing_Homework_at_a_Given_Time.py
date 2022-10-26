n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
t=int(input())
count=0
for i in range(n):
    if l[i]<=t and l1[i]>=t:
        count+=1
print(count)
    