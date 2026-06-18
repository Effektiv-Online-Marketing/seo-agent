---
tags: [kunde]
status: aktiv
---

# VHV — SEO Knowledge Base

## Eckdaten
- **Kunde / Domain:** VHV Versicherungen — `www.vhv.de` (Versicherer, Hannover; Firmen + Privat)
- **Schwester-Marke im Mandat:** `www.hannoversche.de` (Backlink-Monitoring) -> VHV-Gruppe
- **Mandatstyp:** monatlicher SEO-Retainer mit festem Stundenbudget (Toggl „vhv.de - SEO - <Monat> 2026"). Aufwand gedeckelt -> Priorisierung zählt.
- **Tools:** Sistrix, GSC, Toggl (Zeit), Wochen-Crawl `seo@eom.de`, Reporting als „Maßnahmen & Doings"-Mail
- **Sammel-Postfach:** `vhv@eom.de`

## Sistrix-Baseline `vhv.de` (08.06.2026)
- Sichtbarkeitsindex: **3,64**
- Organische Keywords: **29.490** (Seite 1: 680, Seite 2: 717)
- Backlinks: **32.770** von **2.814** Domains; Monats-Dynamik +10.170 / −6.709
- Top-Wettbewerber (Keyword-Overlap): ADAC 71,3 % · HUK 66,8 % · Check24 53,5 % · Allianz 43,4 % · Verivox 36,8 % · DEVK 30,7 % · Finanztip 22,8 % · CosmosDirekt 22,3 % · R+V 21,2 % · AXA 18,6 %
- **Kunden-KPI:** Gesamt-Sichtbarkeitsindex; bei Rückgang aktiv Einordnung/Erklärung liefern

## Arbeitsmodell (wichtigster Unterschied zu NIBE)
EOM hat **keinen direkten CMS-Schreibzugriff** — Output = übergabefertige Empfehlung, Umsetzung kundenseitig:
- CMS: Magnolia (`author.stage.k8s.vhv.de`), Stage `https://stage.k8s.vhv.de/`
- Umsetzungs-Dienstleister: **Neoskop**
- Zugang: feste IP `72.62.49.215` (Whitelisting) + Team-User `vhv@eom.de`
- Ablauf: EOM-Empfehlung (PDF/DOCX) -> interne QS -> an VHV -> Neoskop -> Stage -> Go-live

## Content-Deliverables (Standardformat)
Jede Empfehlung enthält: Keywords (mit Wettbewerbs-Intent-Hinweis), Meta-Titel & -Description, semantische Begriffe (Top-10-Scrape), interne Verlinkungen (mit fertigen Texten). Lieferung als **PDF + DOCX**, zusätzlich auf Stage. Pflicht-QS vor Versand.
Belegte Objekte (Mai–Jun 2026): Produktseiten Unfall-, Wohnwagen-, Wohnmobil-Versicherung; Ratgeber „Wohnwagen Führerschein", „Wohnwagen TÜV/Zulassung".

## Technisches Monitoring (Wochen-Crawl `seo@eom.de`)
- Umfang ~1.020–1.040 URLs; **Health Score ~71–72** (großer Hebel)
- Issues: Missing Alt-Text (~148), Duplicate without canonical (~7), Non-canonical in Sitemap (~24), 3XX in Sitemap (~6), Slow Pages (~8)
- Monatlicher Backlink-Report: vhv.de + hannoversche.de
- Spezial: „Druckstücke"-404s (Print-Links) -> Seite + Ankertext an VHV melden; Legacy-/Leerseiten weiterleiten
- Rechner-/Parameter-URLs (`…/tarifrechner/?ivmnr=…`): x-robots noindex + Canonical (Logik prüfen, nicht „reparieren")

## Strukturierte Daten & GEO/AI
- Schema-Markup aktiv: GSC-Fehler in Produktdaten (u. a. fehlende Bewertungen); Produktseiten oft mit 0 Schema-Blöcken
- llms.txt-Empfehlung erstellt (kuratierte Schlüssel-URLs)

## Intent-/Strategie-Logik (Beispiel Kautionsversicherung)
- Produkte teils B2B/Firmen-only, generische Keywords aber Misch-Intent (~60 % Privat-Mietkaution, die VHV nicht anbietet)
- Regel: generisches Head-KW auf Gewerbe-Intent schärfen + Schema; reine Gewerbe-KW haben kaum Volumen -> kein Volumen erfinden
- VHV oft nicht in Top 50 bei Money-KW, Brand-KW Pos. 1 -> Brand halten, generische Themen über Ratgeber/Produkt-Content

## Cadence
| Takt | Output |
|---|---|
| Wöchentlich | Technisches Crawl-Audit; 404-/Druckstück-Meldungen + Legacy-Redirects |
| ~14-tägig | Jour Fixe „JF SEO: VHV/EOM" (MS Teams) |
| Monatlich | Reporting „Maßnahmen & Doings"; Backlink-Report (vhv.de + hannoversche.de) |
| Laufend | Toggl-Zeiterfassung gegen Monatsbudget (50/75/100 %-Alerts) |

## Offene Punkte / Lücken
- Kein strukturiertes Dashboard belegt (Reporting = „Maßnahmen & Doings"-Mail)

## Verwandt
[[SEO-Methodik]] · [[Reporting-Standards]] · [[Schreibstil]] · [[NIBE]]
