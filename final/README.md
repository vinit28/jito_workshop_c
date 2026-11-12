# Track C print files

Print [the four-page participant packet](../worksheets/Track-C-Workshop-Packet.pdf): 200 copies, US Letter, duplex, long-edge flip. Two sheets per packet.

Coordinators use [the three-page run sheet](facilitator-run-sheet.pdf), single-sided. [The two-page plan](plan.pdf) describes curriculum, outcomes and readiness checks. Sources: `plan.md`, `facilitator-run-sheet.md`, `../scripts/build_workshop_pdfs.py`.

## Packet assembly

1. Updated agenda, with the three supplied LinkedIn QR images in a compact bottom row.
2. Original `worksheets/Track-C-Worksheet-final.pdf`, page 1, unchanged.
3. Original `worksheets/Track-C-Worksheet-final.pdf`, page 2, unchanged.
4. Evaluation and exit card.

The supplied agenda/exit source is retained in `worksheets/source/Track-C-Agenda-and-Exit-Card.pdf`. Its letterhead is reused. Its 20-minute exercise allowance is corrected to 25; the new schedule totals 45 minutes. There is no account-demo path. Anyone declining email connection may follow a willing neighbor who controls what is shown. Paper reasoning remains available if sharing is unsuitable.

The original exercise is preserved. Its "back" is page 3 in the new packet; print all four pages in order. Older `final/worksheets/` exports and `plan-proposed.md` are superseded.

## Rebuild and verify

Run `python3 scripts/build_workshop_pdfs.py` from the repo root with reportlab, pypdf and Poppler installed. It writes the packet and two coordinator PDFs. Render every page before printing. QR images are supplied by Vinit and embedded without alteration. Their payloads were decoded locally; the printed codes target:

- Aditya Singh: https://www.linkedin.com/in/adityas5/
- Dhruv Gupta: https://www.linkedin.com/in/dhruv-gupta-dev/
- Vinit Shah: https://www.linkedin.com/in/vinit-shah/

Scan a printed sample before the full run; decoder success does not verify profile ownership beyond the names supplied with the images.

The files are print-formatted, not evidence of rehearsal or agreement. Keep `selection.md` honest about approval and tests. Do not print the older three-worksheet set as well as the packet.
