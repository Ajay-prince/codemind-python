import math as m
def fun():
    x=int(input())
    q=int(m.sqrt(x))
    if q*q==x:
        print('True')
    elif q*q>x:
        print('False')
    else:
        print('False')
fun()
            