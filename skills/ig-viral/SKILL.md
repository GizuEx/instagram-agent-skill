---
name: ig-viral
description: >-
  Go and find the reels that are actually working right now in the user's
  niche, rank them by how far each beat its own account, name the hook formula
  each one used, and turn that into a swipe file they can shoot from. Use when
  the user says "find viral videos", "what's working right now", "what are
  people posting in my niche", "reverse engineer this account", "build me a
  swipe file", "why is this reel doing numbers", or asks what to make next and
  has no evidence to answer with.
---

# ig-viral

The research skill. Everything else in this pack writes; this one goes and
looks. Run it monthly, not daily. Formulas last a season.

One tool lives in this folder and it runs:

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

## The one idea that makes this worth doing

**Raw views are not evidence.** An account with two million followers doing
400,000 views had a quiet Tuesday. An account with four thousand followers
doing 400,000 views found something, and that something is copyable.

So everything here ranks on the **outlier multiple**: views divided by that
account's own recent median. Anything above 3x is a signal. Anything below 1.5x
is that account's normal day and it teaches you nothing, no matter how big the
number looks.

Collect accounts **within about 10x of the user's own size**. A formula that
works at 2M followers often works because it is at 2M followers.

## Step 1: pick the accounts

Ask the user for 6 to 12 accounts, or propose them and get approval:

- **4 direct** - same niche, same offer, slightly ahead.
- **4 adjacent** - different niche, same audience. This is where formats get
  borrowed from before anybody in the niche has them.
- **2 to 4 outsized** - much bigger accounts, for format only, never for
  cadence or tone.

Also ask them to open their own **Saved collection**. It is the fastest and
most relevant corpus that exists and it is already filtered by their taste.

## Step 2: go and look

Use whatever browsing tool this session actually has: an in-app browser, a
browser extension connected to the user's own Chrome, or a computer-use tool.
There is no API for this and there does not need to be, because the volume is
small enough to read.

**Rules that are not negotiable:**

- **Never log into Instagram on the user's behalf and never ask for a
  password.** If a page needs a login, the user is the one who is already
  logged in. Drive their browser with them present, or ask them to paste.
- **This is reading, not scraping.** Ten accounts, a dozen reels each, at human
  speed. Automated collection at volume violates Instagram's Terms of Use and
  gets accounts action-blocked. Do not build a crawler, do not use a scraping
  service, and do not loop this in the background.
- **Copy the formula, never the video.** The hook shape, the structure, the
  length, the pattern of cuts. Not their script, not their voice, not their
  edit. Attribute every row in the swipe file to the account it came from.

**What to capture per reel**, in the creator's own words:

| field | notes |
| --- | --- |
| account | handle |
| followers | from the profile |
| median | eyeball the last 12 reels and take the middle view count |
| views | this reel |
| hook | the first line, spoken or on screen, verbatim including bad grammar |
| on-screen | the first text card, if different |
| length | seconds |
| cta | what they asked for at the end |

Median is the important one. Without it you are back to ranking by follower
count, which is the thing this skill exists to stop.

**When Instagram will not show you enough:** the same hook grammar runs on
YouTube Shorts, where view counts and transcripts are public and no login is
involved. It is a legitimate second corpus, and the spoken hook is easier to
get:

```bash
# view counts for a channel's shorts
python3 -m yt_dlp --flat-playlist --playlist-end 40 -J \
  "https://www.youtube.com/@HANDLE/shorts" > channel.json

# the spoken first line of one short, from its auto-captions
python3 -m yt_dlp --skip-download --write-auto-subs --sub-langs "en.*" \
  --sub-format json3 -o hook "https://www.youtube.com/watch?v=VIDEO_ID"
```

Take every caption word with a timestamp under 3.0 seconds. That is the hook,
as said, not as written.

## Step 3: rank it

Fill a tab-separated file with a header row and run the script:

```
account	followers	median	views	hook
@someone	48000	11000	412000	nobody tells you your first 30 reels are supposed to flop
```

```bash
python3 swipe.py captured.tsv --out ~/.claude/instagram/swipe.md
```

It computes the outlier multiple, names the hook formula using the same 26
formulas `/ig-reel` writes from, scores each hook with `hookscore.py`, and
prints what separates the top third from the bottom third.

## Step 4: say what it means, carefully

Report three things and no more:

1. **Which formulas over-index** in the top third, with counts. Two formulas
   appearing four times each across six accounts is a finding. One appearing
   twice is not.
2. **What the top third have in common structurally** that the bottom third do
   not: hook length, whether the payoff is visual, whether the first frame
   moves, where the ask is.
3. **The unclassified rows.** Every hook the classifier could not name is
   either noise or a formula that is not in `hooks.json` yet. Read them by
   hand. This is the most valuable column in the output and it is the reason
   the script prints the count.

Then state the sample size and the confidence in plain words. Forty reels
across six accounts supports a claim. Twelve does not, and saying so is the
difference between research and horoscopes.

## Step 5: turn it into something to shoot

For the top three formulas, write **the user's version**: their own story,
their own number, in the shape that is working. Hand each one to `/ig-reel`
with the formula id already chosen.

Never hand back "make a reel like this one". Hand back a hook line they could
say tomorrow.

## Output

```
SWIPE  ·  38 reels  ·  7 accounts  ·  baseline: account median

OUTLIERS (above 3x)
  38.4x  hook 86  #3  Nobody Tells You   @acct_a    412,000  (median 10,700)
  11.2x  hook 79  #9  The Steal          @acct_c    180,000  (median 16,100)
  ...

WHAT IS OVER-INDEXING
  #3 Nobody Tells You   x5 in the top third, 0 in the bottom
  #2 Negative Command   x4
  median hook length    8 words up top, 19 at the bottom

UNCLASSIFIED (6)
  Two of these are the same shape and it is not in hooks.json: a hook that
  opens on someone else's comment read out loud. Worth adding.

YOUR VERSION
  #3  "Nobody tells you the first 20 proposals are supposed to lose."
  ...
```

Write the swipe file to `~/.claude/instagram/swipe.md`. `/ig-reel` and
`/ig-plan` both read it, which is the point: after this runs once, the rest of
the pack is working from the user's own evidence instead of from defaults.

Nothing is posted, followed, liked or messaged by this skill. It reads.
 

## Dancing Flamme – Brand Customization for Viral Research

These instructions customize the ig-viral skill for Dancing Flamme. They complement the original research methodology and must not replace its technical rules.

### 1. Brand identity

- Brand: Dancing Flamme – The Feeling Good Movement Association.
- Founder: Giselle Estupinan.
- Instagram: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).

The objective is to build an authentic local community and attract participants to intuitive dance workshops.

### 2. Research niche

Prioritize Instagram Reels related to:

- Intuitive dance and free movement.
- Dance therapy and body expression.
- Emotional expression through movement.
- Reconnection with the body.
- Women's well-being and self-expression.
- Creative movement and personal development.
- Dance without choreography or performance expectations.
- Community-based dance workshops.

### 3. Giselle's personal identity

When identifying content opportunities, consider Giselle's personal and artistic background:

- Colombian roots, where dance is a cultural language of celebration, emotion and connection.
- Classical ballet training from an early age.
- Performances in The Nutcracker and Paquita at Teatro Colón in Bogotá.
- Personal transformation and rediscovery of dance following her cancer experience.
- Dance Therapy training at ARTEC in 2023.
- Experience facilitating intuitive dance workshops in Chantilly, including involvement with Les Rubans de la Vie (ERC) and the Centre Culturel de Chantilly.

Use these elements to identify authentic storytelling opportunities. Never turn personal experiences or cancer into sensationalist marketing hooks.

### 4. Viral content adaptation

Do not simply copy viral Reels.

For every relevant trend:

- Identify the original hook and why it works.
- Understand the emotional trigger or audience need.
- Identify the visual structure and storytelling technique.
- Adapt the concept to intuitive dance.
- Propose an original version that Giselle can realistically film.
- Preserve the welcoming, non-judgmental philosophy of Dancing Flamme.

Never sacrifice authenticity for views.

### 5. Local audience priority

Prioritize content that can attract people living around:

- Gouvieux.
- Chantilly.
- Senlis.
- Lamorlaye.
- Compiègne.
- Nearby towns in Oise.

Favor content that encourages local discovery, workshop participation, community engagement and returning participants.

### 6. Storytelling and tone

Always follow voice.md when developing personal storytelling ideas.

Content must feel:

- Warm and authentic.
- Human and emotionally engaging.
- Inspiring without being overly spiritual.
- Accessible to people with no dance experience.
- Personal without becoming exclusively autobiographical.

Write in Giselle's first-person voice when appropriate.

### 7. Research and recommendations

For every research session:

- Distinguish genuine performance outliers from simply popular accounts.
- Prioritize relevance to Dancing Flamme over raw view counts.
- Identify trends that can be adapted without expensive equipment or complex production.
- Include a mix of educational, emotional, personal and promotional content.
- Explain why each recommendation is relevant to the brand.

Do not invent performance metrics, engagement figures or viral trends.

### 8. Final objective

The goal is not to make Dancing Flamme another viral dance account.

The goal is to use effective Instagram formats to help more people discover intuitive dance, understand its value, connect with Giselle's story and eventually participate in local workshops.
