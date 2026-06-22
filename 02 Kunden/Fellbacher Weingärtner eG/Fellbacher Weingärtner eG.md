---
tags: [kunde, seo]
kunde: "Fellbacher Weingärtner eG"
stand-Datum: 2026-06-19
---

# Fellbacher Weingärtner eG

> Wissensdatei (EOM SEO Operating System). Logik durchgehend: **Befund → Begründung → Maßnahme**. Quellen mit Datum am Ende. Es wurden keine Rankings/Suchvolumina/Backlinks geschätzt — fehlende oder nicht zugängliche Daten sind offen benannt.

## Überblick

- **Wer:** Fellbacher Weingärtner eG — Winzergenossenschaft (eG) aus Fellbach im Remstal, Württemberg. Vermarktet eigene Weine, u. a. die Jungwinzer-Kooperation „next generation".
- **Branche:** Wein / E-Commerce (Wein-Onlineshop) + lokaler Weinverkauf, Veranstaltungen/Weinproben.
- **Domain:** `https://fellbacher-weine.de/` (WordPress + WooCommerce, Theme „gwyneth", Plugins u. a. Yoast SEO, WP-Optimize, WooCommerce PDF Vouchers).
- **Mandatsdauer:** langjähriges Mandat — Dokumente reichen von 2020 bis laufend 2026; betreut wird neben SEO auch SEA (Google Ads).
- **Wettbewerbsumfeld:** Laut Reporting liegt die Domain im Sichtbarkeitsindex-Vergleich mit den wichtigsten Wettbewerbern „weiterhin im oberen Bereich" (Reporting Nov 2025). Konkrete Wettbewerber sind in den ausgewerteten Dateien nicht namentlich genannt.

## Mandat & Gewerke

Belegt durch Ordnerstruktur und Dokumente:

- **SEO (Kern):** Technik/Crawl-Checks, On-Page (Startseite, Kategorien, Produkt-/Rebsorten-Seiten, Landingpages), Content/Ratgeber, interne Verlinkung, Disavow/Off-Page (`disavow-fellbacher-2021-07-05.txt`).
- **SEA:** Google Ads (eigener Reporting-Block, siehe Nov 2025).
- **Content:** Ratgeber-Empfehlungen (Wein-Themen) und Produkt-/Kategorietexte (Ordner `7.0_Content` mit „Rebsorten" und „Kategorieseiten").
- **Usability & Tracking:** eigene Ordner `5.0_Usability`, `8.0_Tracking`.
- **Analyse & Strategie:** Ordner `9.0_Analyse & Strategie` inkl. KPI-Sammlung und einem 2026er „Strategie-Scan"-Angebot.
- **Reporting:** monatliche externe Reportings (Looker Studio), Jahresreporting; Drive-Ordner `3.0_Reportings - EXTERN` (2022–2025).

## SEO-Status & Befunde

### Technik / Crawl (aktuellster Stand: Crawl-Check Nov 2025)

> Quelle: „Fellbacher I (Crawl-)Check fellbacher-weine.de I Update November 2025" (Google Doc, 2025-11-19).

- **Doppelte Seitentitel auf 275 Seiten.** *Begründung:* Vermutetes Zusammenspiel von Yoast + neuem WP-Theme — im Quelltext erscheinen jeweils 2 identische Meta-Title; ein Test zeigte, dass eine Yoast-Änderung automatisch in den zweiten Title übernommen wird. *Maßnahme:* Ursache im Theme/Yoast-Setup beheben (Theme gibt vermutlich einen eigenen zweiten Title aus), damit nur ein Title pro Seite gerendert wird.
- **404-Fehler bei Bildern und URLs**, u. a. ein verlinktes Produkt mit Leerzeichen in der URL (`…2024-rose-next-generation-%20trocken/`). *Maßnahme:* Bild-/URL-Verweise korrigieren, fehlerhafte URL bereinigen.
- **Mehrere H1** auf `/veranstaltungen-und-weinproben/`. *Maßnahme:* auf eine H1 reduzieren.
- **Fehlende Alt-Texte/Alt-Attribute** bei zahlreichen Bildern (lange Liste im Doc). *Maßnahme:* Alt-Texte ergänzen (Barrierefreiheit + Bild-SEO).
- **Fehlende Meta-Descriptions** u. a. `/unsere-partner/`, `/produkt-kategorie/magnum-sondereditionen/` (inkl. Pagination-Seite). *Maßnahme:* Meta-Descriptions ergänzen.
- **Bild-Performance:** Bilder über 200 kB / 100 kB (insgesamt 155 Bilder über 100 kB), fehlende Größenattribute. *Maßnahme:* Bilder komprimieren, `width`/`height` setzen.
- **PageSpeed / Core Web Vitals:** Core Web Vitals nicht bestanden; viele Shopseiten nur ~60/100, v. a. mobil. Render-blockierende Plugins; **Schriftart wirft 404** (prioritär). Filter-Menü im Shop lädt sehr langsam/unvollständig; Produktbilder werden mobil teils nicht geladen. *Maßnahme:* Plugins auf Notwendigkeit prüfen/aktualisieren (inkl. WP-Optimize-Einstellungen), Font-404 beheben, Shop-Filter und mobile Bildauslieferung optimieren.
- **Layout/Usability:** fehlendes Favicon, verrutschte Buttons/Elemente auf mehreren Seiten, Angebot-Banner überlappt Produktdarstellung bei reduzierten Artikeln, unregelmäßige Cookie-Consent-Abfrage. *Maßnahme:* Frontend-Fixes + Consent-Einstellungen prüfen (auch Datenschutz-relevant).

Hinweis: Diese Technik-Auffälligkeiten werden im **Reporting November 2025** ausdrücklich als noch offen markiert („bestehen jedoch noch weiterhin die Auffälligkeiten aus unserem letzten Technik-Check").

### Performance / KPIs (Reporting November 2025, Jahresvergleich)

> Quelle: „11 Reporting 2025" (Google Doc, 2025-12-07), Datenbasis GA4 + Google Search Console + Sichtbarkeitsindex.

- **Organic (GA4):** Nutzer −35,3 %, Transaktionen −10,5 % ggü. Vorjahr.
- **Engagement verbessert:** Absprungrate −7,2 %, Seiten/Sitzung +27 % → intensivere Auseinandersetzung mit Inhalten.
- **GSC:** Klicks +4,1 %, Impressionen −23,3 %, CTR +35,7 % ggü. Vorjahr.
- **Sichtbarkeitsindex:** leichte Verbesserung ggü. Vormonat; im Wettbewerbsvergleich „oberer Bereich".
- **SEA (Nov 2025):** 24 Conversions (+4,3 %), Klicks +13,1 %, Impressionen +26,4 %, CPC/Conversion −6,2 % bei Gesamtkosten 295,01 €.
- **Gesamtumsatz (GA4, Jahresvergleich):** −5,2 %; organischer Umsatz gleichbleibend, Google-Ads-Umsatz −41,2 %.

*Einordnung:* Rückläufiger organischer Traffic bei steigender CTR und besserem Engagement deutet auf qualitativ relevanteren, aber volumenmäßig schrumpfenden Suchtraffic hin — die offenen Technik-Themen (CWV, Title-Dubletten) sind plausible Mitursachen und der naheliegende Hebel.

### On-Page / Content-Maßnahmen (Verlauf)

- **Aktuelle On-Page-Empfehlung:** Nachoptimierung der „next generation"-Landingpage (`/next-generation/`) inkl. zugehöriger Produktseiten — Title/Meta/H1/Alt-Tags + Content-Erweiterung. Quelle: Doc 2025-05-28. (Detaillierte Title/Meta-Konvention siehe „Schreibstil-Notizen".)
- **Content-Schwerpunkt Ratgeber:** Über Jahre laufend (Sulfite, Lagerung, Weinglas, Weinstein, vegane Weine, Wein-zu-Essen-Pairing, Wein-zu-Schokolade). 2024er Analyse: Ratgeber zum Thema **Wein-Pairing** als noch offene Empfehlung.
- **Aktuelle Content-Pipeline:** „Potential-Liste für Fellbacher (Ratgeber & Content-Ideen)" (Doc 2025-10-15) mit Keyword-recherchierten Themen (Suchvolumina aus dem Doc, nicht von mir geschätzt), u. a.:
  - „Wie lange ist Wein haltbar?" (SV 1.000 / „offener wein haltbarkeit" SV 320)
  - „Wie dekantiere ich Wein richtig?" (wein dekantieren SV 1.000)
  - „Erntezeit / Weinlese" (weinlese SV 1.600, wann ist weinlese SV 390)
  - „Trinktemperatur von Weinen" (rotwein trinktemperatur SV 1.300, trinktemperatur weißwein SV 1.000)
  - „Wein-Drinks/Cocktails 2025" (wein cocktails SV 480), „Kochen mit Wein", „Weindegustation", „Geschichte des Weinbaus", „Weinfehler".
- **Weitere aktuelle On-Page/Strukturthemen:** Shop-Kategorien nach Rebsorten, Rebsorten-Seiten-Übersicht, Shop-Duplikate, 404-Liste, VfB-Business-Partner-Seite, Auszeichnung „MUNDUS vini Summer Tasting 2025 – Best Producer Germany" (Empfehlung 2025-10-15), Sitemap in robots.txt (Empfehlung 2025-06-04).

### Off-Page

- Disavow gepflegt (`disavow-fellbacher-2021-07-05.txt`, Doc „Disavow-Update" 2021-07-05) und Empfehlungen zu externen Verlinkungen (2022). Keine aktuellen Off-Page-/Backlink-Kennzahlen in den ausgewerteten Dateien — **nicht geschätzt**.

## GEO / KI-Sichtbarkeit

**Keine GEO-Daten gefunden.** In den ausgewerteten Dateien und der Ordnerstruktur (Stand 2026-06-19) gibt es **kein** Material zu KI-Sichtbarkeit (AI Overviews, ChatGPT/Perplexity-Zitierungen, LLM-Mentions, llms.txt, Peec AI o. ä.). Der „Strategie-Scan 2026" erwähnt KI nur allgemein als Markttrend („KI verändert … Kundenverhalten fundamental"), enthält aber keine GEO-Analyse oder -Maßnahme für Fellbacher.

*Konsequenz / offener Hebel:* GEO ist für diesen Kunden bisher ungenutzt. Die vorhandene, breite Ratgeber-Content-Basis (Wein-Wissen, Pairing, Lagerung, Trinktemperatur) ist inhaltlich gut für KI-Zitierfähigkeit geeignet — ein eigener GEO-/AI-Visibility-Check wäre ein sinnvoller nächster Schritt, liegt aber aktuell nicht vor.

## Doc-Typen & Aufbau

Wiederkehrende Deliverable-Typen im Kundenordner:

- **Crawl-/Technik-Check** (Google Doc): nummerierte Befundliste mit URL-Beispielen und Screenshots; Abschnitt Crawl-Ergebnisse, PageSpeed, Core Web Vitals.
- **On-Page-/Nachoptimierungs-Empfehlung** (Google Doc): fester Aufbau — 1. Keywords (Haupt-/Nebenkeywords mit SV), 2. Meta-Daten (Ist/Empfohlen für Title, Description, Alt-Tags, H1), 3. Content (mit Farbcode rot=entfernen / orange=anpassen / grün=hinzufügen), 4. Interne Verlinkungen, 5. zugehörige Produktseiten.
- **Content-/Ratgeber-Empfehlung** (Google Doc): Themenvorschlag + Keywords mit SV.
- **Potential-/Keyword-Liste** (Google Doc): Themen-Cluster mit Keywords + Suchvolumen.
- **Keyword-/Struktur-Sheets** (Google Sheets): KWR Veranstaltungen, Rebsorten-Seiten-Übersicht, Shop-Kategorien-Liste, 404-Fehler, fehlerhafte Verlinkungen, Bilddateien-Listen, Rankings.
- **Monatsreporting** (Google Doc + PDF + Looker Studio): Blöcke SEO / SEA / Gesamtumsatz, jeweils Jahresvergleich mit Prozentwerten und Seitenverweisen.
- **Analyse & Strategie** (Doc/Sheet/Slides): KPI-Sammlung, „Analyse & Übersicht", „Strategie-Scan 2026" (Slides).

## Schreibstil-Notizen

- **Anrede/Schreibweise:** „Sie", „KI" statt „AI" (EOM-Hausstil); in Kunden-Copy Fließtext zu Wein eher emotional/sensorisch („leichtfüßig, filigran", „fruchtbetont", „Perlage").
- **Title-/Meta-Konvention (belegt an `/next-generation/`):**
  - Title-Muster: Keyword-führend + Marke + Nutzen, mit Pipe — z. B. „Junge Winzer der Fellbacher Weingärtner eG | Moderne Weine".
  - Meta-Description: Nutzen + Aufzählung + CTA mit Pfeil-Symbol „➧ Jetzt mehr erfahren!".
  - H1: deskriptiv, keyword-haltig (z. B. „Junge Winzer Weine – Die Jungwinzerkooperation ‚next Generation' …").
  - Alt-Tags: beschreibend mit Produkt-/Markenbezug.
- **Marken-/Sortimentsbegriffe:** „next generation" (Jungwinzer-Kooperation, gegr. 2007), Rebsorten/Linien (Riesling, Lemberger/Lämmler, Trollinger-Rosé, Schillerwein, Federle, Sondereditionen Magnum, Pétillant Naturel, Sekt brut nature), Region Remstal/Fellbach/Kappelberg.
- **Content-Farbcode in Empfehlungen:** rot = entfernen, orange = anpassen, grün = hinzufügen.

## Offene Punkte / Datenlücken

- **Technik-Befunde aus Nov-2025-Check sind laut Reporting noch offen** (Title-Dubletten, CWV, Font-404, Bilder, Alt-Texte) — Umsetzungsstand unklar.
- **Keine GEO/KI-Visibility-Daten** im Ordner vorhanden (s. o.).
- **Keine aktuellen Off-Page/Backlink-Kennzahlen** ausgewertet (Disavow nur historisch 2021).
- **Sistrix-/Ahrefs-/GSC-Rohdaten nicht in dieser Datei** — Reporting referenziert Looker Studio + GA4/GSC, exakte absolute Zahlen liegen in den Reports/PDFs, nicht hier; keine Werte geschätzt.
- **Office-Dateien (.pptx/.xlsx)** wie die 2026er „Strategie Scan"-Slides wurden teils nur über Doc-Export/Namen ausgewertet; einige reine PDF-Reportings (z. B. Monats-PDFs) wurden nicht voll geparst.
- **Wettbewerber nicht namentlich** in den ausgewerteten Dateien.

## Quellen (ausgewertete Dateien, Account ben@eom.de)

- Kundenordner-Root: `1r6dc85lJDzyh2nebe6dCYqdVeaPc-XIp` (Struktur 1.0_Orga … 9.0_Analyse & Strategie).
- **Fellbacher I (Crawl-)Check fellbacher-weine.de I Update November 2025** — Google Doc, 2025-11-19 (`17bN5savGnoYZn2uh-_zjnCuzW1Fgbl0NuyJdE30X02k`).
- **11 Reporting 2025** — Google Doc, 2025-12-07 (`1efhIzJ03LvnTmpEQwsducEwoF5QD6PcfrfpvZYCVxDE`).
- **Potential-Liste für Fellbacher (Ratgeber & Content-Ideen)** — Google Doc, 2025-10-15 (`1GqOaJUna90kRcoQ_SQCTTEOd3y3o_NDMC8shKeIkGkI`).
- **Empfehlung Nachoptimierung Next Generation Landing-Page & Produktseiten** — Google Doc, 2025-05-28 (`1J9fTYAFZPvO49Cz1x_hhrFfOuMFEB6pTm3HbqsXK5fY`).
- **Fellbacher_Strategie Scan – 2026** — Google Slides, 2026-03-24 (`1sbj8q5BcziE1ZziuzWuJnVPxo1kU94qZwwoMUDJyJlc`).
- **2024-09-06 Analyse & Übersicht** — Google Doc, 2024-09-06 (`1nxZUvRL1s4JaKEZkpG19LjDlbs9IP4Jf3_ciVhZxDNM`).
- **2024-09-05 Sammlung KPIs** — Google Sheet (`1l5YyU6whDnim_sQilNa2rW_WEfPn9fZgDPzeH7hg_N8`).
- Ergänzend per Dateiname/Metadaten gewertet: Reporting-Ordner 2022–2025, „Entwicklung 2025"-Slides (2026-01-27), 404-/Verlinkungs-/Bilder-Sheets, Disavow 2021, Rebsorten-/Kategorie-Content-Ordner.
