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

**Design call.** Muse is the provisional primary facilitator demo because it makes the value of AI
beside a work page or email easy to see. Muse is not yet an attendee prerequisite. Its official FAQ
describes a Chrome/Edge browser extension, a one-request-per-day free tier, and Gmail drafting from
the open message without Gmail API access or automatic sending. Phone support must be verified
before we ask attendees to use it directly. Until then, the core path uses sanitized text and a
saved output, with Muse run by the facilitator on a synthetic example.

## 2. Attendee preparation and tool choice

**Send before the workshop.** Bring a charged phone and think of one repetitive task you do at work.
Do not bring or upload confidential, personal, financial, customer, credential, or unreleased
information. Write a sanitized version on paper. No app installation or Gmail connection is
required for the core workshop.

| Tool | Role | Access and limits | Data and permission rule | Fallback and evidence |
| --- | --- | --- | --- | --- |
| [Muse AI Companion](https://getmuseai.app/faq) | Required facilitator demo; optional attendee trial if mobile support is verified | Chrome/Edge extension; no Muse login; free tier says one AI request per day | Reads page context only when invoked; official FAQ says it does not use Gmail API, list/download inbox, or send mail. Never use real email in the demo. | Synthetic Gmail page, screenshots, and printed output. Docs reviewed October 29, 2026; device test pending. |
| Attendee's existing chat tool | Optional individual practice | Use a tool already available on the attendee's phone; do not require a paid plan or named vendor | Paste only sanitized text; do not connect work apps | Paper prompt card and facilitator's saved output. Availability and limits vary; verify at rehearsal. |

**Muse demonstration setup.** Prepare a fictional Gmail message from “Jordan Lee, Acme Services”
asking to move a project review. Use Muse to draft a concise reply, then edit the draft for accuracy
and tone. Show that the facilitator chooses the Gmail reply action, reviews the inserted draft,
and sends nothing. Also show a mock permission request for broad inbox access; the correct response
is to deny or narrow access. The mock screen must not grant a real permission.

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

## 4. Copyable exercises and safety demonstrations

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

## 5. Takeaway and delivery readiness

- **30-day plan:** week 1 drafting, week 2 summarizing or research, week 3 repetitive-task mapping;
  measure minutes saved or quality improved; review every output before it leaves the desk.
- **Failure plan:** no Wi-Fi or account uses paper and saved examples; unsupported phone uses the
  facilitator demo; Muse's free limit means attendees do not depend on live Muse requests.
- **Facilitator checklist:** test Muse on the presentation device; prepare synthetic Gmail page,
  screenshots, prompt cards, safe-to-share cards, and printed outputs; rehearse at 45 minutes;
  cut the tool tour first if time slips, never the safety checkpoint or task lab.
- **Open decisions:** verify Muse mobile availability; confirm room Wi-Fi and display; decide whether
  organizers permit a facilitator browser extension; select a second phone-accessible fallback;
  confirm exact draft cutoff and session assignments.

**Self-review:** [x] 45 minutes [x] phone/free core path [x] offline path [x] safety examples
[x] complete prompts [x] outcome checks [x] no sensitive data [ ] Muse mobile test
[ ] peer rehearsal [ ] coordinator review.

**Sources:** [Muse FAQ](https://getmuseai.app/faq), [Muse email assistant](https://getmuseai.app/ai-email-assistant),
[Muse terms](https://getmuseai.app/terms), and the [Track C brief](../../docs/workshop-brief.md).
