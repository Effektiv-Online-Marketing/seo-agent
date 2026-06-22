---
tags: [kunde, seo]
kunde: "LiGaLo GmbH"
stand-Datum: 2026-06-19
---

# LiGaLo GmbH

> Wissensdatei auf Basis des Google-Drive-Kundenordners (Account `ben@eom.de`). Alle Daten stammen aus dem EOM-Projektordner LiGaLo; das Material ist überwiegend aus **2021** (SEO-Audit, Technik-Tracking) mit einer letzten Aktualisierung am SEO-Audit-Deck im **Juli 2023**. Neuere SEO-Daten (Sistrix/GSC/Ahrefs-Exporte mit aktuellen Zahlen) liegen im Ordner **nicht** vor — entsprechend ist diese Notiz eine Bestandsaufnahme des Mandats-Wissens, kein aktueller Performance-Stand.

## Überblick

- **Kunde / Auftraggeber:** LiGaLo GmbH (Online-Händler im Bereich **Pool & Garten**).
- **Branche:** E-Commerce, Produktsegmente Pools (v. a. Stahlwandpools), Wasserpflege, Poolreiniger, Filteranlagen, Poolheizung, Poolzubehör, Spa/Whirlpool/Sauna, Ersatzteile sowie Gartensortiment.
- **Domains (zwei Shops im selben Mandat):**
  - [[fresh-pool.de]] — Spezialshop Pool & Poolzubehör.
  - [[garten.com]] — breiteres Garten-Sortiment.
  - Im Wettbewerbsvergleich genannt: planet-pool.de, teichking.de (Mitbewerber-Kurzanalyse vorhanden).
- **Shop-System:** Shopware 6 (belegt durch Hinweis im Technik-Tracking: 302-Weiterleitungen im Account-Bereich = „Shopware 6 Standard"). Technische Umsetzung über Dienstleister **netformic** (Jira-Tickets `LIG-…`), Projektsteuerung historisch über Basecamp.
- **Ansprechpartnerin Kunde:** Melanie Mayer, Senior Online Marketing Managerin (melanie.mayer@ligalo.com, +49 7024 4048354). Ansprache „Du". Quelle: Projektstart-Checkliste, EOM.
- **Betreuung:** EOM Agency. Leistungsumfang laut Angebot/Checkliste: **SEO-Audit (ca. 3 PT netto)** für beide Projekte, **Amazon-Betreuung (ca. 2 PT)**. Ordnerstruktur weist zusätzlich SEA und Content aus.

## Mandat & Gewerke

Die Ordnerstruktur (`1.0_Orga`, `2.0_SEO`, `3.0_Content`, `4.0_Amazon`, `5.0_SEA`) zeigt ein **Full-Service-Mandat** mit SEO-Schwerpunkt. Belegte aktive Gewerke:

- **Technisches SEO** (umfangreichster Bereich): laufendes Issue-Tracking 2021 (Crawls per Screaming Frog, Ahrefs-Audits), Übergabe von Tickets an netformic.
- **On-Page:** Title/Meta-Optimierung, H1-Struktur, Alt-Attribute, interne Verlinkung, Keyword-/Seiten-Mapping.
- **Content:** Content-Briefing für Texterstellung, Ratgeber-Themen-Sammlung für fresh-pool.de + garten.com.
- **Off-Page:** Ordner `Offpage` + Backlink-/Broken-Backlink-Analysen (Ahrefs). Aktiver Linkaufbau im Material nicht dokumentiert.
- **Marken-/Sichtbarkeits-Strategie:** Deck „Sichtbarkeit der Marke Fresh-Pool" (06.10.2021) — antizyklischer Marken-Push für High-Season 2022 (Display, YouTube, Advertorials, Content auf Drittseiten, Remarketing).
- **Amazon & SEA:** als Gewerke angelegt; im SEO/GEO-Scope dieser Notiz nicht ausgewertet.

## SEO-Status & Befunde

Quelle, soweit nicht anders genannt: **EOM SEO-Audit fresh-pool.de & garten.com** (Slides, Ordner `1.0_Orga`/`SEO-Audit`; Deck zuletzt geändert 27.07.2023, inhaltliche Datenbasis 2021) sowie **Technik-Übersicht „November 21"** (Sheet, Ordner `Technik`, geändert 17.11.2021). Das Audit-Deck ist teils ein Template mit Platzhaltern („xy", „ready4out") — belastbare Befunde unten, Platzhalter ausgeklammert.

### Sichtbarkeit (Sistrix)
- **Befund:** fresh-pool.de mit sehr niedrigem Sistrix-Sichtbarkeitsindex **0,009** (Stand laut Deck ~2021). **Begründung:** Marke/Shop nahezu unsichtbar im organischen Index, hoher Hebel über Basisoptimierung. **Maßnahme:** Crawl-/Index-Budget bereinigen, relevante Seiten optimieren, Content-Relevanz aufbauen. *Hinweis: kein aktueller SI-Wert verfügbar — Zahl nicht fortschreiben.*

### Indexierung & Crawl-Budget
- **Befund:** Zu viele irrelevante Seiten im Index; Ziel ist nur relevante, zielführende Seiten zu indexieren. Login-/Checkout-/Recover-/Service-/Rechtliches-URLs sind bereits korrekt von der Indexierung ausgeschlossen. **Maßnahme:** unwichtige Kategorie-/System-Seiten per `noindial`/X-Robots-Tag entfernen (Sheet „noindex Kategorieseiten").
- **Befund:** **PDFs sind indexiert** — fresh-pool.de-PDFs ranken für **145 Keywords**. **Begründung:** PDFs erlauben keine Navigation/Conversion; Traffic-Verlust. **Maßnahme:** alle PDFs auf `noindex`, Inhalte (z. B. Aufbauanleitungen) in Ratgeber-/Landingpages überführen.

### Sitemaps & robots.txt
- **Befund:** garten.com — XML-Sitemap **nicht korrekt in robots.txt** verlinkt (`Sitemap:`-Zeile fehlte). **Maßnahme:** `Sitemap: https://www.garten.com/sitemap.xml` ergänzen.
- **Befund:** Sitemaps enthalten URLs mit Statuscode **301 / 404** sowie canonicalisierte und noindex-pflichtige URLs (fresh-pool.de: nur 301-URLs ohne www; garten.com: 404 + Canonical-Verweise). **Maßnahme:** Sitemaps so bereinigen, dass nur **Status 200** enthalten ist — erst **nachdem** noindex-Maßnahmen umgesetzt sind. (Laufende Sitemap-Checks bis 18.01.2022 dokumentiert.)

### Redirects & Statuscodes
- **Befund:** http→https und non-www→www vorhanden; **keine** Weiterleitung ohne→mit Trailingslash und **keine** Groß→Klein-Normalisierung in URLs (z. B. `/ratgeber/` und `/Ratgeber/` beide erreichbar → Duplicate-Content-Risiko). **Maßnahme:** Trailingslash- und Lowercase-Redirects (301) einrichten.
- **Befund:** Interne Verlinkungen zeigen auf 301-Weiterleitungen (fresh-pool.de u. a. `/service/ueber-uns/` verlinkt http-Version; garten.com mehrere). **Maßnahme:** interne Links auf finale Zielseite umstellen (Ticket LIG-147).
- **Befund:** intern eine gecrawlte 404-URL (PLANET-POOL-Ovalformbeckenset); garten.com 16 404-Bilder-URLs + Broken Backlinks auf beide Domains. **Maßnahme:** 404 → 301 wo Ersatz vorhanden, sonst **410**; Broken-Backlink-Ziele weiterleiten. Status: Broken-Backlink-Thema 2021 **bewusst zurückgestellt** (Aufwand bei netformic zu hoch).
- **Befund:** Weiterleitungsketten, Soft-404, fehlerhafte externe Links — **nichts gefunden** (Technik-Tracking). 302er im Account-Bereich = Shopware-6-Standard, korrekt.

### Canonicals
- **Befund:** **Canonical + noindex kombiniert** auf 15 URLs (widersprüchliche Anweisung an Google); 2 URLs mit **mehreren Canonicals**. **Maßnahme:** bei noindex-Seiten Canonical entfernen; Mehrfach-Canonicals auflösen (Ticket LIG-145).

### On-Page: H1, Title, Meta
- **Befund:** Doppelte/fehlende/mehrfache H1en; Cookie- und Footer-Elemente („Newsletter", „Datenschutz") fälschlich als Überschriften (H2–H5) deklariert, zudem leere H5 auf allen Seiten. **Maßnahme:** Überschriftenstruktur bereinigen, Footer/Cookie optisch statt semantisch (Ticket LIG-146).
- **Befund:** **22 doppelte Page Titles, 101 doppelte Meta Descriptions**; Produktdetailseiten nutzen Produktbeschreibung als Meta Description, Titles generisch/doppelt; Kategorieseiten oft **leere** Meta-Daten. **Maßnahme:** dynamische Title-/Description-Templates, z. B. `[Produkt-/Kategoriename] online kaufen | fresh-pool.de` bzw. `… | garten.com`, Description mit USP-Häkchen (✓ große Auswahl ✓ ab 39 € versandkostenfrei ▶ Jetzt bestellen!). Zeichengrenzen: Title ~58 Zeichen, Description ~150 Zeichen. Tool: Sistrix SERP-Snippet-Generator.

### Bilder & Performance (Core Web Vitals)
- **Befund:** viele Bilder ohne Alt-Text; **>192 Bilder über 100 KB**; Bildelemente ohne explizite width/height. **Maßnahme:** Alt-Texte mit Hauptkeyword, Komprimierung (<100 KB, Squoosh/TinyPNG), responsive Größen, width/height setzen.
- **Befund:** schwache mobile Ladegeschwindigkeit; **CLS ~0,28** (GSC, Schwellwertüberschreitung), LCP-Startseite sehr hoch (Headerbild zu spät geladen). Betroffene CLS-URLs u. a. `/`, `/Ratgeber/`, `/Zubehoer/`, `/Blog/`. **Maßnahme:** Bild-Optimierung, Caching, Lazy-Loading nicht-sichtbarer Bilder, ungenutztes CSS/JS entfernen. Status (Tracking): CWV-Tickets LIG-74/75 bei netformic „wohl abgeschlossen".
- **Befund:** GSC ohne gravierende Probleme; sichtbare Fehler nur durch irrelevante `/widgets/`-URLs (entfernen). Meiste Klicks mobil.

### Strukturierte Daten (Schema)
- **Befund:** als offener Technik-Task gelistet (Status nicht erledigt): **strukturierte Daten auf Kategorieseiten/Blogartikeln (FAQ)** und **Rich Snippets für Produkte** (Preis, Verfügbarkeit). **Maßnahme:** Produkt- und FAQ-Schema einführen.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten im Ordner gefunden.** Das gesamte Material stammt aus 2021–2023 (jüngste Aktualisierung Juli 2023) und enthält keinerlei Bezug zu AI Overviews, ChatGPT/Perplexity-Zitaten, LLM-Sichtbarkeit, `llms.txt` oder KI-Crawlern (GPTBot/ClaudeBot/PerplexityBot). Sollte GEO für LiGaLo relevant werden, ist eine Neuerhebung nötig (z. B. Peec AI / Sistrix AI). Anknüpfungspunkt für GEO-Vorbereitung: die ohnehin empfohlenen **FAQ-/Produkt-Schemas** und der geplante **Ratgeber-Content** (Pool winterfest machen, Aufbauanleitungen) sind klassische, gut zitierbare Antwort-Formate.

## Doc-Typen & Aufbau

Typische Deliverable-Formen im LiGaLo-Ordner:

- **Slides (Google Präsentation):** SEO-Audit (Befund→Begründung→Maßnahme je Folie, EOM-Branding, Montserrat), Marken-Sichtbarkeits-Strategie, Mitbewerber-Kurzanalyse.
- **Sheets:** Issue-/Task-Tracker („Übersicht Technik Themen") mit Spalten Prio / Thema / Beschreibung / Link Tabelle / Basecamp-Task / netformic-Ticket / Zuständig / Status / Erledigt; dazu Detail-Tabellen je Befund (Metadaten, H1en, Canonicals, Sitemaps, Broken Backlinks, Bilder, interne Verlinkung, Keyword-/Seiten-Mapping).
- **Docs:** Content-Briefing (Fragebogen zur Tonalität), Optimierungsvorschläge.
- **Rohdaten/Exporte:** Screaming-Frog-Crawls (`.seospider`/`.xlsx`), Ahrefs-CSV (broken_links, broken backlinks, orphan pages), GSC-Coverage-Exporte, XML-Sitemaps.
- **Naming-Muster:** `LiGaLo - fresh-pool.de + garten.com - <Thema> - <Datum>`. Detailtabellen sind im Audit-Deck per „→ Zur Tabelle" verlinkt.

## Schreibstil-Notizen

- **Audit-/Analyse-Sprache (EOM-intern → Kunde):** durchgängig **Befund → Begründung → Maßnahme**, Sie-/sachliche Erklärungston, Fachbegriffe mit Kurzdefinition (Crawl-Budget, Canonical, CWV-Metriken LCP/FID/CLS). Haftungsausschluss in Decks Standard.
- **Tonalität Kunden-Content noch offen:** Das Content-Briefing fragt Ansprache (Sie/ihr/du), Selbstbezeichnung, Tabu-/Pflicht-Wörter, Gendering und Positionierung **ab** — im Ordner liegen **keine ausgefüllten Antworten** vor. Im EOM-Vault gilt für Kunden-Copy generell Sie-Anrede und „KI" statt „AI"; die LiGaLo-spezifische Tonalität ist nicht final dokumentiert.
- **Interne Projektkommunikation:** locker, „Du" mit Melanie Mayer; Tickets sachlich mit Akzeptanzkriterien an netformic.
- **Title/Meta-Konvention (vorgeschlagen):** `[Produkt-/Kategoriename] online kaufen | fresh-pool.de` / `… | garten.com`; Description mit ✓-USPs und ▶-CTA.

## Offene Punkte / Datenlücken

- **Aktualität:** Material ist 2021er-Bestand (Deck zuletzt 07/2023). **Kein** aktueller SEO-Performance-Stand (Sistrix-SI, GSC-Klicks/Impressionen, Rankings, Backlink-Zahlen) im Ordner — nicht aus alten Werten fortschreiben.
- **GEO/KI:** vollständig offen, keine Daten.
- **Content-Briefing:** unausgefüllt — Tonalität/Positionierung von LiGaLo nicht final geklärt.
- **Ratgeber-Themen-Sheet:** erste Tab nur Header (Übergreifendes Thema / Keyword / SV); konkrete Themenliste auf nicht-exportierten Tabs (per Name nicht auswertbar).
- **Keyword-/Seiten-Mapping (`Seitenübersicht für Keywords und Metadaten`):** Struktur der fresh-pool.de-Kategorien erfasst; finale Fokus-Keywords je URL inkl. Suchvolumen nicht im exportierten Tab — **kein** SV/Ranking geschätzt.
- **Office-Dateien (.xlsx/.docx):** mehrere Crawl-/Sitemap-/Optimierungs-Dateien liegen als Office-Format vor und sind per CLI **nicht exportierbar** → nur über Namen gewertet, Inhalt nicht gelesen.
- **Status offener Technik-Tasks:** im Tracker viele auf `FALSE` (nicht erledigt) bzw. „liegt bei LiGaLo/netformic" — tatsächlicher heutiger Umsetzungsstand unbekannt.
- **Amazon & SEA:** als Gewerke vorhanden, hier bewusst nicht ausgewertet (außerhalb SEO/GEO-Scope).

## Quellen (ausgewertete Dateien)

Alle aus dem Google-Drive-Kundenordner LiGaLo (Account `ben@eom.de`):

- **LiGaLo - SEO-Audit** (Google Slides, geändert 27.07.2023) — Haupt-Befundquelle Technik/On-Page/CWV.
- **_LiGaLo - Übersicht Technik Themen - November 21** (Google Sheet, 17.11.2021) — Issue-/Task-Tracker mit netformic-Tickets.
- **LiGaLo - Content Briefing** (Google Doc, 03.05.2021) — Tonalitäts-Fragebogen (unausgefüllt).
- **EOM-für-Fresh-Pool-Sichtbarkeit-Marke-06102021** (Google Slides, 06.10.2021) — Marken-/Sichtbarkeitsstrategie.
- **LiGaLo _ Seitenübersicht für Keywords und Metadaten - V2_4LiGaLo** (Google Sheet, 24.01.2022) — Kategorie-/Seiten-Mapping fresh-pool.de.
- **LiGaLo | Checkliste Projektstart, Tools & Zugänge, SEO** (Google Sheet, 25.03.2021) — Eckdaten, Ansprechpartnerin, Leistungsumfang.
- **LiGaLo - fresh-pool.de + garten.com - Ideen für Ratgeber-Themen** (Google Sheet) — Content-Ideen (Detail-Tabs nicht exportiert).
- Ergänzend per Name/Struktur gesichtet: SEO-Audit-, Technik-, KWR-, Infos-Kunde-, Crawls-Unterordner (Screaming-Frog-Crawls, Ahrefs-CSV, GSC-Coverage, XML-Sitemaps, Mitbewerber-Kurzanalyse planet-pool.de/teichking.de).
