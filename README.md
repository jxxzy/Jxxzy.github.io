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
