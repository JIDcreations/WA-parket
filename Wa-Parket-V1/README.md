# W&A Parket: redesign V1

Klikbaar hifi-prototype voor de nieuwe wa-parket.be. Het is een statische site zonder build-stap, dus je kunt de map zo op Netlify of GitHub Pages zetten. `index.html` opent meteen de nieuwe homepage.

## Mappen

```
Wa-Parket-V1/
├── index.html            Home (hifi)
├── collectie.html        Collectie met werkende filters (?type= ?vorm= ?merk= in de URL)
├── product.html          Productpagina: Di Legno Visgraat Regorio
├── afspraak.html         Afspraak- en offerteformulier (prototype, verstuurt niets)
├── assets/
│   ├── css/tokens.css    Design tokens: één bron voor site en brand board
│   ├── css/main.css      Componenten en layout
│   ├── js/main.js        Megamenu, mobiel menu, filters, galerij, formulier
│   ├── img/              Web-geoptimaliseerde foto's (+ products/, regorio/)
│   └── logo/
└── _design/              Ontwerpproces, om aan de klant te tonen → /_design/
    ├── index.html        Overzicht van het proces
    ├── README.md         Werkwijze en open vragen voor de klant
    ├── 01-brand/         Brand board, brand.md, logo-bestanden, foto-archief
    ├── 02-structure-lofi/  Sitemap en lo-fi wireframes
    └── 03-hifi-build/    Bron van de HTML-pagina's (zie hieronder)
```

## Pagina's aanpassen

Header, footer en productkaarten zijn gedeeld. Pas daarom de bron aan in `_design/03-hifi-build/` (`pages/*.html`, `data.py`, `build.py`) en bouw opnieuw:

```sh
python3 _design/03-hifi-build/build.py
```

CSS en JS pas je rechtstreeks aan in `assets/`.

## Prototype, nog niet productie

- Promotiepercentages en einddata zijn **placeholders**. De echte cijfers moeten van de klant komen.
- De foto's hebben nog het W&A-watermerk en zijn maximaal 1.600px breed. Voor productie zijn de originelen nodig.
- Diensten, realisaties en advies linken nu naar secties op de homepage. De eigen pagina's volgen in een volgende fase.
- Alle productkaarten openen de voorbeeldpagina Visgraat Regorio.
