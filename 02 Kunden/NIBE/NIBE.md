---
tags: [kunde]
status: aktiv
---

# NIBE — SEO Knowledge Base

## Eckdaten
- **Kunde / Domain:** NIBE Systemtechnik GmbH — `www.nibe.eu/de-de` (Wärmepumpen, Sitz Celle)
- **Scope:** nur `/de-de`, nur DE-Daten. Andere Länderpfade ausschließen.
- **Tools:** Sistrix (Projekt `ET4v9vh9fyPvZCwT`, inkl. Optimizer), GSC, GA4, Looker Studio, Wochen-Crawl über `seo@eom.de`
- **Ziel:** Leadgenerierung („Wärmepumpen anfragen")
- **Mandatstyp:** kollaborativ, Content-Review direkt im Google Doc (Grün = neuer Vorschlag, Gelb = Bestand anpassen)
- **Ausgeschlossen:** Arbeitsordner `…1wIAbiC48F…` (Monoblock-Recherche, Backlink-Defekt-Analysen) — bewusst NICHT verwenden.

## Sistrix-Baseline (15.06.2026, exakter Pfad `https://www.nibe.eu/de-de`)
- Sichtbarkeitsindex: **0,0733**
- Ranking-Keywords (exakter Pfad): **119**, davon 9 auf Seite 1
- Top-Rankings fast nur Brand/Herkunft: „nibe", „nibe heizung", „nibe systemtechnik gmbh", „wärmepumpe schweden", „schwedische wärmepumpe"
- **Mess-Hinweis:** Pfad = nur Startseiten-Cluster; Verzeichnis `/de-de/` ist viel größer. Offene Frage: misst man `/de-de` oder `/de-de/`? -> bei jeder Auswertung klarstellen.
- Sistrix-Auto-Wettbewerber: kfw.de, viessmann.de, heizung.de, bosch-homecomfort.com, haustechnikdialog.de, buderus.de, schwaebisch-hall.de

## Wettbewerber-Benchmark (Reporting-Standard, fix)
- Groß: Vaillant, Viessmann, Stiebel-Eltron
- Klein: NOVELAN, alpha innotec, Dimplex, WOLF, WATERKOTTE

## Technisches Monitoring (Wochen-Crawl `seo@eom.de`)
- Umfang ~1.500 URLs; **Health-Score-Ziel >= 90** (Nov/Dez 25: 31–38 -> ab Jan 26: 91–93)
- Dauerthemen: Missing Alt-Text (~1.300), Orphan Pages (~80–99), 5XX in Sitemap, X-/Twitter-Cards (~1.235), Slow Pages
- Backlinks via Sistrix (DataForSEO nicht freigeschaltet, Fehler 40204)
- **Redirect-Regel:** defekte Ziele per 301 auf thematisch passende Live-Seite — **nie** auf Startseite (= Soft-404)

## URL-/Indexierungs-Konventionen
- Struktur: `/de-de/wissen/…`, `/de-de/produkte/…`, `/de-de/beratung-kauf/…`, `/de-de/partner…`, `/de-de/ueber-nibe/…`
- noindex: AGB, Beratung-Kauf-Übersicht, Heizungstausch-Schritte
- Partner-Filter-URLs (`?partner=…`) = canonicalised
- Title-Schema: „… | NIBE"
- **Relaunch 2026 läuft** -> lückenlose 301-Redirects sichern; alte Umlaut-/Query-Slugs sind 404-Quellen
- hreflang prüfen (nibe.at / nibe.eu/ch ranken teils in DE)

## Content-/On-Page-Konventionen
- Deutsch, Sie-Anrede, fachlich; CRO-Kritik: „zu technisch, zu wenig Nutzen/Emotion/USP"
- Title ~57 Z., Schema „… | NIBE"
- Produktanker: S2125, VVM-Serie, S2060
- Review im Google Doc: Grün = neuer Vorschlag, Gelb = Bestand anpassen; Produktangaben vor Go-live durch NIBE prüfen
- CRO: Lead-Formular above the fold, Mobile-First (~45 % Mobile), CTA nicht ans Seitenende

## Strategische Prioritäten
- Organic-Risiko: ~53 % Traffic-Anteil, rückläufig; nur 29 % Anteil an Schlüsselereignissen
- GEO/AI-Visibility ausbauen (aktuell gering)
- Saisonalität (Winterloch) in Roadmap berücksichtigen
- Content-Lücke: starke Brand-/Produkt-Rankings, generische Wärmepumpen-Themen unbesetzt

## Cadence
| Takt | Output |
|---|---|
| Wöchentlich | Technisches Crawl-Audit; monday-Routine „NIBE – Aufgabenplanung prüfen" |
| Monatlich | Keyword- + Backlink-Report; Monatsreporting-Dokument; Looker-Dashboard |
| Jährlich/anlassbez. | Strategie-Scan & Quick-Check |

## Offene Punkte / Lücken
- `/de-de` vs. `/de-de/`-Messlogik ungeklärt
- mehrere Looker-Module „in Arbeit"
- monday-Boards nicht direkt durchsuchbar -> Task-Status unverifiziert

## Verwandt
[[NIBE — Schreibstil]] · [[NIBE — Doc-Aufbau]] · [[SEO-Methodik]] · [[Reporting-Standards]] · [[Schreibstil]] · [[VHV]]
