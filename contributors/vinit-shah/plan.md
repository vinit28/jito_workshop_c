# Vinit Shah's Track C workshop plan

Status: **Draft for review**
Author: Vinit Shah
Updated: October 29, 2026
Target duration: 45 minutes

## 1. Position and success

**Audience and promise.** Working professionals with phones, mixed AI experience, and no assumed
paid account. They leave knowing what AI tools can help with, how to choose one, and how to improve
one real work task safely.

**Hypothesis.** If attendees see a short tool map, learn a repeatable prompt pattern, and apply it
to a sanitized version of their own task, then they will identify one useful Monday experiment and
one review or data boundary because the value becomes visible in their own workflow.

**Exit checks.** At least 80% of attendees should be able to (1) name one task AI can help with,
(2) improve a weak prompt with context, intent, format, and constraints, (3) identify one thing
that must not be uploaded, and (4) write a Monday experiment with a human review step and a
measure. We should disconfirm the hypothesis if most attendees only watch the demo, cannot
produce an output, or believe connecting email is required.

**Design call.** Muse is the provisional primary tool because a mobile agent makes AI's value
visible in everyday work. This draft assumes [Muse from Meta](https://ai.meta.com/muse/) is the
intended product, not Muse AI Companion or another app with the same name. Meta describes Muse as
an iPhone and Android personal agent that can connect to apps and ask for permission before some
actions. Confirm this product identity, US availability, exact Gmail connector behavior, age/account
requirements, and current free limits before publishing attendee setup instructions. The core path
must still work without a Gmail connection.

## 2. Attendee preparation and tool choice

**Send before the workshop.** Bring a charged phone and think of one repetitive task you do at work.
Do not bring or upload confidential, personal, financial, customer, credential, or unreleased
information. Write a sanitized version on paper. No app installation or Gmail connection is
required for the core workshop.

| Tool | Role | Access and limits | Data and permission rule | Fallback and evidence |
| --- | --- | --- | --- | --- |
| [Muse from Meta](https://ai.meta.com/muse/) | Required facilitator demo; optional attendee setup after verification | iPhone/Android app; account, age, region, connector, and free-limit details to verify | Treat Gmail, calendar, files, and browser actions as separate permissions. Use a synthetic account or mock screen; never connect attendee work accounts in the room. | Synthetic examples, screenshots, and printed output. Official product page reviewed October 29, 2026; hands-on setup pending. |
| Attendee's existing chat tool | Optional individual practice | Use a tool already available on the attendee's phone; do not require a paid plan or named vendor | Paste only sanitized text; do not connect work apps | Paper prompt card and facilitator's saved output. Availability and limits vary; verify at rehearsal. |

**Muse demonstration setup.** Prepare a fictional Gmail message from “Jordan Lee, Acme Services”
asking to move a project review. Use Muse to draft a concise reply, then edit the draft for accuracy
and tone. Show the exact permission screen before connecting Gmail, select the narrowest useful access,
review the generated draft, and stop before sending. Also show how to disconnect the connector. The
demo account must contain no real mail, contacts, credentials, or payment details.

## 3. Run of show

| Time | Outcome | Facilitator and attendee activity | Fallback |
| --- | --- | --- | --- |
| 00:00-05:00 | See where AI helps | Explain AI as a work partner for drafting, summarizing, research, translation, and repetitive-task planning. Name failure modes: confident errors, generic output, bias, and over-sharing. | Printed tool/use-case cards. |
| 05:00-12:00 | Understand the tool landscape | Map task types to tool types. Use Muse as the browser/email example. Explain that brands differ, but the method transfers. | One-page tool map and screenshots. |
| 12:00-20:00 | Improve an output | Live prompt progression: vague request → add context, intent, audience, format, and constraints → review and iterate. Attendees rewrite a fictional email or agenda prompt on paper. | Printed before/after example. |
| 20:00-25:00 | Apply safety before use | Ask attendees to redact names, account numbers, client details, secrets, and unreleased work. Show the synthetic Gmail draft and mock broad-permission request. Discuss human review and fact-checking. | Paper “safe to share?” card sort. |
| 25:00-38:00 | Use AI on a normal task | Each attendee selects a work task, writes a sanitized input, runs it through a tool if available, and improves the result once. Facilitator circulates using the prompt card. | Printed task, prompt, and saved Muse output. |
| 38:00-42:00 | Map the workflow | Attendees write trigger → AI step → human approval → destination, plus one time or quality measure. Identify what should remain manual. | Paper workflow card. |
| 42:00-45:00 | Leave with a next action | Each attendee writes one Monday experiment, one review rule, and two follow-up tasks for the next 30 days. Invite two quick shares. | Printed commitment card. |

## 4. Facilitator notes

Use these bullets as speaker notes. Every coordinator should cover the same points, even if their
examples and wording differ.

**Where AI helps**

- Drafting: turn rough points into an email, proposal, agenda, or outline.
- Summarizing: reduce a long, supplied text to decisions, actions, and open questions.
- Research: generate search terms, compare supplied sources, and expose missing questions.
- Communication: adjust tone, length, language, and audience while preserving intent.
- Repetitive work: classify, extract, route, and prepare a draft before human approval.
- Learning: explain unfamiliar material, create practice questions, and translate.
- Creation: produce first-pass images, tables, or structures when a human owns the brief and review.
- AI is most useful when the task has a clear goal, enough context, a reviewable output, and a
  meaningful measure of improvement.

**Real-world examples to make the value concrete**

- Customer support agents using an AI assistant resolved about 14% more issues per hour in an
  NBER field study of 5,172 agents; the benefit was larger for newer and lower-skilled workers.
  Use this to explain why AI can help someone who is still learning a workflow, not only an expert.
- In a Harvard and BCG field experiment, consultants using GPT-4 completed eligible knowledge-work
  tasks over 25% faster, with over 40% higher human-rated quality. The study also found that AI can
  hurt performance on tasks outside its capability frontier. Use this to connect speed with judgment.
- Samsung employees reportedly pasted confidential source code and internal meeting content into
  ChatGPT, after which Samsung restricted generative AI use. Use this as a relatable “I pasted the
  wrong thing into a work tool” story, then ask attendees what they would redact.
- In Moffatt v. Air Canada, a customer relied on incorrect bereavement-fare information from the
  airline's chatbot, and the tribunal held Air Canada responsible for the information on its site.
  Use this to show that a polished answer still needs source checking and organizational ownership.

Label the first two examples as research findings, the Samsung example as a reported incident, and
the Air Canada example as a tribunal decision. Do not present any of them as proof that every task
will improve or that one product caused the outcome.

**What to say about tool choice**

- Start with the task, then choose the tool: chat, research, writing, meeting, automation, or agent.
- A chatbot waits for the next instruction. An agent may browse, connect apps, and take actions.
- More capability means more permission and failure surface, not automatic better judgment.
- Use the smallest access and simplest tool that can complete the task.

**What to say about Muse**

- Muse is the worked example, not the only valid AI tool.
- Demonstrate the useful action, then pause at the permission boundary.
- Make clear whether the next step is read, draft, send, edit, or delete.
- Review the exact recipient, content, date, tone, and attachments before any action.
- Never use an attendee's work inbox or ask the room to connect a work account.

**What to say about the attendee task lab**

- Choose a task you do at least weekly and make a sanitized version first.
- Give the model the role, goal, context, audience, format, constraints, and uncertainty request.
- Treat the first answer as a draft. Improve it once, then check it against the original task.
- Keep the human approval step explicit. Save the prompt only after removing sensitive details.

**Questions to ask after each real-world example**

- What part of this task is repetitive, and what part requires judgment?
- What information would you remove before using an AI tool?
- What source, person, or policy would you check before acting on the output?
- What permission would the tool need, and what permission would be unnecessary?
- What simple measure would tell you whether the tool helped?

## 5. Risks and safety demonstrations

| Risk | What attendees should see | Coordinator control |
| --- | --- | --- |
| Sensitive data leakage | Names, client details, financials, credentials, and unreleased work in a prompt | Use synthetic data; redact first; follow employer policy; do not imply paid means approved |
| Excessive permissions | A request for inbox, calendar, files, contacts, or send access when only a draft is needed | Deny or narrow; explain read versus write; show disconnect and account settings |
| Unapproved action | A polished draft sent to the wrong person or an agent acting in the background | Stop before send, purchase, delete, or share; require human approval |
| Hallucination and stale information | Confidently wrong dates, names, facts, or citations | Ask for uncertainty; verify against the source; do not use live mistakes as the only demo |
| Bias and tone drift | Different treatment or an inappropriate tone in a generated message | Inspect assumptions, audience, and language; rewrite and review |
| Retention and third-party processing | Prompt text traveling through the product's provider chain | Show the product privacy/data controls; treat claims as product-specific and time-sensitive |
| Access failure | No app, account, network, or supported phone | Paper prompt cards, screenshots, saved outputs, and a facilitator-led demo |

**Real-world risk examples**

- **Confidentiality:** Samsung's reported code and meeting-content incident makes “do not paste
  company secrets” concrete. The lesson is about data classification and policy, not a claim that
  every public AI tool stores prompts the same way.
- **Incorrect customer guidance:** Air Canada's tribunal case makes the cost of an unchecked answer
  visible. The lesson is to verify policy answers and assign human ownership.
- **False authority:** Lawyers in *Mata v. Avianca* filed nonexistent cases generated by ChatGPT and
  were sanctioned. Use a short saved citation example to teach source verification, not as legal advice.
- **Agent permissions:** Meta describes Muse as able to connect to apps and request approval for
  sensitive actions. Ask attendees to compare “draft this email” with “read and send from my inbox.”
  The lesson is least privilege and explicit approval, even when a product has safeguards.

Do not grant real permissions in the workshop. Every safety demonstration must show the decision
point, the safe choice, and what to do afterward.

## 6. Copyable exercises

**Prompt card.** “I am [role]. I need to [task] for [audience]. Use this context: [sanitized facts].
Return [format and length]. Keep [tone and constraints]. State what you are unsure about. First
give me a draft, then list what I should verify before using it.”

**Synthetic email exercise.** Input: “Hi Jordan, can we move our fictional Acme Services project
review from Tuesday to Thursday at 2 pm? Please confirm.” Ask Muse for a concise, warm reply with
the new date and a request to confirm. Then ask attendees to check the date, recipient, tone, and
whether the output invented any facts. Expected lesson: AI can accelerate drafting, but the human
owns accuracy and sending.

**Data and permissions exercise.** Show two versions of a request: one containing a client name,
contract value, phone number, and unreleased launch date; one with placeholders. Ask what to remove
and whether the tool needs inbox-wide access. Expected lesson: sanitize first, deny unnecessary
access, and never treat a free or paid label as employer approval.

## 7. Slide deck and delivery readiness

**Draft deck, in this order:**

1. Title, audience, and the promise: make one work task better safely.
2. Where AI helps: the task-based map above.
3. Chatbot, copilot, and agent: what changes when a tool can act.
4. Muse setup: app link, account prerequisites, exact screen sequence, and what not to connect.
5. Muse Gmail demo: synthetic message, permission review, draft, human edit, stop before send.
6. Prompt anatomy: role, goal, context, audience, format, constraints, uncertainty.
7. Personal task lab instructions and timer.
8. Risk checkpoint: data, permissions, actions, output review, and bias.
9. Workflow card: trigger → AI step → human approval → destination.
10. 30-day plan and Monday commitment.

Create facilitator notes for every slide using the bullets above. Prepare a no-network PDF, device
screenshots, synthetic Gmail account or mock screens, prompt cards, risk cards, and printed outputs.

**Takeaway and readiness**

- **30-day plan:** week 1 drafting, week 2 summarizing or research, week 3 repetitive-task mapping;
  measure minutes saved or quality improved; review every output before it leaves the desk.
- **Failure plan:** no Wi-Fi or account uses paper and saved examples; unsupported phone uses the
  facilitator demo; Muse's free limit means attendees do not depend on live Muse requests.
- **Facilitator checklist:** test Muse on the presentation device; prepare synthetic Gmail page,
  screenshots, prompt cards, safe-to-share cards, and printed outputs; rehearse at 45 minutes;
  cut the tool tour first if time slips, never the safety checkpoint or task lab.
- **Open decisions:** confirm the exact Muse product and official app link; verify mobile setup,
  Gmail connector, permissions, region, age/account requirements, and free limits; confirm room
  Wi-Fi and display; select a second phone-accessible fallback; confirm exact draft cutoff and
  session assignments.

**Self-review:** [x] 45 minutes [x] phone/free core path [x] offline path [x] safety examples
[x] complete prompts [x] outcome checks [x] no sensitive data [ ] Muse mobile test
[ ] peer rehearsal [ ] coordinator review.

**Sources:** [Meta Muse](https://ai.meta.com/muse/), [Meta Muse productivity](https://ai.meta.com/muse/productivity/),
[Muse from Meta in the App Store](https://apps.apple.com/us/app/muse-from-meta/id6760173601), the
[NBER customer-support study](https://www.nber.org/system/files/working_papers/w31161/revisions/w31161.rev0.pdf),
[Harvard and BCG field experiment](https://aiinstitute.hbs.edu/navigating-the-jagged-technological-frontier/),
[Samsung incident summary](https://oecd.ai/en/incidents/2023-04-06-93c9), [CanLII's Air Canada case summary](https://blog.canlii.org/2024/03/),
[Mata v. Avianca sanctions order](https://www.nhd.uscourts.gov/sites/default/files/pdf/Mata-v-Avianca-sanctions-order.PDF),
and the [Track C brief](../../docs/workshop-brief.md). The previously cited [Muse AI Companion FAQ](https://getmuseai.app/faq)
describes a different browser extension and should not be used for Meta Muse setup claims.
