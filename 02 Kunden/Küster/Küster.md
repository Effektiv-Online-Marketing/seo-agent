---
tags: [kunde, seo]
kunde: "Küster"
stand-Datum: 2026-06-19
---

# Küster (Gerhard Küster GmbH)

> Wissensdatei auf Basis des Google-Drive-Kundenordners (Account `ben@eom.de`). Analyse-Logik: Befund → Begründung → Maßnahme. Es werden keine Rankings, Backlinks oder Suchvolumina geschätzt — Suchvolumen-Angaben stammen 1:1 aus den Drive-Sheets/Empfehlungen.

## Überblick

- **Kunde:** Gerhard Küster GmbH — familiengeführter **Fachgroßhandel für Sanitär & Heizung** (SHK). Sortiment laut Empfehlungen: Sanitär, Heizung, Installation, Werkzeuge (sowie Lüftung & Klima auf der Bestandsseite).
- **Domain:** `sanikue.de` (Marke „Sanikü"/„sanikue"). Sprache: **Deutsch (DE)**, regionaler Fokus.
- **Standorte / Geo-Fokus:** Hannover und Hildesheim (Badausstellungen) sowie Abhollager „Holfix" (Hannover-Südstadt, Hannover-Vahrenwald, Burgwedel/Zentrallager, Hildesheim). Geo-Keywords durchgängig auf Hannover/Hildesheim ausgerichtet.
- **Zielgruppen:** B2B (Fachbetriebe/Handwerk, Gewerbekunden) und B2C (private Bauherren). Eigener Geschäftskundenbereich (`/geschaeftskunden/`), Küster-App, ZUGFeRD.
- **Kontext Relaunch:** Es gab/gibt eine Schwesterseite **Friedrich Lange** (`friedrich-lange.de`); die neue Küster-Website wurde im Kern nach dem Friedrich-Lange-Muster aufgebaut. Umsetzungspartner Technik/Webseite: Agentur **„Die Creativen"**. EOM liefert SEO-Konzeption, Content-Empfehlungen und QA.

## Mandat & Gewerke

Aus den Deliverables ableitbar — Schwerpunkt ist ein **SEO-begleiteter Website-Relaunch** auf `sanikue.de`:

- **On-Page & Content:** Seitenweise Content-Empfehlungen inkl. Keywords, Meta-Titel/-Description, H-Struktur und CTA-Vorgaben (Startseite, Bäder-Kategorien, Badausstellung, Abhollager, Karriere/Ausbildung/Stellenangebote, Geschäftskunden, Sortiment, Über uns, Kontakt).
- **Technical SEO / Relaunch-QA:** SEO-Checks vor und nach Livegang (404, H1, Duplicate Content, strukturierte Daten, HTTP-Assets, Meta-Descriptions), Weiterleitungskonzept, Staging-Abnahme.
- **Keyword-Recherche:** Initiale KWR (Seiten-Keyword-Mapping) plus KWR für Magazin-/Ratgeber-Artikel.
- **Content-Roadmap Blog/Magazin:** Ratgeber-Artikel-Ideen mit Keyword- und Wettbewerber-Mapping.
- **Analytics-Setup:** Einbindung Google Analytics über Küster-Google-Konto angestoßen (Zugang im Rückfragen-Doc übergeben).

## SEO-Status & Befunde

Quellen: **„KÜSTER | Relaunch SEO Check"** (Google Doc, zuletzt 12.11.2025; enthält Termine 04.11. und 07.11.2025) und **„Friedrich Lange | SEO Check"** (Google Doc, 09.10.2025). Befunde betreffen die Relaunch-/Staging-Phase von `sanikue.de`.

**Technik / Indexierung**
- **Interne 404-Fehler** (Stand 04.11.): `/vom-plan-zum-bad/` in mobiler Navi verlinkt aber nicht erreichbar; tote Bild-URLs (`Friedrich-Lange-Welle-links.svg` als http und https). → Begründung: 404 verschwenden Crawl-Budget und stören UX. → Maßnahme: Links entfernen/zielführend umbiegen, Assets bereitstellen.
- **Blindtext-Seiten indexierbar:** `/badausstellungen/`, `/lorem-ipsum-dolor/`, `/ueber-uns/` enthielten nur Platzhaltertext. → Begründung: kein Mehrwert, Thin Content. → Maßnahme: löschen bzw. mit Inhalt füllen.
- **Duplicate Content:** `/standort/` und `/standorte/` identisch. → Maßnahme: `/standorte/` löschen, alle Verlinkungen auf `/standort/` umstellen (Verzeichnis `/standort/hannover/` bleibt führend).
- **Strukturierte Daten falsch:** In mehreren Karriere-Stellenseiten stand „Friedrich Lange" als Unternehmen im Markup. → Maßnahme: auf „Küster" korrigieren.
- **HTTP-Assets:** Icons/Bilder auf `/kuester-and-friends/` als `http://` eingebunden. → Begründung: unverschlüsselt/Mixed-Content. → Maßnahme: auf `https://` umstellen.
- **Externer 404:** ZUGFeRD-Link auf `/geschaeftskunden/zugferd/` defekt → auf gültige ferd-net.de-/zugferd-community.net-URL umbiegen.

**On-Page**
- **Fehlende H1:** `/abhollager/hannover-suedstadt/` und `/abhollager/burgwedel/` ohne H1 → vorgegebene H1 auszeichnen.
- **Mehrfach-H1:** `/sortiment/` (zweite H1 → H2) und `/kataloge/` (saubere H1/H2-Hierarchie für Diana/Ditech/Vamigo/Splash).
- **Fehlende Meta-Descriptions:** für `/karriere/`, `/geschaeftskunden/zugferd/`, `/kataloge/`, `/ausbildung/`, `/stellenangebote/`, `/abhollager/`, `/geschaeftskunden/kuester-app/`, `/standort/` — fertige Texte im Doc geliefert.
- **Falsche Personen-/Markennennung im Content:** Bewerbungsformular-Titel zeigte „Lange" statt „Küster"; Mitarbeiterbild (Markus Wicke statt Heiko) auf Stellenangebote-Seite. → Maßnahme: korrigieren.

**Friedrich-Lange-Check (09.10.2025, Schwesterseite, relevant fürs Muster)**
- Automatisch generierte Abhollager-Seiten → `noindex`.
- Sitemap enthielt leere/Beispielseiten → bereinigen.
- Unnötige Paginierungsseiten (Über uns, Startseite, Karriere, Abhollager) und Paginierung mit 404 (Stellenangebote, Ausbildung, Standorte) entfernen.
- HTTP-Links im Quellcode (Wellen-Bild) → https.
- „Nach Relaunch": zu große Bilder und fehlende Meta-Descriptions als Folgethemen markiert.

**Keyword-Mapping (aus „Küster | Inititale KWR" und Startseiten-Empfehlung)**
- Startseite Hauptkeywords: `sanitär großhändler` / `sanitär großhandel` (je 1.600 SV laut Sheet). Nebenkeywords stark Geo-getrieben: `hannover sanitärhandel`, `sanitärgroßhandel hannover`, `heizungsgroßhandel hannover` (260–590).
- Bäder-Cluster: `badezimmer ideen` (22.800), `bad idee` (6.600), `bad inspiration`/`inspiration badezimmer` (je 2.900) auf der „Unsere Bäder"-Übersicht; Unterseiten für Basicbad, Familienbad(ezimmer), Komfortbad, Designbad mit kleineren Volumina.
- Hinweis im Sheet: KWR teils noch auf Staging-URLs (`b13yu3w.myrdbx.io`); URL `familienbad` → `familienbadezimmer` empfohlen.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten im Kundenordner gefunden.** Es liegen keine Dokumente zu AI Overviews, ChatGPT/Perplexity/Copilot-Zitierfähigkeit, LLM-Traffic oder Brand-Mentions vor. Das Mandat ist (Stand der Drive-Inhalte) klassisch On-Page/Technical/Content-getrieben rund um den Relaunch. → Offener Ansatzpunkt: GEO-Audit (Peec AI / Sistrix AI / DataForSEO LLM) ist noch nicht Teil des Scopes.

## Doc-Typen & Aufbau

Im Ordner `04_SEO` mit Unterordnern `01_Blog`, `02_OnPage`, `03_Technik`, `04_Infos für Technik – "Die Creativen"`, `05_Layouts`:

- **Content-/On-Page-Empfehlungen** (Google Docs, viele): Pro Seite eine Datei „Küster | Empfehlung zu …". Fester Aufbau: `URL nach Relaunch` → **1. Keywords** (Haupt-/Nebenkeywords mit SV) → **2. Metas** (Meta-Titel + Meta-Beschreibung) → **3. Content** mit explizit ausgezeichneten H1/H2/H3-Tags, CTA-Texten und eckigen `[Klammer-Hinweisen]` an die Umsetzung (Bilder, WebP, max. 250 kB im Slider, Alt-Text-Keywords, Verlinkungen). Farb-Konvention: **gelb = Anpassung am Bestand, grün = neuer Inhalt**.
- **SEO-Checks** (Google Docs / zusätzlich als PDF + .docx-Versionen): listenbasiert nach Befundtypen gruppiert (404, H1, Duplicate Content, strukturierte Daten, Metas …), datiert nach Termin, mit „bereits in Arbeit/behoben"-Markierung.
- **Keyword-Recherchen** (Google Sheets): Spalten `Seite | Keyword | SV | Notiz` (Seiten-Mapping) bzw. `Artikel-Idee | Keyword | Suchvolumen | Mitbewerber` (Magazin).
- **Weiterleitungskonzept** (Sheet): `Alte Website | Neue Website | Kommentar`; leere Zielzelle = keine Weiterleitung nötig; Hinweise auf `noindex` (Datenschutz/Impressum).
- **Staging-Abnahme** (Sheet): Matrix `Dimension × Seite` — Prüfdimensionen Content, Medien/Ladegeschwindigkeit, interne Verlinkungen, UX/Mobile, Formulare; pro Seite konkrete Mängel-Notizen.
- **Rückfragen-/Abstimmungsdoc** mit „Die Creativen": nummerierte Punkte mit „Antwort EOM / Küster".
- **Sitemap/Struktur**: PDF-Sitemap-Layout + Sheet „Struktur neue Website".

## Schreibstil-Notizen

- **Tonalität:** Sie-Anrede, nahbar und regional („echte Nähe zur Region", „familiengeführt", „aus einer Hand"). Markenname im Fließtext „Gerhard Küster GmbH" bzw. „Küster". Trust-/USP-Sprache mit Häkchen-Listen (`✓`) in Meta-Descriptions.
- **Title-Konvention:** Marke + Leistung + Geo, Pipe-getrennt — Beispiel Startseite: `Küster - Großhändler für Sanitär & Heizung | Hannover & Hildesheim`.
- **Meta-Description-Konvention:** Leistungsversprechen + USP-Häkchen + Call-to-Action mit Pfeil — Beispiele: „… ✓ Hochwertige Badausstellung ✓ Individuelle Beratung ✓" und „… ► Jetzt bewerben" / „➧ Mehr erfahren!".
- **H-Struktur:** strikt sequenziell (eine H1/Seite; Hover-/Kachel-Überschriften als H3 statt H4). Keywords in Bild-Dateiname, Alt-Text und Titel.
- **Begriffe:** „KI" statt „AI". Keine Artikelnummern/Preise im Content (Kundenvorgabe). „Historie" statt doppelter „Unternehmensgeschichte".

## Offene Punkte / Datenlücken

- **Keine GEO/KI-Sichtbarkeit** im Ordner (siehe oben) — kein AI-Overview-/LLM-Monitoring.
- **Keine Reportings/Analytics-Auswertungen** im SEO-Ordner gefunden (GA erst während Relaunch eingebunden); keine GSC-/Sistrix-Sichtbarkeitsdaten abgelegt → tatsächliche Rankings/Traffic nicht belegbar.
- **Suchvolumina** stammen aus den Sheets/Empfehlungen; Quelle/Tool dort nicht dokumentiert — nicht unabhängig verifiziert.
- **Office-Dateien** (`KÜSTER _ Relaunch SEO Check (2).docx`, `Mitarbeiterstimmen_Küster.docx`) und **PDFs** (Sitemap-Layout, SEO-Check 10/25) nur per Name/Parallel-Doc gewertet — .docx/.xlsx sind über die CLI nicht als Text exportierbar.
- **Korrigierte Versionen / Layouts der „Creativen"** (Unterordner) nicht im Detail ausgewertet.
- Verwandte Domain **`friedrich-lange.de`** als Muster relevant, aber kein eigenes laufendes Mandat hier abgebildet.

## Quellen (ausgewertete Drive-Dateien)

- KÜSTER | Relaunch SEO Check — Google Doc (Stand 12.11.2025)
- Friedrich Lange | SEO Check — Google Doc (09.10.2025)
- Küster | Beantwortung der Rückfragen Mail die Creativen – 24.10.2025 — Google Doc
- Küster | Inititale KWR — Google Sheet
- Küster | KWR für Magazin-Artikel — Google Sheet
- Küster | Empfehlung zur Startseite — Google Doc (repräsentativ für On-Page-Empfehlungen)
- Küster | Weiterleitungskonzept — Google Sheet
- Küster_Staging Umgebung_Check (mit Küster Freigabe) — Google Sheet
- Ordnerstruktur `04_SEO` (Blog / OnPage / Technik / Infos für Technik / Layouts) sowie ~30 weitere Seiten-Empfehlungen (per Liste gesichtet)
- Nur per Name gewertet: KÜSTER SEO-Check 10_25.pdf, KÜSTER _ Relaunch SEO Check (2).docx, 2025 04 KÜS Sitemap Lay01.pdf, Küster | Struktur neue Website (Sheet), Mitarbeiterstimmen_Küster.docx
