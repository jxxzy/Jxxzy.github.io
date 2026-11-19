from pathlib import Path
import subprocess, math
from PIL import Image, ImageOps, ImageDraw
R=Path(__file__).resolve().parents[1]
previews=R/'previews'; previews.mkdir(exist_ok=True)
review=R/'review';review.mkdir(exist_ok=True)
tmp=review/'rendered';tmp.mkdir(exist_ok=True)
pdfs=sorted((R/'downloads').glob('*.pdf'))
for f in pdfs:
    subprocess.run(['pdftoppm','-f','1','-l','1','-r','90','-png','-singlefile',str(f),str(previews/f.stem)],check=True)
    subprocess.run(['pdftoppm','-r','75','-png',str(f),str(tmp/f.stem)],check=True)
docxdir=review/'docx-converted';docxdir.mkdir(exist_ok=True)
docs=sorted((R/'downloads').glob('*.docx'))
subprocess.run(['libreoffice','-env:UserInstallation=file:///tmp/mr4nony-lo','--headless','--convert-to','pdf','--outdir',str(docxdir),*map(str,docs)],check=True)
assert len(list(docxdir.glob('*.pdf')))==len(docs)
for f in docxdir.glob('*.pdf'):
    subprocess.run(['pdftoppm','-r','75','-png',str(f),str(tmp/('docx-'+f.stem))],check=True)
items=sorted(tmp.glob('*.png'))
for start in range(0,len(items),12):
    batch=items[start:start+12];sheet=Image.new('RGB',(1200,math.ceil(len(batch)/4)*450),'#e6e8ec');draw=ImageDraw.Draw(sheet)
    for i,p in enumerate(batch):
        im=Image.open(p).convert('RGB');im.thumbnail((285,410));x=(i%4)*300+7;y=(i//4)*450+26;sheet.paste(im,(x,y));draw.text((x,y-19),p.stem[:43],fill='black')
    sheet.save(review/f'sheet-{start//12+1:02}.png')
assert len(list(previews.glob('*.png')))==44
print('Rendered',len(pdfs),'PDFs and',len(docs),'DOCX; visual sheets for human review')
