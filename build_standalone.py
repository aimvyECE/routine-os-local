"""Package reviewed sources as one offline HTML file. No network or user data."""
from pathlib import Path
root = Path(__file__).resolve().parent
html = (root / 'index.html').read_text()
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>' + (root / 'style.css').read_text() + '</style>')
for name in ('core.js', 'app.js'):
    source = (root / name).read_text()
    if '</script' in source.lower():
        raise ValueError('Inline script closing tag requires escaping')
    html = html.replace(f'<script src="{name}"></script>', '<script>' + source + '</script>')
(root / 'RoutineOS.html').write_text(html)
