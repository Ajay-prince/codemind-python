n=int(input())
list1=list(map(int,input().split()))
list2=reversed(list1)
str1=''
str2=''
for i in list1:
    str1+=str(i)
for j in list2:
    str2+=str(j)
str1=int(str1)
str2=int(str2)
list3=[]
length=n
while str1>0:
   
    re=str2%10
    list3.append(re)
    rem=str1%10
    list3.append(rem)
    str1=str1//10
    str2=str2//10
    length-=1
    
    
while len(list3)>n:
    list3.pop()
if len(list3)%2!=0:
    list3.append(0)
for k in list3:
    print(k,end=' ')