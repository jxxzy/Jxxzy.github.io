import json, time, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright, expect
R=Path(__file__).resolve().parents[1]; BASE='http://127.0.0.1:8765'
ART=R/'browser-evidence'; ART.mkdir(exist_ok=True)
server=subprocess.Popen([sys.executable,'-m','http.server','8765','--bind','127.0.0.1'],cwd=R,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
def ready():
    import urllib.request
    for _ in range(50):
        try: urllib.request.urlopen(BASE,timeout=.5).close();return
        except Exception: time.sleep(.1)
    raise RuntimeError('HTTP server not ready')
def mock(route):
    u=route.request.url
    if '/events/' in u: value=[]
    elif '/repos?' in u: value=[{'name':'sample','language':'C#','html_url':'https://github.com/jxxzy/HyperBoostX','fork':False,'description':'Fixture','stargazers_count':1,'updated_at':'2026-11-19'}]
    elif '/releases?' in u: value=[{'tag_name':'v-test','published_at':'2026-01-01','assets':[]}]
    else: value={'public_repos':7,'followers':3,'following':2,'login':'jxxzy'}
    route.fulfill(status=200,content_type='application/json',body=json.dumps(value),headers={'Access-Control-Allow-Origin':'*'})
def visit(p,path):
    response=p.goto(BASE+path,wait_until='domcontentloaded');assert response.status==200
    expect(p.locator('h1')).to_be_visible()
def size(p,label):
    delta=p.evaluate('document.documentElement.scrollWidth - innerWidth')
    assert delta<=2,(label,delta)
try:
    ready()
    with sync_playwright() as pw:
        for engine in ('chromium','firefox','webkit'):
            b=getattr(pw,engine).launch()
            ctx=b.new_context(viewport={'width':1440,'height':900},reduced_motion='reduce',service_workers='block',accept_downloads=True)
            ctx.route('https://api.github.com/**',mock)
            ctx.route('https://avatars.githubusercontent.com/**',lambda r:r.abort())
            ctx.route('https://raw.githubusercontent.com/**',lambda r:r.abort())
            p=ctx.new_page();errors=[];p.on('pageerror',lambda e:errors.append(str(e)))
            for width in (1440,768,390):
                p.set_viewport_size({'width':width,'height':900})
                for path in ('/','/cv.html','/experience.html','/project-hbx.html'):
                    visit(p,path);size(p,(engine,width,path))
                    if engine=='chromium': p.screenshot(path=str(ART/f"{path.strip('/').replace('.html','') or 'home'}-{width}.png"),animations='disabled')
            visit(p,'/experience.html')
            p.locator('#catalog-search').fill('HyperBoostX')
            assert p.locator('.u-project:visible').count()>=2
            p.locator('#catalog-search').fill('unmatched-zzzz')
            assert p.locator('.u-project:visible').count()==0
            p.locator('#catalog-search').fill('')
            expect(p.locator('#compare-output article')).to_have_count(2)
            p.locator('#compare-b').select_option('topo')
            expect(p.locator('#compare-output')).to_contain_text('TopoSurvey')
            p.locator('#terminal-input').fill('help');p.locator('#terminal-form button').click()
            expect(p.locator('#terminal-output')).to_contain_text('projects')
            p.locator('#live-dashboard').click();expect(p.locator('#live-stats')).to_contain_text('7')
            p.locator('#release-load').click();expect(p.locator('#release-results')).to_contain_text('v-test')
            p.locator('#api-run').click();expect(p.locator('#api-output')).to_contain_text('jxxzy')
            p.locator('#run-code').click();expect(p.frame_locator('#code-frame').locator('h2')).to_have_text('Hello, MR.4NONY')
            p.locator('#inquiry-scope').fill('Test scope');p.locator('#inquiry-form button[type=submit]').click()
            expect(p.locator('#inquiry-output')).to_contain_text('Test scope')
            p.locator('#u-contrast').click();assert p.locator('html').evaluate("x=>x.classList.contains('high-contrast')")
            p.locator('#u-contrast').click()
            p.locator('#u-motion').click();expect(p.locator('#u-motion')).to_have_attribute('aria-pressed','true')
            p.locator('#u-motion').click()
            visit(p,'/cv.html');p.locator('#cv-role').select_option('devops');p.locator('#cv-lang').select_option('id')
            expect(p.locator('#cv-pdf')).to_have_attribute('href','/downloads/devops-id-ats.pdf')
            p.wait_for_function("document.querySelector('#cv-preview-projects').children.length>0")
            p.locator('#job-description').fill('C# and GitHub Actions');p.locator('#job-analyze').click()
            expect(p.locator('#tailored-output')).to_contain_text('MR.4NONY')
            expect(p.locator('#cover-output')).to_contain_text('Daslan Josua')
            p.locator('#pdf-preview-load').click();expect(p.locator('#pdf-preview-image')).to_be_visible()
            with p.expect_download() as d: p.locator('#cv-pdf').click()
            assert d.value.suggested_filename.endswith('.pdf')
            assert not errors,(engine,errors)
            ctx.close();b.close();print('PASS',engine,'desktop/tablet/mobile and tested interactions')
        b=pw.chromium.launch();ctx=b.new_context(reduced_motion='reduce');p=ctx.new_page()
        visit(p,'/experience.html');p.wait_for_function('!!navigator.serviceWorker.controller',timeout=25000)
        ctx.set_offline(True);visit(p,'/cv.html');visit(p,'/project-hbx.html')
        ctx.set_offline(False);ctx.close();b.close();print('PASS offline core')
finally:
    server.terminate();server.wait(timeout=5)
