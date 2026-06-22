---
tags: [standard, corporate-design]
status: aktiv
erstellt: 2026-06-19
quelle: EOM-eigene Master-Vorlagen (Google Drive, Account ben@eom.de)
---

# EOM Corporate Design

Diese Notiz dokumentiert das **EOM-eigene Corporate Design** (Hausschrift, Farbpalette, Stilregeln), wie es sich aus den verbindlichen EOM-Master-Vorlagen im Drive ableiten lässt. Sie ist die interne Referenz für alle EOM-Deliverables (Slides, Docs, Webapp-Copy-Layout).

> **Methodischer Hinweis (ehrlich markiert):** Es wurde **kein dediziertes Brand-/CI-Manual** (z. B. „EOM Styleguide.pdf") im zugänglichen Drive gefunden. Die hier dokumentierten Werte sind **aus den tatsächlich verwendeten Master-Vorlagen rekonstruiert** (Schrift- und Farb-Markup direkt aus der Slides-API ausgelesen), nicht aus einem offiziellen CD-Dokument abgeschrieben. Zwei unabhängige EOM-Master-Decks bestätigen sich gegenseitig — die Schriftart gilt damit als gesichert, einzelne Sekundärfarben sind als „abgeleitet" zu verstehen.

## Hausschrift (Schriftart)

**Befund:** Hausschrift ist **Montserrat**.

- In beiden ausgewerteten EOM-Master-Decks dominiert `Montserrat` mit Abstand (1.436 bzw. 1.194 Vorkommen im Schrift-Markup). `Arial` tauct nur als Restbestand/Fallback auf (128 bzw. 100 Vorkommen).
- Das EOM Master-Layout (GEO-Audit-Vorlage) nennt Montserrat sogar explizit im Foliendesign: *„Montserrat 18px, doppelter Abstand"* (Agenda-Folie).

**Begründung:** Montserrat ist eine geometrische Grotesk (Google Font, frei lizenziert) — gut für Web/Slides/Docs einsetzbar, einheitlich über alle Kanäle.

**Maßnahme / Anwendungsregeln (aus dem Master-Layout abgeleitet):**

| Element | Stil |
|---|---|
| Fließtext / Aufzählung | Montserrat, ~18px |
| Kapitelnummer (Trenner) | ultrafett, ~138px |
| Kapitel-Titel (Trenner) | VERSALIEN, halbfett, ~36px |
| Standard-Akzent in Titeln | halbfett |

- **Fallback:** Arial (wenn Montserrat technisch nicht verfügbar ist).

## Farbpalette

**Befund:** Wiederkehrende, nicht-zufällige Akzentfarben (in beiden Decks identisch vorhanden):

| Hex | Rolle (abgeleitet) |
|---|---|
| `#000036` | Marken-Dunkelblau / Marine (primärer dunkler Markenton) |
| `#16F4C4` | Türkis / Mint (Signal-/Akzentfarbe) |
| `#F41847` | Rot/Pink (Akzent-/Highlight-Farbe) |
| `#121212` | Fast-Schwarz (Text/Flächen) |
| `#000000` | Schwarz (Text) |
| `#FFFFFF` | Weiß (Hintergrund) |
| `#595959`, `#999999`, `#BFBFBF`, `#EFEFEF` | Grautöne (Sekundärtext, Linien, Flächen) |

**Begründung:** `#000036`, `#16F4C4` und `#F41847` sind keine Office-Default-Farben, sondern bewusst gesetzte Markenfarben — sie treten in beiden unabhängigen EOM-Master-Vorlagen auf und bilden damit die plausibelste EOM-Akzentpalette. Grau- und Neutraltöne dienen als unterstützende Systemfarben.

**Maßnahme:** Für EOM-Deliverables Montserrat + diese Akzentpalette verwenden; Akzentfarben sparsam (Highlights, Signal), Neutraltöne für Fläche/Text. **Vor finaler Verwendung in Kundenmaterial mit einem aktuellen offiziellen CD-Dokument abgleichen, falls eines auftaucht** — die Hex-Werte sind hier aus Vorlagen rekonstruiert.

## Logo- und Stilregeln

**Befund (aus dem EOM Master-Layout / GEO-Audit-Vorlage):**

- **Firmierung / Impressum-Standard:** „EOM – Effektiv Online-Marketing GmbH, Bödekerstraße 85 in 30161 Hannover, Registergericht Hannover HRB 204938, Geschäftsführer Ernest Mavriqi."
- **Outro-Folie:** EOM-Standard „Bödekerstraße 85, Hannover" — *nicht verändern*.
- **Haftungsausschluss-Folie:** Standardtext — inhaltlich *nicht verändern*.
- **Kontakt-Folie:** Kreisbild des Ansprechpartners + Name, Titel, Kontakt — *immer aktuell halten*.
- **Titelfolie:** zentrierter Titel (Kundenname + Audit-Typ), Subtitle „EOM | Datum".
- **Tabellen:** immer native Tabellen (`createTable`), nie ASCII-Tabellen (Regel R9 des Master-Layouts).

**Begründung:** Diese Elemente sind in der Vorlage als „EOM-STANDARD / nicht verändern" markiert und bilden den festen, wiedererkennbaren Rahmen jedes EOM-Decks.

**Maßnahme:** Outro-, Haftungs- und Impressumsangaben unverändert übernehmen; Kontakt-/Titeldaten pro Projekt befüllen.

## Quellen (EOM-eigene Vorlagen, Drive)

- `EOM Master-Layout — GEO-Audit [VORLAGE — NICHT BEARBEITEN]` (Google Slides) — Schrift- & Farb-Markup ausgelesen.
- `EOM Agency Vorlage / 20210318` (Google Slides) — Schrift- & Farb-Markup ausgelesen, bestätigt Montserrat + Palette.
- `01 EOM Agency Vorlage Word` (Google Doc) — Impressum/Firmierung.

## Offene Punkte

- Kein offizielles **CD-/Brand-Manual** im Drive zugänglich → exakte Farb-Definitionen (z. B. ob `#000036` oder ein nahe liegender Ton der „echte" Markenwert ist) und Logo-Schutzraum/Mindestgröße sind **nicht** verbindlich dokumentiert.
- `.docx`/`.pptx`-Office-Dateien (z. B. `EOM | GEO.pptx`) lassen sich nicht per Text exportieren und wurden nicht ausgewertet.
- Falls ein offizielles EOM-Styleguide-Dokument existiert, sollte es hier nachgetragen und diese rekonstruierten Werte dagegen geprüft werden.

Siehe auch: [[Doc-Sheet-Slide-Aufbau]], [[Kundenordner-Struktur]]
