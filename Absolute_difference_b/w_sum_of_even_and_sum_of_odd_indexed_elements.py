n=int(input())
l=list(map(int,input().split()))
sum_e=0
sum_o=0
for i in range(0,len(l)):
    if i%2==0:
        sum_e+=l[i]
    else:
        sum_o+=l[i]
print(abs(sum_e-sum_o))