---
tags: [kunde, seo]
kunde: "Prange Schuhe"
stand-Datum: 2026-06-19
---

# Prange Schuhe

> Wissensdatei (SEO/GEO) aus dem Google-Drive-Kundenordner. Aufbau je Befund: **Befund -> Begründung -> Maßnahme**. Quellen mit Datum am Abschnittsende und unter [[#Quellen]]. Keine geschätzten Rankings/Suchvolumina/Backlinks – fehlende Daten sind offen benannt.

## Überblick

- **Wer:** Prange Schuhe, Online-Schuhhändler (Schuh-E-Commerce). Teil einer Shop-Gruppe "PGJ" = **Prange / GISY / Juppen** (drei Schwester-Shops, teils gemeinsame technische Basis und gemeinsame SEO-Bearbeitung). Schwester-Shops sind als eigene Kunden im Vault geführt: [[GISY-Schuhe.de]] und [[Juppen]].
- **Branche:** E-Commerce / Mode / Schuhe (Damen, Herren, Kinder; Marken-, Kategorie- und Produktdetailseiten).
- **Domain:** `www.prangeschuhe.de` (Schreibweise in Crawl-Dateien teils `prangeschuhe.de`; ältere Domain-Erwähnung `prangegruppe.de`).
- **Technik-Stack (Befund):** Frontend auf **Nuxt** (CSS/JS-Pfade unter `/_nuxt/...`), CDN über CloudFront; Shop-Backend offenbar **xt:Commerce-basiert** (Admin unter `xtc.gisy-schuhe.de/admin/start.php`, gemeinsames Backend für die Gruppe). Technische Umsetzung läuft über einen Dienstleister namens **DMF**.
  - Quelle: PageSpeed-Empfehlung 19.07.2022; Backend-Anleitung 02.12.2025.

## Mandat & Gewerke

EOM betreut Prange (im Verbund mit GISY/Juppen) breit über mehrere Disziplinen. Belegt durch die Ordnerstruktur und Dokumente:

- **SEO** (eigener Ordner `SEO`): OnPage-Optimierungen, technische Audits, Content-/Bilder-Empfehlungen, Sitemap-/Redirect-Pflege.
- **SEA** (eigener Ordner `SEA`): Google-Ads-Tracking-Snippets, Anzeigenschaltung Mobile/Tablet.
- **Reporting** (Ordner `REPORTINGS` mit Jahrgängen 2019–2022).
- **Relaunch-Begleitung** (Ordner `Relaunch`; Dokument "Wichtige Tasks hinsichtlich Relaunch", 2020).
- **Laufende Content-Empfehlungen** (saisonale Kategorie-/Ratgebertexte, zuletzt August 2025).
- **Digitale Barrierefreiheit (BFSG)** – eigener Ordner, modifiziert Juni 2025 (Inhalt nicht ausgewertet; nur per Name erfasst).

Operative Arbeitsweise (Befund aus Backend-Anleitung 02.12.2025): Empfehlungen werden über interne Google-Sheets gepflegt ("Schwellenkeywordliste & URL-Übersicht", Reiter "Empfehlungen INTERN" -> "URL Übersicht OUT" -> automatisch befülltes Kunden-Doc). Änderungen an Marken-/Kategorietexten kann EOM teils selbst im Shop-Backend (Hersteller > Kategorietexte) umsetzen.

> Hinweis: Es liegt **kein zentrales, datiertes Gesamt-SEO-Audit** als ein Dokument vor. Der SEO-Status ergibt sich aus vielen Einzel-Checks (s. u.).

## SEO-Status & Befunde

### 1. Technische SEO – wiederkehrende Crawl-/Index-Themen (2020/2021, Nachkontrollen bis 2025)

Der Ordner `SEO` enthält eine lange Serie technischer Einzel-Checks. Die Bandbreite zeigt die historisch bearbeiteten Baustellen:

- **404-/500-Fehler:** mehrere Listen (404-Links Prange 08/2021, Kontrolle 09/2021, neue 404 10/2021, 404/500 01/2022, Status-500-Liste 10/2020). **Aktuellste Wiederholung: "Prange | Interne 404 Fehler" (26.02.2025).**
  - Begründung: 404/500 verschwenden Crawl-Budget, brechen interne Linkpfade und verschlechtern UX.
  - Maßnahme: Weiterleitungs-/Redirect-Pflege (ein Weiterleitungstool wurde lt. Doku 10/2021 eingeführt); interne 404 erneut prüfen und auflösen (Stand 02/2025 noch offen).
- **Doppelte/fehlende Title-Tags & H1:** Listen zu "Duplicate Titles" (Mai 2021), "gleiche Title-Tags" (10/2020), doppelte/fehlende H1 (2021); **aktuellste Wiederholung: "PGJ | Doppelte Title Tags" (26.02.2025).**
  - Begründung: Duplikate bei Title/H1 schwächen die thematische Differenzierung der Seiten und damit Rankings.
  - Maßnahme: eindeutige, keyword-relevante Titles/H1 je Seitentyp (s. Content-Logik unten).
- **Canonical-/Parameter-Probleme:** "Parameter-URLs ohne Canonical-Tag" (02/2021), "Mehrfache Canonical-Tags" (04/2021), "Indexbereinigung" (02/2021).
  - Begründung: Parameter-URLs ohne sauberes Canonical erzeugen Duplicate Content und unkontrollierte Indexierung.
- **Sitemap-Pflege:** mehrere Sitemap-Status-Code-Checks (2021); **aktuellste Wiederholung: "Prange | Sitemap Check" und "Prange | Sitemap.xml" (26.02.2025).**
- **Interne Verlinkung:** Dokumente zu interner Verlinkung von Produktseiten und Marken-Verlinkung über Produktseiten (2021); "inlinks-suche.xlsx" (12/2024, nur per Name erfasst).
- **Defekte Backlinks:** Liste 06/2021 (nur als historischer Befund; **keine aktuellen Backlink-Daten** im Ordner, daher kein Off-Page-Status ableitbar).
  - Quelle: Ordner `SEO` Dateiliste, Datumsangaben wie oben.

### 2. PageSpeed / Core Web Vitals (Stand 19.07.2022)

- **Befund:** Laut Google Search Console hatten zum Stand 07/2022 **sämtliche Seitentypen weder mobil noch Desktop ausreichende Core-Web-Vitals-Werte**; der PageSpeed hatte sich gegenüber der Vorprüfung teils **weiter verschlechtert**. Untersucht: Startseite, Kategorieseite (Bsp. `/konstantin-starke`), Produktdetailseite.
- **Konkrete Schwachstellen:**
  - **CLS:** Layout-Shift durch Slider/Hero-Image (Start/Kategorie) und durch erstes Produktbild + prev/next-Buttons (PDP).
  - **LCP:** Serverantwortzeit Ø ~1,2 s (Origin); Startseite ~800 ms, Kategorie ~1,3 s, PDP ~1 s (Googles "Good"-Grenze: < 800 ms). Render-blockierende CSS-Ressourcen unter `/_nuxt/css/*`.
  - **FID:** zu viel/zu langsames JavaScript; übermäßige DOM-Größe auf Kategorieseiten; mehrere Cookie-Consent-Skripte gleichzeitig geladen.
- **Maßnahmen (empfohlen):** feste Bild-Dimensionen (width/height), Hero-/erstes Produktbild via `preload`; Serverantwortzeit < 800 ms; render-blockierende Ressourcen entzerren (Fonts vor CSS); ungenutztes CSS/JS reduzieren; DOM verkleinern; Umsetzung mit Dienstleister **DMF** klären.
  - Quelle: "Prange / GISY / Juppen | PageSpeed-Empfehlung – 19.07.2022".
  - **Datenlücke:** Kein aktueller CWV-/PageSpeed-Stand (2024–2026) im Ordner – Verbesserung unbestätigt. FID ist inzwischen durch INP abgelöst; keine INP-Daten vorhanden.

### 3. Bilder-SEO (Stand 25.02.2021)

- **Befund (Datenbasis 2020):** Bildersuche ist ein **wesentlicher Traffic-Kanal**. Für prangeschuhe.de kamen 2020 **> 38.000 Nutzer über die Google-Bildersuche = 30,9 % des Gesamttraffics** (Web+Bilder = 124.882); Bild-Impressionen lagen über den Web-Impressionen. Bei einigen Produktseiten lagen Bild-Klicks über den Web-Klicks. Top-Bildersuche-Keyword 2020: **"weiße sneaker herren"** (zwei Prange-Bilder vorn, vor Amazon).
  - (Vergleich Gruppe: GISY 36,6 % / Juppen 27,8 % Bildtraffic-Anteil.)
- **Begründung:** Im Schuh-E-Commerce ist visuelle Suche ein eigener, starker Hebel – darf nicht nur als Beiwerk der Websuche behandelt werden.
- **Maßnahmen:** aussagekräftige **Alt-Texte mit Markennennung** (Empfehlung: Breadcrumb-Text + "Bild 1/2/…"); **sprechende Bild-Dateinamen/URLs** statt `32733_5.jpg` -> z. B. `silber-schwarze-damen-sneaker-von-michael-kors-703849-bild-6.jpg`; **stabile Bild-URLs** (bei Änderung Redirect, da Bilder selten gecrawlt werden); Bilder vor Upload **komprimieren** (hohe Qualität, geringe Dateigröße); Produktbeschreibungen als Kontext erweitern.
  - Quelle: "GISY / Prange / Juppen – Empfehlungen zur Bilder-SEO", 25.02.2021.

### 4. Content-Logik Marken-/Kategorieseiten (Stand 28.05.2021)

- **Befund:** Markentexte über die drei Shops waren **nicht einheitlich aufgebaut**, ohne klare Zwischenüberschriften/Absätze; Haupt-, Damen- und Herren(unter)seiten einer Marke grenzten sich inhaltlich zu wenig voneinander ab.
- **Maßnahme (Soll-Struktur):**
  - Markenhauptseite (z. B. `/copenhagen`): dreht sich um die **Marke** (Herkunft, Besonderheit, USPs wie Made in Germany / vegan) – H1 = Marke + "Schuhe", H2 zu Design, H2 zu Materialien, H2 zum Kauf.
  - Damenschuhe der Marke (`/copenhagen/damenschuhe`): Fokus **Zielgruppe Damen** – H1 = "[Marke] Schuhe für Damen", H2 zu Vorteilen/Besonderheiten, H2 zum Kauf.
  - Herrenschuhe der Marke (`/copenhagen/herrenschuhe`): analog für Herren.
  - Hinweis aus Backend-Anleitung: Marken-Unterkategorien **mit** Marke (z. B. `/konstantin-starke/damen-stiefeletten`) sind im Backend **nicht** editierbar – nur Markenseite, Marken-Damen/Herren-Seiten und marken-unabhängige Kategorien.
  - Quelle: "Prange / GISY / Juppen – Allgemeine Content-Empfehlung für Marken & Kategorieseiten", 28.05.2021; Backend-Anleitung 02.12.2025.

### 5. Saisonale Kategorie-/Ratgeber-Empfehlungen (aktuellster Content, August 2025)

Aktuellste inhaltliche Arbeit sind Title-/Meta-/Content-Empfehlungen je Ziel-URL nach festem Schema (Hauptkeyword + Suchvolumen, Title-Tag IST/SOLL, Meta-Description IST/SOLL, H1 + H2-gegliederter Fließtext). Beispiele:

| Datum | Ziel-URL | Hauptkeyword | SV (lt. Doc) |
|---|---|---|---|
| 25.08.2025 | `/new` (Prange) | damen herbstschuhe | 6.600 |
| 25.08.2025 | (Prange) | damen moonboots | – |
| 25.08.2025 | (Prange) | herren herbstschuhe | – |
| 15.08.2025 | (GISY) | peter kaiser schuhe damen | – |
| 25.08.2025 | `/combat-boots` (GISY) | combat boots damen | 590 |

- **Befund:** Die Empfehlungen ersetzen generische Bestands-Titles (z. B. Startseite/`/new`: "Neue Schuhe online kaufen für Damen, Herren & Kinder bei Prange") durch keyword- und saison-fokussierte Varianten (z. B. "Herbst Damen Schuhe 2025: Entdecken Sie die neuesten Trends").
- **Begründung:** Saisonkeywords (Herbstschuhe, Moonboots, Combat Boots) heben generische Kategorie-Landingpages auf konkrete, suchstarke Intents.
- **Maßnahme:** Title/Meta/H1+H2-Texte je Saison gemäß Doc einpflegen; H2-Struktur folgt einem Ratgeber-Muster (Was macht X aus? / Für wen geeignet? / Worauf achten? + Abschluss-CTA "im Prange Onlineshop entdecken").
  - Quelle: GISY/Prange-Empfehlungs-Docs 15.–25.08.2025.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten im Kundenordner gefunden.** Es liegen keine Dokumente zu AI Overviews, ChatGPT/Perplexity/LLM-Sichtbarkeit, llms.txt, KI-Crawler-Zugriff (GPTBot/ClaudeBot/PerplexityBot) oder Brand-Mention-Monitoring vor. Die jüngsten Arbeiten (08/2025) sind klassische OnPage-/Content-Empfehlungen ohne expliziten GEO-Bezug.

- **Anknüpfungspunkt (nicht belegt, als Hypothese):** Die in den 08/2025-Empfehlungen genutzte Frage-Antwort-H2-Struktur ("Was macht … aus?", "Für wen geeignet?", "Worauf achten?") ist grundsätzlich gut für passage-basierte KI-Zitierbarkeit geeignet – ein gezielter GEO-Check (FAQ-/Schema-Auszeichnung, Zitierfähigkeit, KI-Crawler-Freigabe) ist bislang nicht dokumentiert.

## Doc-Typen & Aufbau

- **Technische Audit-Listen:** Google Sheets je Thema/Datum (404, Titles, Canonicals, Sitemap-Status, H1) – Dateinamen mit Datumspräfix `JJJJ-MM-TT`.
- **Empfehlungs-Dokumente (Google Docs):** zwei Muster:
  - *Konzept-/Audit-Doc* nach Schema **IST -> SOLL -> Warum** (PageSpeed, Bilder-SEO, Content-Struktur).
  - *Keyword-/Seiten-Empfehlung* nach Schema **Hauptkeyword (+SV) -> 2. Metas (Title/Meta IST+SOLL) -> 3. Content (H1, [Produkt-Grid], H2-Blöcke)**.
- **Prozess-/Anleitungs-Docs:** z. B. Backend-Pflege, Verweise auf interne Steuer-Sheets.
- **Reportings:** nach Jahrgängen 2019–2022 abgelegt (Inhalt nicht ausgewertet).
- **Office-Dateien (.xls/.xlsx):** vorhanden (alte Crawls, "Seiten ohne Produkte" 01/2025, "inlinks-suche" 12/2024) – **nicht exportierbar, nur per Name erfasst**.

## Schreibstil-Notizen

- **Anrede:** durchgängige **Sie-Form** in kundenseitigen Texten ("Entdecken Sie …", "Worauf sollte man achten").
- **Struktur der Kategorietexte:** Einleitung + 3–4 H2-Blöcke nach Ratgeber-Logik; Abschluss mit CTA ("Jetzt online bei Prange stöbern!" / "im Prange Onlineshop entdecken").
- **Tonalität:** verkaufs- und nutzenorientiert, modisch-beratend ("stilvoll & komfortabel", "Statement setzen", "Stilbruch"), ohne Fachjargon.
- **Meta-Descriptions:** mit Symbolen/Trennern (►, ✓, ❤️) und Trust-/USP-Stichworten (große Auswahl, neueste Trends, Kauf auf Rechnung).
- **Interne EOM-Doc-Sprache:** klare IST/SOLL/Warum-Begründungen, Du-Form gegenüber Dienstleister/intern ("Wäre es für Euch möglich …").

## Offene Punkte / Datenlücken

- **Kein aktuelles Gesamt-Audit:** Status ist aus Einzel-Checks rekonstruiert; technische Themen (404, Doppel-Titles, Sitemap) tauchen **2025 erneut** auf -> möglicherweise nicht nachhaltig gelöst.
- **PageSpeed/CWV veraltet (2022)** und seinerzeit durchweg "schlecht"; **kein aktueller CWV-/INP-Stand**. FID-Bezug überholt.
- **Keine aktuellen Off-Page-/Backlink-Daten** (nur defekte-Backlinks-Liste 2021).
- **Keine Ranking-/Sichtbarkeits-/Traffic-Kennzahlen** im ausgewerteten Material (außer Bildtraffic-Zahlen aus 2020) – Ranking-Status nicht belegbar.
- **Keine GEO/KI-Sichtbarkeitsanalyse** vorhanden (s. o.).
- **BFSG/Barrierefreiheit (2025):** Ordner existiert, Inhalt nicht ausgewertet – möglicher SEO-/UX-Querbezug offen.
- **Office-/xlsx-Dateien** (Crawls, inlinks, "Seiten ohne Produkte") nicht maschinell auswertbar.
- **Domain-Schreibweise/-historie** (`prangeschuhe.de` vs. `prangegruppe.de`) nicht abschließend geklärt.

## Quellen

Ausgewertete Dateien aus dem Google-Drive-Kundenordner (Account ben@eom.de):

- "2025-25-08 Prange Empfehlung 'Damen Herbstschuhe'" (Google Doc, 25.08.2025) – Title/Meta/Content für `/new`, KW "damen herbstschuhe" (SV 6.600).
- "2025-25-08 GISY Empfehlung 'Combat Boots für Damen'" (Google Doc, 25.08.2025) – Beispiel Empfehlungs-Schema (Schwester-Shop).
- "Anleitung Prange/GISY Änderungen im Backend durchführen" (Google Doc, 02.12.2025) – Tech-Stack-/Prozess-Hinweise, editierbare Seitentypen.
- "Prange / GISY / Juppen – Allgemeine Content-Empfehlung für Marken & Kategorieseiten" (Google Doc, 28.05.2021) – Soll-Struktur Marken-/Kategorieseiten.
- "Prange / GISY / Juppen | PageSpeed-Empfehlung – 19.07.2022" (Google Doc) – Core Web Vitals (CLS/LCP/FID), Serverzeit, Nuxt/CloudFront.
- "GISY / Prange / Juppen – Empfehlungen zur Bilder-SEO" (Google Doc, 25.02.2021) – Bildtraffic-Anteil 30,9 %, Alt-Text-/Dateinamen-/Komprimierungs-Empfehlungen.
- Ordner-Listings `SEO`, `REPORTINGS`, Kundenhauptordner (Stand-Auflistung 2026-06-19) – technische Audit-Historie, u. a. "Prange | Interne 404 Fehler", "PGJ | Doppelte Title Tags", "Prange | Sitemap Check" (alle 26.02.2025).

Verwandt: [[GISY-Schuhe.de]] · [[Juppen]] (gemeinsame Shop-Gruppe PGJ, gemeinsames Backend & gemeinsame SEO-Bearbeitung).
