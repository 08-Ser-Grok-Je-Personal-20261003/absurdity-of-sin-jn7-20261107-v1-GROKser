"""示意图：耶路撒冷／圣殿局部框 + 加利利（含迦特希弗）。非比例，不画精确疆界。"""
import html
def esc(s): return html.escape(s)
def lines(txt,x,y,lh=16,anchor='middle',cls='svgt',extra=''):
    parts=txt.split('\n')
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" {extra}>'+''.join(
        f'<tspan x="{x}" dy="{0 if i==0 else lh}">{esc(p)}</tspan>' for i,p in enumerate(parts))+'</text>'
def card(x,y,w,h,title,body,fill,tc='#fff',fs=13,lh=16):
    n=1+body.count('\n')
    y0=y+22
    t=f'<text x="{x+w/2}" y="{y+16}" text-anchor="middle" font-size="13" font-weight="800" fill="{tc}">{esc(title)}</text>'
    b=lines(body,x+w/2,y0+14,lh,'middle','',f'font-size="{fs}" font-weight="650" fill="{tc}"')
    return f'<g class="node"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="rgba(0,0,0,.12)"/>{t}{b}</g>'

def galilee():
    """两框示意图。坐标手排，保证 360 宽的 viewBox 在约 335px 显示时文字不重叠。"""
    W,H=360,1048
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="非比例示意图：上框为加利利（含迦特希弗、拿撒勒与加利利海）、撒马利亚与耶路撒冷的方向；下框为耶路撒冷圣殿区局部，标出差役、领袖与尼哥底母。不是历史疆界，也不是考古测绘图。">']
    o.append('<rect class="sea" width="360" height="1048" rx="12"/>')
    # banner
    o.append('<rect x="10" y="10" width="340" height="32" rx="8" fill="#1d3d9e"/>')
    o.append(lines('非比例示意图 · 不是行政疆界 · 不是考古测点',180,31,16,'middle','','font-size="13" font-weight="800" fill="#fff"'))
    # ===== panel 1 =====
    o.append('<rect x="10" y="50" width="340" height="470" rx="12" fill="var(--glass-strong)" stroke="#0a9b6b" stroke-width="2"/>')
    o.append(lines('区域框 · 北在上 · 距离不按比例',180,72,16,'middle','svgt','font-size="14" font-weight="800"'))
    # galilee zone
    o.append('<rect x="22" y="84" width="316" height="214" rx="10" fill="rgba(10,155,107,.16)" stroke="#0a9b6b" stroke-width="1.5"/>')
    o.append(lines('加利利',46,104,16,'start','svgt','font-size="15" font-weight="800"'))
    o.append(lines('北 ↑',318,104,16,'end','svgm','font-size="12" font-weight="700"'))
    # sea (east)
    o.append('<ellipse class="lake" cx="262" cy="176" rx="40" ry="26"/>')
    o.append(lines('加利利海',262,180,16,'middle','svgt','font-size="12" font-weight="800"'))
    # capernaum above sea
    o.append('<circle class="place" cx="262" cy="128" r="5"/>')
    o.append(lines('迦百农',262,118,14,'middle','svgt','font-size="12" font-weight="700"'))
    # gath-hepher box — left, clear of the sea (sea left edge ≈ 222)
    o.append('<rect x="32" y="118" width="158" height="58" rx="8" fill="var(--glass-strong)" stroke="#e0245e" stroke-width="1.6"/>')
    o.append(lines('迦特希弗\n约拿的家乡（王下14:25）\n通常辨认 · 非测点',111,136,15,'middle','svgt','font-size="12" font-weight="700"'))
    o.append('<circle class="place" cx="198" cy="147" r="6" fill="#e0245e"/>')
    o.append('<line x1="190" y1="147" x2="198" y2="147" stroke="#e0245e" stroke-width="1.4"/>')
    # nazareth below gath box, still left of sea
    o.append('<circle class="place" cx="48" cy="230" r="6"/>')
    o.append('<rect x="62" y="210" width="132" height="40" rx="8" fill="var(--glass-strong)" stroke="#2d5be3" stroke-width="1.5"/>')
    o.append(lines('拿撒勒 · 成长的家乡',128,235,16,'middle','svgt','font-size="12.5" font-weight="800"'))
    o.append('<line x1="54" y1="230" x2="62" y2="230" stroke="#2d5be3" stroke-width="1.4"/>')
    # route down the right gutter (x=318), clear of sea right edge 302
    o.append('<path class="route dash" d="M318,200 L318,430" stroke="#7a3ff2" style="stroke-width:2.5px"/>')
    o.append('<polygon points="312,428 318,442 324,428" fill="#7a3ff2"/>')
    # samaria
    o.append('<rect x="22" y="308" width="316" height="40" rx="8" fill="rgba(224,36,94,.08)" stroke="#e0245e" stroke-width="1.4" stroke-dasharray="6 4"/>')
    o.append(lines('撒马利亚 · 箭头只表「上京」方向',168,333,16,'middle','svgt','font-size="13" font-weight="700"'))
    # judea / jerusalem
    o.append('<rect x="22" y="358" width="316" height="148" rx="10" fill="rgba(45,91,227,.10)" stroke="#2d5be3" stroke-width="1.5"/>')
    o.append(lines('犹太',46,380,16,'start','svgt','font-size="15" font-weight="800"'))
    o.append('<circle class="place" cx="56" cy="440" r="7"/>')
    o.append('<circle cx="56" cy="440" r="12" fill="none" stroke="var(--rose)" stroke-width="2"><animate attributeName="r" values="10;16;10" dur="2.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="2.4s" repeatCount="indefinite"/></circle>')
    o.append('<rect x="78" y="400" width="214" height="86" rx="8" fill="var(--glass-strong)" stroke="#2d5be3"/>')
    o.append(lines('耶路撒冷 · 住棚节（约7）\n领袖审问差役、羞辱尼哥底母\n见下方「圣殿局部框」',185,428,18,'middle','svgt','font-size="13" font-weight="700"'))
    # ===== panel 2 =====
    o.append('<rect x="10" y="532" width="340" height="500" rx="12" fill="var(--glass-strong)" stroke="#d99100" stroke-width="2"/>')
    o.append(lines('局部框 · 耶路撒冷／圣殿（示意方框）',180,556,16,'middle','svgt','font-size="14" font-weight="800"'))
    o.append('<rect x="22" y="570" width="316" height="70" rx="10" fill="rgba(217,145,0,.18)" stroke="#d99100" stroke-width="1.6"/>')
    o.append('<rect x="36" y="582" width="52" height="46" rx="4" fill="none" stroke="#d99100" stroke-width="2"/>')
    o.append(lines('圣殿',62,610,16,'middle','svgt','font-size="13" font-weight="800"'))
    o.append(lines('只是院子示意，不是测绘图',100,610,16,'start','svgt','font-size="13" font-weight="700"'))
    # 2×2 cards, gaps of 12px; no overlap with temple strip (ends y=640)
    o.append(card(22,652,152,112,'耶稣','节期末日发出邀请\n干渴的人可以来\n约7:37–39','#2d5be3',fs=12.5,lh=16))
    o.append(card(186,652,152,112,'差役','奉命捉拿，却空手而回\n被他的话震动\n约7:45–46','#0a9b6b',fs=12.5,lh=16))
    o.append(card(22,776,152,128,'祭司长与法利赛人','不审话语，先贴标签\n搬权威，贬群体\n约7:47–49','#e0245e',fs=12.5,lh=16))
    o.append(card(186,776,152,128,'尼哥底母','先听本人，再作判断\n反被加利利羞辱\n约7:50–52','#7a3ff2',fs=12.5,lh=16))
    o.append(lines('四格彼此留白；差役往返只是情节方向，经文没有画出路线。',180,938,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('迦特希弗标在加利利框内，表示通常的地理辨认，不是发掘坐标。',180,960,16,'middle','svgm','font-size="11.5"'))
    o.append(lines('7:53–8:11 的抄本问题不在此图论证之内。',180,982,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def mindmap():
    W,H=360,820
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="思维导图：罪的荒谬，从箴言5章的欲望与约翰福音7章的自义，到十字架、圣灵与听查判改。">']
    o.append('<rect class="sea" width="360" height="820" rx="12"/>')
    o.append(card(30,12,300,72,'罪的荒谬','宁可扭曲真理，不肯降服基督','#1d3d9e',fs=13,lh=16))
    rows=[
        (100,'#e8590c','两条入口','欲望的捆绑 · 箴言5章\n自义的遮蔽 · 约翰福音7章'),
        (214,'#e0245e','对差役','没有带回囚犯，带回见证\n于是贴标签、搬权威、贬群体'),
        (328,'#7a3ff2','对尼哥底母','律法转而照向执法的人\n答不出，就攻击提问的人'),
        (442,'#2d5be3','十字架','无罪的主担当罪刑\n人的恶仍是恶，神的恩仍是恩'),
        (556,'#0a9b6b','圣灵与感恩','要的是新心，不只是新资料\n听 — 查 — 判 — 改'),
    ]
    prev_bottom=84
    for y,c,t,b in rows:
        o.append(f'<path d="M180,{prev_bottom} L180,{y}" stroke="{c}" stroke-width="3" opacity=".8"/>')
        o.append(card(30,y,300,100,t,b,c,fs=13,lh=17))
        prev_bottom=y+100
    o.append(lines('手机上整图随页宽缩小，文字仍在各自色块内，不互相压住。',180,792,16,'middle','svgm','font-size="11.5"'))
    o.append('</svg>')
    return ''.join(o)

def paths():
    W,H=360,470
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="流程图：听见反证之后的旧路与恩典中的新路。">']
    o.append('<rect class="sea" width="360" height="470" rx="12"/>')
    o.append(lines('听见反证之后',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    old=['地位受威胁','贴标签、拒绝听','不义判断','旧路 · 自我捆绑']
    new=['回到圣经与事实','承认自己有限','信靠基督、愿意改','新路 · 公义与爱']
    for i,t in enumerate(old):
        y=48+i*78
        o.append(card(12,y,160,64,f'旧 {i+1}',t,'#e0245e',fs=13,lh=16))
        if i<len(old)-1:
            o.append(f'<path d="M92,{y+64} L92,{y+78}" stroke="#e0245e" stroke-width="2.4" marker-end="url(#ar)"/>')
    for i,t in enumerate(new):
        y=48+i*78
        o.append(card(188,y,160,64,f'新 {i+1}',t,'#0a9b6b',fs=13,lh=16))
        if i<len(new)-1:
            o.append(f'<path d="M268,{y+64} L268,{y+78}" stroke="#0a9b6b" stroke-width="2.4"/>')
    o.append('<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8Z" fill="#e0245e"/></marker></defs>')
    o.append('</svg>')
    return ''.join(o)

def loop_redemptive():
    W,H=360,640
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="救赎历史闭环：从创造中的顺服，经堕落与律法，到基督受死复活、圣灵更新，再回到感恩的顺服。">']
    o.append('<rect class="sea" width="360" height="640" rx="12"/>')
    o.append(lines('救赎历史闭环',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    steps=[
        ('创造','智慧与顺服','#0a9b6b'),
        ('堕落','篡夺判断权','#e0245e'),
        ('以色列','领受律法与应许','#7a3ff2'),
        ('基督','被拒绝、受死、复活','#2d5be3'),
        ('圣灵','开人的心','#0a84c6'),
        ('教会','等候完全更新','#d99100'),
    ]
    for i,(a,b,c) in enumerate(steps):
        y=44+i*88
        o.append(card(70,y,220,68,a,b,c,fs=14,lh=18))
        if i<len(steps)-1:
            o.append(f'<path d="M180,{y+68} L180,{y+88}" stroke="{c}" stroke-width="2.5" stroke-dasharray="4 3"><animate attributeName="stroke-dashoffset" from="14" to="0" dur="1s" repeatCount="indefinite"/></path>')
    o.append('<path d="M292,92 C340,300 340,480 292,560" fill="none" stroke="#1d3d9e" stroke-width="2" stroke-dasharray="5 4" opacity=".7"/>')
    o.append(lines('回到\n感恩',328,330,16,'middle','svgm','font-size="12" font-weight="800"'))
    o.append('</svg>')
    return ''.join(o)

def triad():
    W,H=360,430
    o=[f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="罪、救赎、感恩三步：用标签躲避真理，基督担当罪刑并赐新心，于是听、查、判、改。">']
    o.append('<rect class="sea" width="360" height="430" rx="12"/>')
    o.append(lines('罪 — 救赎 — 感恩',180,28,16,'middle','svgt','font-size="15" font-weight="800"'))
    o.append(card(24,46,312,90,'① 罪','我用标签躲避真理\n愿意用律法量别人\n不肯让真理量自己','#e0245e',fs=14,lh=18))
    o.append('<path d="M180,136 L180,156" stroke="#596277" stroke-width="2.4"/>')
    o.append(card(24,156,312,100,'② 救赎','基督为我担当罪刑\n圣灵藉福音使我回转\n不是等我先变得合理','#2d5be3',fs=14,lh=18))
    o.append('<path d="M180,256 L180,276" stroke="#596277" stroke-width="2.4"/>')
    o.append(card(24,276,312,100,'③ 感恩','不再靠赢争论证明自己\n听本人 · 查事实\n按圣经判断 · 被纠正就改','#0a9b6b',fs=14,lh=18))
    o.append(lines('这是蒙恩之后的操练，不是重生的方法。',180,404,16,'middle','svgm','font-size="12"'))
    o.append('</svg>')
    return ''.join(o)

REG={'galilee':galilee,'mindmap':mindmap,'paths':paths,'loop-redemptive':loop_redemptive,'triad':triad}
CAP={
 'galilee':'示意图，不是比例地图：上框标出加利利（含通常所辨认的迦特希弗与拿撒勒）、撒马利亚与耶路撒冷的方向；下框把圣殿区画成方框，标出约7:37–52的四组人物。不同时代的行政疆界没有画出。迦特希弗的精确遗址仍有讨论，图上的点只表示「在加利利」，不是考古坐标。住棚节上京的具体路线经文没有记载。',
 'mindmap':'讲章思维导图。色块上下相接，缩小到手机宽度时文字仍留在色块内。',
 'paths':'听见反证之后的两条路。左为旧路，右为在恩典中的新路。',
 'loop-redemptive':'救赎历史闭环。右侧虚线表示终点不是另一套宗教，而是回到顺服——这次是感恩的顺服。',
 'triad':'海德堡要理问答问2的三件事，用在本讲：罪、救赎、感恩。',
}
def render(name):
    name=name.strip(); svg=REG[name]()
    cls='svg-wrap map' if name=='galilee' else 'svg-wrap'
    return f'<figure class="{cls}">{svg}<figcaption class="svg-cap">{esc(CAP[name])}</figcaption></figure>'
