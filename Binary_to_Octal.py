for i in range(int(input())):
    n=int(input())
    t=n
    sum=0
    i=0
    while n>0:
        rem=n%10
        sum+=rem*pow(2,i)
        n=n//10
        i+=1


    l=[]
    while sum>0:
        re=sum%8
        l.append(re)
        sum=sum//8
    l.reverse()
    for i in l:
        print(i,end="")
    print(end='
')