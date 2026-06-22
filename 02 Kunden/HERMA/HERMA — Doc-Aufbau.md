---
tags: [kunde, herma, doc-aufbau, vorlage]
status: aktiv
quelle: Lokale HERMA-Exporte (InNo-Liner-Empfehlung, SEO-Crawl-Auswertung, Reportings 2024, KI-Meetings 2025, YouTube-SEO, Meeting 2024), gelesen 19.06.2026
---

# HERMA — Doc-Aufbau

Wiederkehrende Dokument-Strukturen der HERMA-Deliverables, je Doc-Typ als Vorlage beschrieben. Basis: gelesene Original-HERMA-Dokumente (Dateinamen genannt). Ergänzt [[HERMA]] und [[HERMA — Schreibstil]]; Methodik-Bezug: [[SEO-Methodik]].

Allen Docs gemeinsam:
- **Fußzeile fix:** „EOM – Effektiv Online-Marketing GmbH / [Adresse Hannover (+ ggf. Stuttgart)] / Registergericht Hannover HRB 204938, Geschäftsführer Ernest Mavriqi". (Ältere HERMA-Docs nennen frühere Adressen Hohenzollernstraße 49 / Oldenburger Allee 4 und teils zusätzlich GF Nico Wutschijewitsch — Adresse/GF haben sich über die Jahre geändert; aktuellen Stand verwenden.)
- Master-Logik **Befund → Begründung → Maßnahme** (bei HERMA als **Ist → SOLL → Doing** umgesetzt).
- Steuerung/Ablage über **Asana**; Reporting begleitet von einer **Du-Ton-Mail** an den Verteiler.

---

## 1) Content-/On-Page-Empfehlung (Einzelseite)
Beispiel: *Empfehlungen für die Seite HERMA InNo-Liner*

**Aufbau:**
1. **Titel** — „Empfehlungen für die Seite [Seitenname]".
2. **`URL:`** der Zielseite (vollständig).
3. **`Ist:`** — was die Seite aktuell behandelt (1–2 Sätze).
4. **`SOLL:`** — „Zur Optimierung … empfehlen wir folgende Punkte:" + **nummerierte Blöcke**:
   1. **Keyword-Optimierung** — Keyword-Liste mit **`(SV …)`**, je mit Einordnung („nur als Nebenkeyword verwenden", „verstärken"); Empfehlung, welche Keywords priorisiert werden.
   2. **Meta Daten** — Title **„Title Alt:" / „Title Neu:"**.
   3. **Content (Keyword-Verstärkung & -Ergänzung)** — auf Basis **WDF\*IDF**, getrennt in „Keywords zur Ergänzung" und „Keywords zur Verstärkung".
   4. **Möglicher Duplicate Content** — Prüfung intern/extern, Einschätzung der Gefahr.
   5. **Mögliche Keyword-Kannibalisierung** — Einschätzung + Gegenmaßnahme (z. B. interne Verlinkung).
   6. **Interne Verlinkungen** — Quell-/Ziel-URL + **vorhandener Linktext-Satz**.
   7. **Bild-Optimierungen** — Alt-Texte ergänzen.
   8. **Usability: Lesbarkeit** — Fettungen als Anker-Punkte.

**Mini-Skelett:**
```
Empfehlungen für die Seite [Name]
URL: https://www.herma.de/...
Ist: …
SOLL: Wir empfehlen folgende Punkte:
1. Keyword-Optimierung  (KW + (SV …) + Einordnung)
2. Meta Daten  (Title Alt / Title Neu)
3. Content: WDF*IDF — zur Ergänzung / zur Verstärkung
4. Duplicate Content  5. Keyword-Kannibalisierung
6. Interne Verlinkungen (Quell-URL → Ziel-URL + Linktext)
7. Bild-Optimierungen (Alt-Texte)  8. Usability/Lesbarkeit (Fettungen)
```

---

## 2) Technik-/Crawl-Auswertung (mehrere Domains)
Beispiel: *Auswertung der Crawlings (SEO-Check)*

**Aufbau:**
1. **Pro Domain ein Block** (`herma.de`, `herma.co.uk`, `herma.nl`, `herma-etikettierer.de`, `herma-etiketten.de`, `herma-labeler.com`, `herma-labels.com`).
2. **Pro Befund-Typ eine Überschrift:** 307-Weiterleitung · Duplikate (Title) · Fehlende Meta-Descriptions · Geringe interne Verlinkung · Sitemap · Hreflang · 404er.
3. Je Befund: kurze **Problem-Erklärung** (warum SEO-relevant, z. B. „Unique Content"-Grundsatz, „Klickrate = Rankingfaktor") → **betroffene URL(s)** (oft als Liste, teils mit Anzahl interner Links + Linktext, teils ausgelagert in ein Google-Spreadsheet) → **„Doing:"** mit konkreter Handlung.
4. **hreflang im IST/SOLL-Format:** „Rückbeziehung IST: … / Rückbeziehung SOLL: …".
5. **Erledigt-Vermerke datiert** im Doc („Ist erledigt! (11.02.19)").

---

## 3) SEO-/SEA-Reporting (je Geschäftsbereich)
Beispiel: *HERMA Reportings OUT Doc* (GBE-I monatlich, GBE-H quartalsweise)

**Aufbau:**
1. **Kopf:** „[GB] /// SEO[ & SEA] Reporting mit Rückblick auf [Monat/Quartal]" + Asana-Link.
2. **Sichtbarkeit** — Standard- & individuelle Sichtbarkeit je **(Prio-)Verzeichnis** im deutschen Google-(Mobile-)Index, mit Trend ggü. Vormonat/Vorquartal.
3. **Mitbewerber-Vergleich** — GBE-H: Avery/avery-zweckform.com; GBE-I: etikett.de, labelprint24.com.
4. **Rankings** — Entwicklung Top-10 & Top-100, gesondert je Prio-Verzeichnis; **„Wichtige Rankings"** als nummerierte Beispiele (Keyword, aktuelle Position, SV, Kontext/Saison).
5. **GA4-Traffic & Leads** — neue Besucher/Sitzungen, **Standard-Leads / RFQ-Leads / CC-Leads**, EAO-Ereignisse; Vorjahresvergleich, Datenaufbewahrungs-Limit (14 Monate) benannt.
6. **GSC-KPIs** — Klicks/Impressionen ggü. Vorjahr, fehlende Impressionen nach generischen Suchbegriffen aufgeschlüsselt.
7. **SEA-Besonderheiten** — messbare Leads/Micro-Conversions, beste Kampagne mit **Kosten/Lead + Conversion-Rate**.
8. **Begleit-Mail** an Verteiler/AP (Du-Ton, Emojis, „Viele liebe Grüße, Julia") mit Verweis auf beigefügte Dateien.

Durchgängig: **hypothesengeführte** Sprache, **an Google-Updates verankert**, Daten-Einschränkungen offen benannt.

---

## 4) GEO-/KI-Strategie- & Schulungs-Doc
Beispiele: *KI-Meeting 2025-08-14*, *KI-Meeting-V2 2025-10-24*

**Aufbau:**
1. **Einstieg/Marktlage** — Marktanteile (global/DE), Such-/Prompt-Volumina, AIO-Abdeckung DE, Google AI Mode, Chatbot-Marktanteile (mit Quellen Sistrix/Bain).
2. **„Was bedeutet das für SEO?"** — Zero-Click/Answer-on-SERP, „als Quelle genannt werden", neuer Kanal „AI-Suche".
3. **„Wird SEO unnötig?"** — Nein; Verschiebung zu Marken-Signalen/Entitäten/strukturierten Daten/zitierfähigen Absätzen (GEO als Teil von SEO).
4. **„Sind wir/Ist HERMA gewappnet?"** — Sistrix-Baseline (Top-100/Top-10 organisch vs. AIO), GA4 „KI Traffic", Entitäts-/Quellen-/E-E-A-T-/Schema-Check.
5. **Handlungsbedarf** — Blöcke A. Sichtbarkeit in AI-Antworten · B. Zero-Click abfedern · C. Messung/Reporting · D. Content-Portfolio; je mit konkreten Maßnahmen (Longtail, Entity-SEO, llms.txt, Evidence-Blöcke, FAQ/HowTo/Product-Schema, Wikidata/Wikipedia, Authority Building).
6. **30-/60-/90-Tage-Plan** + **nächste Schritte** (Top-20-ohne-KI-Ausspielung identifizieren → checken → optimieren → Monitoring).

---

## 5) YouTube-/Video-SEO-Konzept
Beispiel: *HERMA YouTube-SEO*

**Aufbau:** Quellen-Liste oben → **Strategie** (Ziel, Zielgruppe, Kanal-Struktur, CI) → **Keywords/W-Fragen** (Haupt-Key in Titel) → **Optimierung je Element** (Titel ≤100 Z., Beschreibung ≤5000 Z. mit Sprungmarken + Wichtigstem in den ersten 100–200 Zeichen, Tags/LSI max. 10–12, eigene Untertitel, Dateiname mit Keyword, Thumbnail 1280×720/16:9) → **Interaktion & Ausbau** (Kommentare/Abos/Playlists/Backlinks/Social-Distribution).

---

## Quell-Landkarte (HERMA)
- **Asana** = zentrale Projekt-/Ticket-Steuerung (alle Tickets, Reporting-Ablage in Aufgabenbeschreibung).
- **Drive** (HERMA-Konto) = Dateiablage je GB; Spreadsheets für ausgelagerte URL-Listen (Duplikate, fehlende Metas).
- Doc-Typen je Anlass: On-Page-Empfehlung (1), Crawl-Auswertung (2), GB-Reporting (3), GEO-/KI-Strategie (4), YouTube-SEO (5).
- Geschäftsbereiche als oberste Gliederung: **GBH / GBM / GBE-H / GBE-I / Corporate** (siehe [[HERMA]]).
