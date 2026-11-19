from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET
ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids=set()
        self.links=[]
        self.labels=[]
        self.titles=0
        self.h1=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, ('duplicate id',a['id'])
            self.ids.add(a['id'])
        if tag=='title': self.titles+=1
        if tag=='h1': self.h1+=1
        if tag=='label' and 'for' in a: self.labels.append(a['for'])
        for key in ('src','href'):
            if key in a:
                value=a[key]
                assert value, ('empty link',tag)
                self.links.append(value)
        if a.get('target')=='_blank':
            assert 'noopener' in a.get('rel','').split()
        if tag=='img': assert 'alt' in a
pages={}
for file in ROOT.glob('*.html'):
    data=file.read_text(encoding='utf-8')
    assert 'SecureToken' not in data and 'yusupsupriyadi' not in data
    p=Page();p.feed(data);p.close()
    assert p.h1==1 and p.titles==1, file
    assert set(p.labels)<=p.ids, file
    pages[file.name]=p
for name,p in pages.items():
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc: continue
        target=unquote(u.path).lstrip('/') or ('index.html' if u.path=='/' else name)
        target=target or 'index.html'
        assert (ROOT/target).is_file(), (name,link)
        if u.fragment and target in pages: assert u.fragment in pages[target].ids,(name,link)
ET.parse(ROOT/'sitemap.xml')
home=(ROOT/'index.html').read_text(encoding='utf-8')
cv=(ROOT/'cv.html').read_text(encoding='utf-8')
assert 'src="https://avatars.githubusercontent.com/u/71040617?v=4"' in home
assert 'img-src \'self\' data: https://avatars.githubusercontent.com;' in home
assert 'href="https://github.com/jxxzymix/presskit"' in home
assert 'id="music"' not in home and 'href="#music"' not in home
assert 'performing artist' not in cv and 'DJ and music production' not in cv
assert 'Jos1.PNG' not in home
assert not (ROOT/'assets/CV-Yusup Supriyadi.pdf').exists()
print(f'PASS: {len(pages)} HTML pages, local links, anchors, labels, asset references, sitemap, legacy cleanup')
