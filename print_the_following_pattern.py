n=int(input())
capital=['A','B','C','D','E','F','G','H'
,'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l=[]
for i in range(n):
    l.append(capital[i])

for k in l:
    for j in range(n):
        print(k,end=' ')
    print()
    
    