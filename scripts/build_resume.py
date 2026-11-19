from pathlib import Path
import json, textwrap
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from xml.sax.saxutils import escape
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'data/resume.json').read_text())
out=R/'downloads';out.mkdir(exist_ok=True)
manifest=[]
def content(role,lang):
    i=int(lang=='id')
    def t(a,b): return b if i else a
    p=D['person']
    rows=[('name',p['name']),('role',role[1+i]+' | MR.4NONY'),('contact','Cimahi, West Java, Indonesia | '+p['email']),('contact',p['github']+' | https://jxxzy.github.io/'),
    ('heading',t('PROFESSIONAL SUMMARY','RINGKASAN PROFESIONAL')),('body',t('Software developer and founder of NEXORAID with hands-on project experience. ','Software developer dan pendiri NEXORAID dengan pengalaman proyek. ')+role[3+i]),
    ('heading',t('EXPERIENCE & CONTRIBUTIONS','PENGALAMAN & KONTRIBUSI')),('sub',t('Founder / NEXORAID','Pendiri / NEXORAID')),('body',t('Manage digital services and software initiatives, product direction and public repositories.','Mengelola inisiatif layanan digital dan software, arah produk dan repositori publik.')),
    ('sub',t('GitHub Workflow contributor / TopoSurvey (team)','Kontributor GitHub Workflow / TopoSurvey (tim)')),('body',t('Team scope: repository management, CI/CD, tests, SemVer, Android build and release workflows.','Cakupan tim: manajemen repositori, CI/CD, tes, SemVer, build Android dan workflow rilis.')),
    ('heading',t('TECHNICAL SKILLS','KEAHLIAN TEKNIS')),('body','; '.join(x[2] for x in D['skillGroups'])),
    ('heading',t('SELECTED PROJECTS','PROYEK PILIHAN'))]
    for key in role[5].split(','):
        p=next(x for x in D['projects'] if x[0]==key)
        rows += [('sub',p[1]+' | '+p[2+i]),('body',p[5+i]),('link',p[7])]
    rows += [('heading',t('EDUCATION','PENDIDIKAN')),('body','Universitas Logistik dan Bisnis Internasional (ULBI) - D4 Teknik Informatika'),('heading',t('RESEARCH INTERESTS','MINAT PENELITIAN')),('body',D['research'][i])]
    return rows
def pdf(path,rows,professional):
    ink=colors.HexColor('#18202C');accent=colors.HexColor('#44356E') if professional else ink
    styles={}
    for x,size,lead,font,space in [('name',21,24,'Helvetica-Bold',4),('role',12,15,'Helvetica-Bold',5),('contact',9,12,'Helvetica',1),('heading',11,15,'Helvetica-Bold',5),('sub',10,13,'Helvetica-Bold',3),('body',9.5,13,'Helvetica',4),('link',8.5,11,'Helvetica',3)]:
        styles[x]=ParagraphStyle(x,fontName=font,fontSize=size,leading=lead,textColor=accent if x in ('heading','role') else ink,spaceBefore=8 if x=='heading' else 2 if x=='sub' else 0,spaceAfter=space,keepWithNext=x in ('heading','sub','name','role'),splitLongWords=True)
    if professional: styles['heading'].backColor=colors.HexColor('#EFEDF7');styles['heading'].borderPadding=4
    story=[]
    for k,v in rows:
        text=escape(v)
        if k=='link': text='<link href="'+escape(v)+'" color="#44356E">'+text+'</link>'
        story.append(Paragraph(text,styles[k]))
    def foot(c,d):
        c.setFillColor(colors.HexColor('#5C6170'));c.setFont('Helvetica',8);c.drawString(42,25,'MR.4NONY');c.drawRightString(A4[0]-42,25,str(d.page))
    SimpleDocTemplate(str(path),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=42,bottomMargin=42,title='MR.4NONY Resume',author=D['person']['name']).build(story,onFirstPage=foot,onLaterPages=foot)
def word(path,rows):
    doc=Document();s=doc.sections[0];s.page_width=Mm(210);s.page_height=Mm(297);s.top_margin=s.bottom_margin=Mm(15);s.left_margin=s.right_margin=Mm(16)
    normal=doc.styles['Normal'];normal.font.name='Arial';normal.font.size=Pt(10);normal.paragraph_format.space_after=Pt(3)
    for k,v in rows:
        p=doc.add_paragraph();p.paragraph_format.keep_with_next=k in ('heading','sub','name','role')
        p.paragraph_format.space_before=Pt(9 if k=='heading' else 3 if k=='sub' else 0)
        run=p.add_run(v);run.bold=k in ('heading','sub','name','role');run.font.size=Pt({'name':21,'role':12,'heading':11,'sub':10,'contact':9,'link':9}.get(k,10));run.font.color.rgb=RGBColor.from_string('44356E' if k in ('heading','role') else '18202C')
    doc.core_properties.author=D['person']['name'];doc.core_properties.title='MR.4NONY Resume';doc.save(path)
for role in D['roles']:
    for lang in ('en','id'):
        rows=content(role,lang)
        for style in ('ats','professional'):
            p=out/f'{role[0]}-{lang}-{style}.pdf';pdf(p,rows,style=='professional');manifest.append(str(p.relative_to(R)))
        p=out/f'{role[0]}-{lang}.docx';word(p,rows);manifest.append(str(p.relative_to(R)))
(R/'data/resume-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Generated',len(manifest),'documents')
