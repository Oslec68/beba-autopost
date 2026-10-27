import sys, numpy as np, soundfile as sf
seed=int(sys.argv[1]) if len(sys.argv)>1 else 1
out=sys.argv[2] if len(sys.argv)>2 else 'music.wav'
_r=np.random.default_rng(seed)
sr=44100; bpm=int(_r.integers(112,130)); beat=60/bpm; T=15.0; N=int(T*sr); t=np.arange(N)/sr
mix=np.zeros(N); rng=np.random.default_rng(seed)
def add(sig,start,gain=1.0):
    i=int(start*sr); j=min(N,i+len(sig)); mix[i:j]+=sig[:j-i]*gain
def env(n,a=0.005,d=0.2):
    x=np.arange(n)/sr; return np.minimum(1,x/a)*np.exp(-x/d)
def kick():
    n=int(.35*sr); x=np.arange(n)/sr; f=50+90*np.exp(-x*30); return np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-x*9)
def clap():
    n=int(.2*sr); return rng.standard_normal(n)*np.exp(-np.arange(n)/sr*25)
def hat():
    n=int(.05*sr); s=rng.standard_normal(n); s=np.diff(s,prepend=0); return s*np.exp(-np.arange(n)/sr*90)
def tone(f,dur,kind="saw",a=.01,d=None):
    n=int(dur*sr); x=np.arange(n)/sr
    if kind=="saw": s=sum(np.sin(2*np.pi*f*k*x)/k for k in range(1,8))
    else: s=np.sin(2*np.pi*f*x)
    e=np.minimum(1,x/a)*np.minimum(1,(dur-x)/0.05); 
    if d: e=e*np.exp(-x/d)
    return s*e
def midi(m): return 440*2**((m-69)/12)
PROG=[[[57,60,64],[53,57,60],[60,64,67],[55,59,62]],[[60,64,67],[57,60,64],[53,57,60],[55,59,62]],[[62,65,69],[58,62,65],[60,64,67],[57,60,64]],[[55,59,62],[52,55,59],[60,64,67],[62,66,69]]]
chords=PROG[seed%4]  # C Am F G
bassn=[c[0]-24 for c in chords]
bar=4*beat; nb=int(T/beat)+1
for b in range(nb):
    st=b*beat
    if st>=T: break
    intro = st<1.0
    add(kick(),st,0.9 if not intro or b%2==0 else 0.6)
    if b%2==1 and not intro: add(clap(),st,0.25)
    if not intro:
        add(hat(),st+beat/2,0.18); add(hat(),st,0.08)
for k in range(int(T/bar)+1):
    st=k*bar; c=chords[k%4]
    if st>=T: break
    for m in c: add(tone(midi(m),bar,"saw",a=.08),st,0.035)
    for q in range(8):
        if st+q*beat/2<T: add(tone(midi(bassn[k%4]+(12 if q%2 else 0)),beat/2*0.9,"sine",d=.25),st+q*beat/2,0.22)
# plucks melody
mel=[76,74,72,76,79,77,76,74]
for k in range(int(T/(beat/2))):
    st=k*beat/2
    if st<3.0 or st>T-1: continue
    if k%4 in (0,3): add(tone(midi(mel[k%8]),0.25,"saw",d=.08),st,0.04)
# whooshes at transitions
for w in [3.0,6.5,11.5]:
    n=int(.5*sr); s=rng.standard_normal(n); x=np.arange(n)/n
    s=np.convolve(s,np.ones(30)/30,'same')*np.sin(np.pi*x)**2
    add(s,w-0.25,0.35)
# fade out
fo=int(1.2*sr); mix[-fo:]*=np.linspace(1,0,fo)
mix/=np.max(np.abs(mix))*1.1
sf.write(out,np.stack([mix,mix],1),sr)
print("ok")
