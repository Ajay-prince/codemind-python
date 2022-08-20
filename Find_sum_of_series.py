n=int(input())
sum=0
for i in range(n,0,-1):
    sum+=1/i
sum1="{:.2f}".format(sum)
print(sum1)
