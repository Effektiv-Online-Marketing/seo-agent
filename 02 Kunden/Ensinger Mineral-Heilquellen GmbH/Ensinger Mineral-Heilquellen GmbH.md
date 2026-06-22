---
tags: [kunde, seo]
kunde: "Ensinger Mineral-Heilquellen GmbH"
stand-Datum: 2026-06-19
---

# Ensinger Mineral-Heilquellen GmbH

> [!info] Quellenlage
> Die im Google Drive verfügbaren SEO-Unterlagen stammen ausschließlich aus **Dezember 2021 / Januar–März 2022** (Erst-Audit-Phase). Es liegen **keine aktuellen Daten, kein laufendes Reporting und kein GEO/KI-Material** vor. Der Ordner `3.0_Reportings` ist leer. Alle Befunde unten sind daher als **historischer Stand 2021/2022** zu lesen und vor Wiederaufnahme einer Betreuung neu zu erheben.

## Überblick

- **Unternehmen:** Ensinger Mineral-Heilquellen GmbH — Mineralwasser- und Heilwasser-Abfüller mit Sitz im Raum Stuttgart (Schiller-Quelle / Ensinger Quelle).
- **Branche:** Getränke / Mineral- und Heilwasser (FMCG, regionaler Hersteller mit eigenem Online-Shop).
- **Domains (im Audit behandelt):**
  - `ensinger.de` — Corporate Website / Marken-Präsenz
  - `shop.ensinger.de` — Online-Shop (Shopware-typische URL-Struktur, Produkt- und Kategorieseiten)
- **Produktwelt (aus Shop-URLs belegt):** Mineral-Heilwasser, Direktsaftschorlen, Iso-Getränke (Ensinger Sport), Kennenlernpakete, Naturelle still/medium, Schiller-Quelle, Sport still/medium/classic.
- **Mandatsverhältnis:** EOM Agency hat für Ensinger 2021/2022 ein SEO-Erst-Audit erstellt. Eine fortlaufende Betreuung war in Verhandlung (siehe Mandat & Gewerke).

## Mandat & Gewerke

- **Stand 2022:** EOM hatte ein Angebot „Kontinuierliche SEO" unterbreitet. Kundenseitig (Johannes Fritz, Mail 16.12.2021) wurde eine **beratende Zusammenarbeit** favorisiert: EOM liefert Monitoring + Handlungsempfehlungen + inhaltlichen Ausbau/Qualitätssicherung, die **Umsetzung erfolgt inhouse bzw. mit der Website-Agentur** des Kunden.
- **Geplante Next Steps (Jan–März 2022, laut IST-Analyse):**
  - 26.01.2022: Übergabe & Besprechung SEO-Setup (technisch)
  - in 2–4 Wochen: Übergabe Analytics-Re-Setup
  - Feb/März: Umsetzung der Maßnahmen + Start ongoing SEO-Betreuung
  - tbd: Analyse SEA-Account inkl. Aufwandseinschätzung
- **Gewerke laut Audit-Scope:** Technik (Crawling/Indexierung), Content/Keywords, Off-Page/Links; perspektivisch SEA und Social (Ads) erwähnt.
- **Offen:** Ob die fortlaufende Betreuung tatsächlich gestartet ist, geht aus den Unterlagen **nicht hervor** (kein Reporting-Material vorhanden).

## SEO-Status & Befunde

Alle Befunde aus dem EOM-Erst-Audit. Quelle in Klammern, Erhebungsdatum wo angegeben.

### Technik (Befunde aus „shop.ensinger.de – SEO-IST-Analyse", 19.01.2022)

- **Befund:** Wichtige Inhalte (u. a. Produkte) werden auf der Startseite per **JavaScript** eingebunden und sind für Google im HTML nicht lesbar.
  **Begründung:** Relevante Inhalte im JS-Bereich werden vom Crawler nicht zuverlässig erfasst → Relevanzverlust.
  **Maßnahme:** Relevante Inhalte ins HTML verlagern; Thema bei fortlaufender Betreuung mit der Technik vertiefen.
- **Befund:** **Keine echte 404-Fehlerseite** — `shop.ensinger.de/xyz` zeigt Startseiten-Inhalte (Statuscode 404, aber Canonical auf die Startseite).
  **Begründung:** Widersprüchliches Signal an Google, irritierend für Nutzer:innen.
  **Maßnahme:** Eigene 404-Seite mit Hilfestellung; Canonical auf Startseite entfernen; entfernte Inhalte per 301 umleiten bzw. 410 bei endgültiger Löschung.
- **Befund:** **Keine Trailingslash-Weiterleitung.** URLs mit und ohne `/` am Ende werden gemischt verwendet, Varianten erzeugen teils 404 (z. B. `…/mineral-heilwasser` vs. `…/mineral-heilwasser/`, `…/das-team/`).
  **Maßnahme:** Auf eine Variante vereinheitlichen, per Wildcard weiterleiten. (http→https und www→non-www sind bereits vorhanden.)
- **Befund:** **57 URLs mit gemischten 302-Weiterleitungs-/Canonical-Ketten und Loops** (Parameter-URLs, v. a. Produktseiten). Beispiel: Iso-Orange-Produktseite leitet per 302 auf `?number=713`, die per Canonical zurückzeigt → Endlosschleife.
  **Maßnahme:** Entstehung der Parameter-URLs klären; Parameter-URLs per Canonical auf Original-URL; interne Verlinkung auf finale Ziele anpassen.
- **Befund:** **38 URLs mit 302-Weiterleitung** (Produktseiten mit Parameter-URLs) und 1 interne 301 (Breadcrumb auf `/cat/index/sCategory/4`).
  **Maßnahme:** Interne Links direkt auf finale Linkziele setzen, um Linkpower nicht zu verlieren.
- **Befund XML-Sitemap:** 19 temporär weitergeleitete (302) URLs in der Sitemap (v. a. Produktseiten), zusätzlich die noindex-Seite `/newsletter` enthalten.
  **Maßnahme:** Nur indexierbare 200er-URLs in die Sitemap; **automatisierte Sitemap** einführen.
- **Befund Indexierung:** AGB-Seite (`/agb`) ist indexiert, ebenso `/checkout/cart` und eine `widgets/index/refreshStatistic`-Parameter-URL.
  **Maßnahme:** AGB/Datenschutz/Impressum auf noindex; technische/Warenkorb-URLs aus dem Index nehmen (Reihenfolge: erst noindex, dann ggf. Crawling-Ausschluss — nicht gleichzeitig).
- **Befund verwaiste Seiten (Orphans):** Wichtige Seiten nur im Mobil-Menü, **nicht im Desktop-Menü** verlinkt (`/das-team`, `/messen`, `/versand`, `/widerrufsrecht`, `/ensinger-mineral-heilquellen-gmbh/`, `/partnerformular`); Kategorieseiten und zwei Produkte (`/295/ensinger-naturelle-still`, `/296/ensinger-naturelle-medium`) nur über Suche auffindbar.
  **Maßnahme:** Desktop-Menü/interne Verlinkung nachziehen, damit relevante Kategorien (Kennenlernpakete, Direktsaftschorle) erreichbar sind.
- **Befund Thin Content / Soft-404-Gefahr:** `/messen` (kein Text), `/das-team` (kein Text), `/unternehmensgeschichte` (Blindtext) — Statuscode 200 bei leerem Inhalt.
  **Maßnahme:** Mit Inhalt befüllen oder entfernen + weiterleiten.
- **Befund Meta Keywords:** Auf Produkt- und Kategorieseiten werden (veraltete) Meta-Keywords ausgespielt, teils in großer Zahl (Keyword-Spamming-Risiko).
  **Maßnahme:** Meta-Keywords entfernen bzw. nur intern im CMS nutzen.
- **Befund H1:** 5 Kategorieseiten ohne H1 (`/produkte/sonstige/`, `/mineral-heilwasser/`, `/kennenlernpakete/`, `/iso-getraenke/`, `/direktsaftschorle/`); Produktseiten teils **mehrere H1**; Startseite **keine sinnvolle H1** (nur H1 in Teaser-Boxen).
  **Maßnahme:** Pro relevanter Seite eine einzigartige, keyword-fokussierte H1.
- **Befund Meta Descriptions:** 14 URLs ohne Meta Description (u. a. Startseite und alle Kategorieseiten).
  **Maßnahme:** Einzigartige, CTR-optimierte Descriptions (~150 Zeichen) ergänzen.
- **Befund Bilder:** Alt-Texte auf Produkt-/Kategoriebildern vorhanden (kein dringender Handlungsbedarf); einige Bilder über 100 KB.
  **Maßnahme:** Große Bilder komprimieren; Icons/unwichtige Bilder ggf. für Barrierefreiheit nachziehen.
- **Befund Core Web Vitals (Startseite, mobil, Felddaten):**
  - **LCP:** gut — < 2,5 s bei 85 % der Ladevorgänge (Cookie-Bereich als Bremse genannt).
  - **FID:** gut — 95 % unter 100 ms.
  - **CLS:** **rot** — nur 44 % im grünen Bereich, 56 % mit Wert 1,06; 4 Elemente als Hauptverursacher (nachladende Inhalte).
  **Maßnahme:** Layout-Shifts beheben (feste Maße für nachladende Elemente), Cookie-Banner-Ladeverhalten optimieren.
- **Befund Mobile Usability:** Trusted-Shops-Icon überdeckt das untere Menü und den Cookie-Ablehnen-Button.
- **Canonicals:** Keine Canonical-Chains auf shop.ensinger.de (positiv).

### Sichtbarkeit & Rankings (Sistrix)

- **ensinger.de** (Quelle: „ensinger.de – Sichtbarkeit & Rankings", 21.01.2022):
  - Desktop-SI **0,0602** und Mobile-SI **0,0623** (Stand 17.01.2022) — Mobil/Desktop nahezu identisch → kaum abweichende mobile Inhalte.
  - Rankt für **4.510 Keywords**, davon **335 Brand-Keywords (≈ 7,4 %)** — für eine Corporate-Site eher niedriger Brand-Anteil.
  - Long-Tail-Keywords (≥ 4 Wörter) machen **~21 %** der Rankings aus.
  - Schwerpunkt der Suchintention: „Know" und „Do".
  - **Wettbewerbsposition: Rang 4** unter den regionalen Mitbewerbern; **Gerolsteiner** mit starkem Sichtbarkeitszuwachs 2021 (v. a. durch das Magazin `/magazin/`).
- **shop.ensinger.de** (Quelle: „shop.ensinger.de – Sichtbarkeit, Rankings und Konkurrenzvergleich", 19.01.2022):
  - Desktop-SI **0,0023** (13.12.2021), Mobile-SI faktisch **0** (zeitweise 0,0023) — sehr geringe Sichtbarkeit.
  - Rankt für nur **55 Keywords**, davon **29 Brand-Keywords**; transaktionale Keywords ~24 %.
  - Für `mineralwasser onlineshop` (SV laut Sistrix: 10) Position 33 (20.12.2021).
  - **Kaum gemeinsame Keywords** mit den regionalen Markenwettbewerbern (Gerolsteiner, Volvic, Römerquelle) — diese betreiben keine vergleichbaren Shops.
  - **Bester SEO-Vergleichswettbewerber: shop.eiszeitquell.de** (61 Keywords vs. 55 bei Ensinger, ähnliches Sortiment). Weitere genannte Shop-Konkurrenz: getraenkewelt.de, supermarkt24h.de, bringmeister.de, shop.rewe.de.

### Content-Strategie (Empfehlungen aus dem Audit)

- **Befund:** ensinger.de/shop ranken überwiegend für Know-/Do-Keywords, der Shop fast nur für Brand-Keywords.
  **Begründung:** Wenig nicht-brandbezogene Sichtbarkeit → geringe Neukunden-Reichweite über Suche.
  **Maßnahme:**
  - shop.ensinger.de: stärker auf **transaktionale** und produktbezogene Long-Tail-Do-Keywords optimieren (z. B. „mineralwasser mit hohem magnesium und calciumgehalt", SV 10).
  - ensinger.de: **informationsorientierte Long-Tail-Keywords** über Blog/Magazin/Ratgeber aufbauen (Vorbild: Gerolsteiner-Magazin) — als Experten positionieren, Brand-Bekanntheit für mehr navigationale Suchen steigern.
  - Featured/Rich Snippets nutzen (z. B. FAQs).

### Off-Page / Links (Stand 20.12.2021)

- **Befund:** Sehr **wenige Backlinks** auf shop.ensinger.de, teils noch von der alten Domain. Beispiel-Link: exconcept.de.
- **Befund:** Ausgehende Links shop.ensinger.de → ensinger.de stehen auf **nofollow** (ensinger.de profitiert nicht von der Shop-Linkpower); umgekehrt ensinger.de → Shop ohne nofollow. Grund laut Audit offen / zu klären.
- **Befund:** **Keine Broken Backlinks** und **keine auffälligen Spam-Links** gefunden.
- **Maßnahme:** Aktiver Linkaufbau — Erwähnungen einsammeln, Broken-Backlinks der Wettbewerber, Partner, eigener externer Content.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** In den vorliegenden Drive-Unterlagen (2021/2022) gibt es kein Material zu AI Overviews, ChatGPT/Perplexity-Sichtbarkeit, LLM-Citations oder llms.txt. Das Audit stammt aus der Zeit vor der breiten Relevanz generativer Suche. Für eine GEO-Bewertung wäre eine Neuerhebung erforderlich.

## Doc-Typen & Aufbau

Die Ensinger-Unterlagen folgen dem klassischen EOM-Erst-Audit-Muster (vor dem heutigen Master-Template):

- **Google Slides:**
  - SEO-IST-Analyse (Technik → Content → Links → Fazit & Next Steps), je Slide „Befund + Status Quo".
  - Sichtbarkeits-/Rankings-Präsentationen (getrennt für ensinger.de und shop.ensinger.de), inkl. Konkurrenzvergleich.
  - Jeweils mit BACKUP-Varianten.
- **Google Sheets (Crawl-Exporte, Screaming-Frog-typisch):** Canonicals (alle / nicht-indexierbare), interne URLs (alle/HTML), Sitemap-URLs, fehlende H1, verwaiste Seiten, Umleitungs-/Canonical-Ketten, Bilder > 100 kB. Dateinamen-Konvention `ensinger-shop-<thema>`; Negativbefunde explizit benannt (z. B. „NICHTS GEFUNDEN").
- **Ordnerstruktur im Drive:** `1.0_Orga`, `2.0_Meetings`, `3.0_Reportings` (leer), `4.0_Webtracking`, `5.0_SEO` (mit Unterordner `Crawls`).

## Schreibstil-Notizen

- **Aufbau durchgängig:** Begriffsdefinition → „Status Quo" (konkreter Befund mit URL-Beispielen) → Handlungsempfehlung. Deckt sich mit dem heutigen EOM-Prinzip Befund → Begründung → Maßnahme.
- **Anrede:** In dieser frühen Phase wurde noch gegendert („Nutzer*innen"). Für aktuelle EOM-Deliverables gilt **Sie-Anrede** und **„KI" statt „AI"** (siehe `[[Schreibstil]]`).
- **Datenehrlichkeit:** Sistrix-SI immer mit Datum und Vergleich zur Konkurrenz; ausdrücklicher Hinweis, dass der SI alleinstehend keine Aussagekraft hat und Tools nischige Keywords nicht erfassen.
- **Disclaimer/Branding:** Standard-EOM-Haftungsausschluss + Kontakt Nord (Hannover) / Süd (Stuttgart) auf der Schlussfolie.

## Offene Punkte / Datenlücken

- **Keine aktuellen Daten:** Gesamter Wissensstand ist 2021/2022. Vor Reaktivierung sind SI, Rankings, Crawl, CWV und Backlinks neu zu erheben.
- **Kein Reporting:** Ordner `3.0_Reportings` ist leer → unklar, ob/wie lange eine laufende Betreuung lief.
- **Mandatsstatus unklar:** Ob die „beratende Zusammenarbeit" zustande kam und aktiv ist, ist aus den Unterlagen nicht ableitbar.
- **GEO/KI vollständig offen:** keinerlei AI-Visibility-Daten.
- **SEA:** Analyse des SEA-Accounts war 2022 „tbd" — kein Material vorhanden.
- **Nofollow-Logik Shop→Corporate:** technischer Hintergrund war offen und sollte geklärt werden.
- **Tool-Zugänge:** Unklar, ob für Ensinger aktuell Sistrix-Projekt, GSC- und GA4-Zugang bestehen.

## Quellen

Ausgewertete Dateien aus Google Drive (Ordner `5.0_SEO`, Account `ben@eom.de`):

- **shop.ensinger.de – SEO-IST-Analyse** (Google Slides, 19.01.2022, modifiziert 29.03.2022) — technisches + Content-Erst-Audit.
- **ensinger.de – Sichtbarkeit & Rankings** (Google Slides, 21.01.2022) — SI, Keyword-Verlauf, Brand-Anteil, regionaler Wettbewerb.
- **shop.ensinger.de – Sichtbarkeit, Rankings und Konkurrenzvergleich** (Google Slides, 19.01.2022) — Shop-SI, transaktionale Keywords, SEO-Konkurrenz (EiszeitQuell).
- Ergänzend gesichtet (Dateinamen/Metadaten): Crawl-Sheets `ensinger-shop-canonicals_*`, `ensinger-shop-h1_fehlende`, `ensinger-shop-verwaiste_seiten`, `ensinger-shop-umleitungs_und_canonical_ketten`, `shop.ensinger.de - Bilder über 100 kB - 27.01.22`.
- Ordner `3.0_Reportings`: **leer** (kein Reporting-Material).

---
*Erfasst am 2026-06-19. Datenbasis ausschließlich Erst-Audit Dez 2021 / Jan–März 2022 — nicht aktuell. Siehe `[[Schreibstil]]`, `[[SEO-Methodik]]`.*
