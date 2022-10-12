n=input()
capital=['A','B','C','D','E','F'
,'G','H','I','J','K','L','M','N','O','P','Q','R',
'S','T','U','V','W','X','Y','Z']
c=0
for i in n:
    if i in capital:
        c+=1
print(c)