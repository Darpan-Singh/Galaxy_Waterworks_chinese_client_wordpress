"""
Generate all Elementor page templates for Galaxy Waterproof site.
Each page embeds header + content + footer so it works with Elementor Free.
"""
import json, os, shutil

BASE = r"C:\Users\01dar\wordpress_website"
IMG  = "https://galaxy-waterproof.vercel.app/wp-content/themes/galaxy-waterproof/assets/images"
LOGO = f"{IMG}/logo.jpg"
WA   = "https://wa.me/85252225111"
FB   = "https://www.facebook.com/galaxywindowhk"
IG   = "https://www.instagram.com/galaxywindowhk"
TEAL = "#5BBCBC"
FONT = "font-family:'Noto Sans TC',sans-serif;"

# ─── shared snippets ──────────────────────────────────────────────────────────

WA_SVG = '<svg width="11" height="11" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>'
FB_SVG  = '<svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg>'
IG_SVG  = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>'
CHK_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>'
EMAIL_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5BBCBC" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>'
PHONE_SVG = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5BBCBC" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.07 1.18 2 2 0 012.03 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92v2z"/></svg>'
PIN_SVG   = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#5BBCBC" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>'

HEADER_HTML = f"""<header style="background:#fff;border-bottom:1px solid #E8EDED;display:flex;align-items:center;justify-content:space-between;padding:14px 60px;gap:20px;width:100%;box-sizing:border-box">
  <a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0">
    <img src="{LOGO}" style="height:44px;width:auto;display:block" alt="銀河防水">
    <span style="{FONT}font-size:22px;font-weight:900;color:#1A1A1A">銀河防水</span>
  </a>
  <nav style="display:flex;align-items:center;gap:28px;flex:1;justify-content:center">
    <a href="/" style="{FONT}font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">首頁</a>
    <a href="/services" style="{FONT}font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">服務範圍</a>
    <a href="/cases" style="{FONT}font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">成功案例</a>
    <a href="/blog" style="{FONT}font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">防水網誌</a>
    <a href="/about" style="{FONT}font-size:14px;font-weight:500;color:#1A1A1A;text-decoration:none">品牌故事</a>
  </nav>
  <div style="display:flex;align-items:center;gap:12px;flex-shrink:0">
    <a href="{FB}" target="_blank" style="width:30px;height:30px;border-radius:50%;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;color:#555;text-decoration:none">{FB_SVG}</a>
    <a href="{IG}" target="_blank" style="width:30px;height:30px;border-radius:50%;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;color:#555;text-decoration:none">{IG_SVG}</a>
    <a href="{WA}" target="_blank" style="display:flex;flex-direction:column;align-items:center;background:{TEAL};color:#fff;border-radius:10px;padding:7px 16px;text-decoration:none;gap:2px">
      <span style="{FONT}font-size:10.5px;font-weight:600;display:flex;align-items:center;gap:4px">{WA_SVG}WhatsApp 快速查詢</span>
      <span style="{FONT}font-size:14px;font-weight:900">9123-4567</span>
    </a>
  </div>
</header>"""

FOOTER_TOP_HTML = f"""<div style="background:#F5F5F3;padding:64px 60px 48px;display:grid;grid-template-columns:2fr 1fr 2fr;gap:48px;box-sizing:border-box;width:100%">
  <div>
    <a href="/" style="display:inline-flex;align-items:center;gap:8px;text-decoration:none;margin-bottom:16px">
      <img src="{LOGO}" style="height:48px;width:auto;display:block" alt="銀河防水">
      <span style="{FONT}font-size:26px;font-weight:900;color:#1A1A1A">銀河防水</span>
    </a>
    <p style="{FONT}font-size:13px;color:#555;line-height:1.8;margin-bottom:24px">本公司為屋宇署認可I級註冊小型工程承建商(公司) 多年來致力為客戶提供專業鋁窗檢驗，維修保養及防漏工程服務。</p>
    <div style="display:flex;flex-direction:column;gap:12px">
      <a href="mailto:galaxywindowhk@gmail.com" style="display:flex;align-items:center;justify-content:space-between;border:2px solid {TEAL};color:{TEAL};border-radius:50px;padding:10px 12px 10px 16px;{FONT}font-weight:600;font-size:14px;text-decoration:none">
        <span style="display:flex;align-items:center;gap:8px"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>網上報價查詢</span>
        <span style="width:26px;height:26px;border:1.5px solid {TEAL};border-radius:50%;display:flex;align-items:center;justify-content:center"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></span>
      </a>
      <a href="{WA}" target="_blank" style="display:flex;align-items:center;justify-content:space-between;background:{TEAL};color:#fff;border-radius:50px;padding:10px 12px 10px 16px;{FONT}font-weight:600;font-size:14px;text-decoration:none">
        <span style="display:flex;align-items:center;gap:8px">{WA_SVG}WhatsApp預約檢查</span>
        <span style="width:26px;height:26px;background:rgba(255,255,255,0.25);border-radius:50%;display:flex;align-items:center;justify-content:center"><svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="9 18 15 12 9 6"/></svg></span>
      </a>
    </div>
  </div>
  <nav>
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:16px">
      <li><a href="/" style="{FONT}font-size:14.5px;color:#1A1A1A;font-weight:500;text-decoration:none">首頁</a></li>
      <li><a href="/services" style="{FONT}font-size:14.5px;color:#1A1A1A;font-weight:500;text-decoration:none">服務範圍</a></li>
      <li><a href="/cases" style="{FONT}font-size:14.5px;color:#1A1A1A;font-weight:500;text-decoration:none">成功案例</a></li>
      <li><a href="/blog" style="{FONT}font-size:14.5px;color:#1A1A1A;font-weight:500;text-decoration:none">防水網誌</a></li>
      <li><a href="/about" style="{FONT}font-size:14.5px;color:#1A1A1A;font-weight:500;text-decoration:none">品牌故事</a></li>
    </ul>
  </nav>
  <div>
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
      <p style="{FONT}font-size:14px;font-weight:700;color:#1A1A1A;margin:0">如有查詢及報價，歡迎與我們聯絡。</p>
      <a href="{FB}" target="_blank" style="width:34px;height:34px;border-radius:50%;border:1.5px solid #ddd;display:flex;align-items:center;justify-content:center;color:#555;text-decoration:none">{FB_SVG}</a>
    </div>
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px">
      <li style="display:flex;align-items:flex-start;gap:10px;{FONT}font-size:13px;color:#555">{EMAIL_SVG}<a href="mailto:galaxywindowhk@gmail.com" style="color:#555;text-decoration:none">galaxywindowhk@gmail.com</a></li>
      <li style="display:flex;align-items:flex-start;gap:10px;{FONT}font-size:13px;color:#555">{PHONE_SVG}<span>(852) 5222 5111 &nbsp;|&nbsp; (852) 6880 0698</span></li>
      <li style="display:flex;align-items:flex-start;gap:10px;{FONT}font-size:13px;color:#555">{PIN_SVG}<span>九龍大角咀通州街123號國貿中心2樓C室</span></li>
    </ul>
  </div>
</div>"""

FOOTER_BOT_HTML = f'<div style="background:#F5F5F3;border-top:1px solid #E8EDED;padding:18px 60px;box-sizing:border-box;width:100%"><p style="{FONT}text-align:center;font-size:12px;color:#888">©2026, 銀河防水有限公司</p></div>'

# ─── helpers ─────────────────────────────────────────────────────────────────

_id_ctr = [1000]
def uid(prefix="x"):
    _id_ctr[0] += 1
    return f"{prefix}{_id_ctr[0]}"

def section(content_cols, bg="#ffffff", pad_tb=80, pad_lr=60, extra_settings=None):
    s = {
        "id": uid("s"),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "background_background": "classic",
            "background_color": bg,
            "padding": {"unit":"px","top":str(pad_tb),"right":str(pad_lr),
                        "bottom":str(pad_tb),"left":str(pad_lr),"isLinked":False}
        },
        "elements": content_cols
    }
    if extra_settings:
        s["settings"].update(extra_settings)
    return s

def section_bg_img(img_url, overlay_color, content_cols, pad_tb=90):
    return {
        "id": uid("s"),
        "elType": "section",
        "settings": {
            "stretch_section": "section-stretched",
            "background_background": "classic",
            "background_image": {"url": img_url, "id": ""},
            "background_size": "cover",
            "background_position": "center center",
            "background_overlay_background": "classic",
            "background_overlay_color": overlay_color,
            "padding": {"unit":"px","top":str(pad_tb),"right":"60",
                        "bottom":str(pad_tb),"left":"60","isLinked":False}
        },
        "elements": content_cols
    }

def col(size, widgets):
    return {"id": uid("c"), "elType": "column",
            "settings": {"_column_size": size}, "elements": widgets}

def html_widget(html_str):
    return {"id": uid("w"), "elType": "widget", "widgetType": "html",
            "settings": {"html": html_str}}

def heading_widget(text, tag="h2", color="#1A1A1A", size=36, weight=900,
                   align="center", mb=12):
    return {
        "id": uid("w"), "elType": "widget", "widgetType": "heading",
        "settings": {
            "title": text, "header_size": tag, "align": align,
            "title_color": color,
            "typography_typography": "custom",
            "typography_font_family": "Noto Sans TC",
            "typography_font_size": {"unit": "px", "size": size},
            "typography_font_weight": str(weight),
            "_margin": {"unit":"px","top":"0","right":"0",
                        "bottom":str(mb),"left":"0","isLinked":False}
        }
    }

def text_widget(html_str, mb=0):
    return {
        "id": uid("w"), "elType": "widget", "widgetType": "text-editor",
        "settings": {
            "editor": html_str,
            "_margin": {"unit":"px","top":"0","right":"0",
                        "bottom":str(mb),"left":"0","isLinked":False}
        }
    }

def btn_widget(text, url, align="center", bg=TEAL, color="#fff", mt=0,
               outline=False):
    s = {
        "text": text,
        "link": {"url": url, "is_external": "true" if url.startswith("http") else ""},
        "align": align,
        "background_color": "rgba(0,0,0,0)" if outline else bg,
        "button_text_color": bg if outline else color,
        "border_radius": {"unit":"px","top":50,"right":50,"bottom":50,"left":50,"isLinked":True},
        "typography_font_family": "Noto Sans TC",
        "typography_font_weight": "700",
        "text_padding": {"unit":"px","top":"13","right":"32","bottom":"13","left":"32","isLinked":False},
        "_margin": {"unit":"px","top":str(mt),"right":"0","bottom":"0","left":"0","isLinked":False}
    }
    if outline:
        s["border_border"] = "solid"
        s["border_width"] = {"unit":"px","top":"2","right":"2","bottom":"2","left":"2","isLinked":True}
        s["border_color"] = bg
    return {"id": uid("w"), "elType": "widget", "widgetType": "button", "settings": s}

def image_widget(url, radius=12, mb=0):
    return {
        "id": uid("w"), "elType": "widget", "widgetType": "image",
        "settings": {
            "image": {"url": url, "id": ""},
            "image_size": "full",
            "image_border_radius": {"unit":"px","top":str(radius),"right":str(radius),
                                    "bottom":str(radius),"left":str(radius),"isLinked":True},
            "_margin": {"unit":"px","top":"0","right":"0",
                        "bottom":str(mb),"left":"0","isLinked":False}
        }
    }

# shared header/footer sections
def hdr_section():
    return section([col(100, [html_widget(HEADER_HTML)])], pad_tb=0, pad_lr=0,
                   extra_settings={"border_border":"solid",
                                   "border_width":{"unit":"px","top":"0","right":"0","bottom":"1","left":"0","isLinked":False},
                                   "border_color":"#E8EDED"})

def ftr_sections():
    return [
        section([col(100, [html_widget(FOOTER_TOP_HTML)])], bg="#F5F5F3", pad_tb=0, pad_lr=0),
        section([col(100, [html_widget(FOOTER_BOT_HTML)])], bg="#F5F5F3", pad_tb=0, pad_lr=0,
                extra_settings={"border_border":"solid",
                                "border_width":{"unit":"px","top":"1","right":"0","bottom":"0","left":"0","isLinked":False},
                                "border_color":"#E8EDED"})
    ]

def page_hero_section(title, subtitle, bg_color="#EDF7F7"):
    return section([
        col(100, [
            heading_widget(title, "h1", "#1A1A1A", 44, 900, "center", 12),
            text_widget(f'<p style="{FONT}font-size:16px;color:#555;text-align:center;line-height:1.8">{subtitle}</p>')
        ])
    ], bg=bg_color, pad_tb=80)

def cta_section():
    return section_bg_img(
        f"{IMG}/cta-bg.jpg", "rgba(230,248,248,0.80)",
        [col(100, [
            heading_widget("不要讓雨季成為你的煩惱", "h2", "#2A7474", 40, 900, "left", 10),
            heading_widget("別再忍受滲漏困擾  從源頭一次解決", "p", "#555555", 17, 400, "left", 36),
            btn_widget("立即 WhatsApp 預約", WA, align="left")
        ])]
    )

def make_template(title, sections_list):
    return {
        "version": "0.4",
        "title": title,
        "type": "page",
        "content": [hdr_section()] + sections_list + ftr_sections(),
        "page_settings": {"hide_title": "yes", "post_status": "publish"}
    }

# ─── SERVICE CARD helper ──────────────────────────────────────────────────────

def svc_detail_section(img_file, tag, title, desc_paras, reverse=False):
    """Alternating image/text layout for each service."""
    img_col = col(45, [image_widget(f"{IMG}/{img_file}", radius=16)])
    text_col = col(55, [
        html_widget(f'<span style="{FONT}font-size:11px;font-weight:700;color:{TEAL};letter-spacing:2px;text-transform:uppercase;display:block;margin-bottom:8px">{tag}</span>'),
        heading_widget(title, "h2", "#1A1A1A", 30, 900, "left", 16),
        *[text_widget(f'<p style="{FONT}font-size:14px;color:#555;line-height:1.85;margin-bottom:12px">{p}</p>')
          for p in desc_paras],
        btn_widget("WhatsApp 即時查詢", WA, align="left", mt=20)
    ])
    cols = [text_col, img_col] if reverse else [img_col, text_col]
    return section(cols, bg="#fff" if not reverse else "#F5F5F3")

# ─── PAGE: HOMEPAGE ───────────────────────────────────────────────────────────
# Load the existing homepage JSON and prepend header + append footer

with open(os.path.join(BASE, "galaxy-waterproof-elementor.json"), encoding="utf-8") as f:
    home_data = json.load(f)

home_data["content"] = [hdr_section()] + home_data["content"] + ftr_sections()
home_data["page_settings"] = {"hide_title": "yes", "post_status": "publish"}

# ─── PAGE: SERVICES ───────────────────────────────────────────────────────────

services_sections = [
    page_hero_section("服務範圍", "結構防水 × 家居局部滲漏，由勘察到施工，全方位保障您的物業"),

    # intro strip
    section([col(100, [
        html_widget(f'''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
  {"".join([f'''<div style="background:#F0FAFA;border-radius:12px;padding:24px 20px;text-align:center">
    <div style="width:48px;height:48px;border-radius:50%;background:{TEAL};display:flex;align-items:center;justify-content:center;margin:0 auto 14px">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2">{icon}</svg>
    </div>
    <h3 style="{FONT}font-size:15px;font-weight:800;color:#1A1A1A;margin-bottom:8px">{t}</h3>
    <p style="{FONT}font-size:13px;color:#555;line-height:1.7">{d}</p>
  </div>''' for icon,t,d in [
    ('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>', '先勘察後施工', '利用專業儀器準確定位滲漏源頭'),
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>', '透明報價', '工程範圍、工序、費用逐項列明'),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>', '品質保證', '專注細節，保證防水效果達標'),
  ]])}
</div>''')
    ])], bg="#fff", pad_tb=60),

    svc_detail_section("svc-1.jpg", "樓宇防水", "天台／平台防水工程",
        ["天台及平台是樓宇最容易滲漏的位置。長期日曬雨淋令防水層老化開裂，雨水沿裂縫滲入樓板，引起室內滲漏及石屎剝落。",
         "我們採用 Polyurea 聚脲或改性瀝青等高效防水材料，配合底漆及收口處理，確保全面覆蓋不留死角。施工後提供年期保養，讓您安心。",
         "適用範圍：住宅天台、商業平台、停車場上蓋、花園平台。"]),

    svc_detail_section("svc-2.jpg", "樓宇防水", "外牆防水及石屎修葺",
        ["外牆長期暴露於風雨及紫外線下，批盪鬆脫、石屎剝落、外牆裂縫均是常見問題，不但影響外觀，更會引致室內滲水。",
         "我們提供外牆清洗、石屎修葺、防水塗料噴塗一站式服務，選用符合香港氣候的外牆防水系統，提升外牆耐候性。",
         "適用範圍：樓宇外牆、石屎剝落修補、外牆裂縫注射。"], reverse=True),

    svc_detail_section("svc-3.jpg", "樓宇防水", "減溫隔熱防水系統",
        ["天台及平台面積大、日照時間長，夏季表面溫度可高達 60°C 以上，加速防水層老化，同時令室內溫度上升。",
         "我們採用高反射率隔熱防水一體化塗料，在提供防水保護的同時，有效降低天台表面溫度最多 20°C，減少冷氣使用，節省能源。",
         "適用範圍：住宅天台、商用天台、工廠上蓋。"]),

    svc_detail_section("svc-4.jpg", "家居防水", "浴室／廁所防水工程",
        ["浴室是家居滲漏最常見的源頭。地台防水層失效後，水氣長期滲入樓板，輕則令樓下天花發霉，重則導致結構損壞。",
         "我們提供全面的浴室防水處理，包括地台批底、防水膜施工、收口及接駁位處理，工程完成後進行閉水測試，確保防水效果。",
         "適用範圍：住宅浴室、廁所、廚房地台。"], reverse=True),

    svc_detail_section("svc-5.jpg", "家居防水", "窗框防漏及修補",
        ["窗框老化、收口膠條脫落是香港家居最普遍的漏水問題。落雨時水分沿窗框縫隙滲入牆內，長期積聚引起牆身發霉及批盪脫落。",
         "我們提供窗框周邊防水注射、密封膠重新收口、窗台批盪修補等服務，徹底堵截滲漏路徑，效果持久。",
         "適用範圍：鋁窗框、窗台、牆角接駁位。"]),

    svc_detail_section("svc-6.jpg", "家居防水", "高壓打針灌漿工程",
        ["高壓灌漿是處理結構性裂縫及地下滲水的有效方法，無需大規模拆卸即可從內部封堵滲漏通道。",
         "技術人員在裂縫或滲水位鑽孔，以高壓注射聚氨酯或環氧樹脂漿液，材料遇水膨脹迅速填充空隙，形成永久防水屏障。",
         "適用範圍：地下室、停車場牆身裂縫、結構性滲漏。"], reverse=True),

    cta_section(),
]

# ─── PAGE: CASES ─────────────────────────────────────────────────────────────

def case_card(img_file, label, desc):
    return f'''<div style="border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.07);background:#fff">
  <div style="position:relative">
    <img src="{IMG}/{img_file}" style="width:100%;height:240px;object-fit:cover;display:block">
    <div style="position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 50%);display:flex;align-items:flex-end;padding:16px">
      <span style="{FONT}font-size:13px;font-weight:700;color:#fff">{label}</span>
    </div>
  </div>
  <div style="padding:18px 20px">
    <p style="{FONT}font-size:13px;color:#555;line-height:1.75">{desc}</p>
    <a href="{WA}" target="_blank" style="{FONT}display:inline-block;margin-top:14px;font-size:12.5px;font-weight:600;color:{TEAL};text-decoration:none">WhatsApp 查詢 →</a>
  </div>
</div>'''

CASE_DATA = [
    ("case-1.jpg","天台防水工程","屯門舊樓天台翻新，採用 Polyurea 聚脲噴塗，施工當日完成，次日可投入使用。工程後進行積水測試確認效果。"),
    ("case-2.jpg","外牆修葺工程","九龍灣工廠大廈外牆批盪大面積鬆脫，我們完成石屎敲鑿、重新批盪及外牆防水塗料噴塗，恢復外牆防水功能。"),
    ("case-3.jpg","浴室防水工程","沙田私人屋苑浴室地台滲漏導致樓下天花剝落，拆除舊瓷磚後重做防水層，並進行 48 小時閉水測試。"),
    ("case-4.jpg","窗框防漏工程","將軍澳住宅窗框四邊大範圍滲水，以高壓注射聚氨酯配合重新收口，徹底解決落雨滲水問題。"),
    ("case-1.jpg","隔熱防水系統","葵涌工廠天台加裝高反射隔熱防水系統，有效降低室內溫度，節省冷氣電費，同時解決滲漏問題。"),
    ("case-2.jpg","灌漿止漏工程","觀塘停車場外牆結構性裂縫持續滲水，採用高壓環氧樹脂灌漿，封堵裂縫，永久止漏。"),
    ("case-3.jpg","露台防水工程","大圍露台積水問題，重做防水層並加設去水坡度，徹底解決積水及滲漏問題。"),
    ("case-4.jpg","廚房地台防水","旺角舊樓廚房地台長期潮濕，重做防水膜，加強收口處理，解決鄰居天花滴水問題。"),
]

cases_sections = [
    page_hero_section("成功個案", "超過 10,000 宗成功防水工程，每一個案均由工程師跟進，確保品質達標"),

    section([col(100, [
        html_widget(f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{"".join(case_card(i,l,d) for i,l,d in CASE_DATA[:4])}</div>')
    ])], pad_tb=60),
    section([col(100, [
        html_widget(f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{"".join(case_card(i,l,d) for i,l,d in CASE_DATA[4:])}</div>')
    ])], pad_tb=0, pad_lr=60),

    # stats bar
    section([col(100, [
        html_widget(f'''<div style="display:flex;justify-content:space-around;align-items:center;padding:48px 0;border-top:1px solid #E8EDED;border-bottom:1px solid #E8EDED">
  {"".join(f'''<div style="text-align:center">
    <span style="{FONT}font-size:42px;font-weight:900;color:{TEAL};display:block;line-height:1">{num}</span>
    <span style="{FONT}font-size:12px;color:#555;display:block;margin-top:6px;line-height:1.5">{label}</span>
  </div>''' for num,label in [("10,000+","成功工程宗數"),("12年","防水工程經驗"),("6大","滲漏問題類型"),("100%","閉水測試通過")])}
</div>''')
    ])], bg="#fff", pad_tb=0),

    cta_section(),
]

# ─── PAGE: ABOUT ──────────────────────────────────────────────────────────────

about_sections = [
    section_bg_img(f"{IMG}/hero-bg.jpg", "rgba(220,245,245,0.85)", [
        col(60, [
            html_widget(f'<p style="{FONT}font-size:12px;font-weight:700;color:{TEAL};letter-spacing:2.5px;text-transform:uppercase;margin-bottom:12px">品牌故事</p>'),
            heading_widget("12 年專注，只做一件事", "h1", "#1A1A1A", 44, 900, "left", 16),
            text_widget(f'<p style="{FONT}font-size:16px;color:#444;line-height:1.85;margin-bottom:32px">銀河防水成立於 2012 年，由一群對防水工程充滿熱情的專業人士組成，致力以科學方法解決香港樓宇滲漏問題。</p>'),
            btn_widget("立即 WhatsApp 查詢", WA, align="left")
        ]),
        col(40, [])
    ], pad_tb=100),

    section([col(100, [
        html_widget(f'''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:32px">
  {"".join(f'''<div style="text-align:center;padding:40px 28px;border-radius:16px;background:#F0FAFA">
    <span style="{FONT}font-size:52px;font-weight:900;color:{TEAL};line-height:1;display:block;margin-bottom:10px">{num}</span>
    <h3 style="{FONT}font-size:16px;font-weight:800;color:#1A1A1A;margin-bottom:8px">{title}</h3>
    <p style="{FONT}font-size:13px;color:#555;line-height:1.7">{desc}</p>
  </div>''' for num,title,desc in [
    ("12+","年防水工程經驗","2012 年創立，深耕香港防水市場，累積豐富實戰經驗"),
    ("10,000+","宗成功工程","橫跨住宅、商業、工廠，每宗工程均有完整記錄"),
    ("3 大","服務優勢","先勘察後施工、報價透明、重視細節，三大承諾貫穿每個工程"),
  ])}
</div>''')
    ])], bg="#fff", pad_tb=80),

    section([
        col(50, [
            image_widget(f"{IMG}/worker.jpg", radius=16)
        ]),
        col(50, [
            html_widget(f'<p style="{FONT}font-size:12px;font-weight:700;color:{TEAL};letter-spacing:2.5px;text-transform:uppercase;margin-bottom:12px">我們的使命</p>'),
            heading_widget("從根源解決滲漏，還您安心居所", "h2", "#1A1A1A", 30, 900, "left", 16),
            text_widget(f'<p style="{FONT}font-size:14px;color:#555;line-height:1.85;margin-bottom:16px">我們相信防水工程不應靠猜測，而是建立在準確診斷和科學選材的基礎上。每一個工程，我們都從勘察開始，找到真正的滲漏源頭，再提供針對性解決方案。</p>'),
            text_widget(f'<p style="{FONT}font-size:14px;color:#555;line-height:1.85;margin-bottom:16px">多年來，我們服務了超過一萬個家庭和商業客戶，從天台、外牆、浴室到窗框，無論大小工程，都以同等的專業態度對待。</p>'),
            text_widget(f'<p style="{FONT}font-size:14px;color:#555;line-height:1.85">本公司持有屋宇署認可 I 級小型工程承建商牌照，所有工程均符合香港建築法規要求。</p>'),
        ])
    ], bg="#F5F5F3"),

    section([col(100, [
        heading_widget("我們的服務承諾", "h2", "#1A1A1A", 32, 900, "center", 44),
        html_widget(f'''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
  {"".join(f'''<div style="border:2px solid #E8EDED;border-radius:16px;padding:32px 28px">
    <div style="width:52px;height:52px;border-radius:12px;background:#EEF9F9;display:flex;align-items:center;justify-content:center;margin-bottom:20px">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2">{icon}</svg>
    </div>
    <h3 style="{FONT}font-size:16px;font-weight:800;color:#1A1A1A;margin-bottom:10px">{title}</h3>
    <p style="{FONT}font-size:13px;color:#555;line-height:1.75">{desc}</p>
  </div>''' for icon,title,desc in [
    ('<circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>','先勘察後施工','利用紅外線熱像儀、微波掃描等儀器精確定位滲漏源頭，確保對症下藥，避免「做完又翻漏」。'),
    ('<path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/>','透明報價無隱費','報價書列明工程範圍、施工工序、所用材料及費用，工程開始後不會突然追加收費。'),
    ('<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>','年期保養保障','工程完成後提供年期保養，期間如有問題可聯絡我們跟進，確保防水效果持久穩定。'),
  ])}
</div>''')
    ])], bg="#fff"),

    cta_section(),
]

# ─── PAGE: BLOG ───────────────────────────────────────────────────────────────

def blog_card(img_file, date, tag, title, excerpt):
    return f'''<a href="{WA}" target="_blank" style="display:block;border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.07);background:#fff;text-decoration:none;transition:box-shadow .2s">
  <img src="{IMG}/{img_file}" style="width:100%;height:200px;object-fit:cover;display:block">
  <div style="padding:20px">
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
      <span style="{FONT}font-size:11px;font-weight:700;color:{TEAL};background:#EEF9F9;padding:3px 10px;border-radius:50px">{tag}</span>
      <span style="{FONT}font-size:11px;color:#aaa">{date}</span>
    </div>
    <h3 style="{FONT}font-size:15px;font-weight:800;color:#1A1A1A;line-height:1.5;margin-bottom:8px">{title}</h3>
    <p style="{FONT}font-size:13px;color:#666;line-height:1.7">{excerpt}</p>
  </div>
</a>'''

BLOG_DATA = [
    ("prob-rooftop.jpg","2026-03","天台防水","為甚麼天台防水每隔幾年就要重做？","防水層有使用年限，加上香港氣候炎熱多雨，天台防水層的老化速度比其他地區更快。本文解釋何時需要翻新及如何選擇合適的防水系統。"),
    ("prob-bathroom.jpg","2026-02","浴室滲漏","浴室漏水的 5 個警示訊號","如何在問題惡化前及早發現浴室滲漏？本文列出 5 個常見警示訊號，幫助業主及早行動，避免引起結構損壞。"),
    ("prob-window.jpg","2026-01","窗框防水","香港舊樓窗框滲水怎麼辦？","窗框老化是香港舊樓最常見的滲漏問題之一。本文介紹窗框滲水的成因、DIY 應急方法及專業修繕方案的分別。"),
    ("prob-concrete.jpg","2025-12","外牆修葺","石屎剝落需要緊急處理嗎？","石屎剝落除了影響外觀，更可能引起結構安全問題。本文說明石屎剝落的成因分類及不同情況的處理優先順序。"),
    ("tech-polyurea.jpg","2025-11","防水技術","Polyurea 聚脲 vs 傳統防水塗料：哪個更好？","聚脲是近年愈來愈受歡迎的防水材料。本文比較聚脲與傳統改性瀝青、PU 防水塗料的優缺點，幫助你了解適用場景。"),
    ("tech-insulation.jpg","2025-10","隔熱防水","天台隔熱防水一體化系統：節能與防水兩者兼得","香港夏天天台表面溫度可超過 60°C，本文介紹如何透過隔熱防水系統同時解決滲漏和室內過熱的問題。"),
]

blog_sections = [
    page_hero_section("防水網誌", "防水知識、案例分析及保養貼士，助您了解滲漏問題的根源與解決方案"),

    section([col(100, [
        html_widget(f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px">{"".join(blog_card(*d) for d in BLOG_DATA[:3])}</div>')
    ])], pad_tb=60),
    section([col(100, [
        html_widget(f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:28px">{"".join(blog_card(*d) for d in BLOG_DATA[3:])}</div>')
    ])], pad_tb=0, pad_lr=60),

    cta_section(),
]

# ─── PAGE: CONTACT ────────────────────────────────────────────────────────────

contact_sections = [
    page_hero_section("聯絡我們", "歡迎 WhatsApp、電話或電郵查詢，我們會盡快回覆"),

    section([
        col(55, [
            html_widget(f'<p style="{FONT}font-size:12px;font-weight:700;color:{TEAL};letter-spacing:2.5px;text-transform:uppercase;margin-bottom:12px">立即聯絡</p>'),
            heading_widget("告訴我們您的問題", "h2", "#1A1A1A", 30, 900, "left", 16),
            text_widget(f'<p style="{FONT}font-size:14px;color:#555;line-height:1.85;margin-bottom:28px">請提供滲漏位置相片及簡單描述，我們的工程師會盡快評估並回覆建議方案。初步評估完全免費。</p>'),
            html_widget(f'''<div style="display:flex;flex-direction:column;gap:16px">
  <a href="{WA}" target="_blank" style="display:flex;align-items:center;gap:16px;background:{TEAL};color:#fff;border-radius:14px;padding:20px 24px;text-decoration:none">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    <div>
      <p style="{FONT}font-size:11px;font-weight:600;opacity:.85;margin:0">最快速查詢方式</p>
      <p style="{FONT}font-size:18px;font-weight:900;margin:2px 0 0">(852) 5222 5111</p>
    </div>
  </a>
  <a href="tel:+85268800698" style="display:flex;align-items:center;gap:16px;background:#F0FAFA;border-radius:14px;padding:20px 24px;text-decoration:none">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.07 1.18 2 2 0 012.03 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.09 7.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 14.92v2z"/></svg>
    <div>
      <p style="{FONT}font-size:11px;font-weight:600;color:#888;margin:0">備用電話</p>
      <p style="{FONT}font-size:18px;font-weight:900;color:#1A1A1A;margin:2px 0 0">(852) 6880 0698</p>
    </div>
  </a>
  <a href="mailto:galaxywindowhk@gmail.com" style="display:flex;align-items:center;gap:16px;background:#F0FAFA;border-radius:14px;padding:20px 24px;text-decoration:none">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
    <div>
      <p style="{FONT}font-size:11px;font-weight:600;color:#888;margin:0">電郵查詢</p>
      <p style="{FONT}font-size:18px;font-weight:900;color:#1A1A1A;margin:2px 0 0">galaxywindowhk@gmail.com</p>
    </div>
  </a>
</div>''')
        ]),
        col(45, [
            html_widget(f'''<div style="background:#F5F5F3;border-radius:20px;padding:36px 32px;height:100%;box-sizing:border-box">
  <h3 style="{FONT}font-size:20px;font-weight:900;color:#1A1A1A;margin-bottom:24px">辦公室地址</h3>
  <div style="background:#fff;border-radius:12px;overflow:hidden;margin-bottom:20px">
    <div style="height:220px;background:linear-gradient(135deg,#EDF7F7 0%,#C8ECEC 100%);display:flex;align-items:center;justify-content:center">
      <div style="text-align:center">
        <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
        <p style="{FONT}font-size:13px;color:{TEAL};font-weight:700;margin-top:8px">大角咀辦公室</p>
      </div>
    </div>
    <div style="padding:16px 20px">
      <p style="{FONT}font-size:13px;color:#555;line-height:1.8">九龍大角咀通州街 123 號<br>國貿中心 2 樓 C 室</p>
    </div>
  </div>
  <div style="display:flex;flex-direction:column;gap:10px">
    <p style="{FONT}font-size:13px;color:#555;display:flex;gap:8px;align-items:flex-start">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="{TEAL}" stroke-width="2" style="flex-shrink:0;margin-top:2px"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
      <span><strong style="color:#1A1A1A">辦公時間：</strong>星期一至五 9:00–18:00<br>星期六 9:00–13:00 / 星期日及公眾假期休息</span>
    </p>
  </div>
</div>''')
        ])
    ], bg="#fff"),

    cta_section(),
]

# ─── WRITE FILES ─────────────────────────────────────────────────────────────

pages = {
    "homepage":  (home_data, "銀河防水 – 首頁"),
    "services":  (make_template("銀河防水 – 服務範圍", services_sections), "銀河防水 – 服務範圍"),
    "cases":     (make_template("銀河防水 – 成功個案", cases_sections), "銀河防水 – 成功個案"),
    "about":     (make_template("銀河防水 – 品牌故事", about_sections), "銀河防水 – 品牌故事"),
    "blog":      (make_template("銀河防水 – 防水網誌", blog_sections), "銀河防水 – 防水網誌"),
    "contact":   (make_template("銀河防水 – 聯絡我們", contact_sections), "銀河防水 – 聯絡我們"),
}

kit_tpl_dir = os.path.join(BASE, "elementor-kit", "templates")
os.makedirs(kit_tpl_dir, exist_ok=True)

for fname, (data, title) in pages.items():
    data["title"] = title
    out = os.path.join(kit_tpl_dir, f"{fname}.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    kb = os.path.getsize(out) // 1024
    print(f"  OK {fname}.json  ({kb} KB)")

# update manifest
manifest = {
    "name": "Galaxy Waterproof",
    "title": "Galaxy Waterproof",
    "version": "2",
    "author": "Galaxy Waterproof",
    "description": "銀河防水 Complete Site – Header, Footer + 6 Pages",
    "thumbnail": "",
    "created": "2026-05-17T00:00:00",
    "elementor_version": "3.1.0",
    "plugins": [],
    "templates": [
        {"name": k, "title": v[1], "type": "page", "thumbnail": "",
         "url": f"templates/{k}.json", "export_date": "2026-05-17T00:00:00",
         "source": "local", "language": ""}
        for k, v in pages.items()
    ],
    "content": {},
    "site-settings": {"settings": {}, "kit_settings": {}}
}

with open(os.path.join(BASE, "elementor-kit", "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
print("  OK manifest.json updated")

# rebuild zip
import zipfile
zip_path = os.path.join(BASE, "galaxy-waterproof-elementor-kit.zip")
if os.path.exists(zip_path):
    os.remove(zip_path)
kit_dir = os.path.join(BASE, "elementor-kit")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(kit_dir):
        for file in files:
            abs_path = os.path.join(root, file)
            arc_name = os.path.relpath(abs_path, kit_dir)
            zf.write(abs_path, arc_name)
zip_kb = os.path.getsize(zip_path) // 1024
print(f"  OK galaxy-waterproof-elementor-kit.zip  ({zip_kb} KB)")

# ─── WORDPRESS XML (WXR) EXPORT ───────────────────────────────────────────────
# Single importable file: Tools → Import → WordPress
# Creates all pages with Elementor content pre-loaded.

PAGE_ORDER = [
    ("homepage", "首頁",    "home",     ""),
    ("services", "服務範圍", "services", ""),
    ("cases",    "成功個案", "cases",    ""),
    ("about",    "品牌故事", "about",    ""),
    ("blog",     "防水網誌", "blog",     ""),
    ("contact",  "聯絡我們", "contact",  ""),
]

def cdata(s):
    # Escape ]]> inside CDATA so it never breaks the XML
    return s.replace("]]>", "]]]]><![CDATA[>")

wxr_items = []
for post_id, (fname, title, slug, _) in enumerate(PAGE_ORDER, start=10):
    tpl_path = os.path.join(kit_tpl_dir, f"{fname}.json")
    with open(tpl_path, encoding="utf-8") as f:
        tpl = json.load(f)
    el_data = json.dumps(tpl["content"], ensure_ascii=False)

    wxr_items.append(f"""
  <item>
    <title>{title}</title>
    <link>https://example.com/{slug}/</link>
    <pubDate>Sat, 17 May 2026 00:00:00 +0000</pubDate>
    <dc:creator>admin</dc:creator>
    <content:encoded><![CDATA[]]></content:encoded>
    <excerpt:encoded><![CDATA[]]></excerpt:encoded>
    <wp:post_id>{post_id}</wp:post_id>
    <wp:post_date>2026-05-17 00:00:00</wp:post_date>
    <wp:post_date_gmt>2026-05-17 00:00:00</wp:post_date_gmt>
    <wp:comment_status>closed</wp:comment_status>
    <wp:ping_status>closed</wp:ping_status>
    <wp:post_name>{slug}</wp:post_name>
    <wp:status>publish</wp:status>
    <wp:post_parent>0</wp:post_parent>
    <wp:menu_order>{post_id}</wp:menu_order>
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
      <wp:meta_value><![CDATA[{cdata(el_data)}]]></wp:meta_value>
    </wp:postmeta>
  </item>""")

wxr_xml = """<?xml version="1.0" encoding="UTF-8" ?>
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
  <generator>Galaxy Waterproof Demo Content</generator>
""" + "".join(wxr_items) + """
</channel>
</rss>"""

wxr_path = os.path.join(BASE, "galaxy-waterproof-demo.xml")
with open(wxr_path, "w", encoding="utf-8") as f:
    f.write(wxr_xml)
kb = os.path.getsize(wxr_path) // 1024
print(f"  OK galaxy-waterproof-demo.xml  ({kb} KB)")
print("\nDone.")
print("  Import galaxy-waterproof-demo.xml via:")
print("  WP Admin -> Tools -> Import -> WordPress -> Upload File")
