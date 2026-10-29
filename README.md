# JITO Workshop Track C: AI for Career & Productivity

Three independent proposals, one shared workshop that any coordinator can run alone.
Coordinators: **Aditya Singh, Dhruv Gupta, Vinit Shah**.

Our audience is working professionals. Assume attendees have only a phone, mixed AI experience,
and no paid AI subscription. Help them do useful work, judge the output, and protect their data.
This is a practical career and productivity workshop, not a tour of every AI product.

## Start here

1. Read [the shared contract](AGENTS.md) and [the source brief](docs/workshop-brief.md).
2. Work in your folder below. Replace the starter with your own proposal using
   [the common template](templates/workshop-plan.md).
3. Submit one complete `plan.md`. Supporting synthetic examples may live in your folder.
4. Compare the proposals in [selection notes](final/selection.md), then assemble
   [the consolidated plan](final/plan.md). Preserve the independent proposals.

| Coordinator | Deliverable | Initial state |
| --- | --- | --- |
| Aditya Singh | [Individual plan](contributors/aditya-singh/plan.md) | Not started |
| Dhruv Gupta | [Individual plan](contributors/dhruv-gupta/plan.md) | Not started |
| Vinit Shah | [Individual plan](contributors/vinit-shah/plan.md) | Not started |

Update status inside your plan; this table only records the initial setup.

## Timing and collaboration

- **Individual drafts: Monday, November 2, 2026.** Date interpreted from the October 28 request;
  exact cutoff and timezone remain to be agreed.
- After drafts: compare, select, and rehearse. Alignment and final freeze dates remain open.
- Event: Sunday, November 15, 2026. The published brief lists rounds at 2:15 pm and 3:00 pm;
  confirm each coordinator's assignment with organizers.
- Pick one integration owner together. Until named, nobody approves a final plan on others' behalf.

Use `proposal/<first-last>` branches and pull requests into `main`. Keep each PR focused on your
folder; propose shared contract changes separately. Review another person's plan after your own
first draft. Agents must not overwrite another contributor's work.

## Using any AI tool

The shared contract is plain Markdown in `AGENTS.md`. It is the single source of truth for
contributors using Claude, Grok/Grokbot, or any other assistant. File discovery depends on the
product and configuration, so always use the explicit prompt below.

- **Repo-connected agents:** open this repository and ask the agent to read the three files named
  below. `CLAUDE.md` also points Claude Code to the shared contract.
- **Chat-only assistants:** upload or paste `AGENTS.md`, `docs/workshop-brief.md`, and
  `templates/workshop-plan.md` with the prompt. A repository URL alone does not guarantee access.
  If browsing is unavailable, mark changing tool claims unverified for a contributor to check.
- **Saving the result:** if the assistant cannot edit files, request the complete Markdown and
  save it in your own `contributors/<first-last>/plan.md`, then submit through the same Git workflow.

Before drafting, ask the assistant to confirm the coordinator name, output path, 45-minute limit,
phone/free-access constraint, and required safety examples. This checks that it received the contract.

## Ask your agent

> Read AGENTS.md, docs/workshop-brief.md, and templates/workshop-plan.md from the repo or the
> attached/pasted copies. If you cannot access them, tell me before drafting. I am [full name].
> Develop my independent Track C proposal in contributors/[first-last]/plan.md. Follow the common
> requirements, verify tools against official sources, and distinguish research from device tests.
> Keep the plan to 1-3 pages with clearly linked optional supporting assets. Do not alter the other
> proposals or consolidate them yet. Ask only for information that blocks a credible draft.

For consolidation, explicitly ask the agent to compare all three submitted plans using
`final/selection.md` before drafting `final/plan.md`.

No dependencies to install. This repository currently contains planning documents only.
