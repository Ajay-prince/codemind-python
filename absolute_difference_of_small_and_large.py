l=list(input().split())
for i in l:
    d=ord(max(i))
    e=ord(min(i))
    print(abs(d-e),end=' ')