# Supporting notes: tool landscape, model evaluation, and prompting trends

Companion to [plan.md](plan.md), segments 2 and 3. Facts are from vendor pages and press, read
November 4, 2026, and are **docs-only** (no phone tests yet). Items marked *verify* need a check before rehearsal.

## 1. Categories of AI tools you can use from a phone today

| Category | What it does for you | Phone examples (Nov 2026) | Best task types | Access it asks for |
| --- | --- | --- | --- | --- |
| **Chat assistants** | Answers, drafts, rewrites, explains | ChatGPT, Claude, Gemini, Microsoft Copilot apps (free tiers) | Emails, proposals, agendas, summaries, learning | Only what you paste in |
| **Deep research agents** | Searches dozens of sources for several minutes, returns a cited report | Research modes in ChatGPT, Gemini, Claude, Perplexity (free tiers limited; *verify*) | Market scans, competitor briefs, prep for a meeting | Web only; check every citation |
| **Personal "do-it-for-me" agents** | Takes actions across apps and the web: email, booking, forms, shopping | **Muse from Meta**: iOS, Android, muse.ai, in the US since Sept 8, 2026; free for most use, paid plans for more | Scheduling, travel, errands, inbox triage, lists | Email read or send, browser, payments with approval. **Highest risk.** |
| **Agentic browsers** | Browses and fills in sites for you | Perplexity Comet (iOS and Android, core is free); Gemini in Chrome on Android (paid AI Pro; *verify*) | Comparing options, filling forms, collecting info | Everything you're signed into in that browser |
| **Phone assistants and shortcuts** | Acts inside your phone's own apps | Gemini on Android, Gemini Live (camera and screen share); Siri with Apple Intelligence and Shortcuts (*verify* AI actions) | Reminders, messages, quick "do this on my phone" | Phone apps, contacts, screen |
| **Meeting and voice notetakers** | Records, transcribes, summarises, lists actions | Otter, the AI in Zoom and Teams, voice memo modes in chat apps | Meeting notes, voice brain-dumps, interviews | Microphone. **Get consent from everyone recorded** |
| **No-code automation agents** | Connects apps and runs a workflow in the background | Zapier (incl. Zapier Agents), Make, Microsoft Power Automate. Set up mostly on web; results arrive on phone | Repetitive, rule-based work you do weekly | Connected accounts. Use only IT-approved work connections |
| **Work-suite copilots** | AI inside your employer's email, docs, and chat | Microsoft 365 Copilot, Gemini in Google Workspace, ChatGPT Enterprise, Claude for Work | Anything with company or client data | Your work account, under your employer's contract |

**Facilitator line:** *"Move down this table and the tool does more for you, and also sees more and can
do more damage. Pick the lowest row that gets the job done."*

### 1b. AI devices (wearables and recorders)

Show one photo of each type. Prices and popularity are from reviews and press, not our own tests.

| Type | Leading examples | How it records | Where data goes | What to say |
| --- | --- | --- | --- | --- |
| **AI voice recorders ("scribes")** | **Plaud Note** (credit-card-sized, sticks to the back of a phone, records calls and meetings) and **Plaud NotePin** (clip, pin or wristband). Plaud is the category leader; [Layer3 Labs](https://www.layer3labs.io/gear/best-ai-note-taker-devices) ranks NotePin #1 (Oct 2026) | Press to record | Cloud transcription and summaries; full AI features need a subscription | Great for meetings, interviews, site visits. Cloud processing "may not suit confidential meetings" |
| **Always-on pendants and bands** | Bee (owned by Amazon since 2025); Limitless Pendant (bought by Meta, new sales paused) | Listens continuously | Cloud | The biggest consent question in the room: it records everyone around you |
| **AI rings** | **Sandbar Stream** (~$249-299, free tier or $10/month Pro; first preorders sold out, $36M raised; mic off by default, hold to record) and **Pebble Index 01** (~$99, no subscription; records only while you hold the button; transcription runs on your phone, not the cloud). Also Wizpr ($199, crowdfunded). No clear sales leader yet; these two get the most coverage ([TechCrunch](https://techcrunch.com/2026/03/10/sandbar-secures-23m-series-a-for-its-ai-note-taking-ring), [TechCrunch](https://techcrunch.com/2025/12/09/pebbles-founder-introduces-a-75-ai-smart-ring-for-recording-brief-notes-with-a-press-of-a-button), [New Atlas](https://newatlas.com/wearables/ai-rings-pebble-index-wizpr-sandbar-stream/)) | Hold to record a thought | Sandbar: not stated (*verify*). Pebble: on your phone | Personal voice notes and to-dos, not meeting recording |
| **AI glasses** | Meta Ray-Ban glasses are the best-known (*verify* current models); Meta says Muse is "coming soon to AI glasses" | Camera and mic, on command | Cloud | A camera on your face: never in client meetings or confidential spaces without consent |
| **Watches** | Apple Watch "Audio Intelligence" summaries, opt-in beta (*verify* availability) | On command | Apple | Built into a device many already own |

**Guardrails for devices (1 minute):**
- **Consent and the law.** Many US states require **every** party's consent to record a conversation.
  Tell people you're recording, every time. Many employers ban recorders in meetings.
- **Press-to-record beats always-on** for work. Prefer devices that process on your phone (Pebble) or
  that your employer has approved.
- **Recordings are data.** A meeting transcript holds client names, numbers, and plans: the same golden rule applies.

**Muse facts to use** ([Meta newsroom, Sept 8 2026](https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/)):
for email, you choose whether it only reads or can also send; it checks with you before sensitive actions
like sending or buying; it keeps working after you close the app; it shows an audit trail; you can disconnect
a service at any time and opt out of training. *Verify:* account and age requirements, free limits, the
exact Gmail permission screen (Vinit owns this test with a synthetic account).

## 2. How to judge a model or tool (2 minutes in the room)

- **Leaderboards as a starting point, not an answer.** [LMArena](https://lmarena.ai) ranks models by blind
  human votes; [Artificial Analysis](https://artificialanalysis.ai) compares quality, speed, and price.
- **The real test is your own task.** Run the same sanitized task in two tools and score each 1-5 on:
  1. **Accuracy:** anything wrong or made up?  2. **Specificity:** does it sound like you, or generic?
  3. **Fix time:** minutes to make it sendable.  4. **Data terms:** training, retention, approved at work?
- For agents add: 5. **Control:** does it ask before acting, and can you see and undo what it did?

## 3. Where to keep learning

- Free vendor courses: [Anthropic Academy](https://www.anthropic.com/learn), [OpenAI Academy](https://academy.openai.com),
  [Google AI Essentials](https://grow.google/ai-essentials/), Microsoft Learn's Copilot paths.
- One practical writer on AI at work: Ethan Mollick, [One Useful Thing](https://www.oneusefulthing.org).
- For automation ideas: the Zapier and Make template galleries (browse, don't connect work accounts).
- Vendor prompting guides: each of OpenAI, Anthropic, and Google publishes one; they agree on most points.

## 4. What's changed in prompting (2026)

Primary source: Anthropic's [Claude prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
(read Nov 4, 2026). Background: [Prompt Engineering, Summer 2026](https://acdigest.substack.com/p/prompt-engineering-summer-2026-what) (opinion summary).

1. **Give context and explain why.** The guide says explaining the reason behind an instruction helps the
   model "deliver more targeted responses." Long documents go first, the question last.
2. **Success criteria over step-by-step scripts.** The guide: "Prefer general instructions over prescriptive
   steps"; use numbered steps only "when the order or completeness of steps matters."
3. **Say what to do, not what not to do**, in normal wording. CAPITALS and "you MUST" can make newer models overreact.
4. **Examples:** "Include 3–5 examples for best results," varied enough not to teach unintended patterns.
5. **A one-sentence role** sets focus and tone: "Even a single sentence makes a difference."
6. **Ask it to self-check** against your criteria before it finishes.

Not from the guide but widely used in chat apps: voice brain-dumps, "ask me what you need first," and
"improve my prompt." The guide's own test: "Show your prompt to a colleague with minimal context on the
task... If they'd be confused, Claude will be too."
