---
name: ig-carousel
description: >-
  Build an Instagram carousel - the cover that earns the swipe, slide-by-slide
  copy, and the 1080x1350 files to upload. Use when the user says "carousel",
  "slides", "swipe post", "turn this into a carousel", or has a list-shaped or
  step-shaped idea that would die as a single image.
---

# ig-carousel

Carousels are the highest-dwell format on the grid, because a swipe is an
interaction and a scroll is not. They also get a second chance: Instagram can
show a carousel again starting from a later slide to someone who did not engage
the first time, so slide two has to stand on its own as well.

The format rewards one idea broken into steps. It punishes a caption cut into
pieces.

## When to use it instead of a Reel

Use a carousel when the idea has **sequence and needs to be re-read**: steps, a
framework with parts, a before and after, a list worth screenshotting. Use a
Reel when the idea has motion, a face, or a payoff that has to be seen
happening.

If the idea is one claim, it is neither. Hand it to `/ig-reel` and say so.

## Structure

6 to 10 slides. The cap is 20 and 20 is almost always a book nobody finishes.
Under 5 and the swipe never starts.

```
1         COVER     the hook. 6 words or fewer, at a size that is legible in
                    the grid at thumbnail. One line of promise under it.
2         THE STAKE why this matters, in one sentence. This slide is also a
                    second cover, so it cannot be setup.
3 to N    ONE IDEA PER SLIDE. A headline of 3 to 7 words, at most 25 words
                    under it. If a slide needs a paragraph, it is two slides.
N+1       RECAP     the whole thing as a list. This is the screenshot slide.
LAST      CTA       one action. Save, comment a keyword, or follow. One.
```

## Slide copy rules

- **The cover is 80% of the result.** Six words. Big. Nothing on the deck saves
  a cover nobody swipes.
- **Design for the grid crop.** The profile grid crops to a portrait rectangle
  that is taller than it is wide, and the exact ratio has moved more than once.
  Build at 1080x1350 and keep the cover text well inside the middle, clear of
  the outer 120 pixels on every side, and the crop stops mattering.
- **Number the slides** (3/8). Completion goes up when people can see the end.
- **No slide is a paragraph.** If it cannot be said in 25 words, split it.
- **The recap slide is the one people screenshot and send.** Sends are the
  strongest signal you can earn. Make it standalone and readable with no
  context.
- **The handle on every slide**, small, bottom corner. Screenshots travel
  without you.
- **Alt text on the cover at minimum.** It is read by screen readers and by
  Instagram.

## Building the files

Instagram wants 1080x1350 (4:5), JPEG or PNG, up to 20 items. Build it as HTML
and print each slide:

```bash
# one <section> per slide, 1080x1350, page-break-after: always
# then Chrome headless --print-to-pdf, or any HTML-to-image you already use
```

Write the HTML with `width:1080px; height:1350px`, a single accent colour, and
type no smaller than 32px, because this is read on a phone at a third of its
real size. If the project has a brand skill or a design system, use it and do
not invent a palette.

## Output

The slide-by-slide copy first, as a numbered list the user can read in ten
seconds and edit before anything is rendered. Then the **caption**, which for a
carousel is Job B in `/ig-caption`: the caption is doing work here, because the
cover has already used its six words.

Run both through `/ig-human`. Build the files only after the user approves the
copy.

```
CAROUSEL  ·  8 slides

1  COVER   THE $18,000 CLAUSE
           One line I now put in every contract.
2  STAKE   I approved the work. They asked for the money back nine days later.
3          WHAT IT SAYS
           Payment on delivery, not on approval.
...
7  RECAP   All four lines, in order.
8  CTA     Comment CONTRACT and I will send the full clause.

Caption: Job B, hook in line 1, one ask, 3 tags.
```


# Dancing Flamme – Brand Customization for Instagram Carousels

These instructions customize the ig-carousel skill for Dancing Flamme. They complement the original carousel workflow and must not replace its technical rules.

## 1. Brand identity

- Brand: Dancing Flamme – The Feeling Good Movement Association.
- Founder: Giselle Estupinan.
- Instagram: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).
- Main objective: Build an authentic local community and attract participants to workshops.

Always create content in Giselle's first-person voice when sharing personal experiences.

Before writing, read `~/.claude/instagram/voice.md` if available. Follow its voice, personal story and communication guidelines.

## 2. Carousel objectives

Every carousel must have one clear purpose:

- Introduce Intuitive Dance to people who have never practised it.
- Explain its philosophy and benefits without making medical claims.
- Encourage self-expression, creativity and reconnection with the body.
- Build trust and emotional connection with the local community.
- Share Giselle's artistic background and personal journey when relevant.
- Present workshops and encourage participation.
- Answer common questions and remove barriers to joining.

Prioritize educational, inspirational, personal and community-building content over purely promotional content.

## 3. Core philosophy of Intuitive Dance

The following principles must be respected:

- You do not need to know how to dance.
- There are no steps to learn or choreography to reproduce.
- There is no performance, competition or judgment.
- Everyone moves according to their own sensations, rhythm and imagination.
- The body becomes a space for expression and exploration.
- Music supports movement and personal expression.
- Every participant is free to explore movement in their own way.

Never present Intuitive Dance as a conventional dance class or fitness programme.

Never promise that dance cures illness, trauma or psychological conditions.

## 4. Personal storytelling

Giselle's personal story can inspire carousel content.

Relevant dimensions include:

- Her Colombian roots and the importance of dance in Colombian culture.
- Her early classical ballet training.
- Her performances in The Nutcracker and Paquita at Teatro Colón in Bogotá.
- Her rediscovery of dance following her cancer experience.
- Her Dance Therapy training at ARTEC in 2023.
- Her experience facilitating Intuitive Dance workshops in Chantilly.
- Her involvement with Les Rubans de la Vie (ERC) and the Centre Culturel de Chantilly.

Use personal storytelling with sensitivity and authenticity.

Do not turn every carousel into a personal story. Never invent experiences, quotations or achievements.

Do not use cancer as a sensationalist marketing hook or imply that dance replaces medical treatment.

## 5. Carousel structure and writing style

- Keep the original technical requirement of 6 to 10 slides.
- Each carousel must communicate one central idea.
- Slide 1 must create curiosity and give a clear reason to swipe.
- Slide 2 must establish why the subject matters.
- Each following slide must add a new idea, question or useful insight.
- Use short, accessible sentences.
- Avoid overcrowded slides.
- Use a natural, warm and conversational tone.
- Create a logical progression between slides.
- The final slide must provide a meaningful conclusion and one clear call to action.

Avoid generic motivational statements, excessive spiritual language and aggressive marketing.

## 6. Visual direction

The visual universe should communicate:

- Freedom of movement.
- Femininity and authenticity.
- Emotion and human connection.
- Nature, softness and creativity.
- Movement rather than performance.

Prioritize authentic photographs and videos from actual Dancing Flamme workshops when available.

Avoid generic fitness imagery, competitive dance poses and overly commercial wellness visuals.

Keep typography readable and visual consistency across slides.

## 7. Language strategy

- French is the default language.
- Use natural, accessible French suitable for a local French-speaking audience.
- English and Spanish versions should be created when explicitly requested.
- Do not mix three languages in the same carousel unless specifically requested.
- Translations must preserve the emotional meaning and natural tone of the original text.

## 8. Local community and calls to action

The primary audience includes women and men living around Gouvieux, Chantilly, Senlis and neighbouring areas.

When relevant, encourage people to:

- Save the carousel for later.
- Share it with someone who might enjoy Intuitive Dance.
- Comment with their feelings or experiences.
- Discover Dancing Flamme.
- Join an upcoming workshop.
- Contact Giselle for practical information.

Use a single, natural call to action per carousel.

Never invent workshop dates, prices, locations or availability. Check the latest confirmed information before including event details.

## 9. Final quality checklist

Before presenting a carousel, verify:

- Is there one clear central idea?
- Does the cover encourage people to swipe?
- Is the content relevant to Intuitive Dance?
- Does it reflect Giselle's voice and Dancing Flamme's identity?
- Is the language accessible to beginners?
- Is each slide useful and easy to read?
- Is the storytelling authentic?
- Are all factual claims verified?
- Is the final call to action relevant?
- Does the carousel complement the existing Instagram content strategy?

Giselle always reviews and approves the final content before publication.

Nothing is published automatically.


Nothing is uploaded. The user posts it.
