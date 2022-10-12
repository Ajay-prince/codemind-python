n=list(input().split())

def reverse(s):
    str=''
    for i in s:
        str=i+str
    print(str,end=' ')
for s in range(len(n)):
    
    if s%2==0:
        reverse(n[s])
    else:
        print(n[s],end=' ')
    
    