l=list(input().split())
d=0
e=0
for i in l:
    d+=ord(max(i))
    e+=ord(min(i))
print(abs(d-e),end=' ')