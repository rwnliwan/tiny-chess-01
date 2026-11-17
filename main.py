import json,os,urllib.request as u
I='PNBRQK';Z=' '*8
V=[100,320,330,500,900,0];KN=[33,31,18,14,-14,-18,-31,-33];RD=[1,-1,16,-16];BD=[15,17,-15,-17];KG=RD+BD;CM={0:13,7:14,4:12,112:7,119:11,116:3};DO=[0,KN,BD,RD,KG,KG];X=lambda b:[b|z<<14 for z in(2,3,4,5)]
MT=1e5;NB=3e4
PS="AAAACCCCGGGGMMMUUUUaaaaiqqquAAAA/49>49>C9>CH>CHM>CHM9>CH49>C/49>7;?C;?CG?CGKCGKOCGKO?CGK;?CG7;?C"
H=[' ']*128;SD=CA=0;EP=-1;KI=[0,0];U=[];ND=LM=AB=0;D={}
n=lambda s:chr(s%8+97)+str(s//16+1)
j=lambda m:n(m&127)+n(m>>7&127)+('xxnbrq'[m>>14]if m>>14 else'')
q=lambda x:ord(x[1])*16+ord(x[0])-881
def ev():
 s=0
 for i,p in enumerate(H):
  if p==' ':continue
  x=I.find(p.upper());r=i>>4;a=abs(r-7*(p>'a'));v=V[x]+(ord(PS[min(x,2)*32+min(i&7,7-i&7)+4*a])-65 if x<5 else-25*a);s+=v if p<'a' else-v
 return s*(1-2*SD)
def A(q,y):
 u=I.lower()if y else I;d=1-2*y
 for o in(-15*d,-17*d):
  t=q+o
  if not t&0x88 and H[t]==u[0]:return 1
 for k,o in enumerate(KN+KG):
  t=q+o
  if not t&0x88 and H[t]==u[1 if k<8 else 5]:return 1
 for k,o in enumerate(BD+RD):
  t=q+o
  while not t&0x88:
   p=H[t]
   if p!=' ':
    if p==u[4]or p==u[2+(k>3)]:return 1
    break
   t+=o
 return 0
def G(c=0):
 m=[];w=SD==0
 for f in range(128):
  if f&0x88:continue
  p=H[f]
  if p==' 'or(p<'a')^w:continue
  t=p.upper()
  if t=='P':
   d=32*w-16;r=f>>4;l=1+5*w
   for y in(f+d,f+d-1,f+d+1):
    if y&0x88:continue
    g=H[y]
    if y==f+d:
     if g==' ':
      if r==l:m+=X(f|y<<7)
      elif not c:
       m.append(f|y<<7)
       if r==7-l and H[y+d]==' ':m.append(f|y+d<<7)
    elif g!=' 'and(g<'a')^w:m+=X(f|y<<7)if r==l else[f|y<<7]
    elif y==EP:m.append(f|y<<7)
   continue
  for o in DO[I.find(t)]:
   y=f
   while 1:
    y+=o
    if y&0x88:break
    g=H[y]
    if g!=' ':
     if(g<'a')^w:m.append(f|y<<7)
     break
    if not c:m.append(f|y<<7)
    if t not in'BRQ':break
  if t=='K'and not c:
   v=SD^1;z=112*(not w)
   for R,ps,em in((4-3*w,(5,6),(5,6)),(8-6*w,(3,2),(1,2,3))):
    if CA&R and all(H[z+s]==' 'for s in em)and all(not A(z+s,v)for s in(4,)+ps):m.append(z+4|z+ps[-1]<<7)
 return m
def M(m):
 global SD,CA,EP,KI;f=m&127;t=m>>7&127;p=m>>14;pc=H[f];w=SD;v=w^1;u=pc.upper();U.append((H[:],SD,CA,EP,KI[:]))
 cs=t+(32*w-16)*(u=='P'and(f&7)^(t&7)and H[t]==' ');cp=H[cs]
 if cp!=' ':H[cs]=' '
 H[f]=' ';pl='QRBNqrbn'[5-p+4*w]if p else pc;H[t]=pl
 if u=='K':
  KI[w]=t
  if abs(t-f)==2:
   r=f+3 if t>f else f-4;H[f+1 if t>f else f-1]=H[r];H[r]=' '
 CA&=CM.get(f,15)&CM.get(t,15);EP=(f+t)>>1 if u=='P'and abs(t-f)==32 else-1
 SD=v
 if A(KI[w],v):W();return 0
 return 1
def W():
 global SD,CA,EP,KI;b,SD,CA,EP,KI=U.pop();H[:]=b
def O(ms):
 ms.sort(key=lambda m:((m==Y),((1000+V[I.find(H[m>>7&127].upper())]-V[I.find(H[m&127].upper())]if H[m>>7&127]!=' 'else 0)+(V[(m>>14)-1]if m>>14 else 0))<<17|m),reverse=1)
def S(d,a,b,pl):
 global ND,AB,Y;ND+=1
 if ND>=LM:AB=1;return 0
 ck=A(KI[SD],SD^1);bt=-MT-1;q=d<=0 and not ck
 if q:
  bt=ev()
  if bt>=b:return bt
  if bt>a:a=bt
 Y=0
 if d>0:K=(''.join(H),SD,CA,EP);Y=D.get(K)
 ms=G(q);O(ms);ln=bm=0
 for m in ms:
  if not M(m):continue
  ln+=1;s=-S(d-1,-b,-a,pl+1);W()
  if AB:return 0
  if s>bt:bt=s;bm=m
  if s>=b:break
  if s>a:a=s
 if ln==0:return-MT+pl if ck else bt*(d<=0)
 if d>0:D[K]=bm
 return bt
def T():
 global ND,LM,AB,Y;mv=[m for m in G()if M(m)and not W()]
 Y=0;O(mv);bm=mv[0];d=ND=AB=0;LM=NB
 while d<12 and not AB:
  d+=1;ND=AB=0;LM=NB;a=bs=-MT-1;bd=bm
  for m in mv:
   M(m);s=-S(d-1,-MT-1,-a,1);W()
   if AB:break
   if s>bs:bs=s;bd=m
   if s>a:a=s
  if AB:break
  bm=bd
 return bm
def P(p,b):
 try:return json.load(u.urlopen(os.environ['MAKEFUN_ENV_URL']+p,json.dumps(b).encode()))
 except:return{'error':1}
def main():
 global H,SD,CA,EP,KI
 while 1:
  g=P('/game',{})
  if 'error'in g or g['status']=='done':break
  while g.get('status')=='your_move':
   try:
    H=list('RNBQKBNR'+Z+'PPPPPPPP'+Z*9+'pppppppp'+Z+'rnbqkbnr'+Z);SD=0;CA=15;EP=-1;KI=[4,116]
    for z in g['moves']:
     if not M(q(z[:2])|q(z[2:4])<<7|('nbrq'.find(z[4:])+2)*(len(z)==5)<<14):break
    mv=j(T())
   except:mv=g['legal_moves'][0]
   g=P('/move',{'game':g['game'],'move':mv})
main()
