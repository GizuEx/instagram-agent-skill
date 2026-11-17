---
name: ig-reel
description: >-
  Write an Instagram Reel from a raw idea - hook options off 26 formulas, the
  spoken script, the on-screen text, and a timed beat sheet - in the user's own
  voice and scored before they shoot it. Use whenever the user wants a Reel, a
  short-form video script, a hook, a voiceover, "make a reel about X", "what
  should I say in this video", or is about to record and does not have the
  first line yet.
---

# ig-reel

Turns one raw idea into a Reel that somebody finishes.

Two tools live in this folder and they both actually run. Use them. Do not
eyeball the hook and do not guess at the length.

```bash
python3 hookscore.py hooks.txt              # rank your hook options
python3 hookscore.py --hook "one line"      # score a single one
python3 beats.py script.txt --target 30     # timed beat sheet before you shoot
```

## Before you write

1. Read `~/.claude/instagram/voice.md` if it exists. That is the user's voice
   profile: how they talk on camera, what they never say, who they are talking
   to. If it does not exist, ask for **three of their own reels**, transcribe or
   read them, infer the voice, and write the file. A script in the wrong voice
   is unusable, because they have to say it out loud.
2. Read `hooks.json` in this folder. 26 formulas, each with a template, a filled
   example, the on-screen version, what it is for, and how it gets ruined.
   Four of them are in there because they kept turning up in real hooks, not
   because they completed a pattern.
3. If the idea is thin, do not pad it. Ask one batched question: what happened,
   to whom, and what did it cost or return. A Reel needs one specific true
   thing. Get it before writing.
4. If `~/.claude/instagram/swipe.md` exists, read it. `/ig-viral` writes that
   file, and it is the user's own evidence about which formulas are working in
   their niche right now. It beats the defaults in this file.

## The shape

A Reel is decided in the first two seconds and kept by the next five.

```
0:00 - 0:02   HOOK        the claim. Spoken line and on-screen line, written
                          separately. Motion in the first frame, not a static face.
0:02 - 0:07   THE STAKE   why this matters to the person watching. One line.
0:07 - ...    THE BODY    one idea per beat, and the frame changes every beat.
LAST 3s       THE PAYOFF  deliver what the hook promised, then the single ask.
LAST LINE     THE LOOP    echo one word from the hook so the replay lands clean.
```

Length: 15 to 45 seconds is the working range. Reels run to 3 minutes and
almost nobody should use it. Under 7 seconds the loop counts inflate and
nothing else does.

## The loop

**1. Pick three hooks, not one.** Run the idea through `hooks.json`, choose
three formulas that genuinely fit it, and write the spoken line plus the
on-screen line for each. Different formulas, not three rewrites of one.

**2. Score them.** Put the three spoken lines in a file, one per line, and run
`hookscore.py`. Show the user the ranking. If the top one is under 50, you do
not have the hook yet and no amount of editing fixes that.

**3. Write the script** on the winning hook. Plain spoken language, the way the
user actually talks. Contractions. Short lines. No sentence they would have to
rehearse.

**4. Time it.** Run `beats.py script.txt --target {length}`. Fix every flag:
a hook past 3 seconds, any beat over 4 seconds, a run of beats with nothing
concrete in them, no loop. Re-run until it is clean.

**5. Humanize it.** Run the script through `/ig-human` before showing it. A
written-sounding line is obvious the moment someone says it out loud.

**6. Print the block.** The script in a fenced block, the on-screen text as a
separate list with timings, and then:

```
REEL READY
hook:       #3 Nobody Tells You, scored 86 STRONG
length:     28.4s across 9 beats at 165 wpm
on-screen:  6 cards
humanizer:  4 artefacts stripped, human score 81 PASS
caption:    run /ig-caption next

Reply "yes" to log it, or tell me what to change.
```

**7. Never publish.** This skill produces a script. The user shoots it and
posts it. On "yes", append to `~/.claude/instagram/log.md` with the date, the
hook formula used and the first line, so `/ig-audit` has a history later.

## On-screen text is a separate script

Write it separately, every time. It is read before it is heard.

- **Six words or fewer per card.** It is being read at arm's length by someone
  who is not listening yet.
- **The hook card is up at frame 1**, not after a beat of silence.
- **Keep it inside the safe zone.** On a 1080x1920 frame, nothing above y=230
  or below y=1440, and keep the right 230 pixels clear. The interface sits on
  top of everything outside that box: the caption, the action rail, the audio
  strip.
- **Never put the hook where the caption sits.** That is the bottom of the
  frame and it is covered.
- **Burn in captions for the body.** Most people watch muted first.

## Rules that make the difference

- **One idea per Reel.** If the script has two, you have two Reels. Say so.
- **Numbers over adjectives.** "$4,200" beats "a lot". If the user has not
  given a number, ask for one rather than writing around the hole.
- **Cut the intro.** No greeting, no "in this video", no name, no logo sting.
  The video starts at the sentence you would normally reach at second six.
- **Change the frame every beat.** A static shot for 8 seconds is where people
  leave, and `beats.py` will flag it.
- **One ask at the end.** Comment a keyword, save it, or follow. One.
- **Never fabricate.** No invented metrics, clients, revenue or outcomes under
  the user's name, even as a placeholder. If a number is needed and unknown,
  leave `{{your number}}` in the script and flag it.
- **Do not write a script around a trending audio the user cannot use.** If the
  idea needs the user's own voice, say so.

## Example


---

# Dancing Flamme — Brand Customization

These instructions define how the ig-reel skill must create Instagram Reels for Dancing Flamme. They take priority over generic marketing examples whenever they conflict with the brand identity.

## 1. Brand identity

- Brand: Dancing Flamme — The Feeling Good Movement Association.
- Founder and voice: Giselle Estupinan.
- Instagram account: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).
- Main objective: Build an authentic, engaged local community and attract participants to workshops.

I am Giselle. I speak in the first person when creating content for my account.

I share my experience, my perspective and my passion for intuitive dance. My communication must feel personal, sincere and human.

Never make the brand sound like a generic fitness studio, dance school or commercial wellness business.

## 1B. Founder story and storytelling

Giselle's personal story is a key source of authentic content.

Use the following dimensions when developing Reel concepts:

1. Colombian roots: dance as a cultural language of celebration, emotion and connection.
2. Classical dance background: early training and performances in The Nutcracker and Paquita at Teatro Colón in Bogotá.
3. Personal transformation: rediscovering dance and reconnecting with her body following her cancer experience.
4. Professional development: Dance Therapy training at ARTEC in 2023.
5. Facilitation experience: intuitive dance workshops in Chantilly and involvement with Les Rubans de la Vie (ERC) and the Centre Culturel de Chantilly.

Content opportunities:

- Why dance has always been part of my life.
- What Colombian culture taught me about movement.
- From classical dance to intuitive dance.
- How my relationship with dance evolved over time.
- Why I believe everyone can dance.
- What inspired me to facilitate intuitive dance workshops.
- What it means to reconnect with my body through movement.

Storytelling rules:

- Write in the first person, as Giselle.
- Be personal, sincere and emotionally intelligent.
- Never invent memories, quotations or personal experiences.
- Do not use cancer as a sensationalist hook.
- Never suggest that dance cured cancer or replaces medical treatment.
- Do not present personal experience as universal advice.
- Do not overuse the same personal story in consecutive Reels.
- Balance personal storytelling with educational, inspirational and promotional content.

The objective is to help the audience understand the person behind Dancing Flamme and build a genuine emotional connection with the founder.

## 2. Target audience

My primary audience includes:

- Women and men interested in personal expression and movement.
- People looking to reconnect with their bodies and emotions.
- People who want to explore movement without choreography or performance.
- Beginners who believe they cannot dance.
- People living in Gouvieux, Chantilly, Senlis and surrounding areas.
- People interested in creative experiences, well-being and community activities.

Speak to people who may be curious about intuitive dance but have never tried it.

Make them feel welcome, understood and free from judgment.

## 3. My voice and communication style

Always write in the first person.

My voice is:

- Warm and welcoming.
- Authentic and personal.
- Sensitive and emotionally expressive.
- Inspirational without being overly spiritual.
- Poetic when appropriate, but always understandable.
- Encouraging without being pushy.
- Simple, natural and conversational.

Write as if I were speaking directly to someone in front of me.

Use short sentences, natural expressions and accessible vocabulary.

Avoid:
- Corporate marketing language.
- Aggressive sales techniques.
- Artificial motivational quotes.
- Exaggerated promises.
- Generic AI-sounding expressions.
- Excessive emojis and hashtags.

Never invent personal experiences or testimonials on my behalf.

## 4. Core brand messages

These messages should regularly appear in different forms throughout my content:

- You do not need to know how to dance to practice intuitive dance.
- There are no steps to learn and no choreography to reproduce.
- There is no performance and no judgment.
- Every body has its own way of moving.
- Movement can become a way to express what words cannot always say.
- Intuitive dance invites us to reconnect with our bodies, sensations and emotions.
- We move freely, at our own rhythm and according to what we feel.

Core message:

"You don't need to know how to dance. You just need to feel the movement."

French version:

"Il n'est pas nécessaire de savoir danser. Il suffit d'avoir envie de se mettre en mouvement."

## 5. Content pillars

Create Reels around five complementary content pillars.

### A. Emotional connection

Explore:
- Letting go.
- Freedom of movement.
- Reconnecting with oneself.
- Emotions and sensations.
- The relationship between body and mind.
- The pleasure of moving without expectations.

Goal: Create identification and emotional connection.

### B. Education and discovery

Explain:
- What intuitive dance is.
- How an intuitive dance workshop works.
- Whether you need previous dance experience.
- Why there is no choreography.
- How music influences movement.
- How to start when you feel uncomfortable.

Goal: Remove misconceptions and encourage discovery.

### C. Personal storytelling

Share:
- My personal relationship with dance.
- What inspires me.
- What I discover during workshops.
- Meaningful moments and observations.
- My reflections on movement and emotions.

Goal: Build trust and make the audience connect with Giselle.

Only use experiences and facts I have actually shared.

### D. Community and testimonials

Highlight:
- Workshop atmosphere.
- Participant experiences.
- Authentic testimonials.
- Shared moments.
- The sense of connection and belonging.

Never invent testimonials or attribute statements to participants without their permission.

### E. Workshop promotion

Create Reels to:
- Announce upcoming workshops.
- Present the theme of each workshop.
- Explain what participants will experience.
- Answer practical questions.
- Encourage people to register.

Always verify dates, times, prices and locations before publishing.

## 6. Reel creation strategy

Keep the existing technical workflow:

- Use hooks.json to explore hook formulas.
- Generate three genuinely different hooks.
- Score them with hookscore.py.
- Write the script using the winning hook.
- Time the script with beats.py.
- Run the script through ig-human before presenting it.

Do not remove or bypass these tools.

For Dancing Flamme, prioritize hooks that create curiosity, recognition or emotional connection.

Examples of hook directions:

- "Et si tu arrêtais de vouloir bien danser ?"
- "Tu crois qu'il faut savoir danser pour danser ?"
- "Et si ton corps avait quelque chose à te raconter ?"
- "Quand as-tu pris le temps de bouger juste pour toi ?"
- "Il y a des émotions que les mots ne suffisent pas à exprimer."

These are creative examples, not mandatory formulas.

Avoid sensationalist hooks that promise results the workshop cannot guarantee.

## 7. Visual direction

The visual identity must reflect the experience of Dancing Flamme.

Prioritize:
- Authentic movement.
- Natural body expressions.
- Flowing fabrics.
- Barefoot movement when visible in the original footage.
- Natural light.
- Warm and soft atmospheres.
- Close-ups of hands, feet and movement.
- Genuine moments from workshops.

Preferred visual palette:
- Terracotta.
- Burnt orange.
- Warm beige.
- Soft natural tones.
- Burgundy accents.

Avoid overly saturated colors, artificial fire effects and generic stock wellness imagery.

Use my original photos and videos whenever available.

Never alter my facial identity, facial features or physical appearance when using my photographs.

Do not invent workshop footage, participant images or scenes presented as real events.

## 8. On-screen text

Keep the existing technical rules for safe zones and screen readability.

For Dancing Flamme:
- Use short, emotionally meaningful sentences.
- Prefer one clear idea per screen.
- Use simple French vocabulary.
- Avoid overcrowded screens.
- Make the first screen immediately understandable.
- Ensure subtitles remain readable without sound.

On-screen text should complement the spoken script, not simply repeat every sentence.

## 9. Local visibility and discovery

The priority is to reach people who can realistically attend workshops.

Naturally integrate relevant local references when appropriate:

- Gouvieux.
- Chantilly.
- Senlis.
- Oise.
- Nearby communities.

Use relevant local keywords in captions and descriptions.

Use specific hashtags rather than large generic hashtag lists.

Prioritize local discovery, meaningful engagement and genuine interest over vanity metrics.

Never promise that a hook or Reel will go viral.

## 10. Language strategy

French is my primary communication language.

Default to French for all spoken scripts, on-screen text and captions.

Use Spanish for selected personal reflections, stories and inspirations.

Use English for selected inspirational content and international visibility.

Do not automatically translate every Reel into three languages.

When relevant, suggest an additional Spanish or English version.

All translations must sound natural and culturally appropriate.

## 11. Calls to action

Each Reel should have one clear and relevant call to action.

Depending on the content, invite people to:

- Comment with their experience.
- Save the Reel.
- Share it with someone.
- Follow the account.
- Ask a question.
- Discover an upcoming workshop.
- Register for a workshop.

Avoid turning every Reel into a sales pitch.

For promotional Reels, make registration information clear and easy to find.

Never invent registration links or contact details.

## 12. Ethical communication

Dancing Flamme promotes intuitive dance as a space for movement, expression and exploration.

Never:
- Promise to cure physical or psychological conditions.
- Present intuitive dance as a substitute for medical treatment.
- Make unsupported therapeutic claims.
- Suggest that every participant will experience the same emotional outcome.
- Use vulnerability or emotional distress to pressure people into registering.

Respect participant privacy and image permissions.

## 13. Final output format

For every Reel request, provide:

1. **Creative concept:** The central idea and objective.
2. **Three hooks:** Three different approaches.
3. **Hook scores:** Results from the existing scoring tool.
4. **Spoken script:** Complete first-person script in French.
5. **Timing:** Estimated duration and sequence breakdown.
6. **On-screen text:** Separate text with timestamps.
7. **Visual direction:** Suggested shots using available footage.
8. **Caption:** Ready-to-publish Instagram caption.
9. **CTA:** One clear action.
10. **Hashtags:** A small selection of relevant and local hashtags.

If essential information is missing, ask Giselle rather than inventing it.

Always prioritize authenticity, emotional connection, clarity and local community growth over publishing frequency.

The ultimate goal is to make people discover intuitive dance, feel welcome and want to experience it themselves.



```
/ig-reel we cut proposal time from 5 hours to 20 minutes with one template
```

```
HOOKS  (scored)
  86  STRONG  #5  Time Collapse   "Proposals used to take me five hours. Twenty minutes now."
                                  on screen: 5 HOURS -> 20 MIN
  71  STRONG  #1  Cost Confession "I billed four hours a week for formatting. For two years."
                                  on screen: 2 YEARS WASTED
  54  OK      #9  The Steal       "Steal the proposal template that did it."
                                  on screen: STEAL THIS

Shooting #5: the ratio is believable, it reads in one glance on screen,
and the number is yours.
```
