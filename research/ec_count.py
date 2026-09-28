"""Earnings-call word counter. Usage: ec_count.py WORDS_JSON COMPANY_SPEAKERS(comma) files...
Transcript text format: [initial letter line] Name line, then paragraphs, until next name line."""
import re,sys,json
words=json.loads(open(sys.argv[1]).read())
company=set(x.strip().lower() for x in sys.argv[2].split(','))
files=sys.argv[3:]
def segments(t):
    t=re.split(r'\nROIC AI\s*\n',t)[0]
    lines=[l.strip() for l in t.split('\n')]
    segs=[];cur=None;buf=[]
    for i,l in enumerate(lines):
        is_name = (0<len(l)<40 and re.fullmatch(r"[A-Z][A-Za-z.'\-]+( [A-Z][A-Za-z.'\-]+){0,3}",l) is not None
                   and i>0 and (re.fullmatch(r"[A-Z]",lines[i-1]) or lines[i-1]=='' or l=='Operator' or (i+1<len(lines) and re.search(r'(Officer|Analyst|Operator|President|Director|Relations|Chairman|Treasurer|Head of)',lines[i+1]) and len(lines[i+1])<70)))
        if is_name:
            if cur: segs.append((cur,' '.join(buf)))
            cur=l;buf=[]
        elif cur and not (len(l)<70 and re.search(r'^(Chief|Analyst|Conference Operator|Senior Vice|Vice President|President|Director|Head of|Chairman|Treasurer)',l)): buf.append(l)
    if cur: segs.append((cur,' '.join(buf)))
    return segs
tot={w:0 for w in words}; per={}
for f in files:
    segs=segments(open(f,errors='ignore').read())
    comp=' '.join(txt for sp,txt in segs if sp.lower() in company).lower()
    spk=sorted(set(sp for sp,_ in segs))
    n=len(comp.split())
    row=[]
    for w,rx in words.items():
        c=len(re.findall(rx,comp))
        if c: tot[w]+=1
        row.append(c)
    per[f]=(n,row)
    print(f, 'company words:',n, 'speakers:',[s for s in spk if s.lower() in company])
print()
print(f"{'word':30s} "+' '.join(f[-18:-4][:10].rjust(10) for f in files)+'  hit-rate')
for j,w in enumerate(words):
    print(f"{w:30s} "+' '.join(str(per[f][1][j]).rjust(10) for f in files)+f"  {tot[w]}/{len(files)}")
