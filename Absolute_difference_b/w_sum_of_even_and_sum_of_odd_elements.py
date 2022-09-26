n=int(input())
l=list(map(int,input().split()))
sum_e=0
sum_o=0
for i in l:
    if i%2==0:
        sum_e+=i
    else:
        sum_o+=i
print(abs(sum_e-sum_o))
    