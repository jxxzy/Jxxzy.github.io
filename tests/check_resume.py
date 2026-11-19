from pathlib import Path
import json, zipfile, subprocess, re
from xml.etree import ElementTree as ET
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'data/resume.json').read_text())
M=json.loads((R/'data/resume-manifest.json').read_text())
assert len(D['roles'])==11 and len(D['projects'])==6 and len(M)==66
for entry in M:
    p=R/entry;assert p.is_file() and p.stat().st_size>1000,p
    if p.suffix=='.pdf':
        info=subprocess.check_output(['pdfinfo',str(p)],text=True)
        assert re.search(r'Pages:\s+[12]\b',info),p
        txt=subprocess.check_output(['pdftotext',str(p),'-'],text=True)
        assert D['person']['name'] in txt and 'MR.4NONY' in txt,p
    else:
        with zipfile.ZipFile(p) as z:
            assert z.testzip() is None,p
            txt=' '.join(ET.fromstring(z.read('word/document.xml')).itertext())
            assert D['person']['name'] in txt and 'MR.4NONY' in txt,p
print('PASS: 44 PDF, 22 DOCX, text extraction, ZIP integrity and page count')
