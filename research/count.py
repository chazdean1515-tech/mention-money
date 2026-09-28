import re,os,sys,json
WORDS={
 "TrumpRx":r"\btrump ?rx'?s?\b",
 "Tariff":r"\btariff(s|'s|s')?\b",
 "Stock Market":r"\bstock markets?'?s?\b",
 "Radical Left":r"\bradical left",
 "Oil / Gas / Gasoline":r"\b(oil|gas|gasoline)('s|es|s)?\b",
 "Nuclear":r"\bnuclear\b",
 "No Tax on Tips":r"\bno tax on tips\b",
 "Most Favored Nation":r"\bmost[- ]favored[- ]nations?\b",
 "Midterm":r"\bmidterms?'?s?\b",
 "Manufacture / Manufacturing":r"\bmanufactur(e|es|ing)\b",
 "Israel / Israeli":r"\bisrael(i|is|'s)?\b",
 "Iran / Iranian":r"\biran(ian|ians|'s)?\b",
 "Invest / Invested / Investment":r"\binvest(ed|ment|ments|s)?\b",
 "Inflation":r"\binflation\b",
 "Immigrant / Immigration":r"\bimmigra(nt|nts|tion)\b",
 "Hottest":r"\bhottest\b",
 "Healthcare":r"\bhealth ?care\b",
 "Fake News":r"\bfake news\b",
 "Crypto / Bitcoin":r"\b(crypto|bitcoin)",
 "China / Chinese":r"\b(china|chinese)\b",
 "Biden":r"\bbiden('s)?\b",
 "AI / Artificial Intelligence":r"\b(ai|a\.i\.|artificial intelligence)\b",
 "Afford / Affordable / Affordability":r"\bafford(s|able|ability)?\b",
}
def president_only(t):
    # drop reporter questions and other speakers' paragraphs (lines starting "Q." or "Name." other than The President)
    out=[];keep=True
    for para in re.split(r'\n\s*\n|\n(?=\s*(?:Q\.|The President\.|[A-Z][a-z]+ [A-Z][a-z]+\.))',t):
        s=para.strip()
        if s.startswith('Q.'): keep=False
        elif s.startswith('The President.'): keep=True
        elif re.match(r'^(Secretary|Vice President|Mr\.|Ms\.|Mrs\.|Dr\.|Senator|Representative|Administrator|Governor|Prime Minister|President [A-Z])[^.]{0,40}\.',s): keep=False
        if keep: out.append(s)
    return '\n'.join(out)
files=sys.argv[1:]
res={w:0 for w in WORDS}
for f in files:
    t=president_only(open(f).read()).lower()
    hits=[w for w,r in WORDS.items() if re.search(r,t)]
    for w in hits: res[w]+=1
print(len(files),'transcripts')
for w,n in res.items(): print(f"{w:40s} {n}/{len(files)} = {n/len(files):.0%}")
