#!/usr/bin/env python3
"""Generate portable static pages. Run from any directory; no browser runtime needed."""
from pathlib import Path
import html,json,re,shutil,hashlib
import xml.etree.ElementTree as ET
import markdown
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
DOWNLOAD='https://pan.baidu.com/s/1gGiIIDEMDAdubAJYSAp9ZQ?pwd=55b5'
SOCIAL='https://www.xiaohongshu.com/user/profile/5fa7aad30000000001005466'
DOMAIN='https://www.filmmmer.com'
UPDATED='2026-10-17'
media=ROOT/'assets/media'
def version(path):
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()[:10]
def img(path,alt,prefix='',eager=False):
    if path.endswith(".svg"):
        root=ET.parse(ROOT/path).getroot();w,h=int(root.attrib["width"]),int(root.attrib["height"])
    else:w,h=Image.open(ROOT/path).size
    return f'<img src="{prefix}{path}?v={version(path)}" alt="{html.escape(alt)}" width="{w}" height="{h}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if eager else '')+'>'
def shell(title,desc,body,path,search=False,hero=False):
    p='../' if '/' in path else ''
    url=DOMAIN+'/'+path
    nav=f'''<a class="skip" href="#main">跳到正文</a><header class="site-nav"><div class="nav-inner wrap"><a class="brand" href="{p}index.html" aria-label="NextFrame 首页"><img src="{p}assets/imgs/opt/icon.webp" width="30" height="30" alt="">NextFrame</a><nav class="nav-links" aria-label="主导航"><a class="nav-home" href="{p}index.html#intro">产品</a><a href="{p}guide/index.html">使用教程</a><a class="nav-download" href="{p}download/index.html">下载 ↗</a></nav></div></header>'''
    footer=f'''<footer class="site-footer"><div class="wrap footer-row"><span>© 2026 NextFrame Studio · 为胶片摄影师打造</span><div class="footer-links"><a href="{p}guide/index.html">使用教程</a><a href="{p}guide/updates.html">文档更新</a><a href="{SOCIAL}" target="_blank" rel="noopener noreferrer">小红书 ↗</a><a href="https://beian.miit.gov.cn" target="_blank" rel="noopener noreferrer">浙ICP备2026017032号</a></div></div></footer>'''
    out=f'''<!doctype html><html lang="zh-Hans"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)} · NextFrame</title><meta name="description" content="{html.escape(desc)}"><link rel="canonical" href="{url}"><meta property="og:title" content="{html.escape(title)} · NextFrame"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{DOMAIN}/assets/media/workspace.webp"><link rel="icon" href="{p}assets/imgs/opt/icon.webp"><meta name="theme-color" content="#f7f7f7"><link rel="stylesheet" href="{p}assets/css/site.css?v={version("assets/css/site.css")}">'''
    if hero:out+=f'<link rel="preload" as="image" href="{manifest["hero"][0]["asset"]}?v={version(manifest["hero"][0]["asset"])}" fetchpriority="high">'
    if search:out+=f'<script defer src="{p}assets/js/search-index.js?v={version("assets/js/search-index.js")}"></script>'
    out+=f'<script defer src="{p}assets/js/site.js?v={version("assets/js/site.js")}"></script></head><body>{nav}<main id="main">{body}</main>{footer}</body></html>'
    dest=ROOT/path;dest.parent.mkdir(exist_ok=True,parents=True);dest.write_text(out)
articles=[]
for f in sorted((ROOT/'content/guide').glob('*.md')):
    source=f.read_text();lines=source.splitlines();title=lines[0].removeprefix('# ');desc=next(x for x in lines[1:] if x.strip());body='\n'.join(lines[lines.index(desc)+1:]);slug=f.stem
    md=markdown.Markdown(extensions=['tables','fenced_code','toc'],extension_configs={'toc':{'permalink':False}})
    rendered=md.convert(body)
    def image_dims(m):
        tag=m.group(0);src=re.search('src="([^"]+)"',tag).group(1);fp=(ROOT/'guide'/src).resolve()
        if not fp.exists():raise FileNotFoundError(fp)
        w,h=Image.open(fp).size
        tag=tag.replace(f'src="{src}"',f'src="{src}?v={version(str(fp.relative_to(ROOT)))}"')
        return tag.replace(' />',f' width="{w}" height="{h}" loading="lazy" decoding="async" />')
    rendered=re.sub(r'<img\b[^>]*>',image_dims,rendered)
    articles.append(dict(slug=slug,title=title,description=desc,body=rendered,toc=md.toc,text=re.sub('<[^>]+>',' ',rendered)))
nav=''.join(f'<a href="{a["slug"]}.html" {{CURRENT_{a["slug"]}}}>{a["title"]}</a>' for a in articles)
sidebar='<aside class="guide-sidebar"><h2>使用文档</h2><label class="sr-only" for="doc-search">搜索教程</label><input id="doc-search" class="doc-search" type="search" placeholder="搜索教程，例如 Dmin" autocomplete="off"><div class="search-results" aria-live="polite"></div><details open><summary>章节目录</summary><nav aria-label="教程章节">'+nav+'</nav></details></aside>'
(ROOT/'assets/js/search-index.js').write_text('window.NF_SEARCH='+json.dumps([{k:a[k] for k in ['slug','title','description','text']} for a in articles],ensure_ascii=False)+';')
for i,a in enumerate(articles):
    side=sidebar
    for item in articles:side=side.replace('{CURRENT_'+item['slug']+'}', 'aria-current="page"' if a==item else '')
    pagination=''
    if i:pagination+=f'<a href="{articles[i-1]["slug"]}.html">← {articles[i-1]["title"]}</a>'
    if i+1<len(articles):pagination+=f'<a href="{articles[i+1]["slug"]}.html">{articles[i+1]["title"]} →</a>'
    body=f'<div class="guide-layout wrap">{side}<article class="article"><span class="eyebrow">NEXTFRAME / 使用文档</span><h1>{a["title"]}</h1><p class="lead">{a["description"]}</p><p class="meta">中文教程 · 更新 {UPDATED} · 界面参考 2.54.0</p><div class="prose">{a["body"]}</div><nav class="doc-pagination" aria-label="相邻章节">{pagination}</nav></article><aside class="toc"><p>本页内容</p>{a["toc"]}</aside></div>'
    shell(a['title'],a['description'],body,'guide/'+a['slug']+'.html',search=True)
cards=''.join(f'<a class="route" href="{a["slug"]}.html"><span class="number">{i+1:02}</span><h3>{a["title"]}</h3><p>{a["description"]}</p><span class="more">阅读教程 ↗</span></a>' for i,a in enumerate(articles))
shell('使用文档','从单张翻拍到整条扫描，学习 NextFrame 的反转、裁切、颜色与导出。',f'<div class="page-intro wrap"><span class="eyebrow">NEXTFRAME / 使用文档</span><h1>NextFrame 使用说明</h1><p>介绍导入、全自动处理、整条裁切、颜色调整与导出。可按章节阅读，或搜索具体功能。</p><div class="actions"><a class="button" href="01-start.html">快速开始 ↗</a><a href="11-shortcuts.html">快捷键速查</a></div></div><section class="wrap three" style="padding-bottom:100px">{cards}</section>','guide/index.html')
shell('文档更新','NextFrame 使用文档与页面更新记录。','<div class="page-intro wrap"><span class="eyebrow">文档更新</span><h1>文档更新记录</h1><p>2026-10-17 · 中文教程首次整理</p><div class="prose"><h2>本次更新</h2><ul><li>加入单张翻拍、整条先分帧与先蒙版三条流程。</li><li>整理 Dmin 可选取样、曝光范围 优先的颜色检查顺序。</li><li>从当前程序定义核对快捷键，加入长按与蒙版作用域说明。</li><li>更新 2.54.0 界面截图，补充全自动模式、联机拍摄、自动除尘、HDR、LIVE 和转盘操作说明。</li></ul><p>此页记录文档变化，不代替安装包的产品发布记录。各功能以你安装的版本为准。</p><p><a href="index.html">返回全部教程 ↗</a></p></div></div>','guide/updates.html')
home=(ROOT/'templates/home.html').read_text()
manifest=json.loads((ROOT/'docs/media-manifest.json').read_text())
hero=''.join(f'<div class="hero-slide">{img(item["asset"],item["alt"],eager=i==0)}</div>' for i,item in enumerate(manifest['hero']))
replacements={'HERO':hero,'WORKSPACE':img('assets/media/workspace.webp','NextFrame 2.54.0 显影界面，raw 目录'),'AUTO':img('assets/media/auto.webp','raw 目录照片保留片基的实际显影结果'),'STRIP':img('assets/media/strip.webp','4879 目录已分帧照片联系表')}

replacements['HERO_COUNT']=str(len(manifest['hero'])).zfill(2)
for n,item in enumerate(manifest['features'],1):
    replacements[f'FEATURE_{n:02}']=img(item['asset'],item['alt'])
for k,v in replacements.items():home=home.replace('{{'+k+'}}',v)
shell('胶片的下一帧','NextFrame 胶片数字暗房：RAW 翻拍、整条扫描、反转与颜色调整。阅读中文教程，下载开始处理。',home,'index.html',hero=True)
download=(ROOT/'templates/download.html').read_text().replace('{{DOWNLOAD}}',DOWNLOAD).replace('{{SOCIAL}}',SOCIAL)
shell('下载','下载 NextFrame，阅读安装与使用说明，访问作者的小红书。',download,'download/index.html')
paths=['index.html','download/index.html','guide/index.html','guide/updates.html']+['guide/'+a['slug']+'.html' for a in articles]
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{DOMAIN}/{p}</loc><lastmod>{UPDATED}</lastmod></url>' for p in paths)+'</urlset>')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+DOMAIN+'/sitemap.xml\n')
# Deployment only includes publicly linked assets; old screenshots and planning docs stay out.
out=ROOT/'_site'
if out.exists():shutil.rmtree(out)
out.mkdir()
for path in paths+['sitemap.xml','robots.txt','CNAME','.nojekyll']:
    dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/path,dest)
for folder in ['css','js']:
    shutil.copytree(ROOT/'assets'/folder,out/'assets'/folder,dirs_exist_ok=True)
asset_paths=set(re.findall(r'(?:src|href)="(?:\.\./)?(assets/[^"?#]+)', ''.join((ROOT/p).read_text() for p in paths)))
for path in asset_paths:
    if not (ROOT/path).is_file():continue
    dest=out/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/path,dest)
print(f'Built {len(paths)} pages, {len(articles)} chapters → _site/')
