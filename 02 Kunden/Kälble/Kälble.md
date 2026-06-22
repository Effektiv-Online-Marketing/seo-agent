---
tags: [kunde, seo]
kunde: "Kälble"
stand-Datum: 2026-06-19
---

# Kälble

> [!warning] Datenstand & Aktualität
> Alle ausgewerteten Unterlagen stammen aus **Oktober–Dezember 2020**. Es liegen **keine aktuellen** Rankings, Sichtbarkeits-, Traffic- oder Backlink-Daten und **keine GEO/KI-Daten** vor. Diese Notiz gibt den dokumentierten Stand von 2020 wieder und markiert offene Punkte. Für eine belastbare heutige Bewertung wäre eine Neuerhebung (Sistrix/GSC/Ahrefs/Crawl) nötig.

## Überblick

- **Kunde:** Anwaltskanzlei **Kälble & Kollegen** (in den Unterlagen auch „Kälble & Partner" genannt; abgestimmte Schreibweise laut Kunden-Call: **„Anwaltskanzlei Kälble & Kollegen"**).
- **Branche:** Rechtsanwaltskanzlei / Rechtsberatung.
- **Domain:** `kanzlei-kaelble.de` (WordPress, Theme **Enfold**; Plugins u. a. RevSlider, Download-Manager).
- **Standort:** Hannover.
- **Ausrichtung:** Bundesweit tätig, fachlich **stark spezialisiert**. Zielgruppe laut Call sind **Pflegeeinrichtungen** (nicht Pflegebedürftige). Schwerpunkte: **Pflegerecht, Heimrecht, Arbeitsrecht, Pflegestrafrecht, Sozialversicherungsrecht, Vorsorge-/Seniorenrecht**.
- **Besonderheit:** Verbundene/zweite Domain **`kanzlei-rokahr.de`** (RA Rokahr, mittlerweile Teil der Kanzlei) mit guten Rankings im **Strafrecht**.

## Mandat & Gewerke

Das ausgewertete Material entspricht einer **initialen SEO-Erstanalyse / Onboarding-Phase** (Projektteam EOM: Maja, Ernest, Sinah; Projektauftrag „Webseite anschauen und allgemeine Ideen ausarbeiten"). Abgedeckte Gewerke:

- **Technisches SEO:** Indexierungs-Audit, PageSpeed-Analyse.
- **On-Page / Content:** Title/Meta, Überschriftenstruktur, WDF\*IDF, interne Verlinkung, Keyword-Empfehlungen je Seite.
- **Strategie:** Domain-Konsolidierung (Rokahr) und Bewertung mehrerer Schwerpunkt-Domains.
- **Conversion-Rate-Optimierung (CRO):** Call-to-Actions, Kontaktwege.

Kein Hinweis auf laufendes Monatsreporting, Off-Page-/Linkaufbau-Mandat oder GEO/KI-Arbeit. Wirkt wie **Projekt-/Beratungsleistung**, nicht wie laufendes Retainer-Mandat.

## SEO-Status & Befunde (Stand 2020)

### Technik — Indexierung
*(Quelle: Sheet „kanzlei-kaelble.de – Empfehlung indexierte Seiten", Stand 06.11.2020; On-Page-Doc 10/2020)*

- **Befund:** Laut Google ~248 Seiten indexiert. Im geprüften Datensatz von **377 URLs** empfiehlt EOM nur **66 weiter zu indexieren** und **312 zu deindexieren**.
- **Begründung:** Viele Tag-, Kategorie-, Bild- (.jpg) und Redirect-URLs (301, teils noch `iso-8859-1`) im Index → **Duplicate Content** durch zu lange Vorschautexte, kein Optimierungspotenzial.
- **Maßnahme:** Index bereinigen — Tag-Seiten auf `noindex, follow`, Bilder/PDF/Kategorie-Seiten deindexieren; bei WordPress Vorschau über `<!-- more -->` kürzen.

### Technik — PageSpeed
*(Quelle: Doc „kanzlei-kaelble.de – PageSpeed Analyse", 16.11.2020; Tools: PageSpeed Insights + WebPagetest)*

- **Befund:** Startseite **Mobile 19/100** (≈5,8 s Ladezeit, „langsam"), **Desktop 54–57/100**. Server-Erstreaktionszeit ~**1,3 s** (Ziel ~200 ms). 25 rendering-blockierende Ressourcen; Logo lädt erst an Position 51 im Wasserfall.
- **Begründung:** PageSpeed ist offizieller Rankingfaktor; hohe Ladezeit erhöht Absprungwahrscheinlichkeit.
- **Maßnahme:** Render-blockierende CSS/JS beseitigen, Serverantwortzeit senken, Bilder in **WebP** + korrekte Ladeabfolge (First View zuerst), nicht genutztes CSS/JS entfernen/komprimieren, Lazy-Loading.

### On-Page — Title/Meta
*(Quelle: SEO-Audit-Slides 09.12.2020 + On-Page-Doc 10/2020)*

- **Befund:** Title-Tags wirken automatisch generiert (z. B. „Anwaltskanzlei Kälble & Kollegen: Startseite"), ~**11 %** überschreiten 60 Zeichen, **Duplikate** bei Title und Meta-Description (u. a. Leistungs- vs. Schwerpunktseite Scheinselbständigkeit), teils **fehlende** Descriptions, **kein einheitlicher Suffix**, keine Handlungsaufforderung.
- **Begründung:** Title = wichtiger Rankingfaktor; Description steuert die CTR; Duplikate wertet Google ab.
- **Maßnahme (Beispiel Startseite):**
  - SOLL-Title: `Fachanwälte aus Hannover | Anwaltskanzlei Kälble & Kollegen`
  - SOLL-Description: `Anwaltskanzlei Kälble & Kollegen aus Hannover: Ihre Fachkanzlei für Arbeits-, Heim- & Pflegerecht ✓ bundesweite Beratung ✓ Jetzt Termin vereinbaren!`
  - Einheitliches Suffix „Anwaltskanzlei Kälble & Kollegen", Haupt-Keyword vorne, lokaler Bezug Hannover, CTA in Description.

### On-Page — Struktur & Content
*(Quelle: On-Page-Doc 10/2020)*

- **Befund Startseite:** Keine `<h1>`/`<h2>` (nur `<h3>` + ein leeres `<h4>`), dünner Content, Haupt-Keyword fehlt als Exact Match, kein lokaler Bezug.
- **Befund Leistungsseite Vorsorgerecht** (URL `…/leistungen/seniorenrecht/`): keine `<h1>`, Keyword nur 2× im Text, **keine internen Content-Links** auf die Seite. Empfehlung URL → `…/leistungen/vorsorgerecht/`.
- **Befund Schwerpunktseite Pflegesatzverhandlung:** kaum Inhalt (nur verlinkte Gliederung), Bild ohne Alt-Text/sprechenden Dateinamen (`Spider-Luis-II-300x185.jpg`).
- **Maßnahme:** Saubere Heading-Hierarchie (1× `h1`, dann `h2`/`h3`), Content-Ausbau, **WDF\*IDF-Terme** je Seite einarbeiten, Bilder mit Alt-Text + sprechenden Dateinamen, **interne Verlinkung mit Keyword-Linktext** (statt „hier"), Blogartikel auf passende Leistungsseiten verlinken.

### Keywords (dokumentierte Suchvolumina aus den 2020er-Unterlagen)
*(Quelle: Audit-Slides + On-Page-Doc; Werte wie im Dokument angegeben — nicht neu erhoben)*

- Startseite: `anwaltskanzlei hannover` (210), `kanzlei hannover` (260), `rechtsanwaltskanzlei hannover` (90).
- `vorsorgerecht` (70), `seniorenrecht` (70).
- `pflegesatzverhandlung` (SV 390; Blogartikel rankte damals ~Platz 9–10, Schwerpunktseite noch nicht).
- Pflegerecht-Cluster: `anwalt pflegerecht` (110), `rechtsanwalt pflegerecht` (70), `fachanwalt pflegerecht` (30).
- Arbeitsrecht-Cluster: `rechtsanwalt arbeitsrecht` (6.600), `anwalt arbeitsrecht hannover` (480), `rechtsanwalt arbeitsrecht hannover` (210).
- Heimrecht: `anwalt heimrecht` (320).
- Empfohlene Methodik: Haupt-Keyword je Seite, Platzierung in Title/Meta/H1/erstem Absatz/Alt-Tags/URL; WDF\*IDF zur semantischen Ergänzung.

### Strategie — Domain-Architektur
*(Quelle: Audit-Slides + Fragenkatalog)*

- **Rokahr-Domain:** EOM rät vom Zusammenschluss **ab** — Strafrecht-Rankings würden bei Weiterleitung auf die inhaltlich abweichende Kälble-Seite verloren gehen. Empfehlung: `kanzlei-rokahr.de` bestehen lassen, zuerst die Kälble-Seite mit Content stärken.
- **Mehrere Schwerpunkt-Domains** (Pflegestrafrecht, Scheinselbständigkeit, Heimrecht, Pflegerecht, Corona-Arbeitsrecht): EOM rät **ab** — Verwaltungsaufwand, Kannibalisierung/Duplicate Content, gestreute Linksignale. Stattdessen **eine** Domain mit **Silo-Struktur** (`/schwerpunkt1/unterseiten`) ausbauen.

### CRO
- **Befund:** Fehlende CTAs; Telefonnummer/Anfahrt im Footer nicht verlinkt; Impressum in der Mobilansicht nicht erreichbar; Navigation mit 9 Punkten (Faustregel ≤8).
- **Maßnahme:** CTA-Elemente (Buttons/Störer) auf allen Seiten, Telefon-/Maps-Verlinkung, Impressum mobil im Footer, Menü verschlanken (Startseite raus, Newsletter unter „Service"); ggf. A/B-Tests.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Die Unterlagen stammen aus 2020 und enthalten keinerlei Bezug zu AI Overviews, ChatGPT/Perplexity-Zitierungen, LLM-Sichtbarkeit, `llms.txt` oder KI-Crawlern. GEO ist für diesen Kunden bislang **kein Thema** im dokumentierten Material und wäre ein potenzielles, noch unbearbeitetes Gewerk.

## Doc-Typen & Aufbau

Der Kundenordner ist **flach** (keine Unterordner) und enthält ausschließlich Google-Formate aus 2020:

| Doc-Typ | Datei | Format | Stand |
|---|---|---|---|
| Onboarding-Briefing | Briefing | Doc | 11/2020 |
| Brainstorming | Brainstorming | Doc | 11/2020 |
| Kunden-Rückfragen + Call-Notizen | Fragen an Kanzlei Kälble und Partner | Doc | 11/2020 |
| SEO-Audit (Hauptdeliverable) | Kanzlei Kälble & Partner \| SEO Audit | Slides | 12/2020 |
| On-Page-Empfehlung (unfertig) | kanzlei-kaelble.de – OnPage Empfehlung (nicht fertig) | Doc | 11/2020 |
| PageSpeed-Analyse | kanzlei-kaelble.de – PageSpeed Analyse | Doc | 11/2020 |
| Indexierungs-Empfehlung | kanzlei-kaelble.de – Empfehlung indexierte Seiten | Sheet | 11/2020 |

Typischer Aufbau (Audit-Slides): nummerierte Sektionen (01 OnPage, 02 …, 03 CRO), Logik **Problem/Befund → Begründung → Empfehlung**, IST-/SOLL-Gegenüberstellung bei Title/Meta/H1. Das Indexierungs-Sheet folgt: URL → IST-Status → Befund/Empfehlung → SOLL (`index`/`noindex`).

## Schreibstil-Notizen

- **Sie-Anrede** durchgängig; Tonalität sachlich-beratend.
- **Befund → Begründung → Maßnahme** als feste Analyse-Logik (deckt sich mit EOM-Methodik).
- Meta-Descriptions arbeiten mit **Trust-Häkchen ✓** und **Pfeil-/CTA-Elementen (▶ ⇒)** sowie klarer Handlungsaufforderung („Jetzt Termin vereinbaren!").
- Kundenspezifisch: konsequent **„Anwaltskanzlei Kälble & Kollegen"** als Marken-/Suffix-Schreibweise.
- **Bundesweiter** Bezug betonen, lokalen Bezug (Hannover) ergänzend für die Startseite — beide Ausrichtungen laut Call gewünscht (Schwerpunkt: bundesweit, Zielgruppe Pflegeeinrichtungen).

## Offene Punkte / Datenlücken

- **Veraltung:** Gesamter Wissensstand = 2020. Heutiger Status von Rankings, Sichtbarkeit, Traffic, PageSpeed und Indexierung **unbekannt**.
- **Umsetzungsstand:** Nicht dokumentiert, welche Empfehlungen (Title/Meta, Index-Bereinigung, PageSpeed, URL-Umzug Seniorenrecht→Vorsorgerecht) tatsächlich umgesetzt wurden.
- **Keine Tool-Daten im Ordner:** keine Sistrix-/Ahrefs-/GSC-/GA4-Exporte; SV-Werte stammen aus den 2020er-Dokumenten und sind nicht verifiziert.
- **On-Page-Doc ausdrücklich „nicht fertig"** — einzelne SOLL-Felder (Alt-Texte, Dateinamen, interne Linkquellen) blieben leer.
- **GEO/KI komplett offen.**
- **Mandatsstatus unklar:** ob das Mandat heute noch aktiv ist, ist aus dem Material nicht ersichtlich.
- **Office-Dateien:** Im Ordner lagen keine `.docx/.xlsx/.pptx` — alle Dateien waren als Google-Format exportierbar und wurden gelesen.

## Quellen (ausgewertete Dateien)

Alle aus Google Drive (Account `ben@eom.de`), Ordner-ID `1LIrpdVEQBZivma39YlLVfJe42jtxC2RS`:

1. **Kanzlei Kälble & Partner | SEO Audit** (Slides, 09.12.2020) — Hauptaudit: Strategie, On-Page, CRO.
2. **kanzlei-kaelble.de – OnPage Empfehlung (nicht fertig)** (Doc, 11/2020) — Title/Meta/H1, WDF\*IDF, interne Links, Keyword-Ideen.
3. **kanzlei-kaelble.de – PageSpeed Analyse** (Doc, 16.11.2020) — Ladezeit-Befunde Mobile/Desktop.
4. **kanzlei-kaelble.de – Empfehlung indexierte Seiten** (Sheet, 06.11.2020) — 377 URLs, Index-/Noindex-Empfehlung.
5. **Fragen an Kanzlei Kälble und Partner** (Doc, 11/2020) — Kunden-Rückfragen + Call-Notizen (Ausrichtung, Schreibweise, Zielgruppe).
6. **Briefing** (Doc, 11/2020) — Projektauftrag, Team, Kundenideen.
7. **Brainstorming** (Doc, 11/2020) — interne Ideensammlung.

Verwandt: [[SEO-Methodik]], [[Schreibstil]], [[Tools-Stack]]
