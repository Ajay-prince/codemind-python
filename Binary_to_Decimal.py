for i in range(int(input())):
    n=int(input())
    sum=0
    i=0
    while n>0:
        rem=n%10
        sum+=rem*pow(2,i)
        n=n//10
        i+=1
    print(sum)
        
    