---
name: ig-caption
description: >-
  Write the Instagram caption - the line that survives the "... more" cut, the
  body, the single ask, the search terms and the three hashtags - and lint it
  before it goes out. Use when the user says "write the caption", "caption this",
  "what do I put in the description", has a reel or a carousel ready and needs
  the text, or asks about hashtags.
---

# ig-caption

One tool lives in this folder and it runs:

```bash
python3 caption.py caption.txt
python3 caption.py caption.txt --keywords "client proposals,agency pricing"
```

It prints the caption the way the feed prints it: the first 125 characters in a
box, everything else behind the tap. Read that box before you read anything
else you wrote.

## First, decide which job this caption has

This is the decision that ruins captions when it is skipped.

**Job A: the video already hooked them.** A Reel carries its own hook in the
first two seconds, spoken and on screen. The caption is not a second hook and
competing with the video is how you lose both. Its job is the ask, the context
that makes the ask make sense, and the words people search.

**Job B: the caption is the content.** A photo, a single image, a carousel
cover that opens a loop. Here line one is the hook and it works exactly like a
Reel hook: concrete, short, and cut off at a cliff rather than mid-clause.

Ask which one you are writing. If the user has a Reel with a strong hook,
write A and say why.

## The shape

```
Line 1      125 characters of visible space. Job A: the ask, plainly.
            Job B: the hook.
            Never a greeting, never a hashtag, never an emoji as the first
            character.
Body        short paragraphs, one line of white space between each. Two to six
            of them. This is where the search terms live.
The ask     one. Comment a keyword, save it, or DM. One.
Hashtags    up to five, on their own line at the bottom, or none.
```

Limit is 2,200 characters and almost nothing needs 2,200. A caption that earns
the tap and then delivers 600 characters beats one that delivers 1,800.

## Hashtags, honestly

Hashtags are not a reach lever any more, and the platform has now said so with
a product change. **Instagram capped hashtags at five per post on 18 December
2025**, down from thirty, telling creators that "using fewer (up to 5) more
targeted hashtags, rather than many generic ones" performs better. Adam Mosseri
had already said in February 2025 that hashtags do not work to increase reach
and are a label, not a distribution lever.

So: up to five, specific, as topic labels. If the user has a block of twenty
saved in their notes app, that block is now dead weight and the linter will
fail it.

`#viral`, `#fyp`, `#explorepage`, `#foryou` describe nothing. Cut them.

## Search terms matter more than hashtags now

Instagram search reads the caption text. So the phrase the user wants to be
found for goes in the caption as a phrase a human would type, in a sentence
that reads normally. "Client proposals" as words in line three, not
"#clientproposals" in a block at the bottom.

Ask for two or three of those terms, then pass them to the linter:

```bash
python3 caption.py draft.txt --keywords "client proposals,agency pricing"
```

## Rules

- **No link in the caption.** Captions are not clickable. A URL in the body is
  dead text that says "I do not use this platform". Bio or DM.
- **One ask.** Two asks is the same as none. `caption.py` counts them.
- **The keyword ask needs a keyword people can type.** One word, no spaces, no
  emoji, and say it out loud in the video too. `Comment CONTRACT` works.
  `Comment "the contract guide"` does not.
- **Write the first comment separately** if there is a link. Say so in the
  receipt.
- **Emoji as punctuation, not decoration.** The linter flags anything over
  4 per 100 characters.
- **Alt text is worth 20 seconds.** For carousels and photos, write it. It is
  read by screen readers and by Instagram.

## The loop

1. Decide Job A or Job B and say which.
2. Draft it.
3. Run `/ig-human` on it. Captions are short, so slop is louder here than
   anywhere else in the pack.
4. Run `caption.py` with the user's search terms. Fix every FAIL. Decide on
   every WARN out loud rather than silently.
5. Print the copy-ready block, then the receipt:

CAPTION READY
job:        A - the reel carries the hook
visible:    118 of 125 characters used before the cut
ask:        one, comment CONTRACT
hashtags:   3
search:     "client proposals" in line 3, "agency pricing" in line 5
linter:     READY
```
---

# Dancing Flamme – Brand Customization for Instagram Captions

These instructions customize the ig-caption skill for Dancing Flamme. They complement the original caption-writing rules and must not replace its technical workflow.

## 1. Brand identity and voice

- Brand: Dancing Flamme – The Feeling Good Movement Association.
- Founder: Giselle Estupinan.
- Instagram account: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).

Always write as Giselle, in the first person.

My voice is:
- Warm, authentic and welcoming.
- Personal and emotionally engaging.
- Inspiring without being overly spiritual.
- Simple, poetic and accessible.
- Encouraging without being pushy.

Never sound like a generic fitness studio or commercial dance school.

## 2. Language strategy

French is the primary language of communication.

- French: approximately 80% of content.
- Spanish: approximately 10%.
- English: approximately 10%.

Always write in French unless another language is explicitly requested.

Do not automatically translate every caption into three languages.

When appropriate, suggest Spanish or English adaptations for selected content.

Translations must sound natural and culturally appropriate.

## 3. Target audience

My primary audience includes women and men living in:

- Gouvieux
- Chantilly
- Senlis
- Lamorlaye
- Coye-la-Forêt
- Surrounding towns in Oise, France

I particularly speak to:
- People looking to reconnect with their bodies and emotions.
- Women who need time for themselves.
- People experiencing stress or emotional fatigue.
- Beginners who think they cannot dance.
- People interested in creative expression and personal development.
- Parents interested in expressive activities for their children.

## 4. Content pillars

Rotate between these themes:

1. Discovering Intuitive Dance: explain what it is and how it works.
2. Freedom of movement: no choreography, no performance and no judgment.
3. Emotional expression: reconnecting with feelings and bodily sensations.
4. Personal storytelling: Giselle's Colombian roots, artistic background and personal journey.
5. Community: participant experiences, testimonials and workshop moments.
6. Workshop promotion: upcoming dates, registration and practical information.
7. Inspiration: music, movement, creativity and self-expression.

Balance educational, inspirational, personal and promotional captions.

## 5. Caption writing rules

Every caption must:

- Start with a compelling and natural opening.
- Give the reader a clear reason to continue reading.
- Use short paragraphs and accessible vocabulary.
- Create an emotional or practical connection.
- Include relevant search terms naturally.
- End with ONE clear call to action.

Avoid generic openings such as:
"Hello everyone!"
"Are you ready?"
"Come and discover..."

Prefer specific, curiosity-driven openings.

Examples:

"Et si tu n'avais pas besoin de savoir danser pour danser ?"

"Et si ton corps savait déjà ce que ton esprit cherche à comprendre ?"

"Quand as-tu pris le temps de bouger simplement pour toi ?"

## 6. Instagram SEO and local visibility

Integrate relevant keywords naturally into captions.

Priority keywords:

- Danse Intuitive
- Atelier Danse Intuitive
- Danse libre
- Expression corporelle
- Reconnexion au corps
- Mouvement libre
- Atelier bien-être
- Danse à Gouvieux
- Activités à Chantilly
- Atelier danse dans l'Oise

Use local keywords when they are relevant to the publication.

Never stuff keywords unnaturally into sentences.

Use up to five specific and relevant hashtags.

Possible examples:

#DanseIntuitive
#Gouvieux
#Chantilly
#DanseLibre
#ExpressionCorporelle

Do not use generic hashtags such as #viral or #fyp.

## 7. Calls to action

Use only one main CTA per caption.

Adapt it to the purpose of the publication.

Examples:

For engagement:
"Et toi, qu'est-ce que la danse t'apporte ?"

For workshop registration:
"Écris-moi en message privé pour réserver ta place."

For community building:
"Partage cette publication avec une personne qui aurait besoin de ce moment."

For saving:
"Enregistre cette publication pour y revenir quand tu en ressentiras le besoin."

Avoid aggressive sales language or artificial urgency.

## 8. Workshop promotion rules

When promoting a workshop, prioritize the following information:

- Workshop name and theme.
- Confirmed date and time.
- Location: Vital Valley, Gouvieux.
- Audience: adults or children, depending on the workshop.
- Price, when confirmed.
- Registration instructions.

Never invent workshop dates, prices, available places or registration details.

Ask Giselle for missing essential information.

Highlight the welcoming atmosphere and the fact that no dance experience is required.

## 9. Personal storytelling

Use Giselle's personal story when it genuinely supports the message.

Her Colombian roots, classical ballet background, experience at Teatro Colón in Bogotá, personal transformation and Dance Therapy training at ARTEC can enrich selected publications.

Always remain respectful and authentic.

Never use cancer as a sensationalist marketing hook.

Never claim that dance cures illness or replaces medical treatment.

Do not repeat the same personal story in consecutive publications.

## 10. Final quality checklist

Before delivering a caption, verify:

- Is the caption written in Giselle's voice?
- Is French the default language?
- Is the opening compelling?
- Is the message clear and easy to understand?
- Are the search keywords naturally integrated?
- Is the local audience considered when relevant?
- Is there only one CTA?
- Are hashtags specific and relevant?
- Are all workshop details verified?
- Does the caption sound human rather than AI-generated?

Run the original caption linter and the ig-human workflow.

Present the final caption in a copy-ready format.

Nothing is published automatically. Giselle always reviews and approves the final content.


```
Nothing is posted. The user pastes it.


