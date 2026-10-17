#!/usr/bin/env python3
"""Build lightweight feature illustrations from the approved photos and vector diagrams."""
from pathlib import Path
from PIL import Image, ImageOps
import io,base64,json,math
ROOT=Path(__file__).resolve().parents[1]
MEDIA=ROOT/'assets/media'

def photo(name,x,y,w,h,crop=None,contain=False):
 im=Image.open(MEDIA/name).convert('RGB')
 if crop:im=im.crop(crop)
 im=ImageOps.pad(im,(w,h),method=Image.Resampling.LANCZOS,color="#181818") if contain else ImageOps.fit(im,(w,h),method=Image.Resampling.LANCZOS)
 b=io.BytesIO();im.save(b,format='WEBP',quality=80)
 return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/webp;base64,{base64.b64encode(b.getvalue()).decode()}"/>'
def rect(x,y,w,h,fill='#2c2c2c',rx=8,stroke='none'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def text(s,x,y,size=18,color='#dedede',anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}">{s}</text>'
def line(x1,y1,x2,y2,color='#666',width=2):
 return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" fill="none"/>'
def circle(x,y,r,fill='none',stroke='#ddd',width=2):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
def path(d,color='#eee',width=2):return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"/>'
def tag(s,x,y,w=90):return rect(x,y,w,32,'#343434',16)+text(s,x+w/2,y+22,14,anchor='middle')
arts=[]
# Optical density, a conceptual logarithmic curve, no fabricated result comparison.
a=text('D = −log₁₀ T',42,68,28)+text('OPTICAL DENSITY',42,96,11,'#999')
for y in [140,190,240,290]:a+=line(44,y,420,y,'#383838',1)
a+=path('M44 124 C60 184 94 223 175 249 C245 269 320 281 420 290',width=3)
a+=line(44,112,44,290)+line(44,290,420,290)
for n,c in enumerate('DCMY'):a+=rect(462,56+n*70,112,54,'#303030')+text(c,487,91+n*70,22)+line(523,84+n*70,554,84+n*70,'#aaa')
a+=text('透射光 → 密度 → 正像',44,340,16,'#aaa');arts.append(a)
# RAW image, framing graphic.
a=photo('auto.webp',28,24,584,277)+rect(28,301,584,58,'#282828',0)
a+=text('RAW',48,337,17)+text('识别  →  裁切  →  反转  →  校色',150,337,16)
a+=path('M54 86V50H90 M550 50H586V86 M54 241V277H90 M550 277H586V241','#eee',2);arts.append(a)
# Strip and individual frames, native photos.
a=rect(22,45,596,226,'#101010',0)
for x in range(33,610,32):
 a+=rect(x,54,14,17,'#bbb',3)+rect(x,244,14,17,'#bbb',3)
for i,name in enumerate(['hero-04.webp','hero-06.webp','hero-10.webp']):
 x=34+i*198;a+=photo(name,x,81,180,154)+rect(x,81,180,154,'none',0,'#ddd')+text(f'0{i+1}',x+7,224,12)
a+=text('一条扫描，逐帧显影',320,327,20,anchor='middle');arts.append(a)
# Supported formats.
a=''
for i,(label,detail) in enumerate([('RAW','相机翻拍'),('DNG','数字负片'),('TIFF','高位深扫描'),('FFF','整条扫描')]):
 x=38+i*146;a+=rect(x,88,126,183,'#2c2c2c',9,'#555')+path(f'M{x+85} 88V128H{x+126}','#777')+text(label,x+63,190,24,anchor='middle')+text(detail,x+63,236,13,'#aaa','middle')
a+=text('同一工作区，连接不同设备',320,326,18,'#ccc','middle');arts.append(a)
# Film edge in an actual RAW result.
a=photo('raw-station.webp',30,34,580,292,contain=True)+rect(30,326,580,30,'#282828',0)+text('边码 · 齿孔 · 留白',320,348,14,'#ccc','middle');arts.append(a)
# HDR: neutral scale schematic with real highlights photograph.
a=photo('hero-09.webp',30,28,580,180)+text('HDR',44,250,24)+text('高光层次',596,250,15,'#aaa','end')
for i in range(12):
 v=int(32+i*20);a+=rect(44+i*46,270,43,30,f'rgb({v},{v},{v})',0)
a+=text('暗部',44,329,14,'#aaa')+text('亮部',592,329,14,'#aaa','end');arts.append(a)
# Color tools: conceptual curves and density controls.
a=rect(32,30,356,265,'#272727',6)
for x in range(62,370,60):a+=line(x,48,x,275,'#3d3d3d',1)
for y in range(65,276,45):a+=line(48,y,372,y,'#3d3d3d',1)
a+=path('M49 275C140 260 200 90 371 51','#eee',3)+path('M49 275C170 260 210 130 371 51','#888',2)
a+=circle(180,190,5,'#eee','none')+circle(288,87,5,'#eee','none')
for i,c in enumerate('DCMY'):
 y=48+i*60;a+=text(c,423,y+20,18)+line(464,y+14,593,y+14,'#666',3)+circle(500+i*19,y+14,6,'#ddd','none')
a+=text('曲线  /  白平衡  /  混色器  /  局部蒙版',320,339,17,'#aaa','middle');arts.append(a)
# Interaction wheel and keys.
a=circle(210,179,112,stroke='#666')+circle(210,179,72,fill='#303030',stroke='#aaa')+text('长按',210,186,22,anchor='middle')
for i,k in enumerate('ASDG'):
 ang=i*math.pi/2-math.pi/2;x=210+93*math.cos(ang);y=179+93*math.sin(ang);a+=text(k,x,y+6,20,anchor='middle')
for i,(k,label) in enumerate([('V','显示标记'),('F','裁切'),('Q','片基取样')]):
 y=84+i*68;a+=rect(386,y,43,38,'#363636',5,'#777')+text(k,407,y+26,18,anchor='middle')+text(label,447,y+26,17)
a+=text('转盘 · 波形拖拽 · 快捷键',320,339,18,'#aaa','middle');arts.append(a)
# Tethered camera and live-view monitor diagram.
a=rect(40,142,180,122,'#323232',15,'#aaa')+rect(70,120,72,27,'#323232',4,'#aaa')+circle(132,202,43,fill='#1e1e1e',stroke='#aaa')+circle(132,202,29,stroke='#555')+circle(197,163,5,'#ccc','none')
a+=path('M236 203H294L283 192M294 203L283 214','#ccc',3)
a+=rect(320,81,282,211,'#2c2c2c',8,'#888')+photo('auto.webp',332,94,258,171)+line(461,292,461,319,'#aaa',4)+line(416,320,506,320,'#aaa',4)
a+=text('拍摄 → 接收 → 显影',320,359,16,'#aaa','middle');arts.append(a)
# Dust removal schematic, not a fabricated before/after photo.
a=photo('hero-06.webp',30,30,360,269)+rect(30,30,360,269,'none',0,'#777')
for x,y in [(105,89),(267,142),(175,230)]:a+=circle(x,y,13,stroke='#eee',width=1)+line(x-4,y,x+4,y,'#eee',1)+line(x,y-4,x,y+4,'#eee',1)
a+=text('检测',444,101,24)+line(467,124,467,151)+text('选区',444,183,24)+line(467,206,467,233)+text('修复',444,265,24)+text('灰尘检测与修复流程示意',320,342,15,'#aaa','middle');arts.append(a)
# Live output photo stack and a playback glyph.
a=rect(115,45,456,271,'#343434',5,'#666')+rect(92,62,456,271,'#292929',5,'#888')+photo('hero-10.webp',69,80,456,271)
a+=circle(297,213,39,'#171717cc','#ddd')+'<path d="M287 193L317 213L287 233Z" fill="#eee"/>'+tag('LIVE',87,96,73);arts.append(a)
# Agent concept. Avoid pretending this is an app screenshot.
a=rect(34,55,386,92,'#333',14)+text('处理这组底片',62,108,23)+rect(78,173,342,111,'#292929',14,'#666')+text('导入 · 裁切 · 调色',102,215,20)+text('在 NextFrame 中继续编辑',102,251,15,'#aaa')
a+=path('M438 179H484M472 167L484 179L472 191','#aaa',2)+rect(503,129,99,99,'#e3e3e3',22)+text('NF',552,193,32,'#222','middle')+text('本地 MCP',320,342,16,'#aaa','middle');arts.append(a)
titles=['密度域反转原理示意','RAW 自动处理与画面识别示意','使用已分帧照片展示整条裁切','RAW、DNG、TIFF、FFF 多格式兼容示意','保留片基与白色齿孔的实际照片','HDR 明暗层次示意','曲线与 DCMY 色彩控制示意','转盘与快捷键操作示意','相机联机拍摄流程示意','自动除尘检测与修复流程示意','LIVE 动态成片播放示意','Agent 通过本地 MCP 调用 NextFrame 的示意']
features=[]
for i,a in enumerate(arts,1):
 name=f'feature-{i:02}.svg'
 (MEDIA/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="640" height="384" viewBox="0 0 640 384"><rect width="640" height="384" fill="#202020"/><g font-family="-apple-system,BlinkMacSystemFont,PingFang SC,Microsoft YaHei,sans-serif">{a}</g></svg>')
 features.append(dict(asset=f'assets/media/{name}',alt=titles[i-1]))
p=ROOT/'docs/media-manifest.json';m=json.loads(p.read_text());m['features']=features;p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
print('Built 12 feature illustrations')
