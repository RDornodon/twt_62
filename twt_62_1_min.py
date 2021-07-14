for _ in[I:=input]*int(I()):
 s,j=I().split();j=int(j)-1;L=[];a=0
 for c in s:L+=[(c,a)];a=a+1if c>'9'else a*int(c)
 while L:
  c,d=L.pop()
  if c<'a':j%=d
  elif j==d:print(c);break