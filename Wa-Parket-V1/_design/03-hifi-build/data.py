# Productselectie voor het prototype: echte producten van wa-parket.be (22/09/2026).
# Kenmerken afgeleid uit de productnamen/-pagina's. Promo-percentages zijn PLACEHOLDERS.

PRODUCTS = [
    dict(slug="admonter-lapis-xxl", brand="Admonter", name="Lapis Naturelle XXL", type="meerlagen", vorm="xxl", hout="eik", kleur="gerookt",
         specs=["Eik", "280 mm", "Gerookt, geolied"], heat=True, promo=None),
    dict(slug="admonter-salis-rustiek", brand="Admonter", name="Salis eik rustiek", type="meerlagen", vorm="plank", hout="eik", kleur="naturel",
         specs=["Eik rustiek", "192 mm", "Geborsteld, geolied"], heat=True, promo="−20%"),
    dict(slug="dilegno-hongaarse-punt-ostia", brand="Di Legno", name="Hongaarse punt Ostia", type="meerlagen", vorm="hongaarse-punt", hout="franse-eik", kleur="gerookt",
         specs=["Franse eik", "120 mm", "Verouderd"], heat=True, promo=None),
    dict(slug="visgraat-franse-eik-1e-bis", brand="W&A selectie", name="Traditionele visgraat, 1e Bis", type="massief", vorm="visgraat", hout="franse-eik", kleur="licht",
         specs=["Franse eik 1e Bis", "Massief", "Traditioneel gelegd"], heat=True, promo=None),
    dict(slug="dilegno-visgraat-ostia-7", brand="Di Legno", name="Visgraat Ostia 7", type="massief", vorm="visgraat", hout="franse-eik", kleur="gerookt",
         specs=["Franse eik", "Massief", "Verouderd"], heat=True, promo="−15%"),
    dict(slug="admonter-noblesse-white", brand="Admonter", name="Noblesse white easy care", type="meerlagen", vorm="plank", hout="eik", kleur="licht",
         specs=["Eik 1e keus", "Wit", "Geborsteld"], heat=True, promo=None),
    dict(slug="dilegno-nibbia", brand="Di Legno", name="Nibbia eik rustiek exclusief", type="meerlagen", vorm="xxl", hout="eik", kleur="licht",
         specs=["Eik rustiek", "300 mm", "Maatwerk-kleur"], heat=True, promo=None),
    dict(slug="bolefloor-walnoot", brand="Bolefloor", name="Walnoot", type="meerlagen", vorm="plank", hout="walnoot", kleur="donker",
         specs=["Walnoot", "Natuurlijke rondingen", "Geolied"], heat=False, promo=None),
    dict(slug="bolefloor-eik-rustiek", brand="Bolefloor", name="Eik rustiek", type="meerlagen", vorm="plank", hout="eik", kleur="licht",
         specs=["Eik rustiek", "Natuurlijke rondingen", "Geolied"], heat=True, promo=None),
    dict(slug="tarkett-segno-old-brown", brand="Tarkett", name="Segno visgraat Old Brown", type="meerlagen", vorm="visgraat", hout="eik", kleur="donker",
         specs=["Eik", "Visgraat", "Samengesteld"], heat=True, promo=None),
    dict(slug="tarkett-grace-century", brand="Tarkett", name="Grace Oak Century", type="meerlagen", vorm="patroon", hout="eik", kleur="naturel",
         specs=["Eik", "Dambord", "Mat"], heat=True, promo=None),
    dict(slug="dilegno-hongaarse-punt-rimini", brand="Di Legno", name="Hongaarse punt Rimini", type="meerlagen", vorm="hongaarse-punt", hout="franse-eik", kleur="naturel",
         specs=["Franse eik", "Hongaarse punt", "Verouderd"], heat=True, promo=None),
]

FILTERS = [
    ("type", "Type", [("massief", "Massief parket"), ("meerlagen", "Meerlagen parket"), ("fineer", "Fineerparket"), ("laminaat", "Laminaat & LVT")]),
    ("vorm", "Vorm", [("plank", "Planken"), ("xxl", "Brede planken (XXL)"), ("visgraat", "Visgraat"), ("hongaarse-punt", "Hongaarse punt"), ("patroon", "Patroon en dambord")]),
    ("merk", "Merk", [("admonter", "Admonter"), ("di-legno", "Di Legno"), ("bolefloor", "Bolefloor"), ("tarkett", "Tarkett"), ("w-a-selectie", "W&A selectie")]),
    ("hout", "Houtsoort", [("eik", "Eik"), ("franse-eik", "Franse eik, verouderd en gerecupereerd"), ("walnoot", "Walnoot")]),
    ("kleur", "Kleur", [("licht", "Licht en wit"), ("naturel", "Naturel"), ("gerookt", "Gerookt"), ("donker", "Donker")]),
    ("toepassing", "Toepassing", [("vloerverwarming", "Geschikt voor vloerverwarming")]),
]
