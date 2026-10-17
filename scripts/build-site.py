#!/usr/bin/env python3
"""Generate portable static pages for each locale. Run from any directory."""
from pathlib import Path
import html,json,os,re,shutil,hashlib
import xml.etree.ElementTree as ET
import markdown
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
DOWNLOAD='https://pan.baidu.com/s/1gGiIIDEMDAdubAJYSAp9ZQ?pwd=55b5'
SOCIAL='https://www.xiaohongshu.com/user/profile/5fa7aad30000000001005466'
DOMAIN='https://www.filmmmer.com'
UPDATED='2026-10-17'
BEIAN='浙ICP备2026017032号'
LANGS=['zh','en']
media=ROOT/'assets/media'
manifest=json.loads((ROOT/'docs/media-manifest.json').read_text())
locales={lid:json.loads((ROOT/'locales'/f'{lid}.json').read_text()) for lid in LANGS}
def version(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:10]
def esc(value):
    return html.escape(value, quote=True)
def dig(data, path):
    cur=data
    for part in path.split('.'):
        if not isinstance(cur, dict) or part not in cur: raise KeyError(path)
        cur=cur[part]
    if not isinstance(cur, str): raise TypeError(path)
    return cur
def apply_template(template, loc, raw):
    def repl(m):
        key=m.group(1)
        return raw[key] if key in raw else esc(dig(loc, key))
    out=re.sub(r'\{\{([A-Za-z0-9_.]+)\}\}', repl, template)
    leftover=re.findall(r'\{\{[^}]+\}\}', out)
    if leftover: raise SystemExit('Unreplaced tokens: '+', '.join(leftover))
    return out
def rel_to(src, dst):
    return Path(os.path.relpath(dst, Path(src).parent)).as_posix()
def img(path, alt, prefix='', eager=False):
    if path.endswith('.svg'):
        root=ET.parse(ROOT/path).getroot();w,h=int(root.attrib['width']),int(root.attrib['height'])
    else: w,h=Image.open(ROOT/path).size
    return f'<img src="{prefix}{path}?v={version(path)}" alt="{esc(alt)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'
def render_markdown(source, extra_ups):
    lines=source.splitlines();title=lines[0].removeprefix('# ');desc=next(x for x in lines[1:] if x.strip());body='\n'.join(lines[lines.index(desc)+1:])
    md=markdown.Markdown(extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'permalink':False}})
    rendered=md.convert(body)
    def image_dims(m):
        tag=m.group(0);src=re.search('src="([^"]+)"',tag).group(1);fp=(ROOT/'guide'/src).resolve()
        if not fp.exists(): raise FileNotFoundError(fp)
        w,h=Image.open(fp).size
        tag=tag.replace(f'src="{src}"', f'src="{src}?v={version(str(fp.relative_to(ROOT)))}"')
        return tag.replace(' />', f' width="{w}" height="{h}" loading="lazy" decoding="async" />')
    rendered=re.sub(r'<img\b[^>]*>', image_dims, rendered)
    # Guide markdown is written as if the page lived at guide/*.html. Assets stay at the site root.
    if extra_ups:
        rendered=rendered.replace('src="../assets/', 'src="'+('../'*(extra_ups+1))+'assets/')
    text=re.sub('<[^>]+>',' ',rendered)
    return title, desc, rendered, md.toc, text
def shell(title, desc, body, path, loc, search=False, hero=False):
    prefix=loc['prefix'];rel=path[len(prefix):]
    up='../'*rel.count('/');asset='../'*path.count('/')
    t=loc['chrome']
    switches=[]
    alternates=[]
    og_alt=''
    for lid in LANGS:
        other=locales[lid]
        target=other['prefix']+rel
        alternates.append(f'<link rel="alternate" hreflang="{other["lang"]}" href="{DOMAIN}/{target}">')
        if lid!=loc.get('id'):
            switches.append(f'<a class="lang-switch" href="{rel_to(path, target)}" hreflang="{other["lang"]}" lang="{other["lang"]}" aria-label="{esc(other["switchAria"])}">{esc(other["switchLabel"])}</a>')
            og_alt+=f'<meta property="og:locale:alternate" content="{other["ogLocale"]}">'
    alternates.append(f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{locales["zh"]["prefix"]+rel}">')
    nav=f'''<a class="skip" href="#main">{esc(t["skip"])}</a><header class="site-nav"><div class="nav-inner wrap"><a class="brand" href="{up}index.html" aria-label="{esc(t["brandHome"])}"><img src="{asset}assets/imgs/opt/icon.webp" width="30" height="30" alt="">NextFrame</a><nav class="nav-links" aria-label="{esc(t["navLabel"])}"><a class="nav-home" href="{up}index.html#intro">{esc(t["navProduct"])}</a><a href="{up}guide/index.html">{esc(t["navGuide"])}</a>{''.join(switches)}<a class="nav-download" href="{up}download/index.html">{esc(t["navDownload"])}</a></nav></div></header>'''
    footer=f'''<footer class="site-footer"><div class="wrap footer-row"><span>{esc(t["footer"])}</span><div class="footer-links"><a href="{up}guide/index.html">{esc(t["footerGuide"])}</a><a href="{up}guide/updates.html">{esc(t["footerUpdates"])}</a><a href="{SOCIAL}" target="_blank" rel="noopener noreferrer">{esc(t["footerSocial"])}</a><a href="https://beian.miit.gov.cn" target="_blank" rel="noopener noreferrer">{BEIAN}</a></div></div></footer>'''
    url=DOMAIN+'/'+path
    ui=json.dumps(loc['ui'],ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    out=f'''<!doctype html><html lang="{loc["lang"]}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} · NextFrame</title><meta name="description" content="{esc(desc)}"><link rel="canonical" href="{url}">{''.join(alternates)}<meta property="og:title" content="{esc(title)} · NextFrame"><meta property="og:description" content="{esc(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/assets/media/workspace.webp"><meta property="og:locale" content="{loc["ogLocale"]}">{og_alt}<link rel="icon" href="{asset}assets/imgs/opt/icon.webp"><meta name="theme-color" content="#f7f7f7"><link rel="stylesheet" href="{asset}assets/css/site.css?v={version("assets/css/site.css")}">'''
    if hero:
        hero_asset=manifest['hero'][0]['asset']
        out+=f'<link rel="preload" as="image" href="{asset}{hero_asset}?v={version(hero_asset)}" fetchpriority="high">'
    if search: out+=f'<script defer src="{asset}assets/js/{loc["search"]}?v={version("assets/js/"+loc["search"])}"></script>'
    out+=f'<script>window.NF_UI={ui}</script><script defer src="{asset}assets/js/site.js?v={version("assets/js/site.js")}"></script></head><body>{nav}<main id="main">{body}</main>{footer}</body></html>'
    dest=ROOT/path;dest.parent.mkdir(exist_ok=True,parents=True);dest.write_text(out)
def load_articles(loc):
    extra=loc['prefix'].count('/')
    articles=[]
    folder=ROOT/loc['content']
    files=sorted(folder.glob('*.md'))
    if not files: raise SystemExit(f'No chapters in {folder}')
    for f in files:
        title,desc,rendered,toc,text=render_markdown(f.read_text(), extra)
        articles.append(dict(slug=f.stem,title=title,description=desc,body=rendered,toc=toc,text=text))
    return articles
def build_lang(loc, articles):
    prefix=loc['prefix']
    (ROOT/'assets/js'/loc['search']).write_text('window.NF_SEARCH='+json.dumps([{k:a[k] for k in ['slug','title','description','text']} for a in articles],ensure_ascii=False)+';')
    art=loc['article']
    nav=''.join(f'<a href="{a["slug"]}.html" {{CURRENT_{a["slug"]}}}>{esc(a["title"])}</a>' for a in articles)
    sidebar=f'<aside class="guide-sidebar"><h2>{esc(art["sidebarTitle"])}</h2><label class="sr-only" for="doc-search">{esc(art["searchLabel"])}</label><input id="doc-search" class="doc-search" type="search" placeholder="{esc(art["searchPlaceholder"])}" autocomplete="off"><div class="search-results" aria-live="polite"></div><details open><summary>{esc(art["summary"])}</summary><nav aria-label="{esc(art["navAria"])}">'+nav+f'</nav></details></aside>'
    paths=[]
    for i,a in enumerate(articles):
        side=sidebar
        for item in articles: side=side.replace('{CURRENT_'+item['slug']+'}', 'aria-current="page"' if a==item else '')
        pagination=''
        if i: pagination+=f'<a href="{articles[i-1]["slug"]}.html">← {esc(articles[i-1]["title"])}</a>'
        if i+1<len(articles): pagination+=f'<a href="{articles[i+1]["slug"]}.html">{esc(articles[i+1]["title"])} →</a>'
        meta=esc(art['meta'].format(updated=UPDATED))
        body=f'<div class="guide-layout wrap">{side}<article class="article"><span class="eyebrow">{esc(art["eyebrow"])}</span><h1>{esc(a["title"])}</h1><p class="lead">{esc(a["description"])}</p><p class="meta">{meta}</p><div class="prose">{a["body"]}</div><nav class="doc-pagination" aria-label="{esc(art["pagination"])}">{pagination}</nav></article><aside class="toc"><p>{esc(art["toc"])}</p>{a["toc"]}</aside></div>'
        path=prefix+'guide/'+a['slug']+'.html'
        shell(a['title'],a['description'],body,path,loc,search=True);paths.append(path)
    g=loc['guideIndex']
    cards=''.join(f'<a class="route" href="{a["slug"]}.html"><span class="number">{i+1:02}</span><h3>{esc(a["title"])}</h3><p>{esc(a["description"])}</p><span class="more">{esc(g["more"])}</span></a>' for i,a in enumerate(articles))
    index=prefix+'guide/index.html'
    shell(g['title'],g['desc'],f'<div class="page-intro wrap"><span class="eyebrow">{esc(g["eyebrow"])}</span><h1>{esc(g["h1"])}</h1><p>{esc(g["lead"])}</p><div class="actions"><a class="button" href="01-start.html">{esc(g["start"])}</a><a href="11-shortcuts.html">{esc(g["shortcuts"])}</a></div></div><section class="wrap three" style="padding-bottom:100px">{cards}</section>',index,loc)
    u=loc['updates']
    items=''.join(f'<li>{esc(item)}</li>' for item in u['items'])
    updates=prefix+'guide/updates.html'
    shell(u['title'],u['desc'],f'<div class="page-intro wrap"><span class="eyebrow">{esc(u["eyebrow"])}</span><h1>{esc(u["h1"])}</h1><p>{esc(u["lead"])}</p><div class="prose"><h2>{esc(u["heading"])}</h2><ul>{items}</ul><p>{esc(u["note"])}</p><p><a href="index.html">{esc(u["back"])}</a></p></div></div>',updates,loc)
    alts=loc['alts']
    if len(alts['hero'])!=len(manifest['hero']) or len(alts['features'])!=len(manifest['features']):
        raise SystemExit(f'Alt text count does not match media manifest for {loc["id"]}')
    home_path=prefix+'index.html'
    asset_prefix='../'*home_path.count('/')
    raw={'HERO':''.join(f'<div class="hero-slide">{img(item["asset"],alts["hero"][i],asset_prefix,eager=i==0)}</div>' for i,item in enumerate(manifest['hero'])),'HERO_COUNT':str(len(manifest['hero'])).zfill(2),'WORKSPACE':img('assets/media/workspace.webp',alts['workspace'],asset_prefix),'AUTO':img('assets/media/auto.webp',alts['auto'],asset_prefix),'STRIP':img('assets/media/strip.webp',alts['strip'],asset_prefix),'DOWNLOAD':DOWNLOAD,'SOCIAL':SOCIAL}
    for n,item in enumerate(manifest['features'],1): raw[f'FEATURE_{n:02}']=img(item['asset'],alts['features'][n-1],asset_prefix)
    home=apply_template((ROOT/'templates/home.html').read_text(), loc, raw)
    download=apply_template((ROOT/'templates/download.html').read_text(), loc, raw)
    download_path=prefix+'download/index.html'
    page=loc['pages']
    shell(page['home']['title'],page['home']['desc'],home,home_path,loc,hero=True)
    shell(page['download']['title'],page['download']['desc'],download,download_path,loc)
    return [home_path,download_path,index,updates]+paths
groups={}
for lid in LANGS:
    locales[lid]['id']=lid
    groups[lid]=load_articles(locales[lid])
slugs=[a['slug'] for a in groups['zh']]
for lid,articles in groups.items():
    found=[a['slug'] for a in articles]
    if found!=slugs: raise SystemExit(f'Slug mismatch for {lid}: {found} vs {slugs}')
paths=[]
for lid in LANGS: paths+=build_lang(locales[lid], groups[lid])
def sitemap_links(rel):
    links=''.join(f'<xhtml:link rel="alternate" hreflang="{locales[lid]["lang"]}" href="{DOMAIN}/{locales[lid]["prefix"]+rel}"/>' for lid in LANGS)
    links+=f'<xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/{locales["zh"]["prefix"]+rel}"/>'
    return links
rels=['index.html','download/index.html','guide/index.html','guide/updates.html']+['guide/'+slug+'.html' for slug in slugs]
entries=''
for rel in rels:
    links=sitemap_links(rel)
    for lid in LANGS:
        loc_url=DOMAIN+'/'+locales[lid]['prefix']+rel
        entries+=f'<url><loc>{loc_url}</loc><lastmod>{UPDATED}</lastmod>{links}</url>'
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'+entries+'</urlset>')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+DOMAIN+'/sitemap.xml\n')
out=ROOT/'_site'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for path in paths+['sitemap.xml','robots.txt','CNAME','.nojekyll']:
    dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/path,dest)
for folder in ['css','js']:
    shutil.copytree(ROOT/'assets'/folder,out/'assets'/folder,dirs_exist_ok=True)
asset_paths=set(re.findall(r'(?:src|href)="(?:\.\./)*(assets/[^"?#]+)', ''.join((ROOT/p).read_text() for p in paths)))
for path in asset_paths:
    if not (ROOT/path).is_file(): continue
    dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/path,dest)
print(f'Built {len(paths)} pages, {len(slugs)} chapters × {len(LANGS)} languages → _site/')
