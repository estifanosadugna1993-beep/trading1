from math import log,sqrt,exp,erf
N=lambda x:0.5*(1+erf(x/sqrt(2)))
def bs(S,K,T,v,c=True,r=0.04):
    if T<=0: return max(S-K,0) if c else max(K-S,0)
    d1=(log(S/K)+(r+v*v/2)*T)/(v*sqrt(T)); d2=d1-v*sqrt(T)
    return S*N(d1)-K*exp(-r*T)*N(d2) if c else K*exp(-r*T)*N(-d2)-S*N(-d1)
# name, spot, exp days, iv now, days to event, iv after event, call?, moneyness list
cases=[
("APLD Oct16 C",24.37,15,0.99,7,0.75,True,[1.20,1.30]),
("APLD Nov20 C",24.37,50,0.86,7,0.75,True,[1.30,1.50]),
("APLD Nov20 P",24.37,50,0.86,7,0.75,False,[0.75,0.65]),
("CRWV Dec18 C",87.12,78,0.76,41,0.62,True,[1.30,1.50]),
("CRWV Dec18 P",87.12,78,0.76,41,0.62,False,[0.75,0.65]),
("NBIS Dec18 C",235.88,78,0.86,40,0.70,True,[1.30,1.50]),
("NBIS Dec18 P",235.88,78,0.86,40,0.70,False,[0.75,0.65]),
("IREN Jan15 C",40.88,106,0.82,60,0.75,True,[1.30,1.50]),
("IREN Jan15 P",40.88,106,0.82,60,0.75,False,[0.75,0.65]),
("SNDK Nov20 P",1739.89,50,0.73,28,0.62,False,[0.85,0.80]),
("SNDK Nov20 C",1739.89,50,0.73,28,0.62,True,[1.15,1.25]),
("CLS Nov20 P",361.43,50,0.72,26,0.58,False,[0.85,0.80]),
("ORCL Jan15 P",137.30,106,0.55,70,0.48,False,[0.80,0.70]),
("ORCL Jan15 C",137.30,106,0.55,70,0.48,True,[1.25,1.40]),
]
for name,S,T,v,te,v2,c,ms in cases:
    for m in ms:
        K=round(S*m,2); p=bs(S,K,T/365,v,c)
        out=[]
        for mv in ([0.15,0.25,0.35,0.50] if c else [-0.15,-0.25,-0.35,-0.45]):
            val=bs(S*(1+mv),K,(T-te)/365,v2,c); out.append(f"{mv:+.0%}:{val/p:5.1f}x")
        print(f"{name} K={K:8.2f} ({m:.0%}) prem={p:7.3f} ({p/S:.2%} of spot) | after event: "+"  ".join(out))
print("--- short-dated event tails (Nov20 bought ~1 day pre-event, event IV loaded) ---")
for name,S,v,c,ms in [("CRWV",87.12,1.10,True,[1.25,1.35]),("CRWV",87.12,1.10,False,[0.75,0.65]),("NBIS",235.88,1.15,True,[1.25,1.35]),("NBIS",235.88,1.15,False,[0.75,0.65])]:
    for m in ms:
        K=S*m;p=bs(S,K,10/365,v,c)
        o=[f"{mv:+.0%}:{bs(S*(1+mv),K,9/365,0.65,c)/p:5.1f}x" for mv in ([0.2,0.3,0.4] if c else [-0.2,-0.3,-0.4])]
        print(name,'C' if c else 'P',f"{m:.0%}",f"prem {p/S:.2%}"," ".join(o))
print("APLD Oct16 30%OTM call contracts per $1M:",round(1e6/(0.253*100)))
print("NBIS Dec 150% call contracts per $1M:",round(1e6/(9.438*100)))
print("SNDK Nov20 80% put contracts per $1M:",round(1e6/(46.18*100)))
