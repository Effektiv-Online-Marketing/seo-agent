---
tags: [kunde, seo]
kunde: "Bikesnboards GmbH"
stand-Datum: 2026-06-19
---

# Bikesnboards GmbH

> Wissensdatei (SEO/GEO) für die Agentur [[EOM]]. Aufbau je Befund: **Befund -> Begründung -> Maßnahme**. Quellen siehe Abschnitt [[#Quellen]].

## Überblick

- **Wer/Branche:** Bikesnboards ist ein Fahrrad-Fachhändler mit Online-Shop. Sortiment: Fahrräder, E-Bikes, Zubehör und Ersatzteile. Geführte Marken laut Title-Tag u. a. **Cube, Specialized, Trek, Scott**; in den Befunden tauchen zusätzlich **Santa Cruz, Orbea, Cervélo, Lee Cougan, Scor, Favero** auf.
- **Domain:** `bikesnboards.de` (mit `www.`).
- **Standorte:** mindestens eine stationäre Filiale; im Shop existiert eine Info-Seite `bikesnboards.de/info/boeblingen` (Böblingen).
- **Shop-System:** Aktuelle Seite ist ein "technisch gewachsenes System, das nicht auf SEO ausgelegt" ist. Ein **Relaunch auf Shopware** ist geplant; die Optimierung läuft bereits auf einer **Shopware-Staging-Umgebung** (Quelle: SEO-Analyse 20.10.2025).
- **Hinweis:** Der Kunde firmiert als "Bikesnboards GmbH"; in den Dokumenten wird durchgängig die Marke/Domain "bikesnboards.de" verwendet. Die genaue Rechtsform/Firmierung ist in den ausgewerteten Dateien nicht explizit bestätigt.

## Mandat & Gewerke

- **Gewerk SEO:** SEO-Bestandsaufnahme und technische Analyse als Grundlage für den geplanten Relaunch (Ordner `1. SEO` mit Unterordner `SEO-Analyse 10/25`).
- **Relaunch-Begleitung:** Der rote Faden aller SEO-Empfehlungen ist der **SEO-getriebene Relaunch** (neues System soll SEO-Standards "verpflichtend mitdenken").
- **Tracking:** Es gibt eine "Tracking Überprüfung bikesnboards.de" (PDF, 25.02.2026) – deutet auf eine Prüfung des Analytics-/Conversion-Trackings hin. Inhalt nicht maschinell lesbar (siehe Datenlücken).
- **Angebote/Auftrag:** Im Ordner `0. Angebote` liegen zwei Angebote (251541 von 08/2025, 261602 von 03/2026) und eine **Auftragsbestätigung zu Angebot 261602** (03/2026). Inhalte der PDFs nicht exportierbar – Leistungsumfang nur aus Dateinamen ableitbar.

## SEO-Status & Befunde

Hauptquelle: **SEO-Analyse bikesnboards.de – V2, Stand 20.10.2025**. Datenbasis u. a. SISTRIX.

### Organische Sichtbarkeit stagniert

- **Befund:** Im Dezember 2020 ca. **2.500 Keywords in den Top-10**, im Oktober 2025 ca. **2.596 Keywords** (inkl. Brand wie "bikesnboards"). In knapp 5 Jahren faktisch kein Fortschritt.
- **Begründung:** Typisches Muster bei technisch gewachsenen Systemen ohne SEO-Ausrichtung; viele Begriffe mit hohem Suchvolumen liegen knapp hinter Seite 1.
- **Maßnahme:** SEO-getriebener Relaunch als stabile Grundlage; Einzelmaßnahmen wirken nur bedingt.

### Schwellenkeywords (Quick-Wins)

- **Befund:** Mehrere Keywords mit Potenzial dicht hinter Top-10 (Quelle: SISTRIX, Stand 10/25):

| Keyword | Position | Suchvolumen/Monat |
|---|---|---|
| fahrradgeschäft | 15 | 10.800 |
| cube e bike damen | 30 | 6.750 |
| cube e bike fully | 63 | 3.800 |
| specialized | 15 | 101.000 |
| specialized e bike | 40 | 8.400 |
| specialized turbo levo | 55 | 4.350 |

- **Wichtige Keywords ohne Ranking:** `cube e bike` (74.000/Monat), `specialized tarmac` (2.400/Monat).
- **Begründung:** Potenzial vorhanden, wird aber nicht ausgespielt – Ursache laut Analyse: fehlende interne Verlinkung, schwache Meta-Daten, technische Barrieren, keine klare SEO-Strategie.
- **Maßnahme:** Diese Begriffe gezielt priorisieren; Kategorie-/Marken-Landingpages stärken.

### Seitenstruktur konzentriert auf Startseite

- **Befund:** Die meisten Rankings und Klicks entfallen auf die Startseite; tiefere Seiten entfalten kaum SEO-Wirkung.
- **Begründung:** Kategorie-/Produktseiten technisch oder semantisch schlecht erreichbar.
- **Maßnahme:** Eigene starke Landingpage je Kategorie; logische Verlinkung von Produkten/Marken/Sortimenten; Filter-/Pagination-/Sortier-URLs dürfen keinen Duplicate Content erzeugen.

### Technische Befunde

- **Interne 404-Links:** Mindestens **85 interne Links** zeigen auf 404-Seiten (verschwendet Crawl-Budget, Linkjuice verpufft, schwächt Domain-Trust). Maßnahme: 301-Redirects auf relevante Alternativen + automatisiertes Monitoring. Viele 404-Ziele sind **falsch konstruierte Marken-URLs** wie `/santa cruz-bike`, `/lee cougan-bike`, `/scor bikes-bike` (Leerzeichen statt Bindestrich) sowie nicht mehr existente Produkt-URLs (Quelle: Sheet "Intern verlinkte 404-Seiten").
- **Defekte eingehende Backlinks:** Mindestens **12 externe Backlinks** zeigen auf nicht erreichbare Inhalte – kritisch, da Vertrauenssignale verloren gehen. Quellen sind v. a. langlebige **Foren-Backlinks** (mtb-news.de, emtb-news.de u. a.). Maßnahme: gezielt per 301 auf passende Seiten sichern.
- **Interne Redirects (301/302):** Zahlreiche interne Links führen über Weiterleitungen (Umwege). Bei 302 wird kein PageRank vererbt und Google kann das Ziel ignorieren. Maßnahme: interne Links direkt auf Ziel-URL setzen.
- **Duplicate Content:** Inhalte über viele Parameter-URLs erreichbar (Filter `?brand=`, Pagination `?page=`, Sortierung `?order=`, `?st=`). Beispiel `/kinderfahrrad/` existiert in vielen Varianten. Maßnahme: Canonical-Tags für Filter/Pagination/Sortierung; Unique Content für Markenseiten.
- **Mehrfacher Title-Tag:** Bei **über 9.000 URLs** mehr als ein `<title>` im Quelltext (Beispiel `/info/boeblingen`: korrekter Title + zweiter Title `<title>trash</title>`). Folge: Google wählt willkürlich oder ersetzt – Kontrollverlust über Snippets. Maßnahme: exakt ein Title pro Seite.
- **Fehlende H1:** Auf **über 9.000 Seiten** fehlt die H1 komplett (Kategorien ohne H1; auf Produktseiten ist der Produkttitel nur eine h2). Maßnahme: sprechende H1 auf Template-Ebene.
- **Doppelte/fehlende Meta-Descriptions:** Bei mehreren tausend URLs doppelt oder fehlend – beeinträchtigt CTR. Maßnahme: einzigartige Descriptions für Startseite, Kategorien, Marken, Produkte.
- **Strukturierte Daten fehlen komplett:** Auf der ganzen Domain keine Schema.org-Daten, obwohl Shop stark von Rich Snippets (Preis, Bewertungen, Verfügbarkeit, FAQ, Breadcrumbs) profitieren würde. Maßnahme: Schema im neuen System verpflichtend einbinden.
- **Ladezeit/Performance:** Viele Seiten laden **über 5 Sekunden** – schadet Core Web Vitals (v. a. mobil), erhöht Bounce. Maßnahme: Bilder komprimieren (WebP/Lazy Load/CDN), JS/CSS reduzieren, Hosting/Caching prüfen, Performance als Relaunch-Kernthema.
- **Defekte Bilder (404):** Produktbilder/Assets im Template eingebunden, aber serverseitig nicht vorhanden. Maßnahme: Media-Check mit automatischem Fallback.

### Shop-/Sortiment-Signal (Klickdaten)

- **Befund:** Top-Offer-Klickliste (Export 11.02.2026) wird klar von **Cube**-Modellen dominiert (Cube Acid 240, Cube Nuroad-Reihe, Cube Attain). Spitzenwert: "Cube Acid 240 Disc | actionteam | 24" mit 66 Klicks.
- **Begründung:** Bestätigt Cube als nachfragestärkste Marke im Shop und stützt die Keyword-Priorisierung (cube e bike, cube e bike damen/fully).
- **Maßnahme:** Cube-Kategorie- und Marken-Landingpages priorisiert optimieren; Top-Produkte sauber intern verlinken.

## GEO / KI-Sichtbarkeit

**Keine GEO-Daten gefunden.** In den ausgewerteten Dateien finden sich keine Inhalte zu KI-Sichtbarkeit, AI Overviews, ChatGPT/Perplexity, LLM-Zitaten oder einer `llms.txt`. Die SEO-Analyse adressiert ausschließlich klassisches SEO (Index-Sichtbarkeit, Technik, Onpage). Offen: GEO-Baseline (z. B. Sichtbarkeit in AI Overviews zu "fahrradgeschäft", "cube e bike") wurde noch nicht erhoben.

> Hinweis: Strukturierte Daten und saubere H1/Title (siehe Befunde) sind auch GEO-Grundlagen – fehlen aktuell vollständig.

## Doc-Typen & Aufbau

- **SEO-Analyse (Google Doc):** Langform-Audit. Aufbau: *SEO-Bestandsaufnahme* (Sichtbarkeit, Keyword-Entwicklung, Schwellenkeywords, Rankingverteilung, Seitenstruktur) -> *Technische Analyse* (404, Backlinks, Redirects, Duplicate Content, Title/H1/Meta, Schema, Performance, Bilder) -> *Fazit*. Viele eingebettete SISTRIX-Screenshots (im Text-Export als Leerzeilen sichtbar).
- **Empfehlungs-Vorlage (Google Doc "01 EOM Agency Vorlage Word"):** Standard-Schema je Empfehlung: **Titel -> IST -> SOLL -> Warum**, mit Überschriften-Ebenen 1–3 für ein automatisches Inhaltsverzeichnis.
- **Issue-Export (.xlsx, 19.10.2025):** Roh-Crawl-Export der Projekt-Issues (Office-Format, nicht exportierbar – nur per Name gewertet).
- **404-Liste (Google Sheet):** Spalten `Status-Code | Ziel-URL (404er) | Quellen` (Quell-URLs komma-separiert).
- **Klick-Reports (Google Sheet + CSV):** `Ihre Angebote | Anzahl der Klicks | Klick-Prozentzahl`.
- **Tracking-Überprüfung (PDF, 25.02.2026):** Vermutlich Analytics-/Conversion-Tracking-Audit (Inhalt nicht maschinell lesbar).
- **Angebote/Auftrag (PDF):** im Ordner `0. Angebote`.

## Schreibstil-Notizen

- Durchgängig **Sie-Anrede**, Wir-Perspektive der Agentur ("Aus unserer Sicht …").
- Struktur pro Punkt: Befund -> "Warum das relevant ist" (oft als Bulletliste) -> Handlungsempfehlung.
- Klartext statt Jargon, Fachbegriffe werden kurz erklärt (z. B. "Linkjuice", "Canonical-Tag", "Schwellenkeywords" in Anführungszeichen eingeführt).
- Wiederkehrende Botschaft: Einzelmaßnahmen reichen nicht, der **Relaunch** ist der strategische Hebel.
- Quellen werden benannt (SISTRIX) und mit konkreten Zahlen/Beispiel-URLs belegt.
- Footer-Signatur: "EOM – Effektiv Online-Marketing GmbH, Bödekerstraße 85, 30161 Hannover".

## Offene Punkte / Datenlücken

- **Angebots-/Auftrags-PDFs** (Leistungsumfang, Honorar) nicht exportierbar – nur Dateinamen bekannt.
- **Tracking-Überprüfung-PDF** nicht maschinell auslesbar (bildbasiert) – konkrete Tracking-Befunde unbekannt.
- **Issue-Export .xlsx** (Office-Format) nicht exportierbar – Detail-Issues nur indirekt über das Google-Doc/404-Sheet.
- **Keine GEO-/KI-Sichtbarkeitsdaten** vorhanden (kein AI-Overview-/LLM-Monitoring).
- Keine aktuellen **GSC-/Analytics-Rohdaten** zu Traffic/CTR im Ordner (nur die Top-Offer-Klickliste).
- Rechtsform/Impressumsdetails der "Bikesnboards GmbH" nicht in den Dateien bestätigt.
- SEO-Analyse ist von **10/2025**; ein Status nach Relaunch/aktuellem Stand 2026 liegt nicht vor.

## Quellen

Ausgewertete Dateien (Google Drive, Account ben@eom.de):

- **SEO-Analyse bikesnboards.de – 20.10.2025 – V2** (Google Doc) — Hauptquelle, vollständig ausgewertet.
- **Intern verlinkte 404-Seiten** (Google Sheet, 19.10.2025) — 404-Ziel-URLs + Quellen, ausgewertet.
- **clicks-top-offers_2026-02-11** (Google Sheet, Export 12.02.2026) — Top-Produkt-Klicks, ausgewertet.
- **01 EOM Agency Vorlage Word** (Google Doc, 15.11.2025) — Empfehlungs-Vorlage (IST/SOLL/Warum), ausgewertet.
- **2025-10-19_projectissues_download_3ac41.xlsx** — nur per Name gewertet (Office-Format, nicht exportierbar).
- **Tracking Überprüfung bikesnboards.de.pdf** (25.02.2026) — heruntergeladen, Text nicht maschinell extrahierbar; per Name gewertet.
- **0. Angebote/** (Angebot-251541, Angebot-261602, Auftragsbestätigung 261602, PDFs) — nur per Name gewertet.
