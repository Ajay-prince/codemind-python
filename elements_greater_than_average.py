n=int(input())
l=list(map(int,input().split()))
import math as m
average=m.floor(sum(l)/len(l))
count=0
for i in l:
    if i>=average:
        count+=1
print(count)