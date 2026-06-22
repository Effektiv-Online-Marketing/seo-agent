---
tags: [kunde, nibe, doc-aufbau, vorlage]
status: aktiv
quelle: Google Drive (02_SEO / 03_Content / 08_Reportings / 10_Strategie), gelesen 18.06.2026
---

# NIBE — Doc-Aufbau

Wiederkehrende Dokument-Strukturen der NIBE-Deliverables, je Doc-Typ als Vorlage beschrieben. Basis: gelesene Original-Docs aus Google Drive (Dateinamen genannt). Ergänzt [[NIBE]] und [[NIBE — Schreibstil]]; Methodik-Bezug: [[SEO-Methodik]].

Allen Docs gemeinsam:
- **Fußzeile fix:** „EOM – Effektiv Online-Marketing GmbH / Bödekerstraße 85 in 30161 Hannover [+ ggf. Seelbergstraße 4 in 70372 Stuttgart] / Registergericht Hannover HRB 204938, Geschäftsführer Ernest Mavriqi".
- Master-Logik **Befund → Begründung → Maßnahme** (= **IST / SOLL / Warum** aus *01 EOM Agency Vorlage Word*).
- Kollaboration im Google Doc statt PDF-Abgabe.

---

## 1) Content-Empfehlung / On-Page-Optimierung
Beispiele: *NIBE | Empfehlung zu /waermepumpe*, *NIBE | Empfehlung Aufschlüsselung der Kosten*, *NIBE | /pvt - Aktualisierung 2025/2026*

**Aufbau:**
1. **Titel** — „Empfehlung zu /<slug>" oder „Empfehlung [Thema]".
2. **`URL:`** der Zielseite (vollständig, `…/de-de/…`).
3. **Legende** des Farb-Markups: „Grün: neu / Gelb: angepasst" (bei Bedarf „Durchgestrichen: entfernen").
4. **Hinweis-Satz** zum Scope, z. B. „Die Empfehlung beinhaltet nur Abschnitte, in denen etwas angepasst werden sollte."
5. **`Content`** — der eigentliche Vorschlag mit inline `<h1>…<h4>` Tags in Live-Reihenfolge.
6. **[Regieanweisungen in eckigen Klammern]** (Layout, Bilder, CTA-Platzierung, Sprungmarken, offene Rückfragen).
7. **Quellenangabe** am Ende (Fachbuch mit Seitenzahl / Studie).

**Mini-Skelett:**
```
[Titel: Empfehlung zu /slug]
URL: https://www.nibe.eu/de-de/...
Legende: Grün = neu · Gelb = angepasst · Durchgestrichen = entfernen
Content
<h1> … (+ Subline)
<h2> Das Wichtigste in Kürze zu …
  * Schlagwort: Erklärung
<h2> Erklärblöcke / Tabellen / Fazit von NIBE
<h2> Häufig gestellte Fragen
  <h3> Frage? → Antwort
Quellen: …
```

---

## 2) Schwellenkeyword-Optimierung
Beispiel: *NIBE | Schwellenkeyword-Optimierung /foerderung*

Wie (1), aber Kopf erweitert um **Keyword-Tabelle mit Potenzial**:
- `Keywords:` Liste mit **`SV.` (Suchvolumen)** und **`Pos.` (aktuelle Position)**, z. B. „zuschuss wärmepumpe — SV. 1150 — Pos. 17".
- Logik dahinter: Seiten/Keywords auf Position ~11–20 („Schwelle" zu Seite 1) gezielt nachschärfen.
- Danach derselbe Content-Block mit Farb-Markup wie Typ (1).

---

## 3) Nachoptimierung (bestehende Seite)
Beispiel: *NIBE | Nachoptimierung /waermepumpe-abstand*

**Aufbau:**
1. Titel „Nachoptimierung /<slug>".
2. `URL:`.
3. **`Keywords`** gegliedert in **Hauptkeyword(s)** und **Nebenkeywords**, je mit `SV.` (oft lange Long-Tail-Liste, regional aufgefächert).
4. **`Metas`** — Status-Vermerk, z. B. „bleiben unverändert".
5. **`Content`** mit voller 3-Farben-Legende (Gelb=Anpassung, Grün=neu, Durchgestrichen=entfernen).
6. Bestehende Passagen werden **im Original gezeigt und markiert** (alte vs. neue Fassung sichtbar), inkl. Tabellen (z. B. Bundesland-Übersicht) und FAQ.
7. „Fazit von NIBE" + FAQ als Abschluss.

---

## 4) Technik-/SEO-Audit
Beispiel: *NIBE | SEO Technik Check Teil 1*

**Aufbau:** thematische **Befund-Blöcke**, je als Überschrift + Problem + konkrete Maßnahme:
- Muster pro Block: *Befund* (z. B. „FAQs ergeben eigene Seiten" → Duplicate Content) → *Maßnahme* (z. B. „per 301 auf … weiterleiten, sonst noindex") → betroffene **URL-Liste**.
- Typische Themen: Orphan Pages / „Seiten ohne eingehende Links", interne Verlinkung, 301-Redirects, FAQ-Duplikate, Local-SEO-Seiten.
- Enthält fertige **Verlink-Vorschläge** (Quell-URL, Ankertext, Zielseite) und einbaufertige Textbausteine (Gelb=Link im Bestand, Grün=neu).
- Redirect-Grundregel (siehe [[NIBE]]): defektes Ziel per 301 auf thematisch passende Live-Seite, **nie** auf Startseite.

---

## 5) Title-/Meta-/H1-Tabelle (Spreadsheet)
Beispiel: *NIBE - /produkte/-URLs Meta Daten + H1*

**Spalten (fix):**
`Bereiche | Adresse (URL) | Weitere ToDos für die Seite | H1 ALT | H1 NEU | Titel ALT | Title NEU | Meta Description ALT | Meta Description NEU`

- **ALT/NEU-Spaltenpaare** zeigen Ist → Soll je Element.
- Spalte „Weitere ToDos" trägt technische Hinweise & **Rückfragen an NIBE** (Canonical, Schreibfehler, „Seite noch relevant?").
- Gruppierung über „Bereiche" (Startseite, Wärmepumpen, Lüftungsgeräte, Photovoltaik, Speicher, Zubehör, Sonstiges).
- Konventionen siehe [[NIBE — Schreibstil]] (Title endet „| NIBE", Meta mit `►`/`✓`).

---

## 6) Monatsreporting
Beispiel: *12.2025 NIBE Reporting - EOM* (Ordner `08_Reportings/JJJJ`, Dateischema „MM.JJJJ NIBE Reporting")

**Aufbau:**
1. Kopf: „Monatsreporting / [Monat Jahr]" + **Dashboard-Link** (Looker) + Verweis auf Excel-Übersicht „NIBE - Reporting - Tasks/Optimierungen/Auffälligkeiten".
2. **SEO-Besonderheiten** (Kontext: Core Updates, auffällige Keywords).
3. **Positive Entwicklungen (Top-3-Zuwächse)** — je Seite KPI-Block: +Klicks / +Impressionen / ±CTR / ±Position + Kurzdeutung.
4. **Negative Entwicklungen (Top-3-Verluste)** — analog.
5. **Allgemeine Bewertung** (hypothesengeführt, mit Saison-/Vorjahresvergleich).
6. **Weiteres geplantes Vorgehen** (Maßnahmen-Bullets nächster Monat).
7. **SEA-Besonderheiten** — umgesetzte Maßnahmen mit Datum, Jahresvergleich Conversions/Kosten/CPO, GA4-Quellenvergleich, Kampagnen-Performance, geplante Maßnahmen.

---

## 7) Strategie / Quick-Check
Beispiele: *NIBE - Strategischer Quick-Check*, *NIBE-Strategie Scan* (Slides) — beide in `10_Strategie`

**Aufbau:** themenblockweise **Stichpunkt-Kritik** entlang strategischer Achsen:
- Kunden- & Zielgruppenansprache (USP, Emotion/Nutzen, CRO).
- Kanal-Risiko (Organic-Abhängigkeit, Paid, GEO/AI-Visibility).
- Service/Retention (Newsletter, Cross-Selling, Customer Care).
- Saisonalität & Roadmap.
- Reporting-Weiterentwicklung („Für euch"-Folie, kanalübergreifender Vergleich).
- Ton intern/direkt (siehe [[NIBE — Schreibstil]] B); dient als Vorbereitung fürs Jahresgespräch.

---

## Quell-Ordner-Landkarte (Drive, NIBE)
- `02_SEO` → Unterordner **Onpage** (Content-Empfehlungen, Nachoptimierungen, Title/Meta-Sheets, interne Verlinkung, Local SEO), **Technik** (Audits, Crawls, 404/Redirect/hreflang-Sheets), GEO, KWR, Wettbewerber, Quick Wins.
- `03_Content` → Content-Pläne, Briefings, „Infos für Max (mit Freigabe)", Texterstellung/Feedback.
- `08_Reportings` → je Jahr ein Ordner, monatliche Report-Docs + Looker-Anpassungen.
- `10_Strategie` → Strategie-Scan (Slides), Quick-Check, Relaunch 2026, Leadgenerierung.
