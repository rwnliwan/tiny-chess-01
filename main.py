import json,os,urllib.request as u
E=os.environ['MAKEFUN_ENV_URL'];V=[100,320,330,500,900,0];KN=[33,31,18,14,-14,-18,-31,-33];RD=[1,-1,16,-16];BD=[15,17,-15,-17];KG=RD+BD;CM={0:13,7:14,4:12,112:7,119:11,116:3};DO={'N':KN,'K':KG,'B':BD,'R':RD,'Q':KG};X=lambda b:[b|z<<14 for z in range(2,6)]
MT=10**5
B=[' ']*128;SD=CA=0;EP=-1;KI=[0,0];U=[];ND=LM=AB=0
n=lambda s:chr(s%8+97)+str(s//16+1)
j=lambda m:n(m&127)+n(m>>7&127)+('xxnbrq'[m>>14]if m>>14 else'')
q=lambda x:ord(x[1])*16+ord(x[0])-881
def ev():
 s=0
 for i,p in enumerate(B):
  if p==' ':continue
  x='PNBRQK'.index(p.upper());r=i>>4;a=abs(r-7*(p>'a'));v=V[x]+((8*a)if x==0 else(-25*a)if x==5 else 0);s+=v if p<'a' else-v
 return s if SD==0 else-s
def st():
 global B,SD,CA,EP,KI;B=[' ']*128;SD=0;CA=15;EP=-1;KI=[4,116]
 B[0:8]='RNBQKBNR';B[112:120]='rnbqkbnr';B[16:24]='PPPPPPPP';B[96:104]='pppppppp'
def A(q,y):
 b=B;u='PNBRQK'if y==0 else'pnbrqk';d=1-2*y
 for o in(-15*d,-17*d):
  t=q+o
  if not t&0x88 and b[t]==u[0]:return 1
 for k,o in enumerate(KN+KG):
  t=q+o
  if not t&0x88 and b[t]==u[1 if k<8 else 5]:return 1
 for k,o in enumerate(BD+RD):
  t=q+o
  while not t&0x88:
   p=b[t]
   if p!=' ':
    if p==u[4]or p==u[2+(k>3)]:return 1
    break
   t+=o
 return 0
def G(c=0):
 m=[];b=B;w=SD==0
 for f in range(128):
  if f&0x88:continue
  p=b[f]
  if p==' 'or(p<'a')!=w:continue
  t=p.upper()
  if t=='P':
   d=32*w-16;r=f>>4;l=1+5*w
   for y in(f+d,f+d-1,f+d+1):
    if y&0x88:continue
    g=b[y]
    if y==f+d:
     if g==' ':
      if r==l:m+=X(f|y<<7)
      elif not c:
       m.append(f|y<<7)
       if r==6-5*w and b[y+d]==' ':m.append(f|y+d<<7)
    elif g!=' 'and(g<'a')!=w:m+=X(f|y<<7)if r==l else[f|y<<7]
    elif y==EP:m.append(f|y<<7)
   continue
  for o in DO[t]:
   y=f
   while 1:
    y+=o
    if y&0x88:break
    g=b[y]
    if g!=' ':
     if(g<'a')!=w:m.append(f|y<<7)
     break
    if not c:m.append(f|y<<7)
    if t not in'BRQ':break
  if t=='K'and not c:
   v=SD^1;z=0 if w else 112
   for R,ps,em in((4-3*w,(5,6),(5,6)),(8-6*w,(3,2),(1,2,3))):
    if CA&R and all(B[z+s]==' 'for s in em)and all(not A(z+s,v)for s in(4,)+ps):m.append(z+4|z+ps[-1]<<7)
 return m
def M(m):
 global SD,CA,EP,KI;f=m&127;t=m>>7&127;p=m>>14;pc=B[f];w=SD;v=w^1;u=pc.upper();U.append((B[:],SD,CA,EP,KI[:]))
 cs=t+32*w-16 if u=='P'and(f&7)!=(t&7)and B[t]==' 'else t;cp=B[cs]
 if cp!=' ':B[cs]=' '
 B[f]=' ';pl='QRBNqrbn'[5-p+4*w]if p else pc;B[t]=pl
 if u=='K':
  KI[w]=t
  if abs(t-f)==2:
   r=f+3 if t>f else f-4;B[f+1 if t>f else f-1]=B[r];B[r]=' '
 CA&=CM.get(f,15)&CM.get(t,15);EP=-1
 if u=='P'and abs(t-f)==32:EP=(f+t)>>1
 SD=v
 if A(KI[w],v):W();return 0
 return 1
def W():
 global SD,CA,EP,KI;b,SD,CA,EP,KI=U.pop();B[:]=b
def O(ms):
 b=B;k=[]
 for m in ms:
  t=m>>7&127;tg=b[t];s=(1000+V['PNBRQK'.index(tg.upper())]-V['PNBRQK'.index(b[m&127].upper())]if tg!=' 'else 0)+(900 if m>>14 else 0);k.append((s<<17)|m)
 k.sort(reverse=1);ms[:]=[x&131071 for x in k]
def S(d,a,b,pl):
 global ND,AB;ND+=1
 if ND>=LM:AB=1;return 0
 ck=A(KI[SD],SD^1);bt=-MT-1
 if d<=0 and not ck:
  bt=ev()
  if bt>=b:return bt
  if bt>a:a=bt
 ms=G(d<=0 and not ck);O(ms);ln=0
 for m in ms:
  if not M(m):continue
  ln+=1;s=-S(d-1,-b,-a,pl+1);W()
  if AB:return 0
  if s>bt:bt=s
  if s>=b:return s
  if s>a:a=s
 if ln==0:return-MT+pl if ck else bt*(d<=0)
 return bt
def T(nb):
 global ND,LM,AB;mv=[]
 for m in G():
  if M(m):W();mv.append(m)
 O(mv);ND=0;LM=nb;AB=0;bm=mv[0];d=0
 while d<12 and not AB:
  d+=1;a=bs=-MT-1;bd=bm
  for m in mv:
   M(m);s=-S(d,-MT-1,-a,1);W()
   if AB:break
   if s>bs:bs=s;bd=m
   if s>a:a=s
  if not AB:bm=bd
 return bm
def P(p,b):
 try:return json.load(u.urlopen(E+p,json.dumps(b).encode()))
 except:return{'error':1}
def main():
 while 1:
  g=P('/game',{})
  if 'error'in g or g['status']=='done':break
  while g['status']=='your_move':
   try:
    st();U=[]
    for z in g['moves']:
     if not M(q(z[:2])|q(z[2:4])<<7|('nbrq'.index(z[4])+2 if len(z)==5 else 0)<<14):break
    mv=j(T(60000))
   except:mv=g['legal_moves'][0]
   g=P('/move',{'game':g['game'],'move':mv})
if __name__=='__main__':main()
