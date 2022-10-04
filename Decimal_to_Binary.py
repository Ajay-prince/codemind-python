for i in range(int(input())):
    n=int(input())
    l=[]
    while n>0:
        rem=n%2
        l.append(rem)
        n=n//2
    l.reverse()
    for j in  l:
        print(j,end="")
    print(end='
')