---
tags: [kunde, seo]
kunde: "VHV Versicherung"
stand-Datum: 2026-06-19
---

# VHV Versicherung

> Wissensdatei für das SEO-/GEO-Mandat. Erstellt aus dem Google-Drive-Kundenordner (Account `ben@eom.de`). Analyse-Logik durchgehend: Befund → Begründung → Maßnahme. Nichts geschätzt — fehlende/nicht zugängliche Daten werden offen benannt.

## Überblick

- **Wer:** VHV Allgemeine Versicherung AG, Sitz Hannover. Laut [[llms.txt]]-Entwurf "führender Versicherer für die Bauwirtschaft und einer der größten deutschen Auto- und Haftpflichtversicherer". VHV = "Vereinigte Hannoversche Versicherung". Teil der VHV-Gruppe; Schwester­marke **Hannoversche** (Leben), die in den GEO-/Methodik-Docs als Referenz herangezogen wird.
- **Branche:** Versicherung. Zwei Geschäftsfelder: **Privatkunden** (Kfz, Haftpflicht, Hausrat, Wohngebäude, Unfall, Leben, Tier) und **Firmenkunden** (Schwerpunkt Bauwirtschaft: Bau-, Haftpflicht-, Kautions-, Cyber-, Energie-, Transportversicherung).
- **Domain / Sprache:** `vhv.de`, einsprachig **Deutsch** (`language: de`), Zielmarkt Deutschland. SEO-Traffic kommt laut Strategie-Doc fast ausschließlich aus DE (positiv gewertet).
- **Mitbewerber (im Drive benannt):** Allianz, HUK, DA Direkt, HanseMerkur, Barmenia Gothaer.

## Mandat & Gewerke

Aus der Ordnerstruktur (`04.1_SEO`, `04.2_GEO`, `07_Content`, `03_Reporting`, `06_Tracking`) und den Deliverables erkennbares Leistungsspektrum:

- **Technical SEO:** Crawls (Screaming-Frog-Exporte), Broken Links / defekte Bilder, Indexierungsprobleme, PDF-Inventar, Kannibalisierungs-Checks, Tarifrechner-Relaunch-Konzept.
- **On-Page / Content:** Ratgeber-Skalierung (Kfz-Ratgeber ab 09/2025, Wohnwagenanhänger-Ratgeber), Produktseiten-Refresh, Content-Briefings nach festem Template, Keyword-Recherchen.
- **Off-Page:** eigener Unterordner `03_OffPage`; im Strategie-Doc mit Mediabudget für Backlinks (19.000–47.500 €) eingeplant.
- **GEO / KI-Sichtbarkeit:** eigener Ordner `04.2_GEO` — OH-SO-Analyse-Ableitungen, RAIDAR-LLM-Analysen, `llms.txt`, strukturierte Daten (Organization, Product).
- **Reporting / Tracking:** monatliches SEO-Reporting (2024 & 2025), "geschärftes Monitoring ab Juni 2025", GA4-Lead-Events, GSC.
- **Strategie:** großes Skalierungs-Konzept "Private Direktvermarktung" mit Traffic-/Conversion-Forecast und Kostenschätzung (ab März 2026).

## Operatives Arbeitsmodell, Tools & Cadence (Retainer)

> Übernommen aus der früheren VHV-Methodik-Notiz (Stand 06/2026), ergänzt die Drive-Befunde um das operative Modell.

- **Mandatstyp:** monatlicher SEO-**Retainer mit festem Stundenbudget** (Toggl „vhv.de - SEO - <Monat> 2026"). Aufwand gedeckelt → **Priorisierung zählt** (50/75/100 %-Alerts).
- **Arbeitsmodell (wichtigster Unterschied zu NIBE):** EOM hat **keinen direkten CMS-Schreibzugriff** — Output = übergabefertige Empfehlung (PDF + DOCX), Umsetzung kundenseitig.
  - CMS: **Magnolia** (`author.stage.k8s.vhv.de`), Stage `https://stage.k8s.vhv.de/`
  - Umsetzungs-Dienstleister: **Neoskop**
  - Zugang: feste IP `72.62.49.215` (Whitelisting) + Team-User `vhv@eom.de`
  - Ablauf: EOM-Empfehlung → interne QS → VHV → Neoskop → Stage → Go-live
- **Sammel-Postfach:** `vhv@eom.de` · **Schwester-Marke im Mandat:** `hannoversche.de` (Backlink-Monitoring) → siehe [[Hannoversche]]
- **Tools:** Sistrix, GSC, Toggl (Zeit), Wochen-Crawl `seo@eom.de`, Reporting als „Maßnahmen & Doings"-Mail.
- **Sistrix-Baseline `vhv.de` (08.06.2026):** SI **3,64**; organische Keywords **29.490** (S1: 680, S2: 717); Backlinks **32.770** von **2.814** Domains. Top-Wettbewerber (KW-Overlap): ADAC 71,3 % · HUK 66,8 % · Check24 53,5 % · Allianz 43,4 % · Verivox 36,8 %. *(Hinweis: Strategie-Doc nennt SI 4,313 aus anderem Erhebungsdatum/Quelle — beide mit Datum führen.)*
- **Technisches Monitoring (Wochen-Crawl `seo@eom.de`):** ~1.020–1.040 URLs, **Health Score ~71–72** (großer Hebel). Issues: Missing Alt-Text (~148), Duplicate without canonical (~7), Non-canonical in Sitemap (~24), 3XX in Sitemap (~6), Slow Pages (~8). Spezial: **„Druckstücke"-404s** (Print-Links) → Seite + Ankertext melden; Legacy-/Leerseiten weiterleiten. Rechner-/Parameter-URLs (`…/tarifrechner/?ivmnr=…`): x-robots noindex + Canonical (Logik prüfen, nicht „reparieren").

### Cadence
| Takt | Output |
|---|---|
| Wöchentlich | Technisches Crawl-Audit; 404-/Druckstück-Meldungen + Legacy-Redirects |
| ~14-tägig | Jour Fixe „JF SEO: VHV/EOM" (MS Teams) |
| Monatlich | Reporting „Maßnahmen & Doings"; Backlink-Report (vhv.de + hannoversche.de) |
| Laufend | Toggl-Zeiterfassung gegen Monatsbudget (50/75/100 %-Alerts) |

## SEO-Status & Befunde

**Quelle für 1–6: `VHV | SEO-Skalierung: Private Direktvermarktung vhv.de` (Doc, Stand 04/2026), Datenbasis Sistrix DE / GSC / GA4.**

1. **Befund:** Organic ist in Q1 2026 der wichtigste Traffic-Kanal, ca. **120.000 SEO-Klicks/Monat**, positiver 12-Monats-Trend. **ABER über 90 % der organischen Klicks sind branded** ("vhv versicherung", "vhv").
   **Begründung:** Der Trend basiert primär auf gestiegenen Markensuchen, nicht auf Non-Brand-/Info-Traffic. Über die letzten 2 Jahre ist viel TOFU-Traffic durch AI Overviews / ChatGPT weggefallen.
   **Maßnahme:** Non-Brand-Wachstum über Ratgeber- und neue Produktseiten aufbauen (siehe Skalierungs-Stellschrauben).

2. **Befund:** Drei Skalierungs-Stellschrauben definiert — (a) BOFU-Rankings bestehender Produktseiten verbessern (mehr Content-Elemente), (b) **neue Versicherungssparten** mit Suchvolumen, die VHV noch nicht anbietet (z. B. Zahnzusatz, SV ~100.000; alle Mitbewerber außer VHV bieten sie an), (c) **Content-Gap** Ratgeber (Filter "auto" ~5.000 Keywords).
   **Maßnahme:** Portfolio-Erweiterung + ~60 neue Ratgeber; Themen händisch bewerten.

3. **Befund (Wettbewerb):** VHV mit ca. **90.000 monatl. Klicks Schlusslicht**; Allianz fast 10×. VHV nur ca. **500 indexierte Seiten** (Website kleiner). Markenbekanntheit am geringsten (~12.000 monatl. Suchen).
   **Begründung:** Kleineres Seiten-/Portfolio-Volumen → weniger abgedeckte Keywords.

4. **Befund (Sistrix-Vergleich VHV vs. HanseMerkur):** SI **4,313 vs. 9,707**; Keywords DE 77.912 vs. 131.817; Top-10 11.405 vs. 32.956; rankende URLs 1.088 vs. 1.638; verweisende Domains 2.967 vs. 4.662.
   *Hinweis: Im Doc tauchen sowohl "~500 indexierte Seiten" (Ahrefs-Logik) als auch "1.088 rankende URLs" (Sistrix) auf — unterschiedliche Metriken/Quellen.*

5. **Befund:** Viele relevante Versicherungs-Rankings stehen auf **Seite 2+** und ziehen keinen Traffic. Zahlreiche Ratgeber-Themen werden noch nicht bespielt.
   **Maßnahme:** Schwellenkeywords heben, Content-Gap schließen.

6. **Forecast (Strategie-Doc):** Bei Position 1–3 für ausgewählte Themen ~**59.600 zusätzl. Klicks/Monat / ~596 Conv./Monat** (angenommene CR 1 %); ~60 neue Ratgeber ~8.237 Klicks/Monat. EOM-Kosten gesamt ~81.660 €, plus Backlink-Mediabudget 19.000–47.500 € → ~100.660–129.160 € (exkl. VHV intern). **Conversion-Annahmen explizit "mit der heißen Nadel gestrickt".**

7. **Befund (Technik – Indexierung):** URL `vhv.de/service/digitale-schadenkarte` wird **nicht indexiert** (Doc 11/2025).
   **Begründung / Hypothesen:** zu wenige Inlinks (3); mögliche Canonical-Erkennung der Alternativ-URL `…/unsere-digitale-schadenkarte`; zu wenig Unique Content / Relevanzsignal.
   **Maßnahme:** interne Verlinkung erhöhen, Content differenzieren. **Blocker:** fehlende GSC-Berechtigung ("Fehlerbehebung überprüfen" / uneingeschränkter Zugriff für erneuten Indexierungsantrag).

8. **Weitere Technik-Themen aus Dateinamen (nicht im Detail exportiert):** Kfz-Autotarifrechner-Rankingveränderungen, Auto-Kannibalisierung (CSV 03/2023), Broken Links & defekte Bilder (01/2025), PDF-Inventar/PDFs mit meisten GSC-Klicks, Verhältnis indexiert/nicht-indexiert + 404-Seiten (Kapitel 4 des Strategie-Docs).

## GEO / KI-Sichtbarkeit

GEO ist ein **aktiv bearbeitetes Gewerk** (eigener Ordner, Material 02–05/2026).

- **Befund (AI Citations, Sistrix DE, Strategie-Doc):** VHV ist **Schlusslicht**. Google AI Mode 977 / AI Overviews 392 / ChatGPT 9 — vs. Allianz 14.261 / 6.486 / 242; HUK 7.176 / 2.935 / 112; DA Direkt 6.724 / 3.061 / 41.
  **Begründung:** geringere Markensichtbarkeit + geringerer Traffic.
- **OH-SO-Analyse → GEO-Maßnahmen** (`VHV | GEO-Maßnahmen aus OH-SO Analyse`, Doc + Sheet, 03/2026): Maßnahmenkatalog mit Status/Zuständigkeit (EOM / VHV / NEOSKOP). Offene Kernpunkte:
  - **Answer-first-Blöcke** ("Auf einen Blick"-Bulletpoints) am Anfang jedes Ratgebers.
  - **FAQs auf Ratgebern** + **FAQ-Schema** (strukturierte Daten aktuell noch **nicht** eingebunden).
  - **Strukturierte Daten / Schema** allgemein fehlen noch (Organization & Product in Arbeit, `Product` mit Befund "lowPrice missing").
  - **Vergleiche / Wettbewerber-Kontext** noch nicht auf Produkt-/Ratgeberseiten.
  - **E-E-A-T-Substanz:** Beispiel-Modul nötig (Referenz Allianz), Testimonials/Cases, Redaktionsteam-Element, Testsiegel als **Text statt nur Bild** (Pop-up-Idee via NEOSKOP).
  - **Klare Kernbotschaft je Produkt** (z. B. "leistungsstark") konsequent in Ratgebern.
  - Tariftabellen besser als **HTML-Listen** auszeichnen (extraktionsfreundlich).
- **OH-SO-zusätzliche Themen (Backlog):** llms.txt, Verknüpfung strukturierter Daten mit Entitäten (**Wikipedia/Wikidata**), Backlinks, Grounding Pages, Medienformate (Podcast/Video/Studien), Aktualität bestehender Ratgeber, Entitäten-Coverage-Analyse.
- **`llms.txt`-Entwurf** (Doc, Stand 2026-05-13): vollständige Sitemap-artige Liste aller Produkt-, Tarifrechner-, Service-, Ratgeber- und Über-uns-URLs, plus Markenbeschreibung. Hinweis im Doc: bei URL-Änderungen (Kautionsversicherung) muss llms.txt nachgezogen werden.
- **RAIDAR-LLM-Analysen** (PDFs, 02/2026): Privat Kfz, Hausrat, Haftpflicht — je eigene Auswertung (Inhalt nicht textlich exportiert, da PDF).

## Doc-Typen & Aufbau

- **Strategie-Docs (Google Doc):** Kapitelstruktur mit Inhaltsverzeichnis (Status Quo → Skalierung → Mitbewerber je Wettbewerber → Technik → Empfehlung/Forecast). Argumentation datengetrieben mit Sistrix/GSC/GA4-Screenshots (im Text-Export als Platzhalter sichtbar) und Forecast-Tabellen inkl. Kostenschätzung.
- **Maßnahmen-Mappings (Doc + Sheet):** zweispaltig "Maßnahme OH-SO" ↔ "Kommentar/Stand EOM"; Sheet zusätzlich mit **Zuständigkeit** und **Status** (offen / zur Info). Hannoversche-Maßnahmen werden auf VHV gemappt.
- **Content-Briefing (`VHV | Template | Content-Briefing`):** fester 6-Block-Aufbau — (1) Allgemeines (Länge ~800–1000 Wörter, Tonalität, Sie-Ansprache, Zielgruppe), (2) Struktur/Seitenelemente + CTA, (3) Inhalte & Gliederung (H1/H2 inkl. "Das Wichtigste in Kürze"), (3.3) WDF*IDF-Begriffe, (4) Keywords (Haupt/Neben/PAA), (5) Einbindungsregeln, (6) **eigener GEO-Block**.
- **Keyword-Recherchen (Sheets):** KFZ-Bereich (Sistrix), "Auto only" für individuellen SI, Mitbewerber-basiert (HanseMerkur), Ratgeber Wohnwagenanhänger (mit/ohne VHV-Freigabe). Extern-/Freigabe-Versionen werden parallel gepflegt.
- **Technik (Sheets/CSV):** Crawl-Exporte (`200_html-all`), Kannibalisierungs-CSV, PDF-Übersichten, Broken-Links-Shortcut.
- **GEO:** PDFs (RAIDAR, OH-SO-Zusammenfassung) + Docs (Maßnahmen, llms.txt, strukturierte Daten).
- **Reporting:** `VHV | SEO-Reporting | 2024 & 2025.xlsx` (Office-Format — **nicht exportierbar**, nur per Name bewertbar).

## Schreibstil-Notizen

- **Sie-Anrede** durchgängig (im Content-Briefing fix vorgegeben: "Direkt 'Sie'").
- **Tonalität:** professionell und zugleich zugänglich, "einfach erklärt", Fachbegriffe in einfacher Sprache; informativ und hilfreich, klar und präzise.
- **On-Page-Konventionen:** klare H1/H2/H3-Hierarchie, "Das Wichtigste in Kürze"-Block oben, Bullet Points, Fettungen für Kernbegriffe, native interne Produkt-CTAs (nicht als Überschrift), externe Verlinkung zu vertrauenswürdigen Quellen.
- **GEO-Schreibmuster (aus Briefing):** 1 Absatz = 1 Aussage; Informationsdichte je Absatz = Kernaussage → Erklärung → Beleg/Beispiel → Handlungsempfehlung; FAQs mit direkten Antworten; Tabellen/Listen/Grafiken inkl. Beschreibung; aktuelle externe Statistiken verlinken.
- **Title/Meta-Konvention:** in den ausgewerteten Docs **nicht explizit dokumentiert** → siehe Datenlücken.

## Offene Punkte / Datenlücken

- **Title-/Meta-Konvention** für VHV nicht in den exportierten Docs auffindbar (ggf. in `01_OnPage` oder Reporting-xlsx). Nicht erfunden.
- **SEO-Reporting 2024/2025** liegt als `.xlsx` vor → über gws **nicht exportierbar**; KPI-Verläufe nicht ausgewertet.
- **RAIDAR-PDFs & OH-SO-PDFs** nur als Dateinamen erfasst (PDF, nicht als Text exportiert) — Detailbefunde der LLM-Analysen offen.
- **Branded-Anteil >90 %:** konkrete Non-Brand-Klickzahl nicht beziffert; nur als Anteil dokumentiert.
- **GSC-Zugriffsrechte** eingeschränkt (kein "uneingeschränkter Zugriff") → blockiert manuelle Indexierungsanträge.
- **Email "Aktuelle Entwicklungen im SI und Google Klicks" (04/2026):** Text-Export lieferte leeren Inhalt (vermutlich nur Tabellen/Bilder) → nicht ausgewertet.
- **Keine eigenständige Backlink-Auswertung** im Vault hinterlegt; Off-Page nur als geplantes Mediabudget benannt.

## Quellen

Ausgewertete Drive-Dateien (Ordner `04.1_SEO`, `04.2_GEO`, `07_Content`):

- `VHV | SEO-Skalierung: Private Direktvermarktung vhv.de | ab März 2026` (Google Doc, 04/2026) — Strategie/Forecast, Wettbewerb, AI Citations.
- `VHV | GEO-Maßnahmen aus OH-SO Analyse` (Google Doc, 03/2026) — VHV- + Hannoversche-Maßnahmen-Mapping.
- `VHV & HL | GEO-Maßnahmen aus OH-SO Analyse` (Google Sheet, 03/2026) — Maßnahmen mit Status/Zuständigkeit.
- `VHV.de | llms.txt` (Google Doc, 05/2026) — llms.txt-Entwurf + URL-Inventar + Markenbeschreibung.
- `VHV | Template | Content-Briefing` (Google Doc, 04/2026) — Briefing-Standard inkl. GEO-Block.
- `VHV I Ideensammlung warum die URL zur "Digitalen Schadensmarke" nicht indexiert wird` (Google Doc, 11/2025) — Technik/Indexierung.
- `VHV | Strukturierte Daten Organization` / `… Product lowPrice missing` (Doc + Sheet, 03–04/2026) — Schema-Befunde (per Name/Kurzcheck).
- RAIDAR-LLM-Analysen Privat Kfz/Hausrat/Haftpflicht + OH-SO-Zusammenfassung (PDFs, 02/2026) — nur per Name erfasst.
- Keyword-Sheets: KFZ Sistrix, "Auto only", Mitbewerber HanseMerkur, Wohnwagenanhänger-Ratgeber (per Name erfasst).
- `VHV | SEO-Reporting | 2024 & 2025.xlsx` (Office-Sheet — nicht exportierbar, per Name erfasst).
