---
tags: [kunde, seo]
kunde: "Officeb2b"
stand-Datum: 2026-06-19
---

# Officeb2b

> Wissensdatei auf Basis der ausgewerteten Google-Drive-Materialien (Account `ben@eom.de`). Logik durchgängig: **Befund → Begründung → Maßnahme**. Es wurden ausschließlich vorhandene Dokumente ausgewertet — keine Rankings, Suchvolumina oder Backlink-Zahlen geschätzt. Fehlende/nicht zugängliche Daten sind offen als [[Datenlücken]] benannt.

## Überblick

**Wer:** Officeb2b GmbH — Online-Shop für Büromaterial, Schul-/Bürobedarf und Betriebsausstattung (B2B). Sortiment u. a. Marken wie AVERY Zweckform, DYMO, Faber-Castell, Durable, STAEDTLER, STABILO, Hama, Brother.

**Branche:** E-Commerce / Online-Handel (Büro- & Schulbedarf), B2B.

**Domains (Mehrländer-Setup, aus Audit/Hreflang-Sektion):**
- `officeb2b.de` — Hauptdomain Deutschland (de-DE)
- `officeb2b.ch` / `www.officeb2b.ch` — Schweiz (de-CH)
- `fr.officeb2b.ch` — Schweiz französisch (fr-CH)
- `officeb2b.at` — Österreich (de-AT)
- `officeb2b.com` — internationale Domain (Ziel der `.si`-Weiterleitung)
- `officeb2b.si` — slowenische Altdomain, nur Startseite leitet auf `.com` weiter (Befund 2022)

**Website-Größenordnung:** sehr großer Shop. Im Audit ist von **über 70.000 `/cgi-bin/`-URLs** und **über 30.000 Bildern > 100 KB** die Rede; das System nutzt ein numerisches URL-Schema (12-stellige Kategorie-IDs, je Ebene 3 Stellen, z. B. `/100100202016/`) sowie Produkt-URLs im Muster `marke-artikelnr,p-id.html`.

## Mandat & Gewerke

Aus den Drive-Ordnern und Reportings abgeleitet (Ordnerstruktur des Kunden: `1.0_Orga`, `2.0_Meetings`, `3.0_Reportings`, `4.0_SEO`, `5.0_SEA`, `6.0_Webtracking`):

- **SEO** — technisches Audit (2022), On-Page-/Content-Empfehlungen, Keyword-/Chancen-Analyse, interne Verlinkung. Quelle: Ordner `4.0_SEO` mit Unterordnern `Audit`, `Crawls`, `Pagespeed-Testing`.
- **SEA** — Google-Ads-Betrieb (Shopping + Search, DE und CH), Gebotsstrategie-Umstellung auf Conversion-/Umsatzoptimierung. **SEA ist 2024 das dominierende, laufend reportete Gewerk** (Ordner `5.0_SEA`, Reporting-Texte).
- **Webtracking** — GA4-Setup (zwei Konten: CH/DE und DE), Consent-/Tracking-Prüfung als offener Punkt 2024 (Ordner `6.0_Webtracking`).
- **Reporting** — monatliches Looker-Studio-Dashboard + PDF-Export; Ansprechpartner kundenseitig: Herr Oeppert (Reportings), Frau Boeck / „Caro" (frühe SEO-Abstimmung).

**Einordnung:** Im jüngsten Zeitraum (2024) ist das aktiv reportete Mandat **SEA-lastig**. Substanzielles SEO-Material stammt überwiegend aus **2022 (Audit) und 2017/2018 (frühe Empfehlungen)**. Aktuelle SEO-Reportings/-Rankings liegen im Drive nicht als auswertbare Doku vor → siehe [[Datenlücken]].

## SEO-Status & Befunde

Hauptquelle: **„Officeb2b – SEO-IST-Analyse" (Slides, EOM Agency, 05.05.2022)** sowie **„officeb2b – Notizen zu Audit" (Doc, 01.06.2022)**. Stichtage der Crawls/Daten: 18.02.2022 – 16.03.2022 (Screaming Frog, Sistrix, GSC, Ahrefs).

### Technik — Crawling & Indexierung
- **Befund:** Über 70.000 `/cgi-bin/`-Parameter-URLs stehen auf `noindex` **und** sind gleichzeitig per `robots.txt` vom Crawling ausgeschlossen; nur drei davon im Index. **Begründung:** Widersprüchliche Signale — der gesperrte Crawl kann das `noindex`-Tag nicht lesen. **Maßnahme:** `noindex` auf gesperrten `/cgi-bin/`-URLs entfernen (Crawl-Budget über Disallow steuern). In den Audit-Notizen (06/2022) wurde dies kundenseitig hinterfragt und EOM kam zum Schluss: Google handhabt diese URLs inzwischen korrekt, Aufwand/Nutzen unverhältnismäßig → niedrige Priorität, Content geht vor.
- **Befund:** PDFs sind ebenfalls `noindex` + per `robots.txt` gesperrt; das Disallow greift nur für `.pdf` (Kleinschreibung), nicht für `.PDF`. **Maßnahme:** `noindex` von PDFs entfernen, Disallow um `.PDF` ergänzen.

### Technik — XML-Sitemaps
- **Befund:** Sitemaps (`/sitemap.xml.gz`, `/sitemap1.xml.gz`) enthalten URLs mit `noindex` bzw. Statuscode 404 (GSC-Meldungen: „als noindex gekennzeichnet", „Soft 404", „nicht gefunden (404)"). **Begründung:** Nicht indexierbare URLs gehören nicht in die Sitemap (nur Statuscode 200). **Maßnahme:** Automatisierte Sitemap-Regeln — Ausschluss von `noindex`-URLs, Nicht-200-URLs und fremd-canonicalisierten URLs.

### Technik — Weiterleitungen & Statuscodes (Crawl 02–03/2022)
- **Befund:** 203 URLs mit 301, **135.193 URLs mit 302** (temporär), 1× Statuscode 500 (`/faxform.php`), 354 vom Crawler entdeckte 404-Seiten, 60 Umleitungsfehler in der GSC (u. a. fehlerhafte `review.cgi?ID=…`-Muster aus einer deaktivierten Review-Funktion). **Begründung:** 302 halten URLs im Index und blockieren optimales Ranking der Zielseite; defekte Weiterleitungen/404 verschwenden Crawl-Budget und Linkpower. **Maßnahme:** 302 prüfen → ggf. auf 301 umstellen; 404 thematisch passend per 301 weiterleiten (kein pauschales Weiterleiten auf Startseite), dauerhaft entfernte Inhalte per 410; interne Links auf Nicht-200-Ziele austauschen.
- **Befund:** Keine echte Verzeichnis-/Hierarchie-Struktur — jede Kategorie/Unterkategorie hat eine eigenständige numerische URL, Ebenen bauen nicht aufeinander auf. **Begründung:** Erschwert Themencluster, interne Verlinkung und Performance-Analyse je Bereich. **Maßnahme (EOM-Einschätzung 06/2022):** Strukturkonzept wäre sinnvoll, aber aufwendig (1–2 Wochen, 2 SEOs); kurzfristig Priorität auf Quickwins (Schwellenkeywords Position 11–20) statt Strukturumbau.

### Technik — Canonicals & Hreflang
- **Befund:** Fehlende/nicht indexierbare Canonicals, mind. eine Canonical-Kette, UTM-Tracking-URLs ohne Canonical (GSC: „Duplikat – vom Nutzer nicht als kanonisch festgelegt"). **Maßnahme:** Self-Canonicals als Standard, Ketten direkt auf Ziel-URL auflösen, UTM-URLs canonicalisieren; `noindex` + Canonical nie kombinieren.
- **Befund:** Kein `de`/`x-default`-Catchall für nicht lokalisierte deutschsprachige Nutzer:innen; fehlerhaftes `hreflang="sl-SI"` (Unknown-Tag) auf allen Seiten; `officeb2b.si` nur Startseite weitergeleitet. **Maßnahme:** `de` und `fr` Catchall ergänzen (de-DE bzw. fr.officeb2b.ch), `sl-SI`-Tag entfernen, komplette `.si` per 301 auf `.com`.

### On-Page & Content
- **Befund:** Fehlende/doppelte Title-Tags, Meta-Descriptions und H1 (eigene Audit-Sheets: „seitentitel_fehlende", „meta_description_duplikate/fehlende", „h1 Fehlende + Duplikate + Mehrere"). **Maßnahme:** Automatisierte Meta-Daten-Templates v. a. für Produktseiten. **Konkretes Muster (aus Slides):**
  - Title: `[H1] | officeb2b`
  - Meta-Description: `[Name] günstig bei officeb2b ✔ Von [Marke] ✔ [Ausführung] ✔ [Maße] ▶ Jetzt bestellen!`
  - Title-Länge ca. 58 Zeichen, Meta-Description ca. 150 Zeichen.
- **Befund:** Suchintention der Rankings überwiegend transaktional („Do" — kaufen/bestellen); Long-Tail-Keywords (ab 4 Wörtern) machen ca. 26 % der Rankings aus (Sistrix). **Maßnahme:** Long-Tail- und Informational-Keywords gezielt aufbauen, inhaltsleere Seiten befüllen, Featured/Rich Snippets (FAQ) nutzen.
- **Schwellenkeyword-Potenzial:** Laut Audit-Notizen rankt officeb2b.de mit **über 3.000 Keywords auf Position 11–20** (Sistrix-Filter dokumentiert) — Quickwin-Hebel auf Seite 1.

### Bilder & Performance
- **Befund:** Über 30.000 Bilder > 100 KB; fehlende Alt-Texte (eigenes Sheet „bilder_fehlender_alttext"). **Maßnahme:** Komprimieren, responsive Bildgrößen (320×240 bis 1280×960), Alt-Texte ergänzen.
- **Befund Core Web Vitals (GSC mobil, 03/2022):** keine Probleme gemeldet. Hinweis: Audit nennt noch FID (alte CWV-Metrik) — heute durch INP ersetzt; bei künftiger Bewertung beachten.

### Off-Page / Links
- **Befund:** Sehr wenige Backlinks, viele davon von officeb2b selbst; 18 Broken Backlinks; auffällige Spam-Domains (`.click`-/Listen-Domains). **Maßnahme:** Aktiver Backlink-Aufbau (Qualität vor Quantität), Disavow-File aktualisieren (vorhandene Datei: `…DisavowLinks.txt`, 04.03.2022).
- **Top-verlinkte Landingpages (Sistrix):** Kategorien Stifte/Schreibgeräte, Künstlerbedarf, Gartenartikel, Sticker/Stickeralben, Geschenk-Tüten.

### Frühe On-Page-Empfehlung (2017, Kontext)
- „Caro Officeb2b Empfehlungen Dez.17": Fokus auf **interne Verlinkung von Top-Produkten** mit gutem Ranking + hohem Suchvolumen; Vorschlag eines Moduls **„Beliebte Produkte"** (bis 10 Textlinks mit Produktnamen als Linktext) auf Übersichts-/Kategorieseiten. Chancen-Keywords damals u. a. „avery zweckform" (Pos. 73), „draht bindegeräte" (Pos. 12), „notebook pad" (Pos. 11), „schulbedarf günstig" (Pos. 12). *Werte mit Stand Ende 2017 — heute nicht mehr gültig, nur als Methodik-/Historien-Beleg.*

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten gefunden.** In keinem der ausgewerteten Dokumente (Audit 2022, Reportings 2024, Empfehlungen 2017) gibt es Hinweise auf AI Overviews, ChatGPT/Perplexity-Zitierungen, LLM-Visibility, `llms.txt`, Brand-Radar oder Peec-AI-Tracking. Das Mandat fokussiert klassisches SEO (2022) und SEA (2024). → Falls GEO relevant wird, ist hier ein **Greenfield**: keine Baseline vorhanden, müsste neu aufgesetzt werden.

## Doc-Typen & Aufbau

Im Kundenordner vorgefundene, SEO-relevante Doc-Typen:
- **Audit-Deck (Google Slides):** „SEO-IST-Analyse" — gegliedert in Technik / Content / Links, je Folie Status-Quo + Maßnahme, mit Verlinkung auf Detail-Sheets und Quellenangaben (Sistrix/GSC/Screaming Frog/Ahrefs). Plus „Sichtbarkeit, Rankings und Konkurrenzvergleich" als separates Deck (+ BACKUP-Versionen).
- **Audit-Notizen (Google Doc):** Q&A-Format zur Klärung von Audit-Befunden mit dem Kunden.
- **Befund-Sheets (Google Sheets):** je Issue ein Sheet (404, 302, Canonical-Ketten, fehlende Titles/Metas/H1, Bilder > 100 KB, hreflang, noindex/Soft-404 aus Sitemaps) — Dateinamen mit Datum und Tool im Namen.
- **Crawl-Rohdaten:** Screaming-Frog-Projektdatei (`.seospider`), `broken_links.csv`, `robots.txt`.
- **Monats-Reporting (Google Doc + PDF):** standardisiertes Anschreiben „Hallo Herr Oeppert …" → Summary (KPI-Entwicklung) → „Maßnahmen & Doings" (letzter Monat / geplant) + Link zum Looker-Studio-Dashboard. 2024 durchgehend SEA-fokussiert.

**Benennungskonventionen:** Datei-Präfix `officeb2b` / `officeb2b.de`, Issue + Tool + Datum im Namen (z. B. `officeb2b.de - 404-Fehlerseiten (Screaming Frog) - 18.02.22`); Reportings `2024-<Monat>_Officeb2b_Reporting`.

## Schreibstil-Notizen

- **Anrede:** durchgängig Sie; persönliche Anrede der Ansprechpartner (Herr Oeppert, Frau Boeck).
- **Gendering:** in den Audit-/Slide-Texten 2022 wird konsequent gegendert („Nutzer*innen") — abweichend vom neutraleren EOM-Kundenstil; in Kunden-Copy künftig EOM-Standard prüfen.
- **Title/Meta-Konvention Officeb2b:** Marke + Produkt + USP, Suffix `| officeb2b`, Häkchen-Aufzählung mit ✔ und Call-to-Action `▶ Jetzt bestellen!`.
- **Reporting-Ton:** sachlich, KPI-getrieben (Klicks, Impressionen, CTR, Conversions, Umsatz, KUV/ROAS), Vergleich Vormonat (GA4 ohne Vorjahreswerte), klare „Doings/Geplant"-Struktur.
- **EOM-Haftungsausschluss** am Deck-Ende ist Standardbaustein.

## Offene Punkte / Datenlücken

- **Keine aktuellen SEO-Rankings/Sichtbarkeitsdaten** im Drive auswertbar — jüngstes auswertbares SEO-Deck ist von **2022**. Aktuelle Sistrix-/GSC-Stände nicht als Doku vorhanden.
- **Reportings 2024 sind reine SEA-/Tracking-Reportings** — kein SEO-Performance-Reporting darin enthalten.
- **GEO/KI-Sichtbarkeit:** komplett ohne Datenbasis (siehe oben).
- **Office-Dateien (.docx/.xlsx/.pptx)** im Ordner wurden nicht inhaltlich ausgewertet (nicht per Drive exportierbar) — nur die Google-nativen Formate. Screaming-Frog-`.seospider` und `broken_links.csv` wurden nicht geöffnet (Binär/Rohdaten).
- **Audit-Umsetzungsstand unbekannt:** Ob die 2022er-Maßnahmen (302→301, Sitemap-Regeln, Meta-Templates, Bildkomprimierung, Catchall-hreflang) umgesetzt wurden, geht aus den Dokumenten nicht hervor. Empfehlung: Re-Crawl + Statuscheck vor neuen Maßnahmen.
- **Consent/Tracking 2024:** im Juni-2024-Reporting als noch zu prüfender Punkt markiert (mehrere SEA-Potenziale hängen daran).

## Quellen

Ausgewertete Dateien (Google Drive, Kundenordner Officeb2b, `ben@eom.de`):
- **Officeb2b – SEO-IST-Analyse** (Google Slides, 05.05.2022 / mod. 29.06.2022) — Haupt-Audit, Technik/Content/Links.
- **officeb2b – Notizen zu Audit** (Google Doc, 01.06.2022) — Kunden-Q&A zu Audit-Befunden.
- **2024-6_Officeb2b_Reporting** (Google Doc, Juni 2024) — jüngstes Reporting, SEA-/GA4-KPIs.
- **2024-1_Officeb2b_Reporting** (Google Doc, Jan. 2024) — SEA-Reporting, Trendvergleich.
- **Caro Officeb2b Empfehlungen Dez.17** (Google Doc, 12/2017) — frühe On-Page-/interne-Verlinkungs-Empfehlung (Chancen-Keywords, Modul „Beliebte Produkte").
- Ergänzend gesichtet (nicht volltextlich): Befund-Sheets im Ordner `4.0_SEO/Audit` (404/302/Canonical-Ketten/Titles/Metas/H1/Bilder/hreflang), `robots.txt`, `broken_links.csv`, Disavow-File, Crawls-Ordner.
