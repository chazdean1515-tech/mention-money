"""Turn a short research reason into a grammatical note.

Uses only the words already in the reason. It does not add counts, prices, or events.
"""
import re

_TRAILING = (
    (re.compile(r"\bFair to slightly rich\.?$"), "The price looks fair to slightly rich."),
    (re.compile(r"\bFair-to-slightly rich\.?$"), "The price looks fair to slightly rich."),
    (re.compile(r"\bFair to slightly cheap\.?$"), "The price looks fair to slightly cheap."),
    (re.compile(r"\bFair-to-slight cheap\.?$"), "The price looks fair to slightly cheap."),
    (re.compile(r"\bFair-to-slight rich\.?$"), "The price looks fair to slightly rich."),
    (re.compile(r"(?<![A-Za-z])Fair\.$"), "The price looks fair."),
    (re.compile(r"\bWide market\.$"), "The market is wide, so this read is low confidence."),
    (re.compile(r"\bSpread too wide to call\.$"), "The spread is too wide to call."),
    (re.compile(r"\bSpread too wide\.$"), "The spread is too wide to call."),
)

_VERBS = (
    " is ", " are ", " was ", " were ", " be ", " hit ", " hits ", " looks ", " look ",
    " has ", " have ", " had ", " needs ", " need ", " counts ", " count ", " says ",
    " said ", " makes ", " make ", " comes ", " come ", " shows ", " show ", " fits ",
    " fit ", " sits ", " sit ", " pays ", " pay ", " leaves ", " left ", " went ",
    " goes ", " got ", " gets ", " missed ", " miss ", " cleared ", " includes ",
    " include ", " depends ", " treated ", " treat ", " can ", " may ", " might ",
    " should ", " would ", " will ", " do ", " does ", " did ", " named ", " accept ",
    " requires ", " require ", " used ", " uses ", " using ",
)


def compose_note(reason):
    t = (reason or "").strip().replace("TrumpRX", "TrumpRx")
    t = re.sub(r"[ \t]+", " ", t)
    if not t:
        return ""
    if t[-1] not in ".!?":
        t += "."
    for pat, repl in _TRAILING:
        updated, n = pat.subn(repl, t)
        if n:
            t = updated
            break
    if len(t) >= 180:
        return t
    # Judge the whole note. A leading fragment ("No corpus.") must not hide a
    # full sentence that follows it.
    low = f" {t.lower()} "
    has_verb = any(v in low for v in _VERBS)
    if not has_verb and len(t) < 180:
        if re.match(r"^\d", t):
            return "Count: " + t
        return "Note on this contract: " + t
    return t
