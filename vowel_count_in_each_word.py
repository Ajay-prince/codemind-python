n=list(input().split())
vowel=['a','e','i','o','u','A','E','I','O','U']
def vowel2(s):
    c=0
    for i in s:
        
        if i in vowel:
            c+=1
    print(c,end=' ')

for s in n:
    vowel2(s)

            
