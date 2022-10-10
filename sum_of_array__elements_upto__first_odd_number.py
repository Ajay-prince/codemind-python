n=int(input())
list1=list(map(int,input().split()))
sum=0

for i in list1:
    if i%2!=0:
        
        break
    else:
        sum+=i
print(sum)