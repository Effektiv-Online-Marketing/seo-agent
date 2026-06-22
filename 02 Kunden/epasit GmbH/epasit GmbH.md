---
tags: [kunde, seo]
kunde: "epasit GmbH"
stand-Datum: 2026-06-19
domain: epasit.de
quelle: "Google Drive Kundenordner 02_SEO (ben@eom.de)"
---

# epasit GmbH

> Wissensbasis für die SEO-Arbeit von [[Über EOM|EOM]]. Logik durchgängig: Befund -> Begründung -> Maßnahme. Stand der ausgewerteten Drive-Dokumente: **2021** (siehe [[#Offene Punkte / Datenlücken]]).

## Überblick

- **Wer:** epasit GmbH, Hersteller von mineralischen Bauprodukten / Sanierungssystemen (Putze, Mörtel, Abdichtungen, Dämmsysteme).
- **Branche:** Baustoffe / Bauchemie, Schwerpunkt Sanierung & Abdichtung (B2B-Hersteller mit Fachhandwerker- und Endkunden-Berührung).
- **Domain:** `epasit.de` (zum Analysezeitpunkt 2021 nach Relaunch live; Test-/Staging-Domain in der Keywordrecherche: `epasit-test.pmdesign-online.de`).
- **Themen-/Produktwelt (aus der Keywordrecherche abgeleitet):** Schimmelsanierung, Innendämmung, Feuchtesanierung, Mineralische Abdichtung, Salzbefall-Sanierung, Horizontalabdichtung/-sperre, Sandstein-/Ziegelsteinsanierung, Denkmalsanierung, Spezialanwendungen (Risssanierung, Reparaturmörtel, Pflaster-/Fugenmörtel), Schnellzement.
- **CMS-Hinweis:** WordPress-typische Strukturen erkennbar (`/page/2`-Paginierung, `/author/nils`, RSS-Sitemap `sitemap.rss`) — aus dem Technik-Check abgeleitet.

## Mandat & Gewerke

EOM-Mandat als SEO-Agentur. Aus den Dokumenten belegte Gewerke:

- **Technisches SEO** — initiale OnPage-Technik-Analyse + Technik-Check nach Website-Relaunch (Crawls 06/2021 und 07/2021).
- **On-Page / Content** — Keywordrecherche je Produkt-/Anwendungsseite, Snippet-/Title-Optimierung, Heading-Struktur, interne Verlinkung, Alt-Texte.
- **Usability / CRO-nah** — initiale Usability-Analyse (Startseite, Navigation, Produktseiten, Call-to-Actions, interne Suche, 404-Seite).
- **Off-Page** — nur perspektivisch erwähnt ("bei Bedarf externe Empfehlungen aufbauen"), kein konkretes Linkbuilding-Material im Ordner.

Hinweis: Es liegt **kein laufendes Reporting** (Monatsreports, Looker, GSC-Exporte) im Ordner — der Materialstand spricht für ein Onboarding-/Relaunch-Projekt 2021.

## SEO-Status & Befunde

Quellen mit Datum sind je Punkt genannt. Status-Quo-Aussagen stammen 1:1 aus den EOM-Analysen 2021.

### Technik (Quelle: "Initiale OnPage-Analyse Technik", 08.02.2021)

- **robots.txt:** Grundlegend korrekt im Root. *Maßnahme:* XML-Sitemap darin verlinken.
- **XML-Sitemap:** Zum Analysezeitpunkt **keine vorhanden**. *Maßnahme:* Sitemap erstellen, im Root ablegen, in robots.txt verlinken.
- **404-Seite:** Vorhanden, aber ausbaufähig. *Maßnahme:* erklärenden Text, Links/Suchschlitz zentraler, optional Bild.
- **SSL:** Vorhanden. *Maßnahme:* durchgehende Gültigkeit des Zertifikats sicherstellen.
- **Redirects:** http- und Trailingslash-Redirect vorhanden. *Maßnahme:* **http-Redirect von 302 auf 301 ändern**, www-Redirect nach Livegang prüfen.
- **Canonicals:** Stichproben zeigen vorhandene Canonicals. *Maßnahme:* nach Livegang vollständig prüfen, Self-Referencing-Canonical als Standard.
- **URL-Aufbau:** Sprechende URLs, Standards umgesetzt. **Flache Struktur** — alle Seiten auf gleicher Ebene (z. B. "Dämmputz" liegt direkt unter Root, obwohl über Innendämmung erreichbar). *Maßnahme:* granularere Verzeichnisstruktur zur Nutzer-Orientierung prüfen.
- **Seitenladezeit:** **Desktop und mobil zu langsam.** *Begründung:* bestätigter (mobiler) Rankingfaktor, Core Web Vitals gewinnen an Bedeutung; Bot crawlt langsame Seiten seltener. *Maßnahme:* Bildgrößen, Core Web Vitals, JS/CSS, Caching/GZip/HTTP-Version optimieren (Ansätze aus PageSpeed Insights).
- **Mobile:** Responsives Design vorhanden, aber Optimierungsbedarf (Schriftgrößen, Inhaltsbreite, Ladezeit). *Begründung:* Mobile-First-Indexing ab 03/2021. *Maßnahme:* GSC-Fehler/Warnungen prüfen und beheben.
- **hreflang:** Nicht nötig — nur deutsche Version geplant. *Maßnahme:* bei künftiger Mehrsprachigkeit berücksichtigen (Beispielsyntax DE/EN im Deck dokumentiert).

### Technik-Check nach Relaunch (Quelle: "Technik Check nach Relaunch", 13.07.2021)

- **404 + 301 intern verlinkt:** 9 Bilder nicht mehr vorhanden (404); zudem interne Verlinkungen auf 301-Weiterleitungen, v. a. über "mehr erfahren"-Buttons der Anwendungsgebiete. *Maßnahme:* Bild-Einbindung prüfen, interne Links direkt aufs korrekte Linkziel setzen. Belege: Sheets *"Epasit - 404-Bilder - 13.07.2021"* und *"Epasit - Internal All, PDFs, Bilder - 2021-07-13"* (Blatt 301er) sowie *"Interne Verlinkungen von 404-Bildern und 301-Weiterleitungen - 18.08.2021"*.
- **noindex + Canonical-Konflikt:** `/page/2`-URLs stehen auf noindex **und** zeigen per Canonical auf eine andere Seite. *Begründung:* widersprüchliches Signal — Google ignoriert dann den Canonical bzw. kann die kanonische URL nicht indexieren. *Maßnahme:* noindex auf diesen Paginierungs-URLs entfernen.
- **Index-Hygiene:** `/author/nils`, `/datenschutz`, `/impressum` sollten auf **noindex**. 134 PDFs stehen auf index — falls nicht ranking-relevant, auf noindex. Testseite `/trending` offline nehmen.
- **XML-Sitemap (`/sitemap.xml`):** enthält 404-Bilder. *Maßnahme:* nur indexierbare 200er-URLs aufnehmen; automatisierte Sitemap-Erstellung empfohlen (Beleg: *"XML-Sitemaps - Nonindexable URLs - 2021-07-13"*).
- **RSS-Sitemap (`/sitemap.rss`):** enthält nicht indexierbare URLs (404er, 301er, Canonicalised). *Maßnahme:* aktualisieren bzw. Notwendigkeit der RSS-Sitemap grundsätzlich klären.
- **404-Seite:** zwei Suchschlitze — der obere kann entfernt werden.
- **Weitere Crawl-Belege im Ordner:** *"Sitemaps Orphan URLs - 2021-07-13"*, *"XML-Sitemaps - URLs not in Sitemap - 2021-07-13"*, *"RSS Sitemaps - All URLs + URLs not in Sitemap - 2021-07-13"* (Orphan-/Sitemap-Abdeckungs-Analysen). Roh-Crawls in Unterordner **Crawls** (Crawl 20210630, Crawl 20210712).

### On-Page / Content (Quelle: Technik-Deck 08.02.2021 + Keywordrecherche)

- **Snippet/Title:** Title-Tag als wichtigster OnPage-Faktor betont; USPs/Vorteile/Sonderzeichen in Title & Meta-Description zur CTR-Steigerung nutzen.
- **Content-Standards:** genau eine H1, hierarchische H2–H6; interne Verlinkung mit Nutzermehrwert; Alt-Texte beschreibend + Keyword, nicht zu lang.
- **Keyword-Mapping vorhanden:** Die Keywordrecherche mappt Keywords inkl. notierter Suchvolumina (SV) auf konkrete Anwendungs-/Produkt-URLs. Höchste notierte SV-Werte u. a.: `pflasterfugenmörtel` (8.100), `horizontalsperre` (4.400), `wärmebrücken` (3.600), `innendämmung` (3.600), `schnellzement` (2.900), `balkonabdichtung` (2.400), `reparaturmörtel` (1.900), `schimmelsanierung` (1.300), `treppe sanierung` (1.300), `pflasterfugenmörtel wasserdurchlässig/-undurchlässig` (je 1.300), `dämmputz` (1.000), `feuchte wand sanierung` (1.000). *Hinweis:* SV-Zahlen sind 1:1 aus dem Kunden-Sheet 2021 übernommen, nicht neu erhoben — Aktualität ist offen (siehe Datenlücken).

### Usability (Quelle: "Initiale Usability-Analyse", 08.02.2021)

- **Startseite:** Produkte ggf. vor "Aktuelles" priorisieren; CTA mit Kontaktdaten einbauen; "Weitere Produkte/Referenzen"-Buttons wirken nicht wie Buttons; Bilder zu groß; mobil überlappende Kacheln + zu kleiner Text.
- **Interne Suche:** mobil nicht in der Navigation; Ergebnisseite wirkt erfolglos (Hinweis "Neue Suche benötigt" zu präsent, Ergebnisse erst nach Scroll); schlechter Kontrast; Suchschlitz dreifach vorhanden.
- **Navigation:** Produkte vs. Anwendungen unklar getrennt — beim Klick auf einen Anwendungsbereich weites Scrollen bis Produkte sichtbar. Trennung "Produkte | Anwendungen" prüfen.
- **Produktkategorie-Seiten** (SEO-zentral): Sprungmarken below the fold, leicht überscrollt; Sinnhaftigkeit weiterer Unterkategorien hinterfragen — eng mit Keyword-/Content-Struktur verzahnt.
- **Produktdetailseiten:** keine direkte Kontaktaufnahme/Außendienstsuche; Shop-Verlinkungen erwägen; Datenblatt doppelt verlinkt; mehr Anwendungsbilder.
- **Call-to-Action:** wichtigste Conversion (Kontaktaufnahme) ist zu schwach hervorgehoben und nicht auf jeder Seite vorhanden; besser Telefon/E-Mail/Formular direkt einbinden.
- **Außendienstsuche:** funktionierte nicht (führte zur internen Suchergebnisseite).
- **Footer:** auf manchen Seiten gestauchte/abweichende Produktkategorie-Links (z. B. `/edelputze`).

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten gefunden.** Der Ordner enthält ausschließlich klassisches technisches und On-Page-/Usability-Material aus 2021 — kein Material zu AI Overviews, ChatGPT/Perplexity-Zitierungen, LLM-Sichtbarkeit, Brand-Mentions in KI-Antworten oder `llms.txt`. GEO war zum Erstellungszeitpunkt der Dokumente noch kein Thema. Für eine GEO-Bewertung wäre eine separate, aktuelle Erhebung nötig (z. B. via [[Tools-Stack|Peec AI / Sistrix AI / DataForSEO LLM]]).

## Doc-Typen & Aufbau

Im Kundenordner `02_SEO` vorhandene Deliverable-Typen:

- **Google Slides (Analyse-Decks):** "Initiale OnPage-Analyse Technik", "Initiale Usability-Analyse" — Aufbau: Vorbemerkungen/Methodik → Befund je Faktor mit "Status Quo" + "To Do" → Abschluss + Haftungsausschluss.
- **Google Doc (Maßnahmen-Check):** "Technik Check nach Relaunch" — Fließtext-Maßnahmenliste mit Verweisen auf die belegenden Sheets.
- **Google Sheets (Crawl-/Daten-Exporte):** 404-Bilder, Internal-All/PDFs/Bilder, Sitemap-Analysen (Nonindexable, URLs-not-in-Sitemap, Orphan), RSS-Sitemap, interne Verlinkungen 404/301 — Screaming-Frog-typische Crawl-Exporte.
- **Google Sheet (Keyword-Mapping):** "Epasit - Keywordrecherche" — Spaltenstruktur Thema/Kategorie → Hauptkategorie-URL → Unterkategorie → Unter-Unterkategorie → Keywords inkl. SV.
- **Unterordner Crawls:** Roh-Crawls (Crawl 20210630, Crawl 20210712).

## Schreibstil-Notizen

- Durchgängig **Sie-Anrede** in der Kunden-Copy ("Bei der Content-Optimierung unterstützen wir Sie gerne…").
- Analyse-Logik klar nach **Status Quo → To Do** strukturiert (entspricht EOM-Muster Befund→Maßnahme).
- Fachsprache der Bauchemie/Sanierung wird vorausgesetzt (Horizontalsperre, Salpeterausblühungen, hygroskopische Salze, Reprofilierung) — Title/Meta und Content müssen diese Fachterme sauber treffen.
- KI-/AI-Schreibregel des Vaults gilt: durchgängig "KI" statt "AI".

## Offene Punkte / Datenlücken

- **Aktualität:** Sämtliche ausgewerteten Dokumente stammen aus **2021** (08.02.–24.08.2021). Ob die Befunde (fehlende XML-Sitemap, 302-http-Redirect, noindex/Canonical-Konflikt etc.) inzwischen behoben sind, ist aus dem Ordner **nicht** ersichtlich. Vor neuer Arbeit: aktueller Crawl + GSC-Abgleich nötig.
- **Office-Dateien:** Keine `.docx/.xlsx/.pptx` im Ordner — vollständige Datenbasis war exportierbar.
- **Sheet-Detailtiefe:** Die Crawl-Sheets (404-Bilder, PDFs, Orphan-URLs etc.) wurden nicht zeilenweise vollständig gelesen; bei Bedarf gezielt nachladen.
- **Suchvolumina/Rankings:** SV-Werte stammen aus dem Kunden-Sheet 2021 und wurden **nicht** neu verifiziert — nicht als aktuelle Werte verwenden. Keine Sichtbarkeits-/Ranking-/Backlink-Daten im Ordner.
- **Kein laufendes Reporting / keine GA4/GSC-Anbindungsdaten** im Ordner dokumentiert.
- **Kein GEO/KI-Material** (siehe oben).

## Quellen

Ausgewertete Dateien aus Drive-Ordner `epasit GmbH / 02_SEO` (Account ben@eom.de):

1. **Initiale OnPage-Analyse Technik** (Google Slides, 08.02.2021) — `18OKd7Ws4fKU4OAU2FgjBzUyNefQCD0F1_ZzL_rME2RE`
2. **Technik Check nach Relaunch** (Google Doc, 13.07.2021) — `1Eg2lgpiwBCJXmjg6HxMnQxdkefAdKrxxeVHStkDB5hs`
3. **Initiale Usability-Analyse** (Google Slides, 08.02.2021) — `1feWWYbDF68BpC7v51f9B4F0ief940D2iKahLayHOpzk`
4. **Epasit - Keywordrecherche** (Google Sheet, 24.08.2021) — `1lobx07FlYSVhPEFsf3EGfXoU-CnM8MMkVMGfVD6Zm68`

Im Ordner vorhanden, als Belege referenziert (nicht zeilenweise gelesen): *404-Bilder 13.07.2021*, *Internal All/PDFs/Bilder 2021-07-13*, *RSS Sitemaps All URLs 2021-07-13*, *Sitemaps Orphan URLs 2021-07-13*, *XML-Sitemaps Nonindexable URLs 2021-07-13*, *XML-Sitemaps URLs not in Sitemap 2021-07-13*, *Interne Verlinkungen 404-Bilder/301 18.08.2021*, Unterordner *Crawls* (20210630, 20210712).
