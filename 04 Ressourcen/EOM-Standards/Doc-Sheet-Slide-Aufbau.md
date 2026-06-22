---
tags: [standard, deliverable]
---

# Doc-/Sheet-/Slide-Aufbau — EOM-Deliverable-Vorlagen

Dokumentation des standardisierten Aufbaus von EOM-Deliverables (Docs, Sheets, Slides) für das Vault. Grundlage sind die im Drive (`ben@eom.de`) abgelegten Master-Vorlagen.

**Grundlogik über alle Formate hinweg:** Befund → Begründung → Maßnahme. Siehe [[SEO-Methodik]].

Quellen (Drive, exportiert 2026-06-19):
- Doc hoch: „01 EOM Agency Vorlage Word" (`1zpDAd4XZKA7I8H9iGN-gSjPVjwi7YtyEiz2_10Qgbf0`)
- Doc quer: „02 EOM Agency Vorlage Word Quer" (`1aFCw5p4RU9earD61RYz2zL8B7BYo7t3AgfABgVnYNL0`)
- Slides: „EOM Agency Vorlage / 20210318" (`1MP4LIZ8VEv0lSvpGu82wEKPaPcq92lE8rArPkw2YrTc`)
- Sheet: „20220126 Agency Tabellen Vorlage" (`1b7NntbnoVYlS2cqVijwzdNtflBtMIjkxDUY-8WJ7HP0`)

---

## 1. Docs — Aufbau eines EOM-Dokuments

### Kopf / Struktur (Hochformat-Vorlage)
Jedes Doc beginnt mit einem **Titel der Empfehlung** und folgt dann der festen Empfehlungs-Logik:

1. **Titel der Empfehlung** (als Überschrift formatiert)
2. **IST:** — der aktuelle Zustand (Befund)
3. **SOLL:** — der angestrebte Zustand (Maßnahme)
4. **Warum:** — die Erklärung/Datenbegründung (Begründung)

> Befund (IST) → Begründung (Warum) → Maßnahme (SOLL). Reihenfolge im Layout ist IST → SOLL → Warum; inhaltlich bleibt die Logik dieselbe.

**Hinweis aus der Vorlage:** „Durch das Hinzufügen von Überschriften (Format > Absatzstile) erscheinen diese im Inhaltsverzeichnis." → Überschriften konsequent als Absatzstile formatieren, damit ein automatisches Inhaltsverzeichnis funktioniert.

### Fußzeile (rechtsverbindlicher Kopf-/Fußteil)
Feststehender Footer mit Firmierung und Kontakt:
- Effektiv Online-Marketing GmbH — Standorte Nord (Hannover) und Süd (Stuttgart)
- Registergericht Hannover HRB 204938; Geschäftsführer Ernest Mavriqi, Nico Wutschijewitsch
- Kontakt: Tel. 0511 898 771 80, Fax 0511 898 771 90, Mail info@effektiv.com
- Seitenzahl-Feld („S. von")

> Achtung: Die exportierten Vorlagen nennen teils unterschiedliche Adressen/Kontakte (Word-Doc: Oldenburger Allee / Rotebühlplatz; Slides: Bödekerstraße 85, 30161 Hannover, hannover@eom.de). Vor Versand die für das Mandat korrekte Firmierung prüfen.

### Querformat-Variante (für Tabellen/breite Inhalte)
Aufbau „Headline / Subline → Fließtext → Themenblock mit Tabelle":
- **Headline** + **Subline**
- Einleitungs-Fließtext
- **Thema**-Block mit Tabelle: Spaltenüberschriften (z. B. „Überschrift / Überschrift / Überschrift") und Wert-Zeilen
- Footer wie oben (Firmierung, Registergericht, Geschäftsführer)

### 3-Farben-Markup
Das Farb-Markup (Grün/Gelb, ggf. Türkis als Akzent) ist eine **EOM-Konvention für Hervorhebungen**, die in den Text-Exporten **nicht** mitkommt — Farbe ist kein Text und geht beim Plain-Text-/Upload verloren (siehe CLAUDE.md: „Reiner Text-Upload überträgt kein Farb-Markup"). Markup-Logik nach EOM-Praxis:
- **Grün** = positiv / erledigt / Soll-Zustand erreicht
- **Gelb** = Hinweis / in Arbeit / zu prüfen
- (Rot, falls genutzt = kritisch / dringend)

> Ehrlich markiert: Die genaue Farbsemantik ist **nicht aus der Vorlagendatei selbst belegt** (Markup ist im Export nicht enthalten). Obige Zuordnung ist die im Vault gepflegte Arbeitskonvention — beim Erstellen im Google Doc das Markup **manuell** setzen.

---

## 2. Sheets — Aufbau

Master: „20220126 Agency Tabellen Vorlage". Es existiert **ein** Tab namens **„Vorlage"**.

> Ehrlich markiert: Der Tab ist **inhaltlich leer** (CSV-Export = 0 Bytes, Wertebereich A1:H30 ohne Inhalt). Die Datei ist eine reine **Formatierungs-/Layout-Vorlage** (Spaltenbreiten, Farben, Branding) ohne vordefinierte Spaltenköpfe oder Tab-Struktur.

Spezifisch für **Keyword-Recherche** gilt zusätzlich eine eigene, gebrandete Arbeitsvorlage:
- Google Sheet: `Ben Agency Tabellen Vorlage`
- Spreadsheet-ID: `1NPggycrxyBidt2n1dcSgeEhEmGJPJ81JADru1SjpoNw`
- Tab: `Vorlage` (`gid=1081565111`)
- Format-Befund aus Live-Zugriff am 2026-06-19: **26 Spalten**, **4 eingefrorene Zeilen**, sichtbare Kopfspalten `Keyword` und `SV`, Schrift `Montserrat`

> Arbeitsregel: Für KWR **immer diese gebrandete Vorlage** verwenden, nicht die generische leere Tabellen-Vorlage.

Spalten-/Tab-Struktur für reale Daten-Deliverables ergibt sich daher aus der **Analyse-/Keyword-Methodik** (siehe [[SEO-Methodik]]), nicht aus dieser Sheet-Vorlage. Typische Spalten bei Keyword-/Content-Deliverables:
- Keyword / Keyword-Cluster
- Suchvolumen (mit **Datenquelle + Erhebungsdatum**)
- Intent / Kategorie (BOFU / MOFU / TOFU)
- Ziel-URL, Title (~57 Z.), Status
- Befund → Maßnahme-Spalte

> Datenregel (CLAUDE.md): kein Suchvolumen/Ranking/Backlinks schätzen; Datenquelle (Sistrix/GSC/Ahrefs/DataForSEO) und Datum am Deliverable nennen.

---

## 3. Slides — Aufbau

Master: „EOM Agency Vorlage / 20210318" — produktisierter Foliensatz mit festen Layout-Typen.

### Folien-Reihenfolge / Layout-Typen
1. **Titelfolie** — Kurzer Projekttitel, „EOM für Unternehmen GmbH", Datum (XX.XX.XXXX)
2. **Agenda** — Titel in Versalien (24px), nummerierte Liste mit doppeltem Abstand, ohne Punkt am Ende, absatzweise Animation
3. **Titel ohne Inhalt** — z. B. für Screenshots; Titel Versalien halbfett 24px + Subline dünn 18px
4. **Kapitel-Trenner** — Titel des Kapitels (Versalien 36px) + große Kapitelnummer (max. 2 Stellen, ultrafett 138px)
5. **Unter-Kapitel** — Unter-Kapitel halbfett 36px, Subline dünn 20px, Foliennummer (max. 3 Stellen, 130px)
6. **Titel mit Text (Stichpunkte)** — Bulletpoints als Pfeil, Abstand 1,5
7. **Titel mit Text (Fließtext)** — Montserrat normal 14px, Abstand 1,15
8. **Titel + linke Spalte** — rechts vertikale Screenshots
9. **Break** — optionale Pausenfolie
10. **Zitat** — Zitat Montserrat Extradünn 36px; Quelle 10px, immer unverlinkt
11. **Bildunterschrift / Quelle / Link** — für größere Screenshots
12. **Lange Headline allein** — extrafett 48px (Themen-Einleitung / Break)
13. **Große Zahl** — Zahl Montserrat halbfett 120px + Fließtext-Erläuterung 14px
14./15. **Mobile Screenshot** — „Weil Mobile wichtig ist"
16. **Tabelle** — Tabellenüberschriften + Wertzeilen (mit +/− X% Veränderungen)
17.–18. **Kontakt** — Ansprechpartner (Name, Position, Mail, Telefon), Bilder als Kreis zugeschnitten
19. **Danke** — „EOM Agency", eom.de/agency, Kontakt Bödekerstraße 85, 30161 Hannover
20. **Haftungsausschluss** — Standard-Disclaimer (geistiges Eigentum, keine Erfolgsgarantie, Google-Algorithmus-Vorbehalt)
21. **Icon-Vorlage** — Symbol-/Icon-Set zur Verwendung
22. **Guidelines** — Schrift- & Abstandsregeln + Endkontroll-Checkliste

### Typografie & Branding (Guidelines-Folie)
- Schrift: **Montserrat** (durchgängig)
- Fließtext: min. 11pt, max. 14pt
- Schriftfarben: **schwarz/grau** = Hauptfarbe; **türkis** nur bei zusätzlichen Hervorhebungen; allgemeine Hervorhebungen über Montserrat **Fett**
- Animationen: nur „einblenden" verwenden
- Endkontrolle: Kunde überall angepasst? Ansprechpartner angepasst?

> Verwandt: Für GEO-Audits existiert ein eigener Slide-Master „EOM Master-Layout — GEO-Audit [VORLAGE — NICHT BEARBEITEN]" (`1rXueYWtxIsozyLOC9S_QM4ZkqiFjnrbuDPIeX_f-DzU`) — separat zu dokumentieren.

---

## Verwandt
[[SEO-Methodik]] · [[Reporting-Standards]] · [[Schreibstil]]
