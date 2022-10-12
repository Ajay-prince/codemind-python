n=input()
capital=['a','b','c','d','e','f'
,'g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z']
c=0
for i in n:
    if i in capital:
        c+=1
print(c)