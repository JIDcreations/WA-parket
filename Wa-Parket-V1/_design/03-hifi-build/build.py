#!/usr/bin/env python3
"""Bouwt de statische hifi-pagina's in de root van Wa-Parket-V1.

Gebruik:  python3 _design/03-hifi-build/build.py
Bron:     pages/*.html (inhoud) + deze file (head, header, footer) + data.py
Output:   ../../index.html, collectie.html, product.html, afspraak.html
Wijzig de output-HTML niet rechtstreeks, maar pas de bron aan en bouw opnieuw.
"""
import re
from pathlib import Path
from html import escape
from icons import icon
from data import PRODUCTS, FILTERS

HERE = Path(__file__).parent
ROOT = HERE.parent.parent

PHONE = "09 225 05 77"
PHONE_HREF = "tel:+3292250577"


# ── Menu-rijen: vierkante foto + titel + één regel uitleg ──
COLLECTIE_ROWS = [
    ("collectie.html?type=massief", "visgraat-warm.jpg", "Massief parket", "Traditioneel, vaak opnieuw te schuren"),
    ("collectie.html?type=meerlagen", "living-garden.jpg", "Meerlagen parket", "Stabiel, ideaal op vloerverwarming"),
    ("collectie.html?vorm=plank", "products/bolefloor-eik-rustiek.jpg", "Planken", "Van smal tot klassiek breed"),
    ("collectie.html?vorm=xxl", "products/admonter-lapis-xxl.jpg", "Brede planken", "Tot 30 cm, rust in grote ruimtes"),
    ("collectie.html?vorm=visgraat", "regorio/regorio-2.jpg", "Visgraat", "Klassiek patroon, moderne afwerking"),
    ("collectie.html?vorm=hongaarse-punt", "products/dilegno-hongaarse-punt-ostia.jpg", "Hongaarse punt", "Het visgraatpatroon, maar dan in punt"),
]
MERK_ROWS = [
    ("collectie.html?merk=admonter", "products/admonter-salis-rustiek.jpg", "Admonter", ""),
    ("collectie.html?merk=di-legno", "products/dilegno-visgraat-ostia-7.jpg", "Di Legno", ""),
    ("collectie.html?merk=bolefloor", "products/bolefloor-walnoot.jpg", "Bolefloor", ""),
    ("collectie.html?merk=tarkett", "products/tarkett-grace-century.jpg", "Tarkett", ""),
]
DIENST_ROWS = [
    ("index.html#werkwijze", "living-sofa.jpg", "Plaatsing", "Door onze eigen vakmensen"),
    ("index.html#werkwijze", "detail-texture-reclaimed.jpg", "Schuren en renovatie", "Uw bestaande vloer als nieuw"),
    ("index.html#werkwijze", "stairs.jpg", "Trappen en maatwerk", "Treden in hetzelfde hout"),
    ("index.html#werkwijze", "detail-plank-light.jpg", "Afwerking en onderhoud", "Olie, lak en onderhoudsproducten"),
    ("index.html#werkwijze", "kitchen.jpg", "Randafwerking", "Plinten, profielen, overgangen"),
    ("index.html#advies", "detail-knots.jpg", "Parketschade herstellen", "Van aangifte tot herstelling"),
]
ADVIES_ROWS = [
    ("index.html#advies", "living-fireplace-wide.jpg", "Parket op vloerverwarming", ""),
    ("index.html#advies", "detail-chevron.jpg", "Het juiste hout kiezen", ""),
    ("index.html#advies", "bathroom.jpg", "Ondergrond en vocht", ""),
    ("index.html#faq", "toonzaal-exterior.jpg", "Veelgestelde vragen", ""),
]

def rows(items):
    out = []
    for href, img, title, sub in items:
        sub_html = f'<small>{sub}</small>' if sub else ''
        out.append(f'                <li><a href="{href}"><img src="assets/img/{img}" alt="" loading="lazy" width="56" height="56"><span><b>{title}</b>{sub_html}</span></a></li>')
    return "\n".join(out)

# ── Header ──────────────────────────────────────────
def header(active):
    def cur(key):
        return ' is-active' if key == active else ''
    return f'''<a class="skip" href="#main">Naar de inhoud</a>
<header class="header" id="top">
  <div class="container header__bar">
    <a class="header__logo" href="index.html" aria-label="W&amp;A Parket, naar de startpagina"><img src="assets/logo/wa-parket-lockup.png" alt="W&amp;A Parket" width="1600" height="192"></a>

    <nav class="nav" aria-label="Hoofdmenu">
      <ul class="nav__list">
        <li class="nav__item">
          <button class="nav__link{cur('collectie')}" aria-expanded="false" aria-controls="mega-collectie">Collectie {icon('chev')}</button>
          <div class="mega" id="mega-collectie">
            <div class="mega__main">
              <p class="mega__title">Parketvloeren</p>
              <ul class="mega__rows">
{rows(COLLECTIE_ROWS)}
              </ul>
            </div>
            <div class="mega__side">
              <p class="mega__title">Merken</p>
              <ul class="mega__rows mega__rows--compact">
{rows(MERK_ROWS)}
              </ul>
              <div class="mega__foot">
                <a class="mega__promo" href="index.html#promoties"><span>Promoties</span><span class="badge">−20%</span></a>
                <a class="btn btn--secondary btn--sm btn--block" href="collectie.html">Alle 196 vloeren</a>
              </div>
            </div>
          </div>
        </li>
        <li class="nav__item">
          <button class="nav__link{cur('diensten')}" aria-expanded="false" aria-controls="mega-diensten">Diensten {icon('chev')}</button>
          <div class="mega" id="mega-diensten">
            <div class="mega__main">
              <p class="mega__title">Wat we voor u doen</p>
              <ul class="mega__rows">
{rows(DIENST_ROWS)}
              </ul>
            </div>
            <div class="mega__side">
              <p class="mega__title">Advies</p>
              <ul class="mega__rows mega__rows--compact">
{rows(ADVIES_ROWS)}
              </ul>
            </div>
          </div>
        </li>
        <li class="nav__item"><a class="nav__link{cur('realisaties')}" href="index.html#realisaties">Realisaties</a></li>
        <li class="nav__item"><a class="nav__link{cur('over')}" href="index.html#over-ons">Over ons</a></li>
      </ul>
    </nav>

    <div class="header__actions">
      <a class="header__phone" href="{PHONE_HREF}">{PHONE}</a>
      <a class="btn btn--primary btn--sm" href="afspraak.html">Afspraak maken</a>
    </div>
    <button class="burger" aria-label="Menu openen" aria-expanded="false" aria-controls="drawer"><span></span></button>
  </div>
</header>
<div class="mega-backdrop" aria-hidden="true"></div>

<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="drawer__top container">
    <img src="assets/logo/wa-parket-lockup.png" alt="W&amp;A Parket" width="1600" height="192">
    <button class="drawer__close" aria-label="Menu sluiten">{icon('close')}</button>
  </div>
  <nav class="drawer__body container" aria-label="Mobiel menu">
    <div class="drawer__group"><button aria-expanded="false" aria-controls="d-col">Collectie {icon('plus')}</button>
      <div class="drawer__sub drawer__sub--thumbs" id="d-col">{''.join(f'<a href="{h}"><img src="assets/img/{i}" alt="" loading="lazy">{t}</a>' for h, i, t, _ in COLLECTIE_ROWS)}<a href="index.html#promoties">Promoties</a><a href="collectie.html">Alle 196 vloeren</a></div></div>
    <div class="drawer__group"><button aria-expanded="false" aria-controls="d-dien">Diensten {icon('plus')}</button>
      <div class="drawer__sub drawer__sub--thumbs" id="d-dien">{''.join(f'<a href="{h}"><img src="assets/img/{i}" alt="" loading="lazy">{t}</a>' for h, i, t, _ in DIENST_ROWS)}<a href="index.html#faq">Advies en veelgestelde vragen</a></div></div>
    <div class="drawer__group"><a href="index.html#realisaties">Realisaties</a></div>
    <div class="drawer__group"><a href="index.html#over-ons">Over ons</a></div>
  </nav>
  <div class="drawer__foot container">
    <p>Antwerpse Steenweg 148, Lochristi<br>Di tot vr 13 tot 18 uur, za 10 tot 18 uur</p>
    <div class="drawer__ctas"><a class="btn btn--secondary" href="{PHONE_HREF}">{icon('phone')} Bellen</a><a class="btn btn--primary" href="afspraak.html">Afspraak maken</a></div>
  </div>
</div>
'''

FOOTER = f'''<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div class="footer__brand">
        <img src="assets/logo/wa-parket-logo-light.png" alt="W&amp;A Parket, Je staat erop" width="1181" height="614" loading="lazy">
        <p>Familiebedrijf in parket, met een eigen toonzaal en eigen plaatsers in Lochristi.</p>
      </div>
      <div><h2>Collectie</h2><ul><li><a href="collectie.html?type=massief">Massief parket</a></li><li><a href="collectie.html?type=meerlagen">Meerlagen parket</a></li><li><a href="collectie.html?type=fineer">Fineerparket</a></li><li><a href="collectie.html?type=laminaat">Laminaat &amp; LVT</a></li><li><a href="index.html#promoties">Promoties</a></li></ul></div>
      <div><h2>Diensten</h2><ul><li><a href="index.html#werkwijze">Plaatsing</a></li><li><a href="index.html#werkwijze">Renovatie</a></li><li><a href="index.html#werkwijze">Trappen en maatwerk</a></li><li><a href="index.html#werkwijze">Onderhoud</a></li></ul></div>
      <div><h2>W&amp;A Parket</h2><ul><li><a href="index.html#realisaties">Realisaties</a></li><li><a href="index.html#advies">Advies</a></li><li><a href="index.html#over-ons">Over ons</a></li><li><a href="afspraak.html">Afspraak maken</a></li></ul></div>
      <div><h2>Toonzaal</h2><ul><li>Antwerpse Steenweg 148<br>9080 Lochristi</li><li><a href="{PHONE_HREF}">{PHONE}</a></li><li><a href="mailto:info@wa-parket.be">info@wa-parket.be</a></li><li>Di tot vr: 13 tot 18 uur<br>Za: 10 tot 18 uur</li></ul></div>
    </div>
    <div class="footer__bottom">
      <span>© 2026 W&amp;A Parket</span>
      <nav aria-label="Juridisch"><a href="#">Privacy</a><a href="#">Cookies</a><a href="#">Disclaimer</a></nav>
    </div>
  </div>
</footer>

<div class="actionbar" aria-label="Snelle acties">
  <a class="btn btn--secondary" href="{PHONE_HREF}">{icon('phone')} Bellen</a>
  <a class="btn btn--primary" href="afspraak.html">Afspraak maken</a>
</div>
'''

def layout(title, desc, body, active="", page_class=""):
    return f'''<!doctype html>
<html lang="nl-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#FAF8F7">
<link rel="icon" href="assets/logo/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500&amp;family=Montserrat:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/main.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="{page_class}">
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''

# ── Collectie: kaarten + filters ────────────────────
def merk_key(b):
    return re.sub(r"[^a-z]+", "-", b.lower().replace("&", "-")).strip("-")

def card(p):
    badge = f'<span class="badge">{p["promo"]}</span>' if p["promo"] else ""
    specs = "".join(f"<li>{s}</li>" for s in p["specs"])
    toep = "vloerverwarming" if p["heat"] else ""
    # Prototype: enkel Regorio heeft een detailpagina, dus alle kaarten linken daarheen.
    return f'''<a class="card" href="product.html" data-type="{p["type"]}" data-vorm="{p["vorm"]}" data-merk="{merk_key(p["brand"])}" data-hout="{p["hout"]}" data-kleur="{p["kleur"]}" data-toepassing="{toep}" data-promo="{1 if p["promo"] else 0}">
  <div class="card__media"><img src="assets/img/products/{p["slug"]}.jpg" alt="{escape(p["brand"])} {escape(p["name"])}" loading="lazy" width="720" height="900">{badge}</div>
  <span class="card__brand">{escape(p["brand"])}</span>
  <h3>{escape(p["name"])}</h3>
  <ul class="card__specs">{specs}</ul>
</a>'''

def filters():
    out = []
    for key, label, opts in FILTERS:
        rows = "".join(
            f'<label class="check"><input type="checkbox" name="{key}" value="{v}"><span class="check__box">{icon("check")}</span><span>{escape(t)}</span><span class="check__count" data-count="{key}:{v}"></span></label>'
            for v, t in opts)
        out.append(f'''<fieldset class="fgroup" style="border:0;margin:0;padding-inline:0">
  <legend><button type="button" class="fgroup__toggle" aria-expanded="true" aria-controls="fg-{key}">{label} {icon("chev")}</button></legend>
  <div class="fgroup__opts" id="fg-{key}">{rows}</div>
</fieldset>''')
    return "\n".join(out)

# ── Build ───────────────────────────────────────────
def render(name, **ctx):
    src = (HERE / "pages" / f"{name}.html").read_text()
    src = re.sub(r"\{\{icon:([a-z]+)\}\}", lambda m: icon(m.group(1)), src)
    for k, v in ctx.items():
        src = src.replace("{{" + k + "}}", v)
    return src

PAGES = [
    ("index", "W&amp;A Parket: parket uit onze toonzaal, gelegd door onze eigen vakmensen",
     "Familiebedrijf met eigen toonzaal in Lochristi en eigen plaatsers. Massief en meerlagen parket, visgraat, Hongaarse punt, renovatie en trappen.", "", "page-home", {}),
    ("collectie", "Parketvloeren | W&amp;A Parket",
     "Bekijk en filter onze parketvloeren op type, vorm, merk, houtsoort en kleur. Alle vloeren zijn te zien in onze toonzaal in Lochristi.", "collectie", "page-plp",
     {"grid": "\n".join(card(p) for p in PRODUCTS), "filters": filters(), "total": str(len(PRODUCTS))}),
    ("product", "Di Legno Visgraat Regorio | W&amp;A Parket",
     "Verouderde Franse eik in visgraat, met een grijze oxidatieve afwerking. Massief, geschikt voor vloerverwarming.", "collectie", "page-pdp",
     {"related": "\n".join(card(p) for p in PRODUCTS if p["slug"] in ("dilegno-hongaarse-punt-ostia", "dilegno-visgraat-ostia-7", "dilegno-nibbia", "dilegno-hongaarse-punt-rimini"))}),
    ("afspraak", "Afspraak in de toonzaal | W&amp;A Parket",
     "Plan een bezoek aan onze toonzaal in Lochristi of vraag een offerte aan.", "", "page-booking", {}),
]

if __name__ == "__main__":
    for name, title, desc, active, cls, ctx in PAGES:
        html = layout(title, desc, render(name, **ctx), active, cls)
        (ROOT / f"{name}.html").write_text(html)
        print("✓", f"{name}.html")
