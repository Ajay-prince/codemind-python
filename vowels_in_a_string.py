n=input()
v=input()

if v in n:
    print(True,end='
')
    print(n.index(v))
else:
    print(False)
