n=input()
if '6' not in n:
    print(''.join(n))
else:
    str=''
    ind=n.index('6')
    str=n[:ind]+'9'+n[ind+1:]
    print(str)