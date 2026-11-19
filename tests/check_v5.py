from pathlib import Path
import json,re
R=Path(__file__).resolve().parents[1]
P=json.loads((R/'data/projects.json').read_text())
assert len(P)==10
for p in P:
    page=(R/f"project-{p['id']}.html").read_text()
    assert p['url'] in page and 'id="architecture"' in page
assert sum(len(p['media']) for p in P)==4
hub=(R/'experience.html').read_text()
cv=(R/'cv.html').read_text()
for section in ['workspace','catalog','compare','github','releases','library','playground','api','snippets','records','inquiry','settings','status']:
    assert f'id="{section}"' in hub
for control in ['job-description','job-analyze','tailored-download','cover-download','pdf-preview-load']:
    assert f'id="{control}"' in cv
manifest=json.loads((R/'manifest.webmanifest').read_text())
assert manifest['start_url']=='/' and manifest['display']=='standalone'
sw=(R/'sw.js').read_text()
for path in json.loads(re.search(r'const CORE=(\[[^;]+\]);',sw).group(1)):
    assert path=='/' or (R/path.lstrip('/')).is_file(),path
assert (R/'assets/career-qr.svg').is_file()
assert len(list((R/'downloads').glob('*.pdf')))==44
assert len(list((R/'downloads').glob('*.docx')))==22
print('PASS: 10 project records, 13 experience sections, 4 media refs, career tools, complete core cache list and 66 documents')
