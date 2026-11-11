# Prompting that works + Exercise A: content outline (v4, Nov 10)

Segment 3, Prompting, 08:00-14:00 (6 min), and segment 4, Exercise A, 14:00-20:00 (6 min). Aditya owns both.
Facilitation and staging notes are left for Aditya to add.

Main source: Anthropic, "Prompting best practices" (Claude docs, the page cited in Aditya's plan), re-read Nov 10, 2026:
https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
The research papers listed under "Why it works" are cited from memory. Check each link before anything gets printed.

---

# Segment 3: Prompting that works

## 1. What is prompting

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

## 2. Principles, and weak vs strong

### 2a. The four parts of a prompt

- **Context:** who you are, what's going on, and why it matters.
- **Intent:** what you want done.
- **Format:** the length, the structure, and who will read it.
- **Restrictions:** tone, what it must not invent, and what to leave out.
- **Plus "good looks like":** one line saying what would make you hit send. This is the core skill, and the
  example below builds it with the room.

### 2b. One example, built up live with the room

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

### 2c. Six habits, with source and reasoning

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

### 2d. Structure and order for larger prompts

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

### 2e. Two phone tricks

- **Talk instead of type:** hold the mic and brain-dump context for 60 seconds. Rambling is fine.
- **Let it interview you:** end with "Ask me the questions you need answered before you start," or "Improve my
  prompt, then run it."

### Close

- Attendees star one habit on the prompt card to use in Exercise A.

---

# Segment 4: Exercise A, prompt a document you actually need (14:00-20:00)

## 1. Intro (about 45 sec)

- **Four tasks almost everyone here does every week, where AI gives the easiest win**
  1. **A tricky email or message:** a delay, a follow-up, a polite no, a request.
  2. **Rough meeting notes into a clean summary:** decisions, actions with owners, open questions.
  3. **Prep for a meeting or call:** agenda, questions to ask, likely objections, a one-line goal.
  4. **A short proposal, plan, or status update:** a one-pager for your boss, a client, or a partner.
- The earlier plan said "design doc." It is swapped for email because design docs are less universal for founders
  and sales folks. Email overlaps a little with Exercise B (inbox triage), so "weekly status update" is the alternative.

## 2. Instructions: the blind taste test

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

## Why this version

- Each person reads two short answers once, as a judge, instead of reading their own output twice. That cuts the
  reading time and turns it into a decision.
- The judge has to use someone else's "good looks like" line, which tests whether that line was clear.
- It sets up segment 7: LMArena ranks models by blind human votes, and attendees will have just done one.

## Alternatives if phones or Wi-Fi fail, or the room is slow

- **Rank the prompts (paper, no phones).** Each table gets four pre-printed prompts for the same task, cut into
  strips, from weak to strong in a shuffled order. The table orders them weakest to strongest in 60 seconds, then the
  facilitator reveals the order and the saved outputs on screen. This pairs well with writing their own prompt.
- **Spot the missing part (paper).** The partner labels C, I, F, R and G ("good") on your prompt, and whatever letter
  is missing is the one change they add. You skip running it.
- **One run only.** Skip running the original and run only the improved prompt, saving about 30 seconds.

## Timing check

- Intro 0:45, write 2:00, swap 0:45, run 0:30, judge 0:45, hands 0:45, bridge 0:15. That is 5:45, with 15 seconds of slack.
- Never cut the 150-word cap or the show of hands.
