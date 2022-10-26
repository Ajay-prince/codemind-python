for _ in range(int(input())):
    a,b=map(int,input().split())
    count=0
    for i in range(a,b+1):
        if i<10:
            if i==2 or i==3 or i==9:
                count+=1
        else:
            re=i%10
            if re==2 or re==3 or re==9:
                count+=1
    print(count)
            