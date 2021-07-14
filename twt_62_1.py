"""
10
l9rw71vyacrdkl6n7ljhu 16
a2b2c2d2e2f2g2 101
a2b2c2d2e2f2g2 102
a2b2c2d2e2f2g2 103
a2b2c2d2e2f2g2 94
a2b2c2d2e2f2g2 95
a2b2c2d2e2f2g2 96
a2b2c2d2e2f2g2 97
a2b2c2d2e2f2g2 98
a2b2c2d2e2f2g2 99
"""
import time
from time import perf_counter

def Q(s,i,t=''):
    for c in s:
        if c<'a':t*=int(c)
        else:t+=c
    return t,len(t)

for _ in[I:=input]*int(I()):
    s,j=I().split();j=int(j)-1
    start = perf_counter()
    L=[];a=0
    for c in s:L+=[(c,a)];a=a+1if c>'9'else a*int(c)
    while L:
        c,d=L.pop()
        try:
            if c<'a':j%=d
            elif j==d:print(c);break
        except:
            print('Index out of bounds!')
    end = perf_counter()
    print(end - start)
