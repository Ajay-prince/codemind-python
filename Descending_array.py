n=int(input())
list1=list(map(int,input().split()))
list3=sorted(list1,reverse=True)
if (list1==list3):
    print('yes')
else:
    print('no')