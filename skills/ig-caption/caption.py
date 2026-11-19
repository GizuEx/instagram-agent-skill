#!/usr/bin/env python3
"""
caption.py - lint an Instagram caption and show exactly what the feed shows
before the "... more".

Instagram gives a caption about 125 characters in the feed and hides the rest
behind a tap. Almost every caption that fails, fails there: the hook is in
sentence three, or the first line is a greeting, or the whole thing opens on a
hashtag. This prints the visible window as a box so you can read it the way a
scrolling stranger does, then checks the eight things that are worth checking.

The 125-character cut is an approximation. The real number moves with the
device, the font size and where your line breaks fall, which is exactly why
you want a margin rather than a caption engineered to end at 125. Change it
with --truncate if you want to test a tighter one.

French mode (--lang fr, or detected automatically with --lang auto, the
default): the English behaviour below is untouched, and for French captions the
script uses its own rules for the call to action (comment, DM, share, save,
follow, tag, join, link, swipe, question), for accented hashtags, for French
links and for the "concrete hook" check (numbers only). See the French section further down.

Usage
  python3 caption.py caption.txt
  python3 caption.py caption.txt --keywords "proposal software,client contract"
  pbpaste | python3 caption.py -
  python3 caption.py caption.txt --json
  python3 caption.py caption.txt --lang fr
"""

import argparse
import json
import re
import sys
import textwrap

LIMIT = 2200             # Instagram's hard caption limit.
TRUNCATE = 125           # Roughly where the feed cuts to "... more".
HASHTAG_LIMIT = 5        # Instagram's cap per post or reel since 18 Dec 2025,
                         # down from 30. Announced by the @Creators account:
                         # "using fewer (up to 5) more targeted hashtags,
                         # rather than many generic ones, can improve both your
                         # content's performance and people's experience".

HASHTAG_RE = re.compile(r"(?:^|\s)(#[A-Za-z0-9_]+)")
MENTION_RE = re.compile(r"(?:^|\s)(@[A-Za-z0-9_.]+)")
LINK_RE = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:com|co|io|net|org|ai|app)/\S*",
                     re.IGNORECASE)
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿←-⇿️]")
CONCRETE_RE = re.compile(r"\$\s?\d|\b\d[\d,.]*\b|(?<!^)\b[A-Z][a-z]{2,}\b", re.MULTILINE)

ASKS = [
    (re.compile(r"(?i)\bcomment (?:the word |\")?[A-Z0-9]{2,}\b"), "comment a keyword"),
    (re.compile(r"(?i)\b(?:dm|message) me\b"), "DM me"),
    (re.compile(r"(?i)\bsave (?:this|it)\b"), "save this"),
    (re.compile(r"(?i)\bshare (?:this|it)\b"), "share this"),
    (re.compile(r"(?i)\bfollow (?:me|for)\b"), "follow"),
    (re.compile(r"(?i)\blink in (?:my )?bio\b"), "link in bio"),
    (re.compile(r"(?i)\b(?:swipe|tap) (?:through|left|right|for|to)\b"), "swipe or tap"),
    (re.compile(r"(?i)\btell me\b|\bwhat would you\b|\bwhich one\b"), "answer a question"),
]

FILLER_TAGS = {"#viral", "#fyp", "#explore", "#explorepage", "#foryou", "#foryoupage",
               "#trending", "#instagood", "#love", "#follow", "#like4like", "#reels",
               "#reelsinstagram", "#viralreels", "#instadaily"}


# ---------------------------------------------------------------- French mode
# Used only when the caption is French (--lang fr, or detected). English captions
# never go through any of this.

HASHTAG_RE_FR = re.compile(r"(?:^|\s)(#\w+)")
LINK_RE_FR = re.compile(r"https?://\S+|\bwww\.\S+|\b[a-z0-9-]+\.(?:com|co|io|net|org|ai|app|fr|eu)/\S*",
                        re.IGNORECASE)
FILLER_TAGS_FR = {"#pourtoi"}
NUMBER_FR_RE = re.compile(r"\d+(?:[.,]\d+)*")

# Only words that are not also common Spanish, Italian or Catalan words, so that a
# Spanish caption keeps the original (English) behaviour.
FR_WORDS = {"les", "des", "une", "est", "pas", "pour", "vous", "je", "qui", "dans",
            "avec", "cette", "sur", "aux", "du", "mon", "mes", "tes", "ton", "nous",
            "ces", "elle", "très", "et"}
EN_WORDS = {"the", "and", "is", "are", "you", "your", "for", "with", "this", "that", "of",
            "to", "it", "my", "we", "was", "have", "not", "be", "will"}
FR_ELISION_RE = re.compile(r"\b(?:c|j|l|d|n|qu|s|m|t)['’]\w", re.IGNORECASE)
CLEAN_FOR_LANG_RE = re.compile(r"https?://\S+|\bwww\.\S+|(?:^|\s)[#@]\S+")


def detect_lang(text):
    """'fr' only when the text is clearly French, otherwise 'en' (the old behaviour).
    A hashtag-only or very short caption stays 'en': force it with --lang fr."""
    body = CLEAN_FOR_LANG_RE.sub(" ", text).lower()
    words = re.findall(r"[a-zàâçéèêëîïôûùüÿœæ]+", body)
    fr = sum(1 for w in words if w in FR_WORDS) + len(FR_ELISION_RE.findall(body))
    en = sum(1 for w in words if w in EN_WORDS)
    return "fr" if fr >= 2 and fr > en else "en"


# One ask per clause at most, in this order. Patterns are anchored on the
# imperative at the start of a clause so that "un moment de partage" or "je
# commente rarement" are not read as calls to action.
_LEAD_RE = re.compile(
    r"^(?:(?:et|puis|ou|alors|donc|sinon|mais|aussi|si tu veux|si vous voulez"
    r"|n['’]hésite(?:z)? pas à|pense(?:z)? à|tu peux|vous pouvez)\s+)+", re.IGNORECASE)
# After a modal lead ("n'hésite pas à partager ce Reel") the verb is an infinitive.
# It is only turned into the imperative in that case: a bare "Partager ce moment,
# c'est un plaisir" is not a call to action.
_MODAL_RE = re.compile(r"(?i)n['’]hésite(?:z)? pas à|pense(?:z)? à|tu peux|vous pouvez")
_INFINITIVES = {"partager": "partage", "enregistrer": "enregistre", "sauvegarder": "sauvegarde",
                "commenter": "commente", "glisser": "glisse", "identifier": "identifie",
                "rejoindre": "rejoins", "réserver": "réserve", "écrire": "écris",
                "envoyer": "envoie", "raconter": "raconte", "dire": "dis"}
_VERB = (r"(?:raconte|racontez|dis|dites|écris|écrivez|laisse|laissez|réponds|répondez|"
         r"partage|partagez|dépose|déposez|commente|commentez|poste|postez)")
_FR_ASKS = [
    ("comment a keyword", re.compile(
        r"^(?i:commente[zs]?)\s+(?:(?i:le mot|le code)\s+)?[«\"“]?\s*[A-ZÀÂÉÈÊÎÔÛÇ0-9]{2,}\b")),
    ("comment", re.compile(
        r"(?i)^commente[zs]?(?:\s|$)|^" + _VERB + r"\b.*\b(?:en|dans les?|sous (?:ce|cette|ma|mon))\s+commentaires?\b")),
    ("DM me", re.compile(
        r"(?i)^(?:écris|écrivez|envoie|envoyez)[- ]moi\b.*\b(?:message|mot|dm|mp|en privé|par message)\b"
        r"|^(?:dm|mp)[- ]moi\b|^contacte[zs]?[- ]moi\b"
        r"|^(?:nous|me|m['’])\s*(?:écrire|contacter|envoyer)\b.*\b(?:message|dm|mp|en privé|par message)\b"
        r"|^(?:me|m['’])\s*(?:écrire|contacter)\b"
        r"|^" + _VERB + r"\b.*\b(?:en|par)\s+(?:message privé|dm|mp)\b")),
    ("save this", re.compile(
        r"(?i)^(?:enregistre|enregistrez|sauvegarde|sauvegardez)[zs]?\b"
        r"|^(?:garde|gardez)\s+(?:ce|cette)\s+(?:post|publication|carrousel|reel)\b")),
    ("share this", re.compile(
        r"(?i)^partage[zs]?(?:[- ](?:le|la|les|ça)\b|\s+(?:ce|cette|ça|ceci|le|la|avec|à)\b)"
        r"|^envoie[zs]?[- ](?:le|la|les|ça)\s+à\b|^envoie[zs]?\s+(?:ce|cette)\b.*\bà\b")),
    ("tag someone", re.compile(r"(?i)^(?:identifie|identifiez|tague|taguez|mentionne|mentionnez)\b")),
    ("follow", re.compile(
        r"(?i)^(?:abonne[- ]toi|abonnez[- ]vous|suis[- ]moi|suivez[- ]moi|suis le compte|suivez le compte)\b")),
    ("join or register", re.compile(
        r"(?i)^(?:rejoins|rejoignez|viens|venez|inscris[- ]toi|inscrivez[- ]vous)\b"
        r"|^(?:réserve|réservez)\s+(?:ta|ton|tes|votre|vos|une|la|les|dès|maintenant)\b")),
    ("link in bio", re.compile(r"(?i)\blien (?:dans|en|de) (?:ma |la )?bio\b|\bdans ma bio\b")),
    ("swipe or tap", re.compile(
        r"(?i)^(?:glisse|glissez|fais défiler|faites défiler|swipe|swipez|balaie|balayez)\b")),
    ("answer a question", re.compile(
        r"(?i)^(?:dis|dites|raconte|racontez)[- ]moi\b|^et (?:toi|vous)\b|^qu['’]en penses[- ](?:tu|vous)\b")),
]


def fr_asks(text):
    """Distinct calls to action in a French caption, in order of appearance."""
    flat = text.replace("‑", "-")
    found = []
    for clause in re.split(r"[.!?…;:,\n]+", flat):
        c = re.sub(r"^[^\wÀ-ÿ«\"“]+", "", clause.strip())
        modal = _MODAL_RE.search(c[: _LEAD_RE.match(c).end()]) if _LEAD_RE.match(c) else None
        c = _LEAD_RE.sub("", c)
        if not c:
            continue
        if modal:
            first, _, rest = c.partition(" ")
            c = (_INFINITIVES.get(first.lower(), first) + " " + rest).strip()
        for name, pattern in _FR_ASKS:
            if pattern.search(c):
                if name not in found:
                    found.append(name)
                break
    return found


def fr_concrete(window):
    """Numbers in the window. Names are deliberately not counted in French: without a
    dictionary there is no reliable way to tell a proper noun from an ordinary word
    that happens to be capitalised ("Découvre : Danser librement", « Danse intuitive »)."""
    return NUMBER_FR_RE.findall(window)


def visible_window(text, cut):
    """What the feed shows. Instagram cuts mid-word, so this does too."""
    flat = text.strip()
    return flat if len(flat) <= cut else flat[:cut]


def render_box(window, truncated, out=sys.stdout, width=52):
    print("\n  WHAT THE FEED SHOWS", file=out)
    print("  +" + "-" * (width + 2) + "+", file=out)
    lines = []
    for raw in window.split("\n"):
        lines.extend(textwrap.wrap(raw, width) or [""])
    for line in lines[:8]:
        print(f"  | {line:<{width}} |", file=out)
    tail = "... more" if truncated else "(whole caption fits)"
    print("  +" + "-" * (width + 2 - len(tail) - 2) + f" {tail} " + "+", file=out)


def analyse(text, cut=TRUNCATE, keywords=None, lang="en"):
    fr = (lang == "fr")
    text = text.rstrip()
    stripped = text.strip()
    chars = len(stripped)
    lines = [l for l in stripped.split("\n")]
    first_line = lines[0].strip() if lines else ""
    tags = (HASHTAG_RE_FR if fr else HASHTAG_RE).findall(stripped)
    mentions = MENTION_RE.findall(stripped)
    links = (LINK_RE_FR if fr else LINK_RE).findall(stripped)
    emoji = EMOJI_RE.findall(stripped)
    window = visible_window(stripped, cut)
    truncated = chars > cut
    asks = fr_asks(stripped) if fr else [name for pattern, name in ASKS if pattern.search(stripped)]
    filler_set = (FILLER_TAGS | FILLER_TAGS_FR) if fr else FILLER_TAGS
    filler = [t for t in tags if t.lower() in filler_set]
    keywords = [k.strip() for k in (keywords or []) if k.strip()]

    checks = []

    def add(name, status, detail):
        checks.append({"check": name, "status": status, "detail": detail})

    add("LENGTH", "FAIL" if chars > LIMIT else "PASS",
        f"{chars} / {LIMIT} characters" + (f", {chars - LIMIT} over the limit"
                                           if chars > LIMIT else ""))

    if not first_line:
        add("FIRST LINE", "FAIL", "the caption opens on a blank line")
    elif first_line.startswith("#") or first_line.startswith("@"):
        add("FIRST LINE", "FAIL",
            "opens on a hashtag or a mention, which is the one position worth a sentence")
    elif len(first_line) > cut:
        add("FIRST LINE", "WARN",
            f"{len(first_line)} characters, so it gets cut at {cut} mid-thought. "
            "Fine if the cut is a cliffhanger, bad if it is a subordinate clause")
    else:
        add("FIRST LINE", "PASS", f"{len(first_line)} characters, lands whole")

    if fr:
        concrete = fr_concrete(window)
        add("HOOK IS CONCRETE", "PASS" if concrete else "INFO",
            f"{len(concrete)} number(s) in the visible window (names are not counted in French)"
            + ("" if concrete else ". Not a problem for a sincere question or "
                                   "an invitation; never add a figure just to fill it"))
    else:
        add("HOOK IS CONCRETE", "PASS" if CONCRETE_RE.search(window) else "WARN",
            f"{len(CONCRETE_RE.findall(window))} number(s) or name(s) in the visible window"
            + ("" if CONCRETE_RE.search(window) else " - nothing checkable before the tap"))

    if len(tags) > HASHTAG_LIMIT:
        add("HASHTAGS", "FAIL", f"{len(tags)} tags, over Instagram's cap of {HASHTAG_LIMIT}. "
                                "Tags past the fifth do not count and the block reads as old")
    elif len(tags) == HASHTAG_LIMIT and filler:
        add("HASHTAGS", "WARN", f"{len(tags)} tags, at the cap, and "
                                f"{len(filler)} of them generic. Spend the five on topics")
    elif filler:
        add("HASHTAGS", "WARN", f"{len(tags)} tags, {len(filler)} of them generic "
                                f"({', '.join(filler[:3])}). Those describe nothing")
    else:
        add("HASHTAGS", "PASS", f"{len(tags)} tag(s)" + (f": {' '.join(tags)}" if tags else ""))

    if not tags:
        add("TAG PLACEMENT", "PASS", "no tags to place")
    elif any(re.search(r"(?:^|\s)" + re.escape(t) + r"\b", window) for t in tags):
        add("TAG PLACEMENT", "WARN", "a hashtag is inside the visible window, "
                                     "spending feed space on a label")
    else:
        add("TAG PLACEMENT", "PASS", "tags are below the fold")

    add("LINKS", "WARN" if links else "PASS",
        f"{len(links)} link(s) in the caption, and captions are not clickable. "
        f"Move it to the bio or the DM" if links else "no dead links in the body")

    if len(asks) == 1:
        add("ONE ASK", "PASS", f"one call to action: {asks[0]}")
    elif not asks:
        add("ONE ASK", "WARN", "no call to action. Decide what this post is for"
            + (" (a post without any ask can be a deliberate choice)" if fr else ""))
    else:
        add("ONE ASK", "WARN", f"{len(asks)} asks ({', '.join(asks)}). "
                               "Two asks is the same as none")

    density = len(emoji) * 100 / max(chars, 1)
    add("EMOJI", "WARN" if density > 4 else "PASS",
        f"{len(emoji)} emoji, {density:.1f} per 100 characters"
        + (" - reads as decoration" if density > 4 else ""))

    if keywords:
        low = stripped.lower()
        found = [k for k in keywords if k.lower() in low]
        missing = [k for k in keywords if k.lower() not in low]
        in_window = [k for k in found if k.lower() in window.lower()]
        status = "PASS" if not missing else ("WARN" if found else "FAIL")
        add("SEARCH TERMS", status,
            f"{len(found)}/{len(keywords)} present"
            + (f", {len(in_window)} in the visible window" if found else "")
            + (f". Missing: {', '.join(missing)}" if missing else ""))

    fails = sum(1 for c in checks if c["status"] == "FAIL")
    warns = sum(1 for c in checks if c["status"] == "WARN")
    verdict = "FIX" if fails else ("REVIEW" if warns else "READY")

    result = {
        "characters": chars, "limit": LIMIT, "truncate_at": cut,
        "visible": window, "truncated": truncated,
        "first_line_chars": len(first_line),
        "hashtags": tags, "mentions": mentions, "links": links,
        "emoji": len(emoji), "asks": asks,
        "checks": checks, "verdict": verdict,
    }
    if fr:
        result["lang"] = "fr"
    return result


def render(a, out=sys.stdout):
    head = (f"CAPTION LINT  ·  {a['characters']} / {a['limit']} chars  ·  "
            f"{len(a['hashtags'])} hashtags  ·  {len(a['asks'])} ask(s)")
    print("\n" + head, file=out)
    print("=" * max(len(head), 62), file=out)
    if a.get("lang") == "fr":
        print("  LANGUAGE  fr (French rules for asks, hashtags, links)", file=out)
    render_box(a["visible"], a["truncated"], out=out)
    print("", file=out)
    for c in a["checks"]:
        print(f"  {c['status']:<5} {c['check']:<17} {c['detail']}", file=out)
    print("-" * max(len(head), 62), file=out)
    print(f"  VERDICT  {a['verdict']}\n", file=out)


def main():
    ap = argparse.ArgumentParser(description="Lint an Instagram caption.")
    ap.add_argument("input", nargs="?", default="-", help="caption file, or - for stdin")
    ap.add_argument("--truncate", type=int, default=TRUNCATE,
                    help=f"characters shown before '... more' (default {TRUNCATE})")
    ap.add_argument("--keywords", default="", help="comma-separated terms you want to be found for")
    ap.add_argument("--lang", choices=["auto", "en", "fr"], default="auto",
                    help="auto (default) switches to the French rules only for a clearly "
                         "French caption; en keeps the original behaviour")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    lang = detect_lang(raw) if args.lang == "auto" else args.lang
    a = analyse(raw, cut=args.truncate, keywords=args.keywords.split(","), lang=lang)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    sys.exit(0 if a["verdict"] == "READY" else 1)


if __name__ == "__main__":
    main()