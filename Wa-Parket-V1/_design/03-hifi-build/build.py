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

# ── Header ──────────────────────────────────────────
def header(active):
    def cur(key):
        return ' is-active' if key == active else ''
    return f'''<a class="skip" href="#main">Naar de inhoud</a>
<header class="header" id="top">
  <div class="container header__bar">
    <a class="header__logo" href="index.html" aria-label="W&amp;A Parket, naar de startpagina"><img src="assets/logo/wa-parket-logo.png" alt="W&amp;A Parket, Je staat erop" width="1181" height="614"></a>
    <nav class="nav" aria-label="Hoofdmenu">
      <div class="nav__item"><button class="nav__link{cur('collectie')}" aria-expanded="false" aria-controls="mega-collectie">Collectie {icon('chev')}</button></div>
      <div class="nav__item"><button class="nav__link{cur('diensten')}" aria-expanded="false" aria-controls="mega-diensten">Diensten {icon('chev')}</button></div>
      <div class="nav__item"><a class="nav__link{cur('realisaties')}" href="index.html#realisaties">Realisaties</a></div>
      <div class="nav__item"><a class="nav__link{cur('promoties')}" href="index.html#promoties">Promoties</a></div>
      <div class="nav__item"><button class="nav__link{cur('advies')}" aria-expanded="false" aria-controls="mega-advies">Advies {icon('chev')}</button></div>
      <div class="nav__item"><a class="nav__link{cur('over')}" href="index.html#over-ons">Over ons</a></div>
    </nav>
    <div class="header__actions">
      <a class="header__phone" href="{PHONE_HREF}">{icon('phone')}<span>{PHONE}</span></a>
      <a class="btn btn--primary" href="afspraak.html">Afspraak maken</a>
    </div>
    <button class="burger" aria-label="Menu openen" aria-expanded="false" aria-controls="drawer"><span></span></button>
  </div>

  <div class="mega" id="mega-collectie">
    <div class="container mega__inner">
      <div><p class="mega__title">Type</p><ul class="mega__list">
        <li><a href="collectie.html?type=massief">Massief parket</a></li>
        <li><a href="collectie.html?type=meerlagen">Meerlagen parket</a></li>
        <li><a href="collectie.html?type=fineer">Fineerparket</a></li>
        <li><a href="collectie.html?type=laminaat">Laminaat &amp; LVT</a></li></ul></div>
      <div><p class="mega__title">Vorm</p><ul class="mega__list">
        <li><a href="collectie.html?vorm=plank">Planken</a></li>
        <li><a href="collectie.html?vorm=xxl">Brede planken (XXL)</a></li>
        <li><a href="collectie.html?vorm=visgraat">Visgraat</a></li>
        <li><a href="collectie.html?vorm=hongaarse-punt">Hongaarse punt</a></li></ul></div>
      <div><p class="mega__title">Merk</p><ul class="mega__list">
        <li><a href="collectie.html?merk=admonter">Admonter</a></li>
        <li><a href="collectie.html?merk=di-legno">Di Legno</a></li>
        <li><a href="collectie.html?merk=bolefloor">Bolefloor</a></li>
        <li><a href="collectie.html?merk=tarkett">Tarkett</a></li></ul>
        <p style="margin-top:var(--space-5)"><a class="link" href="collectie.html">Volledige collectie</a></p></div>
      <a class="mega__feature" href="collectie.html?merk=admonter">
        <img src="assets/img/products/admonter-salis-rustiek.jpg" alt="" loading="lazy">
        <div><span class="badge">−20%</span><span class="promo__brand">Admonter, promotie</span><h3 class="h3">Salis eik rustiek</h3><span class="small muted">Geldig tot 31 oktober</span></div>
      </a>
    </div>
  </div>

  <div class="mega" id="mega-diensten">
    <div class="container mega__inner mega__inner--services">
      <div><ul class="mega__list">
        <li><a href="index.html#werkwijze">Plaatsing<small>Door onze eigen vakmensen</small></a></li>
        <li><a href="index.html#werkwijze">Schuren en renovatie<small>Uw bestaande vloer als nieuw</small></a></li></ul></div>
      <div><ul class="mega__list">
        <li><a href="index.html#werkwijze">Trappen en maatwerk<small>Treden in hetzelfde hout</small></a></li>
        <li><a href="index.html#werkwijze">Afwerking en onderhoud<small>Olie, lak en onderhoudsproducten</small></a></li></ul></div>
      <div><ul class="mega__list">
        <li><a href="index.html#werkwijze">Randafwerking<small>Plinten, profielen, overgangen</small></a></li>
        <li><a href="index.html#advies">Parketschade herstellen<small>Van aangifte tot herstelling</small></a></li></ul></div>
      <a class="mega__feature" href="index.html#werkwijze">
        <img src="assets/img/stairs.jpg" alt="" loading="lazy">
        <div><h3 class="h3">Eén team, van staal tot laatste plint</h3><span class="small muted">Zo werken we</span></div>
      </a>
    </div>
  </div>

  <div class="mega" id="mega-advies">
    <div class="container mega__inner">
      <div><p class="mega__title">Uw vloer kiezen</p><ul class="mega__list">
        <li><a href="index.html#advies">Ondergrond</a></li>
        <li><a href="index.html#advies">Parket op vloerverwarming</a></li>
        <li><a href="index.html#advies">Plaatsingsmethodes</a></li>
        <li><a href="index.html#advies">Parketvormen</a></li></ul></div>
      <div><p class="mega__title">Houtkennis</p><ul class="mega__list">
        <li><a href="index.html#advies">Het juiste hout kiezen</a></li>
        <li><a href="index.html#advies">Houtsoorten vergeleken</a></li>
        <li><a href="index.html#advies">Binnenklimaat en werking</a></li>
        <li><a href="index.html#advies">Afwerking en onderhoud</a></li></ul></div>
      <div><p class="mega__title">Snel antwoord</p><ul class="mega__list">
        <li><a href="index.html#faq">Veelgestelde vragen</a></li>
        <li><a href="index.html#advies">Nieuws en blog</a></li></ul></div>
      <a class="mega__feature" href="index.html#advies">
        <img src="assets/img/living-fireplace-wide.jpg" alt="" loading="lazy">
        <div><span class="promo__brand">Gids</span><h3 class="h3">Parket op vloerverwarming</h3></div>
      </a>
    </div>
  </div>
</header>
<div class="mega-backdrop" aria-hidden="true"></div>

<div class="drawer" id="drawer" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="drawer__top">
    <img src="assets/logo/wa-parket-logo.png" alt="W&amp;A Parket" width="1181" height="614">
    <button class="drawer__close" aria-label="Menu sluiten">{icon('close')}</button>
  </div>
  <div class="drawer__body">
    <div class="drawer__group"><button aria-expanded="false" aria-controls="d-col">Collectie {icon('plus')}</button>
      <div class="drawer__sub" id="d-col"><a href="collectie.html?type=massief">Massief parket</a><a href="collectie.html?type=meerlagen">Meerlagen parket</a><a href="collectie.html?vorm=visgraat">Visgraat</a><a href="collectie.html?vorm=hongaarse-punt">Hongaarse punt</a><a href="collectie.html"><b>Volledige collectie</b></a></div></div>
    <div class="drawer__group"><button aria-expanded="false" aria-controls="d-dien">Diensten {icon('plus')}</button>
      <div class="drawer__sub" id="d-dien"><a href="index.html#werkwijze">Plaatsing</a><a href="index.html#werkwijze">Schuren en renovatie</a><a href="index.html#werkwijze">Trappen en maatwerk</a><a href="index.html#werkwijze">Afwerking en onderhoud</a></div></div>
    <div class="drawer__group"><a href="index.html#realisaties">Realisaties</a></div>
    <div class="drawer__group"><a href="index.html#promoties">Promoties</a></div>
    <div class="drawer__group"><button aria-expanded="false" aria-controls="d-adv">Advies {icon('plus')}</button>
      <div class="drawer__sub" id="d-adv"><a href="index.html#advies">Uw vloer kiezen</a><a href="index.html#advies">Houtkennis</a><a href="index.html#faq">Veelgestelde vragen</a></div></div>
    <div class="drawer__group"><a href="index.html#over-ons">Over ons</a></div>
    <p class="drawer__meta">Antwerpse Steenweg 148, 9080 Lochristi<br>dinsdag tot vrijdag 13 tot 18 uur, zaterdag 10 tot 18 uur</p>
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
