n=list(input().split())

def reverse(s):
    str=''
    for i in s:
        str=i+str
    print(str,end=' ')
for s in n:
    
    reverse(s)
    
    