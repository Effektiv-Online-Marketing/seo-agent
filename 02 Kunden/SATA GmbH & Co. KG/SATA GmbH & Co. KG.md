---
tags: [kunde, seo]
kunde: "SATA GmbH & Co. KG"
stand-Datum: 2026-06-19
---

# SATA GmbH & Co. KG

> Wissensdatei für SEO/GEO. Quellen sind ausschließlich Google-Drive-Dokumente aus dem SATA-Kundenordner (Account `ben@eom.de`). Nichts geschätzt; nicht zugängliche Daten sind als Lücke markiert.

## Überblick

- **Wer:** SATA GmbH & Co. KG — Hersteller hochwertiger Lackier-/Spritzpistolen (Profi-Werkzeug für Lackierer). Produktwelt rund um die neue Lackierpistole **SATAjet X** und Begleitprodukte (Atemschutzmaske, Lackierbecher/Liner Cup System, Lackieranzug/suit standard, airStar F2).
- **Branche:** Industrie / Werkzeug-Hersteller (Oberflächentechnik, Lackiertechnik). Zielanwendungen reichen von Autolackierung (Refinish) über Handwerk (Schreiner/Holz) bis Maschinenbau/Metallbau.
- **Domains/Sprachen:**
  - Haupt-Domain: `https://www.sata.com/de-dat/` (Sprachverzeichnisse).
  - Microsite: `https://jetx.sata.com/jetx` (für die EOM-Betreuung initial der relevante Bereich).
  - Geplante/dokumentierte Sprach-Märkte (Stand 18.12.2024): USA, CA, UK, DE (ggf. AT), PL — wobei im Sprachmenü Inkonsistenzen auftraten (PL fehlte, IT erschien). hreflang mit `x-default` global.
  - CMS-Historie: Microsites zuerst Contao geplant, kurz vor Livegang auf **TYPO3** umgestellt (inkl. Agenturwechsel). Kommender Shop unter sata.com mit **Shopware**. Technik-Dienstleister: ixomo (Oliver Sigmund).

## Mandat & Gewerke

Aus [[Projektübergabe SATA]] und Meeting-Notizen ableitbar:

- **SEO-Begleitung Microsites/Relaunch** (punktuell/projektbezogen, nicht durchgängiges Retainer-SEO): On-Page-Empfehlungen, technische SEO-Einschätzungen zu Sketches/Relaunch, Keyword-Recherchen.
- **SEA:** laufende Kampagnen US und DE für jet X, Mediabudget max. 5.000 €/Monat (zwei Kampagnen). Tracking via **Matomo** (kein GA4 möglich), Conversion-Import nach Google Ads bisher nicht gelungen.
- **Relaunch-Projekt SATA (2025):** kein klassischer Relaunch, sondern digitales Gesamtprojekt — kombinierte **Anwendungs-/Produktseiten** (sollen für SEO funktionieren + Shop-Element enthalten), reguläre Produktseiten bewusst **noindex** (nur interne Auffindbarkeit). Externer Berater: Jan Günther. Content-Erstellung der Anwendungsseiten **mit LLM** geplant.
- **Selbstständigkeit-Niveau** des Kunden: niedrig; Stefan Schempp (Leiter Digital Business, früher HERMA) hat EOM an Bord geholt, legt großen Wert auf EOM-Meinung.
- **Ansprache:** "Du" (siehe Kundenkonvention unten).

## SEO-Status & Befunde

### SEO-Kurzcheck (Quelle: `2024-09_SATA_SEO-Kurzcheck`, 17.09.2024)
Befund → Begründung → Maßnahme:
- **Indexierung lückenhaft** — z. B. DE-LCS (Liner Cup System) nicht im Index → fehlende Sichtbarkeit. **Maßnahme:** GSC einrichten für Index-Steuerung & Monitoring.
- **Ladezeit sehr hoch** — Desktop 50/100, Mobil 28/100 (Quelle nennt keine Tool-Herkunft) → Ranking-/UX-Risiko. **Maßnahme:** Performance-Optimierung.
- **Meta-Daten fehlen.** **Maßnahme:** Title/Description nachpflegen.
- **Überschriftenstruktur nicht ideal** — mehrere H1, Hierarchie nicht eingehalten. **Maßnahme:** saubere H1→H2-Struktur.
- **Bilder** ohne Alt-Texte/sprechende Dateinamen. **Maßnahme:** Alt-Texte, Dateinamen, ggf. Bildtitel pflegen.
- **404-Fehler** — z. B. `https://jetx.sata.com/en-ca/translate-to-en-ca-jet-x` (zusätzlich noch in hreflang gelistet); Sprachwechsel von 404-Seite führt erneut auf 404. **Maßnahme:** Fehler beheben, aus hreflang entfernen.
- **Keine robots.txt und Sitemap.** **Maßnahme:** beides anlegen.
- **hreflang fehlerhaft** — falsche Länder-/Sprachauszeichnungen, 404 enthalten, falsche `x-default`-URL. **Maßnahme:** korrigierter hreflang-Block dokumentiert (en-GB, de-DE, fr-FR, en-US, es-US, fr-CA, en-CA, it-IT, x-default). Hinweis: Seiten ohne alle Sprachversionen (airStar, suit standard) dürfen die fehlende Sprache nicht in hreflang führen.

### Relaunch SEO-Blick auf Sketches (Quelle: `20250522_SATA_Relaunch_SEO-Blick`, Mai 2025)
Strukturierter Anforderungs-/Fragenkatalog an Relaunch-Konzept (Sketch-Phase):
- **Navigation/URL:** alle Navigationspunkte hart im HTML (`<nav>` + Listen), keine JS-Nachladung; klare URL-Struktur; klären ob URL/SEO-Text bei Variantenwahl bzw. Produktfinder-Auswahl wechselt; Trennung Produktdetailseite vs. PDP-Anwendungsfall (eigene, indexierbare URLs?).
- **Überschriften:** H1-Definition pro Seitentyp klären; Hero-Überschrift vs. Produkt-Überschrift sauber als H1/H2 auszeichnen.
- **SEO-Texte/Content-Module:** mehrere Textblöcke je Seite ermöglichen; Module für Listen/Tabellen; Startseite mit Fließtext.
- **Linktexte:** generische Anker wie "Mehr erfahren" vermeiden, Keywords nutzen; interne Links aus Fließtext ermöglichen.
- **Auslesbarkeit durch Google & KIs:** möglichst kein JavaScript für Inhalts-Elemente (Hilfstexte, Technik-Kacheln) → wichtig für GEO.
- **Indexsteuerung:** Suchergebnisseiten, Checkout-/Bestellschritte, "Mein Konto", Affiliate auf **noindex**.
- **Strukturierte Daten (JSON-LD), allgemeine Empfehlung:** FAQ, Breadcrumb, Produkt (pro Produkt im `@graph`, nicht pauschal für Liste), Organisation auf Startseite; Entitäten-Verknüpfung via `sameAs`/`mentions` zu eindeutigen Entitäten (Wikipedia-Beispiele Fließbecherpistole/Spritzpistole) — explizit als Mittel, "Google & KIs" das Thema eindeutig mitzuteilen.
- **Bilder:** `srcset`/`sizes` und Alt-Texte vorsehen.
- **Mehrsprachigkeit:** Umsetzung über Sprachverzeichnisse; hreflang inkl. `x-default`.

> Hinweis: Such-Plugin Bloomreach Discovery (Search Intelligence) bleibt gesetzt; Checkout mit mobilem Kontrastproblem (schwarzer Hintergrund) angemerkt (UX, nicht SEO).

## GEO / KI-Sichtbarkeit

GEO ist bei SATA **operativ verankert**, jedoch über LLM-gestützte Content-Produktion, nicht über Monitoring (kein Peec/AI-Visibility-Tooling dokumentiert):

- **LLM-Content-Prozess:** Die Anwendungsseiten im Relaunch sollen **mit einem LLM erstellt** werden (Quelle: Projektübergabe + Kick-off 27.05.2025). Bilderstellung erfolgt nach der Texterstellung; Bildquellen: Marketing-Pool (v. a. Refinish), Stock, KI-Erstellung + Nachbearbeitung.
- **KI-Auslesbarkeit als SEO-Anforderung:** Im Relaunch-SEO-Blick wird mehrfach gefordert, dass Inhalte ohne JavaScript für "Google & KIs" auslesbar sind und Entitäten (`sameAs`/`mentions`) gesetzt werden, damit KIs das Seitenthema eindeutig erkennen.
- **LLM-Keyword-Recherche** (Quelle: `202412_SATA_KWR_Anwendungen_LLM`, Stand 01/2025): EOM-Recherche nach Keywords mit Google-DE-Suchvolumen, strukturiert nach **Branche → Anwendung → Keyword → SV → Wettbewerber (Sistrix)**. Branchen u. a.: Handwerk/Schreiner (z. B. "holz lackieren" 2.900, "lackierung von möbeln" 1.600, "möbel lackieren sprühen oder streichen" 210) und Maschinenbau/Metallbau (z. B. "stahlträger lackieren" 210, "chromteile lackieren" 170). Dient als Themen-/Anwendungsgerüst für die LLM-Anwendungsseiten.
- **Keine GEO-Messdaten gefunden:** Keine AI-Overview-/ChatGPT-/Perplexity-Zitations- oder Sichtbarkeitsmessung im Ordner vorhanden.

## Doc-Typen & Aufbau

Im SATA-Ordner liegende Deliverable-Typen:

- **On-Page-Empfehlungen (Google Doc)** — pro Produkt/Seite (`2024-07_SATA_OnPage_<Produkt>`: jetX, airStar F2, Liner Cup System, suit standard, Übersicht Neuheiten). Aufbau: URL → Fokus-Keywords → Neben-Keywords → Semantische Begriffe (ergänzen/verstärken) → mögliche Inhalte → **Meta-Daten (Title + Description)** → ausformulierter Text je Modul (Hero/H1, Intro, Abschnitte).
- **Keyword-Recherchen (Google Sheets)** — `2024-07_SATA_KWR_Produktneuheiten` und `202412_SATA_KWR_Anwendungen_LLM`. Spalten u. a. Branche, Anwendung, Keyword, SV (Google DE), Wettbewerber (Sistrix).
- **Technische/SEO-Einschätzungen (Google Doc)** — `SEO-Kurzcheck`, `Relaunch_SEO-Blick`. Befund-/Fragen-Listen mit konkreten technischen Anweisungen (hreflang-Snippets, JSON-LD-Empfehlungen).
- **Meeting-Notizen (Google Doc + PDF/Screenshots)** — Kick-offs (jetX, Contenterstellungsprozess), digitale Roadmap.
- **Orga (Google Sheets)** — `Projektübergabe SATA`, `Allgemeine Projektinfos`.
- **Microsite-Texte (.docx)** — z. B. `Microsite_Texte_sci_Cn.docx` (Office-Format, per Drive nicht als Text exportierbar — nur per Name gewertet).

Markup-Konvention: Reine Text-Uploads übertragen kein Farb-Markup; technische Empfehlungen werden inline als HTML/JSON-LD-Snippets im Doc gepflegt.

## Schreibstil-Notizen

- **Anrede: "Du"** (Kundenkonvention laut Projektübergabe: "Ansprache Kunde: Du"). Abweichung von der EOM-Standard-Sie-Anrede — bei SATA-Copy konsequent duzen. ("KI" statt "AI" bleibt Standard.)
- **Tonalität:** technik-/nutzenorientiert, profi-gerichtet ("Profi-Lackierpistole", "überlegene Zerstäubung", "perfekte Spritzbilder"), Anwender im Fokus ("Die Lackierpistole, die für Dich arbeitet").
- **Title-Konvention (Beispiel jetX):** `SATA jet X: Die Profi-Lackierpistole für erstklassige Ergebnisse` — Marke + Produktname + Nutzenversprechen, mit Doppelpunkt.
- **Description-Konvention (Beispiel):** `Entdecke die SATA jet X Lackierpistole mit überlegener Zerstäubung, digitalen Funktionen & verbesserter Ergonomie. Perfekt für höchste Qualität und Effizienz.` — Verb-Einstieg ("Entdecke"), Feature-Aufzählung, Nutzen-Abschluss.
- **Markenschreibweise:** "SATA jet X" / "SATAjet X" (uneinheitlich in den Docs), Produktnamen klein (jetX, airStar F2, suit standard).

## Offene Punkte / Datenlücken

- **Kein durchgängiges SEO-Tooling:** GSC nicht eingerichtet (nur angedacht), Sistrix bisher nur punktuell genutzt, kein Looker Studio. Kein GA4 (DSGVO-Gründe) → Tracking via Matomo; Conversion-Import nach Google Ads ungelöst.
- **Keine Rankings/Sichtbarkeitsindex/Backlink-Daten** im Ordner vorhanden — daher hier keine Performance-Aussagen.
- **Keine GEO-Messung** (AI Overviews/LLM-Zitate) dokumentiert.
- **Relaunch-Status offen:** Go-Live war zum Erfassungsstand mit 02.11.2025 geplant (Stand Kick-off 05/2025); aktueller Live-/Index-Status nicht aus den Docs verifizierbar.
- **Office-Dateien (.docx/.xlsx)** nicht per Drive-Export auslesbar (z. B. Microsite-Texte) — nur per Name berücksichtigt.
- **KPI-/Conversion-Ziele unklar** ("tbd - irgendwie alles: Reichweite, Leads, Käufe"), keine KPI-Vorgaben.

## Quellen

Ausgewertete Drive-Dateien (Ordner `14SpjHQeqrsCetDtAe5RWoBY5RJ0fhWfW`):

- `20250522_SATA_Relaunch_SEO-Blick` (Google Doc, Mai 2025) — technischer SEO-Anforderungskatalog Relaunch.
- `2024-09_SATA_SEO-Kurzcheck` (Google Doc, 17.09.2024) — technischer Kurz-Audit Microsite.
- `SATA | Kick-off Contenterstellungsprozess Anwendungsseiten | 27. Mai 2025` (Google Doc) — LLM-Content-Prozess, Long-Tail, Roadmap.
- `202412_SATA_KWR_Anwendungen_LLM` (Google Sheet, 01/2025) — Keyword-Recherche je Branche/Anwendung für LLM-Anwendungsseiten.
- `2024-07_SATA_KWR_Produktneuheiten` (Google Sheet) — Keyword-Recherche Produktneuheiten (per Name/Struktur gewertet).
- `2024-07_SATA_OnPage_jetX` (Google Doc) — On-Page-Empfehlung inkl. Title/Meta/Struktur (Schreibstil-Referenz).
- `202506_Projektübergabe SATA` (Google Sheet, 06/2025) — Mandat, Ansprechpartner, Tooling, Historie.
- Weitere im Ordner (per Name gewertet): OnPage airStar F2 / Liner Cup System / suit standard / Übersicht Neuheiten, `20241205-SATA-Digitale-Roadmap`, `20240708_Microsite_Texte_sci_Cn.docx`.
