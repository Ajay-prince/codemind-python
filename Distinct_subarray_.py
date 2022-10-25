n=int(input())
n1=int(input())
l=[]
for i in range(n,n1+1):
    l.append(i)
count=0
count2=0
for j in l:
    if (j%2)!=0:
        count+=1
    else:
        count2+=1
count3=count*count2
print(count+count3)