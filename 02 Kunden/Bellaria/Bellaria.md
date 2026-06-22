---
tags: [kunde, seo]
kunde: "Bellaria"
stand-Datum: 2026-06-19
---

# Bellaria

> Wissensdatei, erstellt aus dem Google-Drive-Kundenordner (Account `ben@eom.de`). Logik: Befund -> Begründung -> Maßnahme. Es wurden ausschließlich vorhandene Drive-Dokumente ausgewertet; nichts geschätzt. Fehlende Daten sind unter [[#Offene Punkte / Datenlücken]] offen benannt.

## Überblick

- **Wer:** Bellaria Technology GmbH, Buschingstraße 5, 81677 München (USt-ID DE268136922; laut [[#Quellen|Angebot 251561]]). Ansprechpartner im Angebot: Giuseppe Leo.
- **Branche:** Sanitär-/Hygiene-Hardware (D2C, mit B2B-Linie). Kernprodukt ist der **„Air Cube"** zur **Geruchsneutralisation und Desinfektion der Toilette** auf Basis von Ionisierung — beworben als chemiefreie Alternative zu Sanitärflüssigkeiten und Duftsprays.
- **Bekanntheit:** Auftritt bei **„Die Höhle der Löwen" (DHDL)** — eigene Landingpage `bellaria.de/pages/die-hohe-der-lowen`, im Presse-Leitfaden als Verlinkungsziel geführt.
- **Domain:** `bellaria.de`, Shop auf **Shopify**.
- **Relevante URL-Struktur** (aus Presse-Leitfaden):
  - Produkt/Kauf: `/products/air-cube-geruchsneutralisation-desinfektion-der-toilette`
  - DHDL: `/pages/die-hohe-der-lowen`
  - Technologie/Wissenschaft: `/pages/die-technologie`
  - Unternehmen/Gründer: `/pages/uber-uns`
  - B2B (Hotels, Gastronomie, Büro): `/products/b2b-aircube`

## Mandat & Gewerke

Quelle: **Angebot 251561** vom 19.09.2025 (EOM – Effektiv Online-Marketing GmbH).

- **Position 1 — SEA (Google Ads):** monatlich fortlaufend, 1,5 PT, 880 € EP = 1.320 €/Monat. Kalkuliertes Mediabudget 2.000–4.000 €/Monat (separat). Umfang u. a. Keyword-/Negativ-Keyword-Management, Anzeigentexte, A/B-Tests, Gebotsstrategien, Re-Marketing, Monatsreporting.
- **Position 2 — SEO inkl. Usability & UX-Optimierung:** monatlich fortlaufend, 1,5 PT, 880 € EP = 1.320 €/Monat. Umfang u. a. kontinuierliche Website-Analyse, Suchmaschinen- und User-Optimierung, **Aufbau neuer Seiten**, A/B-Test-Szenarien (z. B. mit VWO), konkrete Empfehlungen + Umsetzung der freigegebenen Empfehlungen, monatliches Reporting.
- **Netto gesamt:** 2.640 €/Monat (zzgl. 19 % MwSt.). **Mediabudgets und Backlinks sind nicht inkludiert.**
- **Vertrag:** Mindestlaufzeit 3 Monate, danach Verlängerung um je 3 Monate (Kündigungsfrist 1 Monat zum Laufzeitende). Alle Accounts gehören dem Kunden, werden ausschließlich von EOM verwaltet.

**Befund:** Bellaria ist ein **kombiniertes SEA-+-SEO/UX-Mandat** mit explizitem Content-/Seitenaufbau-Auftrag. **Maßnahme:** SEO-Arbeit auf den im Mandat genannten Schwerpunkten (technisches On-Page, neuer Content, A/B-Tests) ausrichten; Off-Page/Backlinks nur über separates Budget bzw. PR.

## SEO-Status & Befunde

### Technisch: Überschriftenstruktur (kritisch)
Quellen: „Empfehlung: Überschriftenstruktur im Shopify Theme korrigieren" (06.12.2025, DE) sowie englische Fassung (16.12.2025); Nachtrag „Shopify Elements Headings" (26.01.2026).

- **Befund:** Die H-Tag-Hierarchie auf `bellaria.de` ist strukturell mangelhaft. **H1 fehlt auf vielen Seiten**, semantische Überschriften sind nicht als H-Tag ausgezeichnet. Beispiel `/pages/die-technologie`: nur zwei H2, **keine H1**. Problem betrifft **nahezu alle Seiten** des Shops.
- **Begründung:** Fehlende H1 = fehlendes Hauptsignal für das Seiten-Keyword; saubere H1→H2→H3-Hierarchie wird von Suchmaschinen **und LLMs** zum Inhaltsverständnis genutzt; zudem Barrierefreiheit (Screenreader).
- **Ursache:** Das Shopify-Theme koppelt **visuelle Größe an den HTML-Tag** — es lässt keine unabhängige Wahl des semantischen H-Tags zu, daher wird aus Designgründen oft der falsche oder gar kein Tag gesetzt.
- **Maßnahme (empfohlen):** Theme erweitern, sodass pro Überschriften-Element **zwei getrennte Optionen** existieren — (1) visuelle Größe (rein Design), (2) semantischer H-Tag (H1–H6 oder p). Scope: **jede Überschrift in jedem Theme-Element/Abschnitt**.
- **Nachtrag 26.01.2026 (offene Stellen):** In mehreren Theme-Elementen fehlt weiterhin die Option, **p statt h** zu wählen — konkret benannt: **Text with Icon, Newsletter, FAQ, Timeline, Testimonials Carousel, Item**.

### Off-Page / PR: SEO-Leitfaden für Presseartikel
Quelle: „Bellaria – SEO-Leitfaden für Presseartikel" (16.12.2025), Hinweise an die PR-Agentur.

- **Befund/Maßnahme:** Deep-Links statt pauschaler Startseiten-Links — Themen-zu-URL-Mapping vorgegeben (Produkt → Air-Cube-PDP, DHDL → DHDL-Seite, Technologie → Technologie-Seite, Unternehmen → Über-uns, B2B → B2B-Air-Cube).
- **Ankertexte:** variieren statt wiederholen; je Zielseite Beispiel-Anker vorgegeben (natürliches Linkprofil).
- **DoFollow:** bei **redaktionellen** Artikeln (nicht bei reinen PMs) aktiv nach DoFollow fragen.
- **Tracking:** UTM-Schema vorgegeben — `?utm_source=[publikation]&utm_medium=pr&utm_campaign=[thema]` (source = Publikation kleingeschrieben, medium = immer `pr`, campaign = Artikelthema).

### Keyword-Strategie
Quelle: „2025 Bellaria Keyword Recherche" (Stand 05.12.2025; 1.365 Zeilen) und „2025 Bellaria Content Ideen" (10.12.2025).

- **Cluster** (aus dem Sheet): Camping/Wohnmobil-Toiletten, Hygiene & Reinigung, Geruchsneutralisierer & -killer, Luftreiniger & Lüftung, Toiletten-Duft & Lufterfrischer, Gewerbliche/Öffentliche Toiletten, Marke & Produkt — plus eine als **„Irrelevant"** markierte Spalte (z. B. „toilette verstopft was tun"), die bewusst aussortiert wird.
- **Strategie-Logik (sichtbar in den Sheets):** breite Problem-/Ratgeber-Keywords werden über eine **„Bellaria Bridge"** auf das Produktversprechen (chemiefreie Ionisierung, Ursachenbekämpfung statt Geruchsüberdeckung) zurückgeführt.
- **Spalten im Recherche-Sheet:** Cluster, Subcluster, Keyword, Suchvolumen, Wettbewerb (%), **Aktuelle Position (Erhebung 03.12.2025)**, Relevanz. Positionsspalte ist überwiegend leer; nur einzelne Keywords haben Werte (siehe unten).

> Hinweis: Die im Sheet stehenden Suchvolumen/Wettbewerbswerte stammen aus dem Kunden-Sheet und werden hier 1:1 referenziert, **nicht von EOM nachgeschätzt**. Tool-Quelle des Sheets ist im Dokument nicht ausgewiesen.

**Im Sheet hinterlegte Ist-Positionen (Stand 03.12.2025):**

| Keyword | Suchvolumen (Sheet) | Position (Sheet) |
|---|---|---|
| bellaria (Brand) | 850 | 1 |
| wc frisch | 2.350 | 39 |
| bmuv (als „Irrelevant" markiert) | 4.850 | 42 |
| cube münchen (Irrelevant) | 600 | 47 |
| absenkautomatik reparieren (Irrelevant) | 450 | 46 |

**Befund:** Außer dem Brand-Begriff ist im Sheet keine relevante Top-Position dokumentiert; relevante Money-/Cluster-Keywords haben (noch) keine eingetragene Position. **Maßnahme:** Rankings für die priorisierten Cluster-Keywords erheben und in das Sheet zurückspielen (Spalte „Aktuelle Position" füllen), Content-Lücken über die Content-Ideen schließen.

### Content-Pipeline
Quellen: „2025 Bellaria Content Ideen" (10.12.2025) + Ordner „SEO Texte" (5 fertige Blog-Drafts, Stand 12.01.2026, .docx).

- **Content-Ideen-Sheet** (Spalten: Thema/Cluster, SEO-Titel-Idee, Fokuskeyword, Suchvolumen, sekundäre Keywords, Relevanz/Bellaria Bridge). Beispiele:
  - Camping → „Campingtoilette ohne Chemie: Die sauberste Alternative" (FK `campingtoilette`, 10.700)
  - Problem-Lösung → „Urinstein entfernen & vorbeugen" (FK `urinstein entfernen`, 15.200)
  - Nachhaltigkeit → „Trockentrenntoilette & Lüftung: Das perfekte Duo für Tiny Houses" (FK `trockentrenntoilette`, 5.800)
  - Lüftung → „Bad ohne Fenster lüften" (FK `badlüfter`, 4.400)
  - B2B → „Öffentliche Toiletten & Büros: Hygiene als Visitenkarte" (FK `öffentliche toilette`, 5.150)
- **Befund:** 5 dieser Ideen liegen bereits als **fertige Blog-Texte** im Ordner „SEO Texte" (Bad ohne Fenster lüften; Campingtoilette ohne Chemie; Trockentrenntoilette & Lüftung; Urinstein entfernen; Öffentliche Toiletten & Büros). **Begründung:** deckt direkt das Mandat „Aufbau neuer Seiten". **Maßnahme:** Veröffentlichung + interne Verlinkung auf die im Presse-Leitfaden definierten Money-Pages prüfen.

## GEO / KI-Sichtbarkeit

- **Keine eigenständigen GEO-/AI-Visibility-Daten gefunden** (keine Peec-AI-/AI-Overview-/LLM-Mentions-Auswertung im Kundenordner).
- **Einziger GEO-relevanter Hinweis:** In der Heading-Empfehlung wird ausdrücklich begründet, dass **LLMs die H1→H2→H3-Struktur zum Inhaltsverständnis nutzen** — die Heading-Korrektur ist damit auch eine GEO-Grundlagenmaßnahme.
- **Maßnahme (Vorschlag):** Sobald Heading-Struktur sauber ist, AI-Sichtbarkeit für die Kern-Cluster (Geruchsneutralisation, chemiefreie Campingtoilette, DHDL-Produkt) baselinen — derzeit keine Datengrundlage im Vault.

## Doc-Typen & Aufbau

Im Kundenordner vorgefundene Deliverable-Typen:
- **Empfehlungs-Doc** (technisch): Aufbau **Problem → Warum wichtig → Ursache → Empfehlung (mit Scope)**, DE und EN parallel gepflegt.
- **Leitfaden-Doc** (Off-Page/PR): nummerierte Abschnitte mit Tabellen (Ziel-URLs, Ankertexte, UTM-Beispiele).
- **Keyword-Sheet:** Cluster/Subcluster/Keyword/SV/Wettbewerb/Position/Relevanz.
- **Content-Ideen-Sheet:** Cluster/Titel/Fokuskeyword/SV/Sekundär-KW/Bellaria-Bridge.
- **Blog-Drafts (.docx):** je ein Artikel pro Content-Idee, Dateibenennung `YYMMDD Bellaria I Blog Post: <Titel>`.
- Alle Docs mit EOM-Fußzeile (Bödekerstraße 85, 30161 Hannover; GF Ernest Mavriqi).

## Schreibstil-Notizen

- **Sie-Anrede** in kundengerichteten Texten; durchgehend deutschsprachig (englische Spiegelfassungen nur für Theme-/Dev-Empfehlungen).
- Analyse-Logik **Problem → Begründung → Maßnahme** mit explizitem **Scope**.
- Produktnarrativ konsequent: **Ursachenbekämpfung statt Geruchsüberdeckung**, **chemiefrei/Ionisierung**, **Plug & Play**, DHDL als Trust-Anker.
- Content-Bridge-Prinzip: breites Ratgeber-Keyword → Hinführung zum Air Cube als Lösung.
- Marke wird im Presse-Leitfaden klein geschrieben („bellaria").

## Offene Punkte / Datenlücken

- **Kein Reporting/Performance-Export** im Ordner (keine GSC-/GA4-/Looker-/SEA-Kennzahlen) → tatsächliche Klicks/Impressionen/CTR/Conversions/CPO unbekannt.
- **Keyword-Sheet:** Spalte „Aktuelle Position" überwiegend leer; Tool-/Datenquelle der Suchvolumen nicht ausgewiesen → Volumen sind ungeprüft übernommen.
- **Keine GEO/AI-Visibility-Daten** (siehe oben).
- **Kein technisches Crawl-Audit** (Broken Links, Redirects, hreflang, Indexierung, Core Web Vitals) im Ordner — nur der Heading-Teilbefund liegt vor.
- **.docx-Blog-Texte** (Ordner „SEO Texte") sind Office-Dateien und wurden **nur per Dateiname** ausgewertet, nicht im Volltext.
- **Umsetzungsstand** der Heading-Empfehlung unklar; der Nachtrag vom 26.01.2026 listet noch offene Theme-Elemente → vermutlich teilweise offen.

## Quellen

Ausgewertete Drive-Dateien (Account `ben@eom.de`, Ordner „Bellaria"):
- Angebot 251561-11059.pdf — 19.09.2025 (Mandat SEA + SEO/UX) — Volltext extrahiert
- „20251205 Empfehlung: Überschriftenstruktur im Shopify Theme korrigieren" (Google Doc) — 06.12.2025 — gelesen
- „20251205 Recommendation: Correct the heading structure in the Shopify theme" (Google Doc) — 16.12.2025 — engl. Spiegelfassung (per Name gewertet)
- „20260126 Shopify Elements Headings" (Google Doc) — 26.01.2026 — gelesen
- „Bellaria – SEO-Leitfaden für Presseartikel" (Google Doc) — 16.12.2025 — gelesen
- „2025 Bellaria Keyword Recherche" (Google Sheet, 1.365 Zeilen) — Stand 03./05.12.2025 — Auszug gelesen
- „2025 Bellaria Content Ideen" (Google Sheet) — 10.12.2025 — gelesen
- Ordner „SEO Texte" — 5 Blog-Drafts (.docx, 12.01.2026) — per Dateiname gewertet (Office-Format, nicht exportierbar)

Verwandt: [[Über EOM]] · [[SEO-Methodik]] · [[Schreibstil]] · [[Tools-Stack]]
