import re,sys,math
sys.argv=[sys.argv[0]]
exec(open('count.py').read().split("files=sys.argv[1:]")[0])
import glob
SEL="DCPD-202600061 DCPD-202600362 DCPD-202600380 DCPD-202600385 DCPD-202600415 DCPD-202600423 DCPD-202600431 DCPD-202600440 DCPD-202600443 DCPD-202600446 DCPD-202600465 DCPD-202600485 DCPD-202600486 DCPD-202600489 DCPD-202600494 DCPD-202600505 DCPD-202600518 DCPD-202600519 DCPD-202600526 DCPD-202600540 DCPD-202600547 DCPD-202600512 DCPD-202600500".split()
docs=[]
for s in SEL:
    raw=open(f'cpd/{s}.txt').read()
    t=president_only(raw).lower()
    docs.append((s,raw.split('\n')[0][:60],len(t.split()),t))
for s,ti,n,t in docs: print(s,n,ti)
# Poisson-ish: per-doc presence vs length; estimate per-word rate lambda per 1000 words with doc-level shrink
L=int(sys.stdin.readline() or 5000) if False else 5000
print("\nword, docs-with-hit, mean hits/1k words, P(>=1 in 5000 words) [negbin-ish via doc resampling]")
for w,r in WORDS.items():
    rates=[len(re.findall(r,t))/n*1000 for s,ti,n,t in docs]
    # doc-level mixture: P = mean over docs of 1-exp(-rate_d*5)
    p=sum(1-math.exp(-x*L/1000) for x in rates)/len(rates)
    hit=sum(1 for x in rates if x>0)
    print(f"{w:38s} {hit:2d}/{len(docs)} {sum(rates)/len(rates):6.2f}  P5k={p:.0%}")
