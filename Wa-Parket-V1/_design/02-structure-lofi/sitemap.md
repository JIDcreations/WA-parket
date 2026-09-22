# W&A Parket: structuur en IA (redesign V1)

Vertrekpunt is de audit van 22/09/2026. Dit document beschrijft de sitemap, de navigatie en de opbouw van elk template. De lo-fi versie staat in `wireframes.html`.

## Aannames (af te toetsen met de klant)

| Vraag uit audit | Werkhypothese V1 |
|---|---|
| Primaire actie? | **Afspraak in de toonzaal**. Het verkoopgesprek gebeurt in Lochristi ("Onze adviseurs hopen uw voorkeur te ontdekken in onze toonzaal"). Offerte is secundair, telefoon staat in de mobiele actiebalk. |
| Propositiezin hero? | Placeholder: *"Parket, gekozen in onze toonzaal en gelegd door onze eigen vakmensen."* Baseline "Je staat erop" blijft in het logo staan. |
| Aantal producten? | Structuur werkt voor 50 tot 1.000 producten dankzij paginering (24 per pagina) en filters. Welke producten blijven, beslist de klant. |

## De grootste IA-beslissing: Collectie ≠ Diensten

De tweede navigatiebalk mengde **producten** (Massief, Fineer, Samengesteld, Laminaat) met **diensten** (Schuren, Renovatie, Trappen & Maatwerk, Onderhoud, Randafwerking). Het waren allemaal `product_type`-categorieën. We trekken die twee uit elkaar:

- **Collectie**: wat u koopt (filterbare catalogus)
- **Diensten**: wat W&A voor u doet (plaatsing is hier de kern-usp)

"Alles over parket" (6 pagina's) en "Alles over hout" (9 pagina's) worden samen **Advies**, met twee duidelijke clusters.

## Sitemap

```
Home
├── Collectie                      /collectie/                (catalogus + filters)
│   ├── Massief parket             /collectie/massief/
│   ├── Samengesteld / meerlagen   /collectie/meerlagen/
│   ├── Fineerparket               /collectie/fineer/
│   ├── Laminaat & LVT             /collectie/laminaat-lvt/
│   ├── Vormen → filter            ?vorm=visgraat | hongaarse-punt | plank | xxl
│   ├── Merken                     /merken/admonter/  /merken/di-legno/  /merken/twinfloor/
│   └── Product (detail)           /collectie/{slug}/
├── Diensten                       /diensten/
│   ├── Plaatsing (eigen ploeg)    /diensten/plaatsing/
│   ├── Schuren & renovatie        /diensten/renovatie/
│   ├── Trappen & maatwerk         /diensten/trappen-maatwerk/
│   ├── Afwerking & onderhoud      /diensten/onderhoud/        (+ onderhoudsproducten)
│   ├── Randafwerking              /diensten/randafwerking/
│   └── Parketschade herstellen    /diensten/parketschade/
├── Realisaties                    /realisaties/              (was: Inspiratie, 811 foto's op één pagina)
│   └── Project (detail)           /realisaties/{project}/     foto's + gebruikte producten
├── Promoties                      /promoties/
│   └── Promotie (detail)          /promoties/{slug}/
├── Advies                         /advies/
│   ├── Uw vloer kiezen            ondergrond · binnenklimaat · vormen · plaatsingsmethodes · vloerverwarming · afwerking
│   ├── Houtkennis                 juiste hout kiezen · houtsoorten · technische kenmerken (7 artikels → 1 vergelijkingspagina + detail)
│   ├── Veelgestelde vragen        /advies/faq/
│   └── Nieuws & blog              /nieuws/                    (sluitingsdagen, events, weetjes)
├── Over ons                       /over-ons/                 (familie, 2 generaties, Chevrolet-truck, missie)
├── Toonzaal & contact             /toonzaal/                 adres, uren, route, kaart
└── Afspraak / offerte             /afspraak/                 1 formulier, 2 intenties (toonzaalbezoek · offerte)
    Footer-only: Privacy · Cookies · Disclaimer
```

## Navigatie (audit §1, §7)

**Desktop**: één sticky balk van 76px. Bij scrollen krimpt die tot 64px met een schaduw.

```
[Logo]   Collectie ▾   Diensten ▾   Realisaties   Over ons              ☎ 09 225 05 77   [ Afspraak maken ]
```

- 4 items, waar het vroeger 9 plus 10 waren. "Home" gaat eruit, want het logo linkt naar home.
- *Update hifi (22/09/2026):* Promoties zit nu in het Collectie-menu en Advies in het Diensten-menu. Beide blijven op de homepage en in de footer. De wireframes hieronder tonen nog de eerste versie met 6 items.
- **Megamenu Collectie**: 4 kolommen. *Type* (4) · *Vorm* (4) · *Merk* (3) · uitgelichte promotiekaart.
- **Megamenu Diensten**: 6 diensten met een regel uitleg, een kolom Advies (vloerverwarming, houtkeuze, ondergrond, FAQ) en een kaart "Zo werken we".
- De actieve pagina krijgt een onderlijn van 2px in rood, en hover dezelfde onderlijn op 40%. Dat is meer dan een kleurverschuiving.
- Contrast: warm zwart op linnen = 13,4:1.
- Een broodkruimel staat alleen op diepere pagina's (niveau 2 en lager), nooit op home.

**Mobiel**: een balk van 64px met logo en hamburger. Het menu opent als fullscreen drawer met accordeon-niveaus, items van 20px in Montserrat 500 in warm zwart en tap targets van 48px.
**Vaste actiebalk onderaan**: `[☎ Bellen] [Afspraak maken]`. Het reCAPTCHA-badge wordt verborgen, met de verplichte tekstvermelding in het formulier.

## Templates

### T1 · Home (doel: ~5.500px, was 10.406)

| # | Sectie | Achtergrond | Doel / audit |
|---|---|---|---|
| 1 | **Hero**: één beeld, H1-propositie, lead, primaire knop "Afspraak in de toonzaal" en secundaire knop "Bekijk collectie" | beeld + linnen | §2: wat doet W&A, voor wie |
| 2 | **Vertrouwensbalk**: eigen plaatsers · 45+ jaar familiebedrijf · toonzaal Lochristi · 50 houtsoorten / 350 kleuren | linnen, lijn boven/onder | §2 |
| 3 | **Collectie-ingang**: 4 grote tegels (Massief · Meerlagen · Visgraat & patronen · Laminaat & LVT) | linnen | §4: kaarten met groot beeld |
| 4 | **Promoties**: max. 3 compacte kaarten (label, product, −%, einddatum, 1 regel) en een tekstlink rechts "Alle promoties →" | crème | §3 |
| 5 | **Zo werken we**: 4 stappen (toonzaal → opmeting → plaatsing door eigen ploeg → nazorg) | linnen | nieuw, maakt de usp concreet |
| 6 | **Realisaties**: 1 uitgelicht project groot en 2 kleiner, elk met plaats en product | warm zwart | §4, §5: per project |
| 7 | **Waarom W&A**: kernzin en 4 usp's met icoon (kwaliteit · gezonde producten · perfecte afwerking · levenslange opvolging), plus de Chevrolet-anekdote | crème | §5: missie van 859 woorden → ±80 |
| 8 | **Advies**: 3 artikels met datum en een FAQ-accordeon van 5 vragen | linnen | §4: blog met datum |
| 9 | **Toonzaal-CTA**: foto, adres, uren, knop "Afspraak maken" en "Route" | beeld + warm zwart | primaire actie herhaald |
| 10 | Footer | warm zwart | |

Ritme: 3 niveaus van witruimte (sectie 128px, blok 48px, item 24px). Er volgen nooit twee secties met dezelfde achtergrond én dezelfde kaartopbouw op elkaar.

### T2 · Collectie-overzicht (audit §6)

- Paginatitel en een intro van 1 regel, met daaronder snelkeuze-chips per type
- **Desktop**: filterkolom links (sticky, 280px), rechts de resultaten
- **Mobiel**: knop "Filters (3)" die een bottom sheet opent. Het eerste product staat boven de vouw (was 3.370px).
- Filtergroepen: Type · Vorm · Merk · Houtsoort · Kleur/afwerking · Toepassing (vloerverwarming, badkamer, keuken…) · Breedte
- Checkbox-patroon: leeg vierkant = uit, gevuld rood vierkant met vinkje = aan. Echte `<input type=checkbox>` of `aria-pressed`. Labels breken af op meerdere regels, zonder fade.
- **Actieve filters** als chips boven de resultaten, elk met ✕, plus "Wis alle filters" als tekstlink
- **Resultatenteller** ("124 parketvloeren") met sortering
- Productkaart: foto · merk (eyebrow) · **echte productnaam** · 3 kenmerken (houtsoort · breedte · afwerking) · eventueel een promo-badge
- Paginering: 24 per pagina, "Toon meer" en genummerde pagina's

### T3 · Productdetail

- Broodkruimel: Collectie › Massief › Di Legno Visgraat Regorio
- Links een galerij (1 groot beeld en duimnagels, inclusief realisatiefoto's). Rechts een **sticky paneel**: merk, naam, kernkenmerken (vorm · houtsoort · afwerking · breedtes), primaire knop "Offerte aanvragen", secundaire knop "Bekijk in de toonzaal" en een telefoonregel.
- Daaronder:
  1. Korte beschrijving (max. 3 alinea's) en merk-blok
  2. **Specificatietabel**: afmetingen · kwaliteit · afwerking · toplaag · opbouw · plaatsing
  3. **Geschikt voor** als iconen: vloerverwarming · keuken · badkamer · gelijmd · op bestaande tegels
  4. Realisaties met dit product
  5. Gerelateerde producten (4)
- Mobiel: een vaste balk "Offerte aanvragen" vervangt de algemene actiebalk

### T4 · Dienst
Hero met beeld en titel, dan "wat we doen" (3 blokken), werkwijze in stappen, voor/na of realisaties, FAQ over de dienst en een CTA.

### T5 · Realisaties
Een raster van projectkaarten (cover, titel, plaats, product). Filter op type ruimte (woning · horeca · trap · badkamer). Een detailpagina toont 8 à 15 foto's, projectbeschrijving, de gebruikte producten als kaarten en een CTA.

### T6 · Advies-artikel
Leeskolom van 66 tekens, inhoudsopgave rechts (sticky), tussentitels in Garamond, afbeeldingen in de tekst en onderaan gerelateerde artikels plus een CTA.

### T7 · Toonzaal & contact / Afspraak
Adres, uren, kaart en foto's van de toonzaal. Eén formulier met keuze *Toonzaalbezoek* / *Offerte* / *Andere vraag*, met datumvoorkeur, telefoon en bericht.

## Van audit naar structuur

| Audit | Opgelost in |
|---|---|
| §1 Dubbele nav, niet sticky, contrast | Eén sticky nav met megamenu, primaire knop, actieve staat |
| §2 Geen hero, 29 slides | T1 #1–2: één beeld en één boodschap, vertrouwensbalk |
| §3 Promokaarten, knoppen | T1 #4, knopsysteem (brand-board §04) |
| §4 Alles even belangrijk | Afwisselende achtergronden, 3 niveaus van witruimte, kaartopbouw per sectie |
| §5 Missie als Word-doc, 811 foto's | T1 #7 (usp's), T5 per project |
| §6 Filters, 980 producten op één pagina | T2: chips, teller, paginering, echte kaartnamen. T3: vaste opbouw met sticky CTA |
| §7 Mobiel | Hamburger met drawer, filter-bottom-sheet, vaste actiebalk, reCAPTCHA verborgen |
