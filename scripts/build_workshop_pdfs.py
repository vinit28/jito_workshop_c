"""Build the print packet and coordinator references. Requires reportlab and pypdf."""
from pathlib import Path
from io import BytesIO
import re
import subprocess
from xml.sax.saxutils import escape

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

ROOT = Path(__file__).resolve().parents[1]
W, H = 612, 792
INK = colors.HexColor('#14212D')
TEAL = colors.HexColor('#087F78')
STYLES = getSampleStyleSheet()
STYLES.add(ParagraphStyle('BodyPrint', fontName='Helvetica', fontSize=10,
                          leading=12, spaceAfter=3, textColor=INK))
STYLES.add(ParagraphStyle('BulletPrint', parent=STYLES['BodyPrint'],
                          leftIndent=10, firstLineIndent=-7, spaceAfter=3))
STYLES.add(ParagraphStyle('TitlePrint', fontName='Helvetica-Bold', fontSize=19,
                          leading=22, spaceAfter=7, textColor=INK))
STYLES.add(ParagraphStyle('SectionPrint', fontName='Helvetica-Bold', fontSize=11.5,
                          leading=14, spaceBefore=5, spaceAfter=4, textColor=INK))
STYLES.add(ParagraphStyle('Packet', fontName='Helvetica', fontSize=10,
                          leading=13, spaceAfter=6, textColor=INK))


def rich(s):
    s = escape(s)
    s = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    return s


def footer(c, doc):
    c.setFont('Helvetica', 8)
    c.setFillColor(colors.HexColor('#53616E'))
    c.drawString(44, 25, 'JITO USA | Track C | November 15, 2026 | Coordinator reference')
    c.drawRightString(W - 44, 25, str(doc.page))


def reference(src, dst):
    flow, pending = [], []

    def flush():
        if pending:
            flow.append(Paragraph(rich(' '.join(pending)), STYLES['BodyPrint']))
            pending.clear()

    for line in src.read_text().splitlines():
        if line == '<!-- pagebreak -->':
            flush()
            flow.append(PageBreak())
        elif line.startswith('# '):
            flush()
            flow.append(Paragraph(rich(line[2:]), STYLES['TitlePrint']))
        elif line.startswith('## '):
            flush()
            flow.append(Paragraph(rich(line[3:]), STYLES['SectionPrint']))
        elif line.startswith('- '):
            flush()
            flow.append(Paragraph('&#8226; ' + rich(line[2:]), STYLES['BulletPrint']))
        elif not line.strip():
            flush()
        else:
            pending.append(line)
    flush()
    doc = SimpleDocTemplate(str(dst), pagesize=(W, H), rightMargin=44,
                            leftMargin=44, topMargin=38, bottomMargin=38,
                            title=src.stem.replace('-', ' ').title(), author='Track C coordinators')
    doc.build(flow, onFirstPage=footer, onLaterPages=footer)


def packet_page(kind):
    b = BytesIO()
    c = canvas.Canvas(b, pagesize=(W, H))
    # Reuse only the letterhead artwork, not hidden obsolete body text.
    header = subprocess.run([
        'pdftoppm', '-f', '1', '-singlefile', '-r', '200', '-x', '0', '-y', '0',
        '-W', '1700', '-H', '300', '-png',
        str(ROOT / 'worksheets/source/Track-C-Agenda-and-Exit-Card.pdf'),
    ], check=True, capture_output=True).stdout
    c.drawImage(ImageReader(BytesIO(header)), 0, 684, W, 108)
    c.setFillColor(colors.HexColor('#53616E'))
    c.setFont('Helvetica', 7.5)
    c.drawCentredString(W / 2, 30,
                       'Track C | AI for Career and Productivity | JITO USA AI Summit | November 15, 2026')

    def text(s, x, y, width=510, size=10):
        style = ParagraphStyle('At', parent=STYLES['Packet'], fontSize=size, leading=size * 1.28)
        p = Paragraph(s, style)
        _, height = p.wrap(width, 700)
        p.drawOn(c, x, y - height)
        return y - height - 7

    def heading(s, y, size=12):
        return text('<b>' + s + '</b>', 51, y, size=size)

    def check(s, y):
        c.setStrokeColor(INK)
        c.rect(52, y - 10, 7, 7, stroke=1, fill=0)
        return text(s, 66, y, width=492, size=10)

    if kind == 'agenda':
        y = heading('AI for Career and Productivity Workshop Agenda', 673, 18)
        y = text('AI for Career and Productivity | 45 minutes | November 15, 2026', 51, y)
        rows = [('Time', 'Segment', 'What you do'),
                ('2 min', 'Intro', 'House rules and the goal'),
                ('5 min', 'Tool landscape', 'Where AI helps; choose the tool and access'),
                ('5 min', 'Prompting', 'Four parts, one habit, a clear quality bar'),
                ('25 min', 'Five-part exercise', 'Prompt; brief and draft; make a document; judge and improve; map an agent'),
                ('5 min', 'Evaluation and guardrails', 'Check facts, AI slop, data and permissions'),
                ('3 min', 'Wrap-up and next steps', 'Write your experiment and complete the exit card')]
        rows = [[Paragraph(escape(v), STYLES['Packet']) for v in row] for row in rows]
        table = Table(rows, colWidths=[53, 144, 313])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#EAEFF1')),
            ('GRID', (0, 0), (-1, -1), .45, colors.HexColor('#BAC3CA')),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 7),
            ('RIGHTPADDING', (0, 0), (-1, -1), 7),
            ('TOPPADDING', (0, 0), (-1, -1), 7),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ]))
        _, th = table.wrap(510, 500)
        table.drawOn(c, 51, y - th)
        y -= th + 16
        y = text('<b>Use the packet in order:</b> agenda; exercise front and back; evaluation and exit card. '
                 'Each of the five exercise parts takes five minutes.', 51, y)
        y = text('<b>Participation:</b> email connection is optional. Follow a willing neighbor if you prefer; '
                 'the owner holds the phone and chooses what to show. Use only non-sensitive material. '
                 'Draft only; nothing is sent, paid, deleted or publicly shared.', 51, y)
        assert y > 220, ('Agenda body overlaps QR area', y)
        heading('Connect with your coordinators on LinkedIn', 207, 10)
        for name, slug, center in [
            ('Aditya Singh', 'aditya-singh', 136),
            ('Dhruv Gupta', 'dhruv-gupta', 306),
            ('Vinit Shah', 'vinit-shah', 476),
        ]:
            c.drawImage(str(ROOT / 'worksheets' / 'assets' / (slug + '-linkedin-qr.png')),
                        center - 35, 108, 70, 70, preserveAspectRatio=True, mask='auto')
            c.setFillColor(INK)
            c.setFont('Helvetica-Bold', 9)
            c.drawCentredString(center, 96, name)
        c.setFont('Helvetica', 8)
        c.drawCentredString(W / 2, 77, 'Scan a QR code to connect on LinkedIn.')
    else:
        y = heading('Evaluation and Exit Card', 673, 18)
        y = text('Complete at minutes 37-45.', 51, y)
        y = text('Name (optional): ______________________________  Table: ______', 51, y)
        y = heading('A  Evaluate your tool and your judgment', y)
        y = text('Tick what you checked. If something failed, note why beside it.', 51, y)
        for s in ['Does it do the job?', 'Is it accurate against the original source?',
                  'Is it fast enough, including checking and fixing?',
                  'Is the access appropriate for this task?', 'Would I use it again for this task?']:
            y = check(s, y)
        y = text('<b>AI slop:</b> what was generic, invented, repetitive or unnecessary?', 51, y)
        y = text('What I changed or deleted: __________________________________________', 51, y)
        y = heading('Green / Yellow / Red', y)
        y = text('GREEN: appropriate to share. YELLOW: check policy or permission first. '
                 'RED: do not upload in this workshop. Keep credentials, confidential records and private details out.', 51, y)
        y = text('Public job posting: ____  Fictional meeting time: ____  Internal notes: ____<br/>'
                 'Client financial record: ____  Password: ____', 51, y)
        y = heading('B  Check your work and choose the next step', y)
        for s in ['A familiar task, chosen tool and written "good looks like" definition.',
                  'One improvement with a measure (time, errors or edits).',
                  'A workflow with human approval, estimated value and an access boundary.',
                  'A concrete next step and date.']:
            y = check(s, y)
        y = text('Today I: [ ] generated output  [ ] followed a neighbor  [ ] worked on paper', 51, y)
        y = heading('Your 30-day experiment', y)
        y = text('Week 1: draft. Week 2: summarize/research. Week 3: map a workflow.<br/>'
                 'Week 4: repeat what worked and compare with your starting point.', 51, y)
        y = text('My next step: ______________________________  By: ______________<br/>'
                 'My measure: __________________________________________________', 51, y)
        y = text('Share a sanitized result at work if appropriate. Measure time including review and fixes; '
                 'do not claim savings you have not measured.', 51, y, size=9)
        assert y > 57, ('Exit body exceeds page', y)
    c.showPage()
    c.save()
    return PdfReader(BytesIO(b.getvalue())).pages[0]


def main():
    final = ROOT / 'final'
    reference(final / 'plan.md', final / 'plan.pdf')
    reference(final / 'facilitator-run-sheet.md', final / 'facilitator-run-sheet.pdf')
    writer = PdfWriter()
    writer.add_page(packet_page('agenda'))
    original = PdfReader(ROOT / 'worksheets/Track-C-Worksheet-final.pdf')
    for page in original.pages:
        writer.add_page(page)
    writer.add_page(packet_page('exit'))
    writer.add_metadata({'/Title': 'AI for Career and Productivity Workshop Packet', '/Author': 'Track C coordinators',
                         '/Subject': 'Agenda, final exercise, evaluation and exit card'})
    target = ROOT / 'worksheets/Track-C-Workshop-Packet.pdf'
    with target.open('wb') as out:
        writer.write(out)
    for f in [target, final / 'plan.pdf', final / 'facilitator-run-sheet.pdf']:
        print(f.relative_to(ROOT), len(PdfReader(f).pages), 'pages')


if __name__ == '__main__':
    main()
