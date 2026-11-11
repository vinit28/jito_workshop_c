# Consolidated Track C workshop plan

Status: **Draft final template, November 9, 2026. Not approved for delivery.**
Based on: merged PR #4, `final/plan-proposed.md` (218 lines), plus the six review comments Vinit left on PR #4 on Nov 4, 8:39-8:43pm ET.
Event: JITO USA AI Summit, Track C, AI for Career and Productivity, Sunday, November 15, 2026, 45 minutes, phone-only, no paid AI subscription.

This replaces the placeholder in `final/plan.md`. Detail lives in `final/plan-proposed.md`; this file is the 1-3 page delivery plan, with owners and fill-in slots. It does not change Aditya's, Vinit's, or Dhruv's original plans.

## Delivery model — open decision, flagged

One 45-minute delivery, repeated. Each coordinator runs one cohort of 30, three tables of about 10, table captains picked at minute 0. Rajeev Pandya (VP, JITO USA, email Nov 4, 4:31pm ET) says the workshop runs twice, rounds 2:15 and 3:00, a different group of 30 each time, 180 seats total, 60 per coordinator. PR #4 as merged says one run, 90 total, repeat still to confirm. This draft follows Rajeev for quantities (180 cards, 60 per coordinator, reset between rounds) because that is the organizer's written instruction, and flags it as the one decision to confirm before freeze. If Vinit confirms one run only, quantities drop back to 90.

## Position and success

Audience: working professionals who already use ChatGPT or similar but have never been taught which tool fits which job, how agents differ from chatbots, or what they give away when an app can read their email or act for them.
Promise: leave able to put AI to work on Monday morning, on your own real tasks, and hand one of them to an agent safely.
Hypothesis: if attendees prompt for a real document and then design one personal automation, defining "good" and the access it needs, they will use both within a week.
Exit checks, cards at the door, target 80%+: (1) a personal task with a chosen tool and a written "good looks like" definition; (2) one improvement with a measure; (3) a value and implications line, with access narrowed; (4) one next step. Disconfirmed if most cards stop at step 1, or most say "allow everything."

## Attendee prep and core path

Prep via Sid from the registration list, personal account only. Bring a charged phone. Think of one weekly chore, write a sanitized version on paper. Optional: Muse from Meta or a free chat app you already use. Do not connect work email. Do not connect Gmail yet. No app required; every exercise works on paper. Do not bring or upload confidential, personal, financial, customer, credential, or unreleased information.
Core path: phone only, free accounts only, paper fallback for every live activity. Muse is facilitator demo only, on a synthetic Gmail account holding only fictional emails (Jordan Lee, Acme Services). Stop at the permission screen. Show read-only vs draft vs send, audit trail, disconnect. Stop before sending. No attendee connects a real inbox in the room, and nothing is sent, paid, or shared live.

## Run of show, 45 minutes — revised timings

Timings changed from PR #4 only to fit Vinit's two timing comments: Prompting 4 min to 5-6 min (Aditya), Guardrails 6 min to about 4 min (Vinit). Net change is zero; every later segment shifts by 2 minutes.

| Time | Segment | Owner | Attendees do/produce |
| --- | --- | --- | --- |
| 00:00-02:00 | 1. Intro | Vinit | Pick table captain |
| 02:00-08:00 | 2. Tool landscape | Dhruv Gupta (@goopgoop) — to fill in | Circle the category they use most and one to try |
| 08:00-14:00 | 3. Prompting that works | Aditya Singh (@Adi-1190) — populated below, 6 min | Star one habit to use in Exercise A |
| 14:00-20:00 | 4. Exercise A: prompt a real document | Aditya Singh (@Adi-1190) — instructions below | Write the prompt with a "good looks like" line; swap; improve once; blind judge picks one |
| 20:00-24:00 | 5. Guardrails and safety | Vinit Shah (@vinit28) — to populate, about 4 min | Tables call out green / yellow / red on five items |
| 24:00-36:00 | 6. Exercise B: design a personal agent, email first | Vinit + Aditya — to collab on instructions and Muse setup with Google connectors | Completed Exercise B card |
| 36:00-40:00 | 7. Evaluating models and tools | Vinit | Score their Exercise B tool on the five checks |
| 40:00-45:00 | 8. Wrap-up and 30-day plan | Vinit | Next-step line; Week 1, 2, 3 plan started |

Cut order if time slips: the "where to learn" bullet first, then the two shares at wrap-up, then shorten part 1 of Exercise B. Never cut guardrails or parts 3 and 4 of Exercise B.

## Section slots to populate — the tasks from PR #4

### 1. Tool landscape — Dhruv (@goopgoop)
Fill in this section. Eight phone-usable categories, chatbot vs copilot vs agent, "lowest tool that does the job," plus the 2-minute desktop vs mobile contrast with saved screenshots. No live desktop setup in the room.

### 2. Prompting that works — Aditya (@Adi-1190), segment 3, 08:00-14:00 (6 min)

Populated from `prompting-section-outline.md` (v4, Nov 10). Facilitation and staging notes are left for Aditya to add.
Main source: Anthropic, "Prompting best practices" (Claude docs, the page cited in Aditya's plan), re-read Nov 10, 2026:
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
The research papers listed under "Why it works" are cited from memory. Check each link before anything gets printed.

#### 1. What is prompting

- **A very smart person who doesn't know you**
  - Speaks perfect English and has read most of the internet. Knows nothing about you: your job, your client, your
    boss, what happened last week, what "done" means to you.
  - Your job is to point their brain and working capacity at *your* problem.
  - The guide's own framing is "a brilliant but new employee who lacks context on your norms and workflows."
  - Test: "If a smart colleague with no context would be confused by your request, the AI will be too." (Anthropic,
    "Be clear and direct")
- **Models are reasoning engines**
  - Describe the problem and the outcome, then leave the grunt work and the implementation to the model: drafting,
    structuring, options, first passes.
  - Be clear about which part of the problem you're handing over and which part stays with you.
    - **Hand over:** first drafts, summaries, reformatting, brainstorming options, "what am I missing?"
    - **Keep:** the goal, the facts, the judgment call, and anything that goes out in your name.

#### 2. Principles, and weak vs strong

##### 2a. The four parts of a prompt

- **Context:** who you are, what's going on, and why it matters.
- **Intent:** what you want done.
- **Format:** the length, the structure, and who will read it.
- **Restrictions:** tone, what it must not invent, and what to leave out.
- **Plus "good looks like":** one line saying what would make you hit send. This is the core skill, and the
  example below builds it with the room.

##### 2b. One example, built up live with the room

Use one task and improve it in rounds, with the output shown on screen after each round.

- **Round 0, weak:** "Write an email to a client about the delay."
  - The output is a generic apology with "[Client Name]" and no dates.
  - Ask the room: "What doesn't it know?" The answers will be context, audience, and tone.
- **Round 1, add context and intent:** "I manage a long-time client account. Their order ships 5 days late because
  of a supplier issue. Tell them, and offer free expedited shipping."
  - The output is now specific, but long and over-apologetic.
- **Round 2, define good together (the interactive moment):**
  - Ask: "What would make you hit send?" Write three of the room's answers on screen.
  - Turn them into one line: "Good looks like: under 120 words, warm and confident, uses only the dates I've given."
- **Round 3, add format and restrictions:** "They read email on their phone, so keep it short. Use only the dates
  I've given. Before you finish, check it against my list and tell me what to verify."
  - The output is a tight email plus a "verify" list (the new ship date, whether expedited shipping is approved).
  - Show weak and strong side by side.
- **Safety beat:** there is no client name and no real number anywhere. Sanitize before you paste.
- **Prep:** run these prompts in a real chat app before the event and save the outputs as screenshots, so the
  segment needs no Wi-Fi and every output shown is a real one.

##### 2c. Six habits, with source and reasoning

Read these aloud and talk through each one. They appear on the back of the prompt card. Each habit comes from the
Anthropic guide above, and the section name is in brackets.

1. **Give context and say why.** [Add context to improve performance]
   - Guide: explaining why "can give Claude more information about your goals and help it deliver more targeted
     responses," and "Claude can generalize from the explanation."
   - Why it works: the model only knows what's on the page. A reason lets it handle cases you didn't spell out.
     For example, "this will be read aloud" implies a dozen formatting rules at once.
2. **Be specific about what you want, including what good looks like.** [Be clear and direct]
   - Guide: "Claude responds well to clear, explicit instructions. Being specific about the output you want can
     help enhance results." If you want more than the bare task, "explicitly request it rather than relying on
     the model to infer this from vague prompts."
   - Why it works: current models are trained to follow instructions (the "instruction tuning" behind ChatGPT;
     Ouyang et al., 2022, *Training language models to follow instructions with human feedback*). They do what
     you asked, so the ask should be the thing you actually want.
3. **Say what to do, not what not to do.** [Control the format of responses]
   - Guide example: instead of "Do not use markdown," say "Your response should be composed of smoothly flowing
     prose paragraphs."
   - The guide gives no reason for this one. Our reasoning: these models are built to follow instructions, and
     "do X" gives them a target to aim at. "Don't do Y" rules out one thing but leaves every other option open,
     and it still puts Y on the page. Research also shows models handle negated instructions worse than plain
     ones (Jang et al., 2022, *Can Large Language Models Truly Understand Prompts? A Case Study with Negated
     Prompts*).
4. **Show an example when format matters.** [Use examples effectively]
   - Guide: examples are "one of the most reliable ways to steer Claude's output format, tone, and structure."
     Use 3-5, and make them "diverse," so the model "doesn't pick up unintended patterns."
   - Why it works: models are pattern-matchers. Showing beats describing. This is the "few-shot" result from
     Brown et al., 2020, *Language Models are Few-Shot Learners*. With a single example the model copies it too
     closely, which is why the guide asks for variety.
5. **Give it a role in one sentence.** [Give Claude a role]
   - Guide: a role "focuses Claude's behavior and tone for your use case. Even a single sentence makes a
     difference," for example "You are my chief of staff."
   - Honest caveat: a role mostly changes tone and focus. Research suggests a role doesn't make the model more
     factually accurate (Zheng et al., 2023, on personas in system prompts). Say "it sets the voice, not the
     IQ."
6. **Ask it to check itself.** [Thinking and reasoning: "Ask Claude to self-check"]
   - Guide: add "Before you finish, verify your answer against [test criteria]." It "catches errors reliably."
   - Why it works: a second pass against explicit criteria catches misses that the first pass makes (Madaan et
     al., 2023, *Self-Refine*). Your "good looks like" line already is the criteria list.
   - Caveat: the guide notes the newest top models already verify their own work well. For free-tier chat apps
     this is still worth doing, and it also gives you a "what to verify" list, which is useful in itself.

##### 2d. Structure and order for larger prompts

- **Long context, comprehensive ask: give it structure.** Use labelled blocks:
  - **Context:** background and pasted material.
  - **Ask:** what you want done.
  - **Output:** format, length, audience.
  - **Definition of good:** the "hit send" line.
  - Why: labels help the model tell your instructions apart from your material. The guide says tags help it
    "parse complex prompts unambiguously, especially when your prompt mixes instructions, context, examples, and
    variable inputs." [Structure prompts with XML tags] Plain headings like "Context:" do the same job in a chat app.
  - Structure also makes it easy to iterate: change one block and rerun, instead of rewriting a paragraph.
  - For small prompts you don't need this. One or two clear sentences are enough.
- **Put the context first and the question last.**
  - Guide: put long documents "near the top of your prompt, above your query, instructions, and examples."
    "Queries at the end can improve response quality by up to 30 percent in tests, especially with complex,
    multidocument inputs." [Long context prompting] Be precise when you say this: the guide gives that figure
    for long inputs, not short ones.
  - Why: a human reading a brief understands the question better once they've seen the background. Models also
    read in order, and research shows they use information at the start and end of a long prompt better than in
    the middle (Liu et al., 2023, *Lost in the Middle*). With the ask at the end, it's the last thing the model
    reads before it starts answering.

##### 2e. Two phone tricks

- **Talk instead of type:** hold the mic and brain-dump context for 60 seconds. Rambling is fine.
- **Let it interview you:** end with "Ask me the questions you need answered before you start," or "Improve my
  prompt, then run it."

##### Close

- Attendees star one habit on the prompt card to use in Exercise A.

### 3. Exercise A, prompt a document you actually need — Aditya (@Adi-1190), segment 4, 14:00-20:00

#### 1. Intro (about 45 sec)

- **Four tasks almost everyone here does every week, where AI gives the easiest win**
  1. **A tricky email or message:** a delay, a follow-up, a polite no, a request.
  2. **Rough meeting notes into a clean summary:** decisions, actions with owners, open questions.
  3. **Prep for a meeting or call:** agenda, questions to ask, likely objections, a one-line goal.
  4. **A short proposal, plan, or status update:** a one-pager for your boss, a client, or a partner.
- The earlier plan said "design doc." It is swapped for email because design docs are less universal for founders
  and sales folks. Email overlaps a little with Exercise B (inbox triage), so "weekly status update" is the alternative.

#### 2. Instructions: the blind taste test

Pairs, plus a judge from the next pair. One judge reads two short answers and picks one. Nobody rereads their own.

- **Write, about 2 min.** Use the four parts and a "good looks like" line, and write it on the card.
  - No names, no clients, no numbers, nothing confidential. Use "Client A," "$X," "my manager."
  - End every prompt with "Keep it under 150 words." This is what makes the timing work.
- **Swap and improve, about 45 sec.** Hand the card to your partner. They make one change: add missing context,
  sharpen the "good" line, or add "lead with the decision" or "what should I verify?"
- **Run both, about 30 sec.** You run your original on your phone. Your partner runs the improved version on theirs.
  Any free chat app works.
- **Blind judge, about 45 sec.** Hand both phones, marked only "left" and "right," to someone from the next pair,
  along with your card. They read your "good looks like" line, skim both answers against it, and point to the one
  they would send. They don't know which version is which.
- **Show of hands, about 45 sec.**
  - "Hands up if the judge picked the improved version." "The original?" "Couldn't tell?"
  - Ask one person: "What one change made the difference?" If the original won, that is a good story too: more is
    not always better, and the "good" line is what decides.
- **Bridge, about 15 sec.** "You just ran a blind test. That is how the leaderboards rank AI models, and we will
  come back to it at the end. Now look at what you just sent. Vinit's going to ask what happens to it."

#### Why this version

- Each person reads two short answers once, as a judge, instead of reading their own output twice. That cuts the
  reading time and turns it into a decision.
- The judge has to use someone else's "good looks like" line, which tests whether that line was clear.
- It sets up segment 7: LMArena ranks models by blind human votes, and attendees will have just done one.

#### Alternatives if phones or Wi-Fi fail, or the room is slow

- **Rank the prompts (paper, no phones).** Each table gets four pre-printed prompts for the same task, cut into
  strips, from weak to strong in a shuffled order. The table orders them weakest to strongest in 60 seconds, then the
  facilitator reveals the order and the saved outputs on screen. This pairs well with writing their own prompt.
- **Spot the missing part (paper).** The partner labels C, I, F, R and G ("good") on your prompt, and whatever letter
  is missing is the one change they add. You skip running it.
- **One run only.** Skip running the original and run only the improved prompt, saving about 30 seconds.

#### Timing check

- Intro 0:45, write 2:00, swap 0:45, run 0:30, judge 0:45, hands 0:45, bridge 0:15. That is 5:45, with 15 seconds of slack.
- Never cut the 150-word cap or the show of hands.

### 4. Guardrails — Vinit (@vinit28), about 4 min
Populate this section. Samsung as the primary story (not Navier-Stokes, unverified). Golden rule, free vs enterprise, green/yellow/red sort, Muse permission screen on the synthetic account, verify and bias (saved Harper v. Northfield example, recall Mata v. Avianca). Keep it to about 4 minutes: opener, story, sort, demo, verify.

### 5. Exercise B — Vinit + Aditya, email first
Collab on instructions and Muse setup with Google connectors. Email is the first exercise. End goal: get a summary of emails, and reply to / draft 1 email. Facilitator demo only, synthetic Jordan account, draft only, stop before sending. Attendees do the triage on paper with the synthetic email, or in their own chat tool with sanitized text and no connection. Four parts: task and tool, implement, improve once against "good," value and implications.

### 6. Template deck — Vinit (@vinit28)
11 slides, built natively in Google Slides so the text is editable, theme from Rajeev's sample case-study deck in email (white, dark navy #011826, royal blue #172EB5, sky #6BBEF2, teal #0F766E, font Ebrima, quiet, no gradients). Deck: [JITO Track C — AI for Career & Productivity — Template Deck](https://docs.google.com/presentation/d/1NKXNYSj1jzorAX9lpf0RNSJLEsMQ99x8dIXllBmGBXQ/edit). Slides: title and promise; where AI helps; chatbot, copilot, agent; Muse setup; Muse Gmail demo; prompt anatomy; personal task lab; risk checkpoint; human judgment; workflow card; 30-day plan and Monday commitment. Speaker notes are placeholders per owner in the .pptx copy at `files/jito-track-c-template-deck.pptx`, to be added to the Slides deck next; prepare a no-network PDF export.

## 30-day plan

Week 1, drafting; Week 2, summarizing or research; Week 3, repetitive-task mapping. Measure minutes saved or edits needed, review every output. Save prompts that worked, sanitized only. Tell your manager what changed with one number.

## Failure plan and readiness

No Wi-Fi / Muse unavailable: screenshots and paper cards. Someone shares sensitive data aloud: thank them, use it as a sanitizing example without repeating details. No app, account, unsupported phone: facilitator demo plus paper.
Print per cohort: 30 attendee cards and 3 table sheets; 180 cards total if two rounds, 90 if one run. Rehearse twice at 45 minutes. Freeze date, integration owner, handout owner, facilitator kit owner, and Sid prep-email sender/date: still unassigned.
Muse claims are docs-only, checked Nov 4, 2026. Gmail permission screen, account/age needs, and free limits still need a synthetic-account test. Owner: Vinit.

## Sources

Aditya Singh's plan, Nov 4, 2026, and tool-landscape.md; Vinit Shah's plan, Oct 29, 2026; merged PR #4; Rajeev Pandya email, Nov 4, 2026; Anthropic prompting guide; NBER customer-support study; Harvard/BCG field experiment; Samsung incident summary; Moffatt v. Air Canada; Mata v. Avianca.
