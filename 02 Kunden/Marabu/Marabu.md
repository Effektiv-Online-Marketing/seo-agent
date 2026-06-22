---
tags: [kunde, seo]
kunde: "Marabu"
stand: 2026-06-19
quelle: "Google Drive Kundenordner (ben@eom.de), Account-Export ben@eom.de"
analyst: Ben (EOM)
---

# Marabu

> [!warning] Datenlage
> Der Drive-Kundenordner ist überwiegend **historisch** und **social-media-lastig**. Echtes SEO-Material existiert, ist aber alt: ein **technisches Post-Relaunch-Audit von 2018** und eine **Keyword-Recherche von 2021**. Aktuelle SEO-Reportings (Sichtbarkeit, Rankings, organischer Traffic) liegen im Ordner **nicht** vor — die jüngeren Reportings (2019–2024) sind fast ausschließlich Social-Media-KPIs (Instagram, Pinterest, YouTube, TikTok, Facebook). Es wurden **keine Rankings/Suchvolumina/Backlinks geschätzt**; SV-Werte unten stammen 1:1 aus der KWR-Datei.

## Überblick

- **Kunde:** Marabu — Hersteller von Kreativ-/Bastel- und Künstlerfarben (Acrylfarben, Acrylstifte/-marker, Window Color, Textilfarben, Porzellan-/Glasmaler, Kreidefarbe „Chalky-Chic", Aqua Ink u. a.). Endkunden-/B2C-Fokus „Kreativ/DIY".
- **Domain (Kreativ-Bereich):** `marabu-creative.com` mit Sprachverzeichnissen `/de/` und `/en/` (DE/EN). Abgeleitet aus Audit-URLs wie `https://www.marabu-creative.com/de/anleitungen-bastelideen/…`.
- **Frühere Domain:** `marabu.de` bzw. `marabu.com` — beim Relaunch 2018 per 301 auf `marabu-creative.com` umgezogen (siehe Befunde).
- **Branche:** Hersteller / E-Commerce-nahe Marken-Website mit starkem Content-Anteil (Anleitungen & Bastelideen, Presse). Saisonalität wahrscheinlich (Basteln zu Ostern/Weihnachten), in den Docs aber nicht belegt.
- **Hauptthema organisch:** Acrylstifte/Acrylmarker und deren Anwendung (Steine, Holz, Leinwand, Glas).

## Mandat & Gewerke

Aus den Dokumenten erkennbar:
- **Technisches SEO** — Schwerpunkt rund um den **Relaunch 2018** (Redirects, Sitemaps, robots.txt, Canonicals, hreflang, Pagination, Meta-Elemente, Screaming-Frog-Crawls). Belege: Ordner `9.0_Relaunch` (Unterordner Canonicals, hreflang, Meta Elemente, Redirects, Screaming Frog Crawls) + Sheet „MARABU - Post Relaunch".
- **On-Page / Content** — **Keyword-Recherche 2021** für Landingpages/Themenseiten/Anleitungen und YouTube (Fokus: Acrylmarker „YONO"). On-Page-Optimierung der Title-Tags (Sheet „MARABU - Meta Elemente").
- **Reporting** — wiederkehrendes **Quartals-Reporting** über Looker/Data Studio; inhaltlich aber stark **Social-Media-KPI-getrieben** (IG, PI, YT, TT, FB), nicht klassisches SEO-Reporting.
- **Social Media / Content-KPIs** — größter laufender Block (Ordner `0.0_Social Media`, Reportings 2019–2024). SEA-Ordner vorhanden, aber leer/ungeprüft.

> [!note] Einordnung
> Das Mandat hat sich über die Zeit von **technischem SEO (Relaunch)** hin zu **Social-Media-/Content-Reporting** verschoben. Ob aktuell noch aktives Such-SEO läuft, ist aus dem Ordner **nicht** belegbar.

## SEO-Status & Befunde

### Technisches Audit — „MARABU - Post Relaunch" (Sheet, Stand 2018)
Strukturiertes Crawl-/Relaunch-Audit (Frage → Status → Kommentar → To-Do). Konkrete Befunde nach **Befund → Begründung → Maßnahme**:

- **Befund:** Keine XML-Sitemap und keine robots.txt vorhanden; keine GSC-Property angelegt.
  **Begründung:** Crawler-Steuerung und Indexierungs-Monitoring fehlen vollständig.
  **Maßnahme:** XML-Sitemaps je Sprachverzeichnis (`/de/`, `/en/`) erstellen, robots.txt anlegen, GSC-Properties einrichten (geplant: Root + `/de/` + `/en/`).

- **Befund:** **528** gecrawlte 404-URLs, auf die **interne Links** verweisen.
  **Begründung:** Interne Verlinkung führt ins Leere → Crawl-Budget-Verschwendung, schlechte UX.
  **Maßnahme:** Betroffene Seiten auswerten, interne Links korrigieren bzw. Weiterleitungsziele definieren (Aufwand laut Sheet ~5–6 h).

- **Befund:** **4.628** Canonical-Tags verweisen auf eine andere Seite; fehlerhafte Canonical- und `rel="next"`-Auszeichnungen.
  **Begründung:** Fehlsteuerung der Indexierung, v. a. bei Produkt-URLs.
  **Maßnahme:** Canonical-Logik korrigieren (Aufwand ~4 h).

- **Befund:** URLs **mit und ohne Trailingslash** erreichbar; aktuelle Canonical-Regel weist die Trailingslash-Variante als Original aus.
  **Begründung:** Duplicate Content / inkonsistente URL-Muster.
  **Maßnahme:** Trailingslash-Handling vereinheitlichen.

- **Befund hreflang:** **3.974×** fehlerhafte Rückverlinkungen (Trailingslash/Canonical), **44×** leeres `hreflang=""`, **215×** fehlender `x-default`.
  **Begründung:** DE/EN-Sprachzuordnung für Google unzuverlässig.
  **Maßnahme:** hreflang-Auszeichnung korrigieren, x-default ergänzen.

- **Befund Pagination:** Viele Produkte mit **unnötigen `rel="next"`**-Auszeichnungen, teils fehlerhaft.
  **Maßnahme:** Paginierungs-Markup bereinigen.

- **Befund Meta/Headings:** Title-Tags >65 Zeichen (**36 URLs**), **duplizierte Title-Tags** (v. a. Produkt-URLs), **duplizierte H1** (domainweit), **fehlende H1** (paginierte Seiten + einige Produkt-Archive), **mehrere H1** auf Startseite DE & EN.
  **Maßnahme:** Title-/Heading-Struktur überarbeiten (mehrere Einzel-To-Dos mit Aufwand 0,5–3 h).

- **Positiv (OK laut Audit):** 301-Redirects alt→neu für `/de/` & `/en/` vorhanden und grundsätzlich erreichbar; keine JS-/Meta-Refresh-Redirects; keine Redirect-Ketten; keine Time-Outs; Ladezeit <5 s; Content nicht durch JS/iframe/Flash blockiert.
  **Einschränkung:** Ein Redirect-Ziel fehlerhaft (Beispiel im Sheet: alte Anleitungs-URL leitet faktisch auf die Startseite statt aufs definierte Ziel) → manuelle Nachkorrektur nötig.

### On-Page — „MARABU - Meta Elemente" (Sheet, 2018)
- URL-Liste mit Empfehlung **„Title kürzen"** und gemessener Title-Länge. Betroffen v. a. `/de/anleitungen-bastelideen/…` und `/de/service/presse/…` (Längen ~66–125 Zeichen).
- **Title-Konvention erkennbar:** `[Seitentitel] - Marabu Kreativ` (Suffix „- Marabu Kreativ" durchgängig).

### Keyword-Recherche — „Marabu - KWR für YONO-Marker (LPs + Youtube)" (Doc, 2021)
- Zielprodukt **YONO Acrylmarker**; Recherche getrennt für **Landingpages** (Produkt-/Themenseite/Anleitung) und **YouTube**.
- Cluster: *Allgemein, Kreative Ideen/Anleitungen, Eigenschaften, Oberflächen, Fragen* — passt zu Suchintention/Funnel.
- SV-Werte **aus der Datei** (nicht von uns geschätzt), Auswahl:
  - `acryl stift` SV 1.600, `acrylmarker` SV 1.300, `acrylmalstifte` SV 480 (allgemein).
  - `acrylstifte für steine` SV 2.900 — stärkster Anwendungs-/Anleitungs-Begriff; weiter `acrylstifte zum steine bemalen` 390, `…wasserfest für steine` 320.
  - Eigenschaft: `acrylstifte wasserfest` SV 880.
  - YouTube: auffällig hoher Wert `acrylstift` SV 21.000 (Datei-Angabe; Plausibilität vor Nutzung prüfen), `acrylmarker` 1.800.
  - Fragen-Cluster (FAQ/GEO-tauglich): „welche acrylstifte für steine", „wie acrylstifte lagern", „welche acrylstifte sind die besten" u. a.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im Kundenordner gibt es keinerlei Material zu AI Overviews, ChatGPT/Perplexity/Copilot, LLM-Zitierfähigkeit, `llms.txt` oder KI-Traffic. Der Fragen-Cluster aus der KWR 2021 („welche acrylstifte für steine", „wie acrylstifte lagern", „welche acrylstifte sind die besten") ist inhaltlich ein guter Ausgangspunkt für künftige answer-first/FAQ-Optimierung Richtung AI Overviews, wurde in den Docs aber nicht als GEO-Maßnahme behandelt.

## Doc-Typen & Aufbau

- **Technisches Audit-Sheet** (Google Sheet, „Post Relaunch"): Spalten `Aufwandseinschätzung EOM | Thema | Tasks | Status | Kommentar | To-Do's`. Themenblöcke (Redirects, Crawlbarkeit, Duplikate, hreflang, Meta-Elemente, Ladezeit) mit Frage→Status-Logik („Ja → OK" / „NEIN → OK" / konkreter Fehlerbefund) und verlinkten Detail-Sheets (404-Liste, Sitemap-Liste). Aufwände in Stunden pro Maßnahme.
- **On-Page-Sheet** („Meta Elemente"): `Empfehlung | URL | Title | Title Länge` — reine Umsetzungstabelle.
- **Keyword-Doc** (Google Doc, KWR YONO): Klartext, gegliedert nach Funnel-Clustern, je Keyword `Begriff SV: <Zahl>`; getrennte Blöcke für LP vs. YouTube.
- **Reporting** (Google Slides + Looker/Data Studio): Quartals-Slides je Kanal (IG, PI, YT, FB, TT), KPI-Übersicht, Top-Posts, Milestones/Doings. Plus KPI-Sheets „Marabu & Wettbewerber KPIs (IG, PI, YT)" je Jahr (2022–2024) und Plattform-KPI-Sheets.
- **Orga/Onboarding** (Sheet „Checkliste Projektstart") — leere Vorlage, kein ausgefüllter Kundenkontext.

## Schreibstil-Notizen

- **Title/Meta-Konvention:** `[Seitentitel] - Marabu Kreativ` (Brand-Suffix „Marabu Kreativ"). Ziel laut Audit: ≤65 Zeichen, keine Dupletten (besonders Produkt-URLs).
- **Tonalität der Marken-Inhalte:** kreativ, emotional, Du-Ansprache in Content-Titeln (z. B. „Let's go shopping!", „Eis, Eis, Baby!"). Hinweis: Das ist **Marabus** Endkunden-Tonalität (B2C/DIY) — nicht zu verwechseln mit der EOM-internen Sie-Anrede in Analyse-/Kunden-Copy.
- **Reporting-Sprache (Data-Studio-Feedback 2021):** Aufwand gering halten, Quartalsrhythmus, Milestones/Doings fortlaufend dokumentieren, Analytics quartalsweise; klare Kanaltrennung (Organic vs. Paid).

## Offene Punkte / Datenlücken

- **Keine aktuellen Such-SEO-Daten:** keine Sichtbarkeits-, Ranking- oder organischen Traffic-Reports im Ordner. Aktueller SEO-Status der Domain unbekannt → bei Bedarf frisch via Sistrix/GSC/Ahrefs erheben.
- **Technische Befunde sind von 2018** (Relaunch). Unklar, welche To-Dos umgesetzt wurden → Re-Crawl/technischer Re-Check nötig, bevor Aussagen getroffen werden.
- **KWR ist von 2021** und auf YONO-Marker beschränkt; SV-Werte sind Datei-Stände, kein aktuelles Volumen. Der YouTube-Wert `acrylstift` SV 21.000 wirkt hoch und sollte vor Nutzung verifiziert werden.
- **GEO/KI-Sichtbarkeit:** komplett unbearbeitet (s. o.).
- **SEA-Ordner** (`6.0_SEA`) nicht ausgewertet; Office-Dateien (.xlsx/.docx) im Ordner nicht exportierbar.
- **Onboarding-Checkliste leer** → kein dokumentierter Ansprechpartner-/Wettbewerber-/Saisonalitäts-Kontext.

## Quellen (ausgewertete Drive-Dateien)

- **MARABU - Post Relaunch** — Google Sheet (technisches Relaunch-Audit, 2018) — *Ordner 5.0_SEO-CRO*
- **Marabu - KWR für YONO-Marker (LPs + Youtube)** — Google Doc (Keyword-Recherche, 2021) — *Ordner 5.0_SEO-CRO*
- **MARABU - Meta Elemente** — Google Sheet (Title-Optimierung, 2018) — *Ordner 9.0_Relaunch / Meta Elemente*
- **Marabu Data Studio Reporting Feedback** — Google Doc (Reporting-Konzept/Feedback, 2021) — *Ordner 3.0_Reportings*
- **MARABU | Checkliste Projektstart, Tools & Zugänge** — Google Sheet (leere Onboarding-Vorlage) — *Kundenordner-Root*
- **9.0_Relaunch** — Ordnerstruktur gesichtet (Canonicals, hreflang, Redirects, Meta Elemente, OffPage, Screaming Frog Crawls, Produkte) — Beleg für techn. SEO-Scope
- **3.0_Reportings (2019–2024)** — Ordner gesichtet: Inhalte überwiegend Social-Media-KPI-Sheets/-Slides (IG, PI, YT, TT, FB), kein Such-SEO-Reporting
