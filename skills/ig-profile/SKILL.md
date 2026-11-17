---
name: ig-profile
description: >-
  Score an Instagram profile out of 100 against a 12-part rubric and rewrite
  the parts that lose points - name field, bio, link, highlights, pinned three,
  grid. Use when the user says "optimize my profile", "fix my bio", "score my
  Instagram", "why don't people follow me", or pastes their profile and asks how
  it reads.
---

# ig-profile

Almost everybody optimises the wrong thing here. The profile is not a
storefront people browse. It is a **decision screen**, arrived at from one
reel, and it gets about three seconds to answer one question: is there more of
that here, and is it for me.

## Input

Ask the user to paste or screenshot: the name field, the handle, the bio, what
the link points to, the highlight names, what is pinned, and the first nine
grid covers. A screenshot of the top of the profile plus the first two grid
rows is enough for a first pass.

Do not log into Instagram on their behalf.

## Score it

Read `rubric.json` in this folder. Twelve items, 100 points, each with what
full marks looks like and how it usually fails. Score every item, show the
table, give the total. Be honest. Most profiles land in the 30s and 40s on the
first pass and a generous score is useless.

```
PROFILE SCORE  38/100

  name field       2/12   name only, no words anyone searches
  bio first line   3/12   three nouns and a coffee emoji
  pinned three     0/10   nothing pinned
  highlights       2/8    "Random", "Life", "2023"
  grid legibility  4/8    six of nine covers are a face mid-sentence
  ...
```

## Then rewrite, in this order

Fix in descending order of points lost. Do not rewrite everything at once, the
user has to actually go and change each of these.

**1. The name field (30 characters).** The bold line under the photo, not the
handle. This is the field Instagram search matches against, and most accounts
put a name in it and nothing else. Format that works:
`{Name} | {what you do, in searched words}`. Give three options.

**2. Bio line one.** Who this is for and what changes. Not a job title, not
adjectives, not a pipe-separated list of identities. The rest of the 150
characters carries one piece of proof or one plain offer.

**3. The pinned three.** Three slots, three different jobs: the best proof, the
clearest explanation of the offer, the best introduction to the person. This is
the highest-leverage fix on the whole profile and it takes four taps. An
unpinned grid shows whatever was posted last, which is a coin flip.

**4. Highlights.** Four to six, named for the questions a buyer asks: Pricing,
Results, How it works, About. Not "Random". Delete the rest.

**5. The link.** One destination that matches what the bio just promised. Five
are allowed; two is already a menu and a menu converts worse than a door.

**6. Grid covers.** The first nine at thumbnail size. Reel covers get chosen,
not left as whatever frame one was. Four words of text on a cover makes a grid
readable in one glance.

## Output

Score table, then the rewrites as copy-ready blocks in fix-first order, each
run through `/ig-human`. Re-score at the end and show the delta honestly. If
the rewrite reaches 84 and not 98, say 84, and say what the rest needs, which
is usually a grid, a story habit and a pinned post that does not exist yet.
None of that is a rewrite.

Nothing is saved to Instagram by this skill. The user edits each field.


---

# Dancing Flamme – Instagram Profile Customization

These instructions customize the ig-profile skill for Dancing Flamme. They complement the original profile optimization framework.

## 1. Brand identity

- Brand: Dancing Flamme – The Feeling Good Movement Association.
- Founder: Giselle Estupinan.
- Instagram handle: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).
- Main language: French.
- Secondary languages: Spanish and English.

Always write as Giselle, in the first person when creating personal content.

The profile must communicate authenticity, movement, freedom of expression and emotional connection.

## 2. Positioning

Dancing Flamme offers welcoming spaces where everyone can explore movement freely, reconnect with their body and express emotions through intuitive dance.

Core positioning:

- No dance experience required.
- No choreography to learn.
- No performance or competition.
- No judgement.
- Everyone moves at their own pace.
- The experience is based on music, sensations, freedom and self-expression.

Never position Dancing Flamme as a conventional dance school, fitness studio or commercial wellness brand.

## 3. Founder story and credibility

Giselle's personal and artistic background is an important part of the brand identity.

Use these elements when relevant:

- Colombian roots, where music and dance are deeply connected to culture, celebration and human connection.
- Classical ballet training from an early age.
- Performances in The Nutcracker and Paquita at Teatro Colón in Bogotá.
- Personal rediscovery of dance following her cancer experience.
- Dance Therapy training at ARTEC in 2023.
- Experience facilitating intuitive dance workshops in Chantilly.
- Involvement with Les Rubans de la Vie (ERC) and the Centre Culturel de Chantilly.

Use this story to build trust and human connection.

Do not make every profile element about the founder's personal story.

Never suggest that dance cures cancer or replaces medical treatment.

## 4. Target audience

Prioritize people living in:

- Gouvieux
- Chantilly
- Senlis
- Lamorlaye
- Coye-la-Forêt
- Surrounding Oise communities

The main audience includes:

- Women and men interested in personal expression.
- Beginners who believe they cannot dance.
- People looking to reconnect with their bodies.
- People interested in creativity and emotional expression.
- People seeking a welcoming, non-judgmental activity.
- Parents looking for creative activities for their children.

The profile should immediately communicate that everyone is welcome.

## 5. Instagram SEO strategy

Optimize the profile for natural Instagram search discovery.

Prioritize relevant French keywords:

- Danse intuitive
- Atelier danse intuitive
- Danse libre
- Danse et expression corporelle
- Atelier bien-être
- Danse à Chantilly
- Activité à Gouvieux
- Atelier danse Oise

Use the strongest relevant keywords in:

- Instagram name field.
- Bio.
- Captions.
- Reel cover titles.
- Highlight titles.

Prioritize local search intent and natural language.

Never stuff keywords into the bio or captions.

## 6. Profile name and bio

The Instagram name field must be clear, searchable and concise.

Provide three name field options, respecting Instagram's 30-character limit.

The bio must:

- Explain what Intuitive Dance is.
- Make it clear that no dance experience is required.
- Communicate the local location.
- Include one clear call to action.
- Respect Instagram's 150-character bio limit.

Always provide three bio alternatives:

A. Clear and SEO-focused.
B. Warm and emotional.
C. Community-focused.

Write all proposed bios in French.

## 7. Instagram highlights

Recommend between four and six highlights.

Suggested categories:

- Découvrir
- Les ateliers
- Mon histoire
- Témoignages
- Infos pratiques
- Enfants

Each highlight must have a clear purpose and relevant content.

Prioritize information that helps a new visitor understand the association and decide to participate.

## 8. Pinned posts

Recommend three pinned publications:

1. DISCOVER DANCING FLAMME
   Explain intuitive dance and why everyone can participate.

2. WHO I AM
   Introduce Giselle, her artistic background and her personal connection with dance.

3. JOIN A WORKSHOP
   Explain how workshops work and how to participate.

All pinned content should be in French by default.

## 9. Profile conversion strategy

The main objective is to turn profile visitors into:

- New workshop participants.
- Returning participants.
- Association members.
- Engaged members of the local community.

Prioritize clear information about workshops, registration, location and contact.

Make the next step obvious.

Use a warm and inviting call to action, never aggressive sales language.

Never invent dates, prices, workshop schedules or registration links.

Ask Giselle for missing information before publishing event-related details.

## 10. Language strategy

French is the primary communication language.

- French: 80%.
- Spanish: 10%.
- English: 10%.

These are editorial guidelines, not strict rules.

All profile optimization proposals must be written in French unless explicitly requested otherwise.

Spanish and English can enrich the brand identity but must not compromise local audience clarity.

## 11. Final quality checklist

Before presenting profile recommendations, verify:

- Is the profile immediately understandable?
- Is Intuitive Dance clearly explained?
- Are the local keywords relevant?
- Is the location visible?
- Does the bio communicate a clear benefit?
- Is there one clear call to action?
- Are the highlights useful?
- Do the pinned posts tell a coherent story?
- Is Giselle's identity authentic and consistent?
- Is the profile designed to encourage workshop participation?

Always provide:

1. The score out of 100.
2. The score breakdown by criterion.
3. The three biggest improvement opportunities.
4. Copy-ready recommendations.
5. The expected impact of each change.

Never claim that a profile change guarantees algorithmic reach or follower growth.

Nothing is changed directly on Instagram. Giselle reviews and implements every recommendation.

