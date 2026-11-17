---
name: ig-comment
description: >-
  Write comments on other people's Instagram posts and reels that read as a
  person with an opinion, not a bot. Use when the user pastes a post or a reel
  and wants a comment, says "comment on this", "engage with this", "what do I
  say here", or wants a batch for their daily engagement round.
---

# ig-comment

Commenting is the highest-leverage twenty minutes on Instagram and the easiest
to do badly. A comment near the top of a reel with 40,000 views is seen by more
people than most accounts' own posts, and it is the one place where a stranger
can tap straight through to a profile.

A generic comment is worse than none. It costs a tap that goes nowhere and it
marks the account as an engagement-pod account to the one person whose opinion
mattered, which is the creator.

## Input

The user pastes the post or reel text, or a screenshot, with the account name.
If they give a URL you cannot open, ask them to paste it. Do not use a browser
tool to scrape the feed and do not post anything.

## The nine comment types

Pick by what the post actually is. Never default to type 1.

| # | type | when | shape |
| --- | --- | --- | --- |
| 1 | **Add a datum** | the post makes a claim you can support with a number | "Same for us: 40% of..." |
| 2 | **Add the missing case** | the post is right but incomplete | "This holds until {condition}." |
| 3 | **Respectful disagree** | you genuinely think it is wrong | name the agreement first, then the fork |
| 4 | **Extend one line** | one line in it is the good one | quote it, build on it |
| 5 | **Ask the real question** | the post skipped the hard part | one question, specific |
| 6 | **The receipt** | you have done the thing they described | what happened, two sentences |
| 7 | **The correction** | there is a factual error | be right, be brief, be kind, be sure |
| 8 | **The reframe** | right facts, wrong frame | "Another way to read this:" |
| 9 | **The one-liner** | the post needs nothing, you want presence | under 10 words, must be funny or true |

## Rules

- **One to three sentences.** Instagram comments are read in a narrow column
  under a video. A paragraph gets collapsed behind "more" and nobody taps it.
- **Never open with** "Great post", "Love this", "So true", "This 👏", "Needed
  this today", or the creator's first name with an exclamation mark. All of
  them are invisible.
- **No emoji-only comments** and no emoji as the first character.
- **Never restate the reel.** Everybody watching just watched it.
- **One idea.** A comment with two points reads as a hijack.
- **Say the specific thing.** If the comment could sit under any post on the
  topic, it is not a comment, it is noise.
- **No pitching, ever.** Not the offer, not the link, not "check out my page".
  That is the fastest way to be blocked by exactly the person you were trying
  to reach.
- **Early matters more here than anywhere.** A comment in the first hour on a
  reel that then travels gets carried with it.

## Output

Give **two options of different types**, labelled, plus one line on which you
would post and why. Run both through `/ig-human` first: comments are short, so
an em dash or a stock phrase is proportionally louder than it is in a caption.

```
COMMENT OPTIONS  (on @acct's reel about pricing)

[6 · Receipt]
We raised ours 40% last March and lost exactly one client, who was the one
taking up half the inbox. Took eight months to stop being scared of it.

[3 · Respectful disagree]
Agree on the anchoring. The part I would push back on is doing it mid-project.
We tried that and it cost us a renewal that was otherwise fine.

Post the first. It concedes something and it has a number in it.
```

## Batch mode

For an engagement round, ask for the 5 to 10 posts as pasted text in one
message, return one comment each in a single block, and keep a running note in
`~/.claude/instagram/log.md` of who has been commented on this week.
Commenting on the same three accounts every day is visible and it looks like
exactly what it is.

## Never

Do not auto-post, do not automate comments, and do not use a browser tool to
publish on the user's behalf. Automated engagement violates Instagram's Terms
of Use and gets accounts action-blocked. This skill writes the comment. The
user posts it.



# Dancing Flamme – Brand Customization for Instagram Comments

These instructions customize the ig-comment skill for Dancing Flamme. They complement the original commenting workflow and must not replace its existing rules.

## 1. Brand identity and voice

- Brand: Dancing Flamme – The Feeling Good Movement Association.
- Founder: Giselle Estupinan.
- Instagram: @dancing_flamme.
- Location: Gouvieux, near Chantilly, Oise, France.
- Main activity: Intuitive Dance (Danse Intuitive).

Always write comments in Giselle's natural voice when representing her account.

Before writing, read `~/.claude/instagram/voice.md` if available.

The voice must be:
- Warm, authentic and welcoming.
- Personal and genuinely interested.
- Sensitive, respectful and empathetic.
- Positive without exaggeration.
- Natural and conversational.

## 2. Engagement priorities

Prioritize meaningful interactions with:

- Local businesses and associations around Gouvieux, Chantilly and Senlis.
- Cultural and artistic organisations.
- Dance, movement and creative communities.
- Local wellness and community initiatives.
- People and organisations promoting social connection and self-expression.

Build genuine relationships rather than seeking visibility through repetitive comments.

## 3. Topics relevant to Dancing Flamme

Look for relevant opportunities to engage with content about:

- Intuitive Dance and free movement.
- Dance and artistic expression.
- Music, creativity and body awareness.
- Community activities and local events.
- Personal development and self-expression.
- Women's initiatives and solidarity.
- Cultural activities and creative workshops.
- Connection, emotions and shared experiences.

Only comment when there is a genuine connection with the publication.

## 4. Commenting style

- Be specific: refer to an actual detail in the post.
- Express a genuine opinion or personal reaction.
- Prefer short, spontaneous sentences.
- Ask a thoughtful question when appropriate.
- Use simple and natural French as the default language.
- Use English or Spanish only when appropriate to the original conversation.
- Use emojis sparingly and naturally.

Avoid:
- Generic comments such as "Beautiful post!" or "Amazing!"
- Excessive compliments.
- Artificial enthusiasm.
- Repeated promotional messages.
- Copy-pasted comments.
- Aggressive networking or sales language.

## 5. Promoting Dancing Flamme naturally

The objective is to develop relationships and local awareness, not to advertise in every comment.

- Never turn an unrelated conversation into a promotion.
- Do not insert workshop dates, prices or registration details into unrelated comments.
- Mention Dancing Flamme only when the context genuinely makes it relevant.
- Never claim that Intuitive Dance cures illnesses or replaces medical treatment.
- Never use Giselle's personal health history as an engagement tactic.
- Never invent personal experiences or professional relationships.

## 6. Relationship-building rules

- Prioritize quality over quantity.
- Engage with local accounts consistently but naturally.
- Avoid commenting on the same accounts repeatedly with identical messages.
- Respect different opinions and perspectives.
- Never pressure people to follow, comment or attend a workshop.
- Do not send unsolicited promotional direct messages.
- Respect privacy and sensitive personal disclosures.

## 7. Final quality checklist

Before presenting a comment, verify:

- Is it genuinely relevant to the original post?
- Does it sound like Giselle?
- Is it specific rather than generic?
- Does it create a natural opportunity for conversation?
- Is the tone respectful and appropriate?
- Is it free from unnecessary promotion?
- Does it respect the original author's perspective?

Always provide comments for Giselle to review and approve.

Nothing is published automatically. Giselle posts every comment herself.


