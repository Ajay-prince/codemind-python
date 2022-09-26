n=int(input())
index_o=[]
l=list(map(int,input().split()))
n1=int(input())
count=0
for i in l:
    if i==n1:
        count+=1
print(count)