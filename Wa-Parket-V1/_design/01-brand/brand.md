# W&A Parket: brandfundament (redesign V1)

Opgehaald uit wa-parket.be op 22/09/2026. De tokens staan in `/assets/css/tokens.css` (één bron voor site en brand board) en de visuele versie in `brand-board.html`.

## Kern

| | |
|---|---|
| **Naam** | W&A Parket |
| **Baseline** | *Je staat erop* |
| **Wat** | Parketspecialist met eigen plaatsingsdienst en toonzaal |
| **Waar** | Antwerpse Steenweg 148, 9080 Lochristi (bij Gent) |
| **Sinds** | Familiebedrijf, 2 generaties. Meer dan 45 jaar sinds de start. |
| **Aanbod** | 50+ houtsoorten, 350 kleuren, 8.000 artikelen |
| **Merken** | Admonter, Di Legno, Twinfloor (dealerschap) |
| **Contact** | 09 225 05 77 · info@wa-parket.be |
| **Open** | di–vr 13–18u · za 10–18u · zo–ma gesloten |
| **Mascotte** | Gerestaureerde Chevrolet-parkettruck |

> ⚠️ Tegenstrijdig op de huidige site: "meer dan 35 jaar expertise" en "méér dan 45 jaar geleden gestart". Dit moet de klant bevestigen voor het in de vertrouwensbalk komt.

## Logo

- `logo/wa-parket-logo.png`: volledig logo (beeldmerk, woordmerk en baseline), bijgesneden, transparant
- `logo/wa-parket-logo-light.png`: variant voor donkere achtergrond (zwart → crème, rood lichter)
- `logo/wa-parket-mark.png`: enkel het beeldmerk "WA" in strepen
- Er is geen vectorbestand. Dat staat bij de open vragen. PNG volstaat voor V1, niet voor productie.

**Beeldmerk als grafisch element.** De vier parallelle diagonale strepen lezen als parketplanken. Die hoek komt maar op één plek terug: het hero-beeld wordt in vier diagonale planken gelegd. Geen streepjes-labels boven secties. Het watermerk op foto's gebruiken we niet.

## Kleur

Gesampled uit het logo. De oude CSS gebruikte `#A02816` en `#A12916`, twee net verschillende roden.

| Token | Hex | Rol | Contrast |
|---|---|---|---|
| Rood | `#9A3324` | Primaire knop, accent, actieve nav | 7,3:1 op wit · 6,1:1 op crème |
| Rood donker | `#7A2519` | Hover/pressed | 10:1 op wit |
| Warm zwart | `#2D2926` | Tekst, donkere secties, footer | 14,4:1 op wit |
| Crème | `#F4EAD5` | Afwisselende sectie-achtergrond (bestaande merkkleur) | — |
| Off-white | `#FAF8F7` | Pagina-achtergrond (neutraal, geen tweede crème) | — |
| Steen | `#6B625A` | Secundaire tekst, meta | 5,0:1 op crème ✓ AA |
| Lijn | `#E4D9C4` | Randen | — |
| Eik | `#C49A6C` | Decoratief, **nooit tekst** | 2,2:1 ✗ |

Oude hoofdnavigatie: rgba(0,0,0,.5) op crème = **3,3–3,8:1 ✗**. Nieuwe navigatie: warm zwart op off-white = **13,4:1 ✓**.

**Verhouding.** Ongeveer 70% off-white/wit, 20% crème en warm zwart, 10% rood. Rood is voor actie, niet voor decoratie.

## Typografie

| Rol | Font | Gebruik |
|---|---|---|
| Display | **EB Garamond** 400/500 | H1–H2, hero, citaten. Sluit aan bij de Garamond-serif van het logo. |
| Tekst/UI | **Montserrat** 400/500/600 | Body, nav, knoppen, labels. Blijft voor continuïteit, maar **nooit meer weight 300**. |

Schaal van hero naar kaarttitel: 80 → 56 → 42 → 24. De body gaat van 14 naar **17px**, met regelhoogte 1,65 en een maximale regellengte van 66 tekens.

Het nieuwe systeem vervangt de oude situatie, waarin 11 H2's allemaal op 26px/300 stonden. H2 is voortaan altijd Garamond. **Geen eyebrows of labels boven sectietitels:** de titel alleen volstaat.

## Knoppen (vaste hiërarchie)

1. **Primair**: gevuld rood, witte tekst Montserrat 600, 48px hoog, radius 2px. Eén per scherm. "Afspraak maken" / "Offerte aanvragen". Eén label per actie, overal hetzelfde.
2. **Secundair**: omlijnd warm zwart, 1,5px rand. "Bekijk collectie".
3. **Tekstlink**: Montserrat 600, onderlijn 1px, zonder pijl. "Alle promoties".

Focus is een zichtbare ring van 2px rood met 2px offset. Hover verandert kleur én vorm: de primaire knop wordt donkerder, de secundaire vult zich.

## Fotografie

- Sterk materiaal: warm daglicht, echte interieurs, detailshots van houtnerf. `/assets/img/` bevat 27 keuzes (web-geoptimaliseerd), het volledige archief staat in `photos-archive/`.
- **Watermerk**: bijna elke foto heeft een rood "W&A Parket"-watermerk rechtsonder. Voor productie hebben we de originelen nodig (zie open vragen).
- De sliderbanners op de huidige site zijn maar 1110×500. Voor de hero hebben we minstens 2400px breed nodig.
- Richting: afwisselen tussen **wijd** (interieur, sfeer) en **dichtbij** (nerf, visgraat, Hongaarse punt). Het detail verkoopt het vakmanschap.
- Horeca-referentie: Relais des Oliviers (Di Legno). Dat project past op een realisatiepagina.

## Toon

- U-vorm. De huidige site wisselt u en je door elkaar, maar de baseline "Je staat erop" staat buiten die regel.
- Kort en zeker, niet uitleggerig. Eén boodschap per blok.
- Vakmanschap en familie, zonder superlatieven. Zeg liever "eigen plaatsers" dan "de allerbeste parketvloeren".
