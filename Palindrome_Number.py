for _ in range(int(input())):
    n=int(input())
    t=n
    rev=0
    while n>0:
        re=n%10
        rev=rev*10+re
        n=n//10
    print(t==rev)