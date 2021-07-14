def P(t):
 r,*t=t
 for c in t:r+=[c,' '+c][c!=r[-1]]
 return[(c[0],len(c))for c in r.split()]
for _ in[I:=input]*int(I()):print('yneos'[len(K:=P(I()))!=len(L:=P(I()))or any(a!=c or b>d for(a,b),(c,d)in zip(K,L))::2])