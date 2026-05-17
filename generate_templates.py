"""
Generate Galaxy Waterproof – full Elementor WXR import.
All sections use native Elementor widgets (heading, text-editor, image,
button, icon-box, image-box).  HTML widget is used ONLY for the site
header/footer bar where a custom flex layout is unavoidable with Free.
"""
import json, os, zipfile

BASE     = r"C:\Users\01dar\wordpress_website"
KIT_DIR  = os.path.join(BASE, "elementor-kit", "templates")
IMG      = "https://galaxy-waterproof.vercel.app/wp-content/themes/galaxy-waterproof/assets/images"
LOGO_URL = f"{IMG}/logo.jpg"
WA       = "https://wa.me/85252225111"
FB       = "https://www.facebook.com/galaxywindowhk"
TEAL     = "#5BBCBC"
DARK     = "#1A1A1A"
GREY     = "#555555"
LTBG     = "#F5F5F3"
TEALBG   = "#EDF7F7"
os.makedirs(KIT_DIR, exist_ok=True)

# ── id counter ────────────────────────────────────────────────────────────────
_c = [0]
def uid():
    _c[0] += 1
    return f"e{_c[0]:05d}"

# ── low-level element builders ────────────────────────────────────────────────
def _pad(tb, lr=60):
    return {"unit":"px","top":str(tb),"right":str(lr),
            "bottom":str(tb),"left":str(lr),"isLinked":False}
def _margin(t=0,r=0,b=0,l=0):
    return {"unit":"px","top":str(t),"right":str(r),
            "bottom":str(b),"left":str(l),"isLinked":False}
def _radius(v):
    return {"unit":"px","top":str(v),"right":str(v),
            "bottom":str(v),"left":str(v),"isLinked":True}

def col(size, widgets, gap="default"):
    s = {"_column_size": size}
    if gap != "default":
        s["column_gap"] = gap
    return {"id":uid(),"elType":"column","settings":s,"elements":widgets}

def section(cols, bg=None, pad_tb=80, pad_lr=60, img_url=None, overlay=None,
            border_bottom=False, stretch=True):
    s = {}
    if stretch:
        s["stretch_section"] = "section-stretched"
    s["padding"] = _pad(pad_tb, pad_lr)
    if img_url:
        s["background_background"] = "classic"
        s["background_image"] = {"url": img_url, "id": ""}
        s["background_size"] = "cover"
        s["background_position"] = "center center"
        if overlay:
            s["background_overlay_background"] = "classic"
            s["background_overlay_color"] = overlay
    elif bg:
        s["background_background"] = "classic"
        s["background_color"] = bg
    if border_bottom:
        s["border_border"] = "solid"
        s["border_width"] = {"unit":"px","top":"0","right":"0","bottom":"1","left":"0","isLinked":False}
        s["border_color"] = "#E8EDED"
    return {"id":uid(),"elType":"section","settings":s,"elements":cols}

# ── widget builders ───────────────────────────────────────────────────────────
def w_heading(text, tag="h2", color=DARK, size=32, weight=900,
              align="center", mb=12):
    return {"id":uid(),"elType":"widget","widgetType":"heading","settings":{
        "title": text, "header_size": tag, "align": align,
        "title_color": color,
        "typography_typography": "custom",
        "typography_font_family": "Noto Sans TC",
        "typography_font_size": {"unit":"px","size":size},
        "typography_font_weight": str(weight),
        "_margin": _margin(b=mb)
    }}

def w_text(html, mb=0):
    return {"id":uid(),"elType":"widget","widgetType":"text-editor","settings":{
        "editor": html, "_margin": _margin(b=mb)
    }}

def w_image(url, radius=12, height=None, mb=0):
    s = {"image":{"url":url,"id":""},"image_size":"full",
         "image_border_radius": _radius(radius),
         "_margin": _margin(b=mb)}
    if height:
        s["image_height"] = {"unit":"px","size":height}
    return {"id":uid(),"elType":"widget","widgetType":"image","settings":s}

def w_button(text, url, align="center", bg=TEAL, color="#fff",
             mt=0, outline=False, size="sm"):
    pad = {"sm":("13","32"),"lg":("16","40")}[size]
    s = {
        "text": text,
        "link": {"url":url,"is_external":"true" if url.startswith("http") else ""},
        "align": align,
        "background_color": "rgba(0,0,0,0)" if outline else bg,
        "button_text_color": bg if outline else color,
        "border_radius": {"unit":"px","top":50,"right":50,"bottom":50,"left":50,"isLinked":True},
        "typography_font_family": "Noto Sans TC",
        "typography_font_weight": "700",
        "text_padding": {"unit":"px","top":pad[0],"right":pad[1],
                         "bottom":pad[0],"left":pad[1],"isLinked":False},
        "_margin": _margin(t=mt)
    }
    if outline:
        s.update({"border_border":"solid",
                  "border_width":{"unit":"px","top":"2","right":"2","bottom":"2","left":"2","isLinked":True},
                  "border_color": bg})
    return {"id":uid(),"elType":"widget","widgetType":"button","settings":s}

def w_icon_box(icon_fa, title, desc, icon_color=TEAL, title_color=DARK,
               bg="#ffffff", radius=12):
    return {"id":uid(),"elType":"widget","widgetType":"icon-box","settings":{
        "selected_icon": {"value":f"fas fa-{icon_fa}","library":"fa-solid"},
        "title_text": title, "description_text": desc,
        "title_size": "h3",
        "icon_color": icon_color, "icon_size": {"unit":"px","size":28},
        "title_color": title_color,
        "description_color": GREY,
        "title_typography_font_family": "Noto Sans TC",
        "title_typography_font_size": {"unit":"px","size":16},
        "title_typography_font_weight": "800",
        "description_typography_font_family": "Noto Sans TC",
        "description_typography_font_size": {"unit":"px","size":13},
        "_padding": {"unit":"px","top":"24","right":"22","bottom":"28","left":"22","isLinked":False},
        "_background_background": "classic",
        "_background_color": bg,
        "_border_radius": _radius(radius)
    }}

def w_image_box(img_url, title, desc, title_color=DARK, radius=12):
    return {"id":uid(),"elType":"widget","widgetType":"image-box","settings":{
        "image": {"url":img_url,"id":""},
        "title_text": title, "description_text": desc,
        "title_size": "h3",
        "title_color": title_color,
        "description_color": GREY,
        "title_typography_font_family": "Noto Sans TC",
        "title_typography_font_size": {"unit":"px","size":16},
        "title_typography_font_weight": "800",
        "image_border_radius": _radius(radius)
    }}

def w_divider(color="#E8EDED", mb=0):
    return {"id":uid(),"elType":"widget","widgetType":"divider","settings":{
        "color": color, "_margin": _margin(b=mb)
    }}

def w_html(html):
    return {"id":uid(),"elType":"widget","widgetType":"html","settings":{"html":html}}

# ── reusable SVGs ──────────────────────────────────────────────────────────────
WA_PATH = "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"

HEADER_HTML = f"""<header style="background:#fff;border-bottom:1px solid #E8EDED;display:flex;align-items:center;justify-content:space-between;padding:14px 60px;gap:20px;width:100%;box-sizing:border-box">
<a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0"><img src="{LOGO_URL}" style="height:44px;width:auto" alt="銀河防水"><span style="font-family:'Noto Sans TC',sans-serif;font-size:22px;font-weight:900;color:#1A1A1A">銀河防水</span></a>
<nav style="display:flex;align-items:center;gap:28px;flex:1;justify-content:center">
<a href="/" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">首頁</a>
<a href="/services" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">服務範圍</a>
<a href="/cases" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">成功案例</a>
<a href="/blog" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">防水網誌</a>
<a href="/about" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">品牌故事</a>
</nav>
<a href="{WA}" target="_blank" style="display:flex;flex-direction:column;align-items:center;background:{TEAL};color:#fff;border-radius:10px;padding:7px 18px;text-decoration:none;flex-shrink:0">
<span style="font-family:'Noto Sans TC',sans-serif;font-size:10.5px;font-weight:600;display:flex;align-items:center;gap:4px"><svg width="10" height="10" viewBox="0 0 24 24" fill="currentColor"><path d="{WA_PATH}"/></svg>WhatsApp 快速查詢</span>
<span style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:900">9123-4567</span>
</a>
</header>"""

FOOTER_HTML = f"""<footer style="background:#F5F5F3;padding:60px 60px 0;box-sizing:border-box">
<div style="display:grid;grid-template-columns:2fr 1fr 2fr;gap:48px;padding-bottom:48px;border-bottom:1px solid #E8EDED">
<div>
<a href="/" style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;margin-bottom:14px"><img src="{LOGO_URL}" style="height:44px;width:auto"><span style="font-family:'Noto Sans TC',sans-serif;font-size:22px;font-weight:900;color:#1A1A1A">銀河防水</span></a>
<p style="font-family:'Noto Sans TC',sans-serif;font-size:13px;color:#555;line-height:1.8;margin-bottom:22px">本公司為屋宇署認可I級註冊小型工程承建商(公司) 多年來致力為客戶提供專業鋁窗檢驗，維修保養及防漏工程服務。</p>
<div style="display:flex;flex-direction:column;gap:10px">
<a href="mailto:galaxywindowhk@gmail.com" style="display:inline-flex;align-items:center;justify-content:space-between;border:2px solid {TEAL};color:{TEAL};border-radius:50px;padding:10px 16px;font-family:'Noto Sans TC',sans-serif;font-size:13px;font-weight:700;text-decoration:none">網上報價查詢 <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></a>
<a href="{WA}" target="_blank" style="display:inline-flex;align-items:center;gap:8px;background:{TEAL};color:#fff;border-radius:50px;padding:10px 16px;font-family:'Noto Sans TC',sans-serif;font-size:13px;font-weight:700;text-decoration:none"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="{WA_PATH}"/></svg>WhatsApp預約檢查</a>
</div>
</div>
<nav><ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px">
<li><a href="/" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#1A1A1A;font-weight:500;text-decoration:none">首頁</a></li>
<li><a href="/services" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#1A1A1A;font-weight:500;text-decoration:none">服務範圍</a></li>
<li><a href="/cases" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#1A1A1A;font-weight:500;text-decoration:none">成功案例</a></li>
<li><a href="/blog" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#1A1A1A;font-weight:500;text-decoration:none">防水網誌</a></li>
<li><a href="/about" style="font-family:'Noto Sans TC',sans-serif;font-size:14px;color:#1A1A1A;font-weight:500;text-decoration:none">品牌故事</a></li>
</ul></nav>
<div>
<p style="font-family:'Noto Sans TC',sans-serif;font-size:14px;font-weight:700;color:#1A1A1A;margin-bottom:18px">如有查詢及報價，歡迎與我們聯絡。</p>
<ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:12px">
<li style="display:flex;align-items:flex-start;gap:10px;font-family:'Noto Sans TC',sans-serif;font-size:13px;color:#555"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2" style="flex-shrink:0;margin-top:2px"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg><a href="mailto:galaxywindowhk@gmail.com" style="color:#555;text-decoration:none">galaxywindowhk@gmail.com</a></li>
<li style="display:flex;align-items:flex-start;gap:10px;font-family:'Noto Sans TC',sans-serif;font-size:13px;color:#555"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2" style="flex-shrink:0;margin-top:2px"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.07 1.18 2 2 0 012.03 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92v2z"/></svg><span>(852) 5222 5111 | (852) 6880 0698</span></li>
<li style="display:flex;align-items:flex-start;gap:10px;font-family:'Noto Sans TC',sans-serif;font-size:13px;color:#555"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2" style="flex-shrink:0;margin-top:2px"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg><span>九龍大角咀通州街123號國貿中心2樓C室</span></li>
</ul>
</div>
</div>
<p style="font-family:'Noto Sans TC',sans-serif;text-align:center;font-size:12px;color:#888;padding:18px 0">©2026, 銀河防水有限公司</p>
</footer>"""

def s_header():
    return section([col(100,[w_html(HEADER_HTML)])], bg="#fff", pad_tb=0, pad_lr=0,
                   border_bottom=True)

def s_footer():
    return section([col(100,[w_html(FOOTER_HTML)])], bg=LTBG, pad_tb=0, pad_lr=0)

def s_cta():
    return section([col(100,[
        w_heading("不要讓雨季成為你的煩惱","h2","#2A7474",40,900,"left",10),
        w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:17px;color:{GREY};line-height:1.7">別再忍受滲漏困擾  從源頭一次解決</p>',mb=32),
        w_button("立即 WhatsApp 預約", WA, align="left")
    ])], img_url=f"{IMG}/cta-bg.jpg", overlay="rgba(230,248,248,0.80)", pad_tb=90)

def p_hero(eyebrow, title, subtitle):
    return section([col(100,[
        w_heading(eyebrow,"p",TEAL,12,700,"center",8),
        w_heading(title,"h1",DARK,44,900,"center",14),
        w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:16px;color:{GREY};text-align:center;line-height:1.8">{subtitle}</p>')
    ])], bg=TEALBG, pad_tb=80)

def wrap(title, content_sections):
    return {
        "version": "0.4", "title": title, "type": "page",
        "content": [s_header()] + content_sections + [s_cta(), s_footer()],
        "page_settings": {"hide_title":"yes","post_status":"publish"}
    }

# ══════════════════════════════════════════════════════════════════════════════
#  HOMEPAGE
# ══════════════════════════════════════════════════════════════════════════════
home_sections = [
    # ── HERO
    section([
        col(55,[
            w_heading("由勘察開始","p",TEAL,14,700,"left",6),
            w_heading("針對性解決滲漏問題","h1",DARK,52,900,"left",20),
            w_text(f'<ul style="list-style:none;padding:0;margin:0 0 32px;font-family:\'Noto Sans TC\',sans-serif;font-size:16px;color:{DARK};line-height:2">'
                   f'<li>天台、外牆、浴室、窗框滲漏</li>'
                   f'<li>先判斷源頭，再建議方案</li>'
                   f'<li>報價清晰，施工透明</li></ul>'),
            w_button("$0 預約科學滲漏檢測", WA, align="left", size="lg")
        ]),
        col(45,[])
    ], img_url=f"{IMG}/hero-bg.jpg", overlay="rgba(220,245,245,0.82)", pad_tb=120),

    # ── TRUST
    section([col(100,[
        w_heading("信任與承諾","p",DARK,24,700,"center",10),
        w_heading("銀河防水深受不同領域的客戶信任","p",GREY,15,400,"center",36),
        w_image(f"{IMG}/trust-logos.png", radius=0)
    ])], bg="#fff", pad_tb=52, border_bottom=True),

    # ── ADVANTAGES
    section([
        col(100,[
            w_heading("服務優勢","h2","#fff",42,900,"center",12),
            w_heading("我們不是靠估計，是用科學和技術處理滲漏","p","rgba(255,255,255,0.85)",15,400,"center",48),
        ]),
        col(33,[
            w_image(f"{IMG}/inspect-service.jpg", radius=12, mb=0),
            w_icon_box("search","先勘察、後施工、根源診斷",
                       "準確尋找漏水根源，避免「做完一輪又翻漏」。",
                       bg="#fff")
        ]),
        col(33,[
            w_image(f"{IMG}/quote-service.jpg", radius=12, mb=0),
            w_icon_box("file-alt","工程師主導、報價透明",
                       "工程範圍、工序、價錢與注意事項、每項清楚列明。",
                       bg="#fff")
        ]),
        col(33,[
            w_image(f"{IMG}/detail-service.jpg", radius=12, mb=0),
            w_icon_box("shield-alt","重視細節、滴水不漏",
                       "收口、轉角、接駁位置重點處理。保證防水效果合乎預期。",
                       bg="#fff")
        ]),
        col(100,[w_button("了解更多","#advantages","center",bg="#fff",color=DARK,mt=40,outline=False)])
    ], bg=TEAL),

    # ── PROBLEMS
    section([
        col(100,[
            w_heading("你是否也經歷<br>同樣的問題？","h2",DARK,38,900,"center",44)
        ]),
        col(25,[
            w_image_box(f"{IMG}/prob-concrete.jpg","石屎剝落、批盪鬆脫","牆身起泡發霉、滲水入室。")
        ]),
        col(25,[
            w_image_box(f"{IMG}/prob-rooftop.jpg","天台積水／排水不良","天台積水或排水不良，雨後長期滯水，加速滲漏與防水層老化。")
        ]),
        col(25,[
            w_image_box(f"{IMG}/prob-window.jpg","窗邊接駁位老化","收口、轉角、接駁位置重點處理，保證防水合乎效果。")
        ]),
        col(25,[
            w_image_box(f"{IMG}/prob-bathroom.jpg","浴室防水層失效","浴室防水層失效，水氣滲入牆身地台，易發霉剝落。")
        ]),
    ], bg="#fff"),

    # ── TECHNOLOGY
    section([
        col(100,[
            w_heading("核心技術","h2","#fff",42,900,"center",12),
            w_heading("以科學選材與工法，從源頭提升防水耐用度","p","rgba(255,255,255,0.85)",15,400,"center",48)
        ]),
        col(50,[w_image_box(
            f"{IMG}/tech-polyurea.jpg","Polyurea 聚脲",
            "7秒快速固化、無縫高彈性、耐候耐磨——天台/平台等長期曝曬環境更穩定",
            title_color="#fff")
        ]),
        col(50,[w_image_box(
            f"{IMG}/tech-insulation.jpg","隔熱降溫",
            "降低室內體感溫度、減少防水層熱老化——特別適合長期日曬、易過熱的上蓋位置",
            title_color="#fff")
        ]),
        col(100,[w_button("了解更多","#services","center",bg="#fff",color=DARK,mt=40)])
    ], bg=TEAL),

    # ── SERVICES
    section([
        col(100,[
            w_heading("核心服務概覽","p",TEAL,12,700,"center",8),
            w_heading("結構防水 × 家居局部滲漏","h2",DARK,32,900,"center",44)
        ]),
        *[col(33,[w_image_box(f"{IMG}/svc-{i}.jpg",t,d)])
          for i,(t,d) in enumerate([
            ("天台／平台防水工程","樓宇防水 · 採用 Polyurea 聚脲，全面覆蓋不留死角"),
            ("外牆防水及石屎修葺","樓宇防水 · 清洗、修葺、防水塗料一站式"),
            ("減溫隔熱防水系統","樓宇防水 · 降溫最多 20°C，節能防水兼得"),
            ("浴室／廁所防水工程","家居防水 · 閉水測試保證效果"),
            ("窗框防漏及修補","家居防水 · 高壓注射加密封收口"),
            ("高壓打針灌漿工程","家居防水 · 無需大規模拆卸，立即止漏"),
          ], start=1)],
        col(100,[w_button("了解更多","/services","center",mt=40)])
    ], bg="#fff"),

    # ── STATS + INSPECTION
    section([
        col(20,[
            w_heading("10,000+","p",TEAL,40,900,"left",4),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:12px;color:{GREY}">超過一萬宗成功保案</p>',mb=24),
            w_heading("12","p",TEAL,40,900,"left",4),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:12px;color:{GREY}">12年以上防水工程經驗</p>',mb=24),
            w_heading("6","p",TEAL,40,900,"left",4),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:12px;color:{GREY}">解決六大樓宇家居防水漏水問題</p>',mb=24),
            w_heading("3","p",TEAL,40,900,"left",4),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:12px;color:{GREY}">三大服務優勢</p>'),
        ]),
        col(40,[w_image(f"{IMG}/worker.jpg",radius=12)]),
        col(40,[
            w_heading("勘察與初步判斷","h3",DARK,22,900,"left",14),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:14px;color:{GREY};line-height:1.85">滲漏處理最忌在未查明滲漏源頭前便貿然施工。我們會按現場實際情況，檢查滲漏位置、可疑滲水路徑，以及各接駁位與收口位的狀況，並就建議方案方向及處理範圍提出專業建議。</p>',mb=20),
            w_heading("專業儀器尋找漏水根源","p",DARK,13,700,"left",12),
            w_icon_box("clock","紅外線熱像儀","精準偵測牆內隱藏水份，無損勘察"),
            w_icon_box("desktop","微波斷層掃描技術","穿透牆體，掃描內部水份分佈"),
            w_icon_box("bolt","導電感應檢測","確認漏水路徑及源頭位置"),
            w_button("WhatsApp 預約檢查", WA, align="left", mt=24)
        ])
    ], bg=LTBG),

    # ── APPOINTMENT
    section([
        col(60,[
            w_heading("馬上準備初步判斷","h2",DARK,32,900,"left",12),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:14px;color:{GREY};line-height:1.85">請提供滲漏位置的室內／室外相片（同位置不同角度）、說明是否只在落雨時出現或長期潮濕，以及過往是否曾做過維修／防水處理。資料越完整，我們越能更快鎖定可疑源頭。</p>')
        ]),
        col(40,[w_button("WhatsApp 預約檢查", WA, align="right")]),
        col(33,[
            w_icon_box("image","01  室內／室外相片","同一位置不同角度拍攝，愈多愈好")
        ]),
        col(33,[
            w_icon_box("tint","02  落雨先漏？","定係長期潮濕？告訴我們出現情況")
        ]),
        col(33,[
            w_icon_box("wrench","03  過往有冇做過","維修／防水處理？告訴我們歷史")
        ]),
    ], bg=LTBG),

    # ── CASES
    section([
        col(100,[w_heading("成功個案","h2",DARK,36,900,"center",44)]),
        *[col(25,[w_image_box(f"{IMG}/case-{i}.jpg",t,d)])
          for i,(t,d) in enumerate([
            ("天台防水工程","採用 Polyurea 聚脲，施工當日完成"),
            ("外牆修葺工程","石屎敲鑿、重新批盪及外牆防水塗料"),
            ("浴室防水工程","閉水測試確認，48小時驗收"),
            ("窗框防漏工程","高壓注射配合重新收口"),
          ], start=1)],
        col(100,[w_button("更多個案","/cases","center",outline=True,mt=40)])
    ], bg="#fff"),

    # ── FAQ
    section([
        col(45,[w_image(f"{IMG}/faq-worker.jpg",radius=12)]),
        col(55,[
            w_heading("常見問題 FAQ","h2",DARK,28,900,"left",28),
            w_icon_box("question-circle","為甚麼要勘察先可以準確報價？",
                       "滲漏問題成因複雜，不同位置的滲漏源頭及處理方法各異。勘察讓我們準確判斷源頭及最佳方案，從而提供精準報價。"),
            w_divider(mb=8),
            w_icon_box("question-circle","是否一定要打爛先做到？",
                       "不一定。我們會根據情況選擇最合適方案，部分情況可採用非破壞性方法（如高壓打針灌漿）處理。"),
            w_divider(mb=8),
            w_icon_box("question-circle","如何避免「做完又翻漏」？",
                       "關鍵在於找準源頭再施工。我們利用專業儀器精準定位滲水點，大大減低翻漏機會。"),
            w_divider(mb=8),
            w_icon_box("question-circle","如果漏水不處理的後果？",
                       "長期漏水導致石屎剝落、鋼筋鏽蝕、霉菌滋生，影響結構安全。問題拖延越久費用越高。"),
            w_button("WhatsApp 預約檢查", WA, align="left", mt=24)
        ])
    ], bg=LTBG),
]

# ══════════════════════════════════════════════════════════════════════════════
#  SERVICES PAGE
# ══════════════════════════════════════════════════════════════════════════════
def svc_row(img_file, tag, title, bullets, reverse=False):
    bg = "#fff" if not reverse else LTBG
    img_c = col(45,[w_image(f"{IMG}/{img_file}",radius=16)])
    txt_c = col(55,[
        w_heading(tag,"p",TEAL,12,700,"left",8),
        w_heading(title,"h2",DARK,28,900,"left",16),
        *[w_icon_box("check-circle",b[0],b[1]) for b in bullets],
        w_button("WhatsApp 即時查詢", WA, align="left", mt=20)
    ])
    return section([txt_c,img_c] if reverse else [img_c,txt_c], bg=bg)

services_sections = [
    p_hero("服務範圍","結構防水 × 家居局部滲漏","由勘察到施工，全方位保障您的物業"),
    section([
        col(33,[w_icon_box("search","先勘察後施工","利用專業儀器準確定位滲漏源頭，確保對症下藥")]),
        col(33,[w_icon_box("file-invoice","透明報價","工程範圍、工序、費用逐項列明，無隱藏收費")]),
        col(33,[w_icon_box("award","品質保證","專注細節，年期保養，保證防水效果達標")]),
    ], bg="#fff", pad_tb=60),
    svc_row("svc-1.jpg","樓宇防水","天台／平台防水工程",[
        ("Polyurea聚脲噴塗","7秒固化，無縫防水，抗UV，使用年期長"),
        ("改性瀝青防水膜","適用大面積天台，成本效益高"),
        ("閉水及積水測試","施工後全面驗收，確保無死角"),
    ]),
    svc_row("svc-2.jpg","樓宇防水","外牆防水及石屎修葺",[
        ("石屎敲鑿及重新批盪","徹底清除鬆脫部分，重建牆面"),
        ("外牆防水塗料","耐候性強，有效阻截雨水滲透"),
        ("裂縫注射及收口","針對性處理接駁位及角位"),
    ], reverse=True),
    svc_row("svc-3.jpg","樓宇防水","減溫隔熱防水系統",[
        ("高反射率塗料","降低表面溫度最多 20°C"),
        ("防水隔熱一體化","一次施工同時解決兩個問題"),
        ("節能效益","減少冷氣使用，長遠節省電費"),
    ]),
    svc_row("svc-4.jpg","家居防水","浴室／廁所防水工程",[
        ("地台全面防水膜","覆蓋地台及牆腳，滴水不漏"),
        ("48小時閉水測試","確認防水效果後方可鋪磚"),
        ("收口及接駁位處理","浴缸、花灑位等特別加強"),
    ], reverse=True),
    svc_row("svc-5.jpg","家居防水","窗框防漏及修補",[
        ("高壓聚氨酯注射","填充窗框與牆體之間的空隙"),
        ("密封膠重新收口","選用耐候性強的防水密封膠"),
        ("窗台批盪修補","恢復窗台外觀及防水功能"),
    ]),
    svc_row("svc-6.jpg","家居防水","高壓打針灌漿工程",[
        ("無需大面積拆卸","從結構內部封堵滲漏通道"),
        ("聚氨酯或環氧樹脂","遇水膨脹，永久填充空隙"),
        ("適用地下室及停車場","結構性裂縫的首選方案"),
    ], reverse=True),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CASES PAGE
# ══════════════════════════════════════════════════════════════════════════════
cases_sections = [
    p_hero("成功個案","超過 10,000 宗","由工程師跟進，確保每個工程品質達標"),

    section([
        col(100,[w_heading("天台及平台防水工程","h3",DARK,22,900,"center",32)]),
        col(33,[w_image_box(f"{IMG}/case-1.jpg","屯門天台翻新","Polyurea聚脲噴塗，施工當日完成，次日可用。積水測試通過。")]),
        col(33,[w_image_box(f"{IMG}/case-2.jpg","葵涌工廠天台","加裝高反射隔熱防水系統，降溫節能同時解決滲漏。")]),
        col(33,[w_image_box(f"{IMG}/case-3.jpg","大圍露台防水","重做防水層並加設去水坡度，徹底解決積水問題。")]),
    ], bg="#fff", pad_tb=60),

    section([
        col(100,[w_heading("家居滲漏修復工程","h3",DARK,22,900,"center",32)]),
        col(33,[w_image_box(f"{IMG}/case-4.jpg","沙田浴室地台","拆除舊磚重做防水層，48小時閉水測試通過。")]),
        col(33,[w_image_box(f"{IMG}/case-1.jpg","將軍澳窗框防漏","高壓注射聚氨酯配合重新收口，徹底解決落雨滲水。")]),
        col(33,[w_image_box(f"{IMG}/case-2.jpg","旺角廚房地台","防水膜加強收口處理，解決鄰居天花滴水問題。")]),
    ], bg=LTBG, pad_tb=60),

    section([
        col(100,[w_heading("結構及外牆工程","h3",DARK,22,900,"center",32)]),
        col(33,[w_image_box(f"{IMG}/case-3.jpg","九龍灣外牆修葺","石屎敲鑿、重新批盪及外牆防水塗料噴塗。")]),
        col(33,[w_image_box(f"{IMG}/case-4.jpg","觀塘停車場灌漿","高壓環氧樹脂灌漿，封堵結構性裂縫，永久止漏。")]),
        col(33,[w_image_box(f"{IMG}/case-1.jpg","荃灣外牆裂縫","裂縫注射修補配合防水塗料，恢復外牆功能。")]),
    ], bg="#fff", pad_tb=60),

    section([
        col(25,[
            w_heading("10,000+","p",TEAL,44,900,"center",6),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">成功工程宗數</p>')
        ]),
        col(25,[
            w_heading("12年","p",TEAL,44,900,"center",6),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">防水工程經驗</p>')
        ]),
        col(25,[
            w_heading("6大","p",TEAL,44,900,"center",6),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">滲漏問題類型</p>')
        ]),
        col(25,[
            w_heading("100%","p",TEAL,44,900,"center",6),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">閉水測試通過</p>')
        ]),
    ], bg=LTBG, pad_tb=60),
]

# ══════════════════════════════════════════════════════════════════════════════
#  ABOUT PAGE
# ══════════════════════════════════════════════════════════════════════════════
about_sections = [
    section([
        col(60,[
            w_heading("品牌故事","p",TEAL,12,700,"left",12),
            w_heading("12 年專注，只做一件事","h1",DARK,44,900,"left",16),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:16px;color:{GREY};line-height:1.85;margin-bottom:32px">銀河防水成立於 2012 年，由一群對防水工程充滿熱情的專業人士組成，致力以科學方法解決香港樓宇滲漏問題。</p>'),
            w_button("WhatsApp 查詢", WA, align="left")
        ]),
        col(40,[w_image(f"{IMG}/worker.jpg",radius=16)])
    ], img_url=f"{IMG}/hero-bg.jpg", overlay="rgba(220,245,245,0.85)", pad_tb=100),

    section([
        col(33,[
            w_heading("2012","p",TEAL,52,900,"center",8),
            w_heading("年創立","h3",DARK,16,700,"center",8),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">深耕香港防水市場，累積豐富實戰經驗</p>')
        ]),
        col(33,[
            w_heading("10,000+","p",TEAL,52,900,"center",8),
            w_heading("宗成功工程","h3",DARK,16,700,"center",8),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">橫跨住宅、商業、工廠，每宗工程均有完整記錄</p>')
        ]),
        col(33,[
            w_heading("I級","p",TEAL,52,900,"center",8),
            w_heading("屋宇署認可承建商","h3",DARK,16,700,"center",8),
            w_text(f'<p style="text-align:center;font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY}">所有工程符合香港建築法規要求</p>')
        ]),
    ], bg="#fff", pad_tb=80),

    section([
        col(50,[w_image(f"{IMG}/inspect-service.jpg",radius=16)]),
        col(50,[
            w_heading("我們的使命","p",TEAL,12,700,"left",12),
            w_heading("從根源解決滲漏，還您安心居所","h2",DARK,30,900,"left",16),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:14px;color:{GREY};line-height:1.85;margin-bottom:14px">我們相信防水工程不應靠猜測，而是建立在準確診斷和科學選材的基礎上。每一個工程，我們都從勘察開始，找到真正的滲漏源頭。</p>'),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:14px;color:{GREY};line-height:1.85;margin-bottom:14px">多年來，我們服務了超過一萬個家庭和商業客戶，從天台、外牆、浴室到窗框，無論大小工程，均以同等的專業態度對待。</p>'),
            w_button("WhatsApp 查詢", WA, align="left", mt=20)
        ])
    ], bg=LTBG),

    section([
        col(100,[w_heading("我們的服務承諾","h2",DARK,32,900,"center",44)]),
        col(33,[w_icon_box("search","先勘察後施工","利用紅外線熱像儀、微波掃描等儀器精確定位滲漏源頭，確保對症下藥。")]),
        col(33,[w_icon_box("file-invoice-dollar","透明報價無隱費","報價書列明工程範圍、工序、材料及費用，工程開始後不追加收費。")]),
        col(33,[w_icon_box("shield-alt","年期保養保障","工程完成後提供年期保養，期間如有問題可聯絡我們跟進。")]),
    ], bg="#fff"),
]

# ══════════════════════════════════════════════════════════════════════════════
#  BLOG PAGE
# ══════════════════════════════════════════════════════════════════════════════
blog_sections = [
    p_hero("防水網誌","防水知識、案例分析及保養貼士","助您了解滲漏問題的根源與解決方案"),

    section([
        col(100,[w_heading("最新文章","h2",DARK,32,900,"center",44)]),
        col(33,[
            w_image(f"{IMG}/prob-rooftop.jpg",radius=12,mb=16),
            w_heading("為甚麼天台防水每隔幾年就要重做？","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">防水層有使用年限，加上香港氣候炎熱多雨，老化速度比其他地區快。本文解釋何時需要翻新。</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
        col(33,[
            w_image(f"{IMG}/prob-bathroom.jpg",radius=12,mb=16),
            w_heading("浴室漏水的 5 個警示訊號","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">如何在問題惡化前及早發現浴室滲漏？本文列出 5 個常見警示訊號，幫助業主及早行動。</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
        col(33,[
            w_image(f"{IMG}/prob-window.jpg",radius=12,mb=16),
            w_heading("香港舊樓窗框滲水怎麼辦？","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">窗框老化是香港舊樓最常見的滲漏問題之一。本文介紹成因及專業修繕方案。</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
    ], bg="#fff", pad_tb=60),

    section([
        col(33,[
            w_image(f"{IMG}/prob-concrete.jpg",radius=12,mb=16),
            w_heading("石屎剝落需要緊急處理嗎？","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">石屎剝落除了影響外觀，更可能引起結構安全問題。本文說明不同情況的處理優先順序。</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
        col(33,[
            w_image(f"{IMG}/tech-polyurea.jpg",radius=12,mb=16),
            w_heading("Polyurea 聚脲 vs 傳統防水塗料","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">比較聚脲與傳統防水材料的優缺點，幫助你了解適用場景和選擇方法。</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
        col(33,[
            w_image(f"{IMG}/tech-insulation.jpg",radius=12,mb=16),
            w_heading("天台隔熱防水一體化系統","h3",DARK,16,800,"left",8),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:13px;color:{GREY};line-height:1.7">香港夏天天台溫度可超過 60°C，如何透過隔熱防水系統同時解決滲漏和過熱問題？</p>',mb=16),
            w_button("閱讀更多", WA, align="left", outline=True)
        ]),
    ], bg=LTBG, pad_tb=60),
]

# ══════════════════════════════════════════════════════════════════════════════
#  CONTACT PAGE
# ══════════════════════════════════════════════════════════════════════════════
contact_sections = [
    p_hero("聯絡我們","歡迎 WhatsApp、電話或電郵查詢","我們的工程師會盡快評估並回覆建議方案"),

    section([
        col(55,[
            w_heading("立即聯絡","p",TEAL,12,700,"left",12),
            w_heading("告訴我們您的問題","h2",DARK,30,900,"left",16),
            w_text(f'<p style="font-family:\'Noto Sans TC\',sans-serif;font-size:14px;color:{GREY};line-height:1.85;margin-bottom:28px">請提供滲漏位置相片及簡單描述，我們的工程師會盡快評估並回覆。初步評估完全免費。</p>'),
            w_icon_box("whatsapp","(852) 5222 5111","點擊直接 WhatsApp 查詢，最快速回覆方式",
                       bg="#EEF9F9"),
            w_divider(mb=8),
            w_icon_box("phone","(852) 6880 0698","備用聯絡電話",bg="#EEF9F9"),
            w_divider(mb=8),
            w_icon_box("envelope","galaxywindowhk@gmail.com","電郵查詢，一般於一個工作天內回覆",bg="#EEF9F9"),
            w_button("WhatsApp 即時查詢", WA, align="left", mt=28, size="lg")
        ]),
        col(45,[
            w_heading("辦公室地址","h3",DARK,20,900,"left",20),
            w_icon_box("map-marker-alt","九龍大角咀通州街123號","國貿中心 2 樓 C 室",bg=LTBG),
            w_divider(mb=16),
            w_icon_box("clock","辦公時間","星期一至五 9:00–18:00　星期六 9:00–13:00　星期日及公眾假期休息",bg=LTBG),
            w_divider(mb=16),
            w_icon_box("car","交通","大角咀地鐵站 C 出口，步行約 8 分鐘",bg=LTBG),
        ])
    ], bg="#fff"),

    section([
        col(33,[w_icon_box("camera","提供相片","室內／室外滲漏位置相片，愈多角度愈好")]),
        col(33,[w_icon_box("tint","描述情況","落雨先漏？定長期潮濕？何時開始出現？")]),
        col(33,[w_icon_box("history","過往記錄","曾否做過防水或維修處理？效果如何？")]),
    ], bg=LTBG, pad_tb=60),
]

# ══════════════════════════════════════════════════════════════════════════════
#  BUILD & WRITE
# ══════════════════════════════════════════════════════════════════════════════
pages = {
    "homepage": ({"version":"0.4","title":"銀河防水 – 首頁","type":"page",
                  "content":[s_header()]+home_sections+[s_cta(),s_footer()],
                  "page_settings":{"hide_title":"yes","post_status":"publish"}},
                 "首頁","home"),
    "services": (wrap("銀河防水 – 服務範圍", services_sections), "服務範圍","services"),
    "cases":    (wrap("銀河防水 – 成功個案", cases_sections),   "成功個案","cases"),
    "about":    (wrap("銀河防水 – 品牌故事", about_sections),   "品牌故事","about"),
    "blog":     (wrap("銀河防水 – 防水網誌", blog_sections),    "防水網誌","blog"),
    "contact":  (wrap("銀河防水 – 聯絡我們", contact_sections), "聯絡我們","contact"),
}

os.makedirs(KIT_DIR, exist_ok=True)
for fname,(data,title,slug) in pages.items():
    out = os.path.join(KIT_DIR, f"{fname}.json")
    with open(out,"w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  OK {fname}.json  ({os.path.getsize(out)//1024} KB)")

# ── manifest
manifest = {"name":"Galaxy Waterproof","title":"Galaxy Waterproof",
            "version":"3","author":"Galaxy Waterproof",
            "description":"Complete site – 6 pages with native Elementor widgets",
            "thumbnail":"","created":"2026-05-17T00:00:00",
            "elementor_version":"3.21.0","plugins":[],
            "templates":[{"name":k,"title":v[1],"type":"page","thumbnail":"",
                          "url":f"templates/{k}.json","export_date":"2026-05-17T00:00:00",
                          "source":"local","language":""}
                         for k,v in pages.items()],
            "content":{},"site-settings":{"settings":{},"kit_settings":{}}}
with open(os.path.join(BASE,"elementor-kit","manifest.json"),"w",encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("  OK manifest.json")

# ── kit zip
zip_path = os.path.join(BASE,"galaxy-waterproof-elementor-kit.zip")
if os.path.exists(zip_path): os.remove(zip_path)
with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as zf:
    for root,dirs,files in os.walk(os.path.join(BASE,"elementor-kit")):
        for file in files:
            ap = os.path.join(root,file)
            zf.write(ap, os.path.relpath(ap, os.path.join(BASE,"elementor-kit")))
print(f"  OK galaxy-waterproof-elementor-kit.zip  ({os.path.getsize(zip_path)//1024} KB)")

# ── WordPress XML (WXR) – single import file
def cdata_safe(s):
    return s.replace("]]>","]]]]><![CDATA[>")

items = []
for pid,(fname,(data,title,slug)) in enumerate(pages.items(), start=10):
    el_json = json.dumps(data["content"], ensure_ascii=False)
    items.append(f"""
  <item>
    <title>{title}</title>
    <link>https://example.com/{slug}/</link>
    <pubDate>Sat, 17 May 2026 00:00:00 +0000</pubDate>
    <dc:creator>admin</dc:creator>
    <content:encoded><![CDATA[]]></content:encoded>
    <excerpt:encoded><![CDATA[]]></excerpt:encoded>
    <wp:post_id>{pid}</wp:post_id>
    <wp:post_date>2026-05-17 00:00:00</wp:post_date>
    <wp:post_date_gmt>2026-05-17 00:00:00</wp:post_date_gmt>
    <wp:comment_status>closed</wp:comment_status>
    <wp:ping_status>closed</wp:ping_status>
    <wp:post_name>{slug}</wp:post_name>
    <wp:status>publish</wp:status>
    <wp:post_parent>0</wp:post_parent>
    <wp:menu_order>{pid}</wp:menu_order>
    <wp:post_type>page</wp:post_type>
    <wp:post_password></wp:post_password>
    <wp:is_sticky>0</wp:is_sticky>
    <wp:postmeta>
      <wp:meta_key>_wp_page_template</wp:meta_key>
      <wp:meta_value><![CDATA[elementor_canvas]]></wp:meta_value>
    </wp:postmeta>
    <wp:postmeta>
      <wp:meta_key>_elementor_edit_mode</wp:meta_key>
      <wp:meta_value><![CDATA[builder]]></wp:meta_value>
    </wp:postmeta>
    <wp:postmeta>
      <wp:meta_key>_elementor_template_type</wp:meta_key>
      <wp:meta_value><![CDATA[wp-page]]></wp:meta_value>
    </wp:postmeta>
    <wp:postmeta>
      <wp:meta_key>_elementor_version</wp:meta_key>
      <wp:meta_value><![CDATA[3.21.0]]></wp:meta_value>
    </wp:postmeta>
    <wp:postmeta>
      <wp:meta_key>_elementor_data</wp:meta_key>
      <wp:meta_value><![CDATA[{cdata_safe(el_json)}]]></wp:meta_value>
    </wp:postmeta>
  </item>""")

wxr = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
  xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
  xmlns:content="http://purl.org/rss/1.0/modules/content/"
  xmlns:wfw="http://wellformedweb.org/CommentAPI/"
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:wp="http://wordpress.org/export/1.2/">
<channel>
  <title>銀河防水</title>
  <link>https://example.com</link>
  <description>專業防水工程 Hong Kong</description>
  <language>zh-TW</language>
  <wp:wxr_version>1.2</wp:wxr_version>
  <wp:base_site_url>https://example.com</wp:base_site_url>
  <wp:base_blog_url>https://example.com</wp:base_blog_url>
""" + "".join(items) + "\n</channel>\n</rss>\n"

wxr_path = os.path.join(BASE,"galaxy-waterproof-demo.xml")
with open(wxr_path,"w",encoding="utf-8") as f:
    f.write(wxr)
print(f"  OK galaxy-waterproof-demo.xml  ({os.path.getsize(wxr_path)//1024} KB)")
print("\nDone — import galaxy-waterproof-demo.xml via:")
print("  WP Admin > Tools > Import > WordPress > Upload File")
