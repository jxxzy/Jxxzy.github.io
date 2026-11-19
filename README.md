# MR.4NONY — Developer Portfolio

Developer portfolio of Josua Siahaan (MR.4NONY) — software engineering, open source and NEXORAID. The separate DJ presskit is at https://github.com/jxxzymix/presskit.

Live: https://jxxzy.github.io/

## Development

Dependency-free static HTML, CSS and JavaScript. Run `python3 -m http.server 8000` in the repository and visit http://localhost:8000. GitHub Pages serves the main branch root. No build step or secret is required.

## Features

- Responsive premium bento layout, GitHub profile avatar, canvas particles, orbit, ticker and reveal animations. Reduced motion support.
- English/Indonesian interface and persistent theme preferences.
- Filterable project cards, optional public GitHub statistics, printable résumé and email-client draft contact.
- Canonical URLs, Open Graph, JSON-LD, favicon, robots and sitemap, custom 404 and privacy page.
- No SMTP credentials, analytics or externally loaded scripts. The profile avatar is loaded from GitHub's avatar CDN. The contact form does not send directly; it opens an email draft. No employment or certification claims imported from the old template.

## Checks

Run `python3 tests/check_site.py` and `node --check assets/js/main.js`. Browser, accessibility and Lighthouse validation should be performed separately before declaring a measured quality score.

## Security follow-up

Revoke the old SMTPJS token through its provider; removal from current files does not remove prior Git history or revoke the token. Historical copies of the old third-party CV and address may remain in Git history. No history rewrite was performed. Review profile content before job applications.

## License

See LICENSE. Original personal media remains subject to its owner's rights.

## Engineering edition

### Implemented navigation and functions

1. 26 homepage sections
2. Command palette and searchable navigation
3. Keyboard Ctrl/Cmd+K
4. Search projects
5. Category filters
6. Alphabetical sort
7. Saved projects
8. Saved-only filter
9. Project count
10. Case study accordions
11. Public GitHub profile stats
12. Live repository explorer
13. Repository search
14. Repository sort
15. Fork visibility filter
16. Recent public GitHub events
17. JSON validation
18. JSON formatting
19. JSON minification
20. Copy formatted JSON
21. Text character and word counter
22. URL encoder
23. URL decoder
24. Copy transformed text
25. Local SHA-256 file checksum
26. Copy checksum
27. Color contrast checker
28. Copy developer alias
29. Copy email address
30. Contact topic selector
31. Email draft form
32. Theme switch
33. Language switch
34. Pause/resume animation
35. Back to top
36. Printable résumé
37. FAQ accordions
38. Open-source links
39. DJ presskit redirect
40. Privacy page
41. Custom 404

### Implemented motion effects (38)

1. Canvas particles
2. Pointer particle links
3. Hero entrance
4. Portrait entrance
5. Orbit rotation
6. Reverse orbit
7. Floating tags
8. Status pulse
9. Ticker marquee
10. Scroll reveal rise
11. Reveal left
12. Reveal right
13. Reveal zoom
14. Reveal clip
15. Reveal perspective
16. Gradient drift
17. Signal pulse
18. Portrait glow
19. HUD pulse
20. Hero scan
21. Scroll cue
22. Heading line
23. Card spotlight
24. Project art perspective
25. Project symbol zoom
26. Timeline node hover
27. Tag lift
28. Concept ring glow
29. Concept bar breathing
30. Detail expansion
31. Architecture flow pulse
32. NEXORAID float
33. Saved star pop
34. Results entrance
35. Command dialog entrance
36. Toast entrance
37. Nav underline
38. Button lift

Motion is disabled by the preference toggle or OS reduced-motion setting. Illustrations are conceptual, not product screenshots or live telemetry. Research treatments are proposals, not publication or measured results. Live GitHub features depend on public API availability and rate limits. Developer toolbox processes user inputs locally. The alias, photo and DJ link remain separate.

## Career Center

The web resume provides 11 career/document variants, two languages, technical evidence, and 66 generated downloads. `data/resume.json` is the curated source, `scripts/build_resume.py` regenerates PDF/DOCX. Build with `pip install reportlab python-docx` and `python scripts/build_resume.py`; validate with `python tests/check_resume.py` (Poppler). The resume documents workflow generates checked artifacts and publishes them to the repository when permitted. Web layout and document rendering still require separate visual review. No invented employment, certificates, publication, GPA or results.

## V5 developer experience

Ten standalone project records, verified repository screenshot references, project comparison, public GitHub dashboard, releases, technical notes, local HTML/CSS sandbox, fixed GET API explorer, snippets, inquiry brief, accessibility preferences and vCard. No fabricated screenshots or credentials. CSS 3D is used instead of external WebGL dependencies.

V5 follow-up: local job description matching, tailored TXT CV and cover letter, on-demand actual first-page PNG previews, vCard and QR, PWA shell and core offline cache. Preview files are generated by the resume preview workflow, which also creates full-page contact sheets as workflow artifacts. Browser validation is recorded separately; do not infer a Lighthouse or ATS score from static checks.

Browser quality workflow runs Chromium, Firefox, WebKit on desktop/tablet/mobile; tests use mock GitHub responses, local assets, actual PDF previews and offline core navigation. Lighthouse and axe produce measured reports, not implied passes. Inline styles are permitted on the sandbox playground page to support CSS preview; scripts remain external-only and the iframe is sandboxed.

### Stable gates

Source, document generation and deployment are necessary but not sufficient. Require passing desktop/tablet/mobile browser interaction tests, offline navigation and actual artifact downloads; review Lighthouse and axe reports, visual output, external links, security and content evidence before labeling a release Stable. The 3D view is CSS, activity calendar is sampled public events, and job matching is not an ATS certification. TopoSurvey animation is now opt-in. No unverifiable credentials or visual assets are fabricated.

The automated stable quality gate requires all browser cases, Lighthouse performance >=95 and SEO=100 on index/CV/experience, zero serious or critical axe violations, structural checks, and PDF/DOCX integrity. Reports are uploaded even on failure. Manual visual review and deployment checks remain separate. The playground filters markup to an inert subset and uses a sandboxed frame.
