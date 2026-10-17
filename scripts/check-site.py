#!/usr/bin/env python3
"""Check generated deployment, local references, anchors and image layout contracts."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json,re,gzip
ROOT=Path(__file__).resolve().parents[1]/'_site'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.images=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id'in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  for key in ['href','src']:
   if key in a:self.refs.append(a[key])
  if tag=='img':self.images.append(a)
pages={}
for f in ROOT.rglob('*.html'):
 p=Page();p.feed(f.read_text());pages[f.resolve()]=p
errors=[]
for f,p in pages.items():
 if p.h1!=1:errors.append(f'{f}: expected one h1')
 for a in p.images:
  if not all(k in a for k in ['alt','width','height']):errors.append(f'{f}: missing image geometry/alt')
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(f.parent/unquote(u.path)).resolve() if u.path else f
  if target.is_dir():target/= 'index.html'
  if not target.exists():errors.append(f'{f.name}: missing {ref}')
  elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:errors.append(f'{f.name}: missing anchor {ref}')
  if not target.is_relative_to(ROOT):errors.append(f'{f.name}: escapes deployment {ref}')
for f in ROOT.rglob('*'):
 if f.is_file() and f.suffix in ['.py','.md','.png']:errors.append(f'Unexpected source/legacy asset {f}')
all_html=''.join(f.read_text() for f in pages)
for expected in ['https://pan.baidu.com/s/1gGiIIDEMDAdubAJYSAp9ZQ?pwd=55b5','https://www.xiaohongshu.com/user/profile/5fa7aad30000000001005466']:
 if expected not in all_html:errors.append('Missing destination '+expected)
if 'apps.apple.com' in all_html:errors.append('Obsolete download destination')
def load_index(name):
 script=(ROOT/'assets/js'/name).read_text();return json.loads(script.removeprefix('window.NF_SEARCH=').removesuffix(';'))
zh_index,en_index=load_index('search-index.js'),load_index('search-index-en.js')
assert len(zh_index)==len(en_index)==15
assert [a['slug'] for a in zh_index]==[a['slug'] for a in en_index]
for query in ['Dmin','齿孔','DCMY','快捷键']:
 assert any(query.lower() in (a['title']+a['text']).lower() for a in zh_index),query
for query in ['Dmin','sprocket','DCMY','shortcut']:
 assert any(query.lower() in (a['title']+a['text']).lower() for a in en_index),query
for f in pages:
 text=f.read_text()
 rel=f.relative_to(ROOT).as_posix()
 english=rel=='en' or rel.startswith('en/')
 if 'hreflang="zh-Hans"' not in text or 'hreflang="en"' not in text or 'hreflang="x-default"' not in text:
  errors.append(f'{rel}: missing hreflang')
 if 'class="lang-switch"' not in text: errors.append(f'{rel}: missing language switch')
 if english and 'lang="en"' not in text[:240]: errors.append(f'{rel}: expected English lang')
 if not english and 'lang="zh-Hans"' not in text[:240]: errors.append(f'{rel}: expected Chinese lang')
zh_home=(ROOT/'index.html').read_text();en_home=(ROOT/'en/index.html').read_text()
if '使用教程' not in zh_home or 'Switch to English' not in zh_home: errors.append('Chinese home language switch')
if '使用教程' in en_home or '>中文<' not in en_home: errors.append('English home language switch')
if errors:raise SystemExit('\n'.join(errors))
assets=sum(f.stat().st_size for f in ROOT.rglob('*') if f.is_file())
print(f'PASS: {len(pages)} pages; local links, anchors, image dimensions, both search indexes and destination URLs.')
print(f'Deployment {assets/1024/1024:.2f} MiB; homepage gzip {len(gzip.compress((ROOT/"index.html").read_bytes()))/1024:.1f} KiB; JS gzip {len(gzip.compress((ROOT/"assets/js/site.js").read_bytes()))/1024:.1f} KiB')
