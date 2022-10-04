n=int(input())
for _  in range(n):
    n1=input()
    l=[]
    l2=[]
    for j in n1:
        l.append(j)
    for k in l:
        if k=='0':
            l2.append('0000')
        elif k=='1':
            l2.append('0001')
        elif k=='2':
            l2.append('0010')
        elif k=='3':
            l2.append('0011')
        elif k=='4':
            l2.append('0100')
        elif k=='5':
            l2.append('0101')
        elif k=='6':
            l2.append('0110')
        elif k=='7':
            l2.append('0111')
        elif k=='8':
            l2.append('1000')
        elif k=='9':
            l2.append('1001')
        elif k=='A' or k=='a':
            l2.append('1010')
        elif k=='B'or k=='b':
            l2.append('1011')
        elif k=='C' or k=='c':
            l2.append('1100')
        elif k=='D' or k=='d':
            l2.append('1101')
        elif k=='E' or k=='e':
            l2.append('1110')
        elif k=='F' or k=='f':
            l2.append('1111')
        
    for r in l2:
        print(r,end='')
    print(end='
')
        
            
    
    