---
tags: [kunde, seo]
kunde: "LIGANOVA GmbH"
stand-Datum: 2026-06-19
---

# LIGANOVA GmbH

> Befund -> Begründung -> Maßnahme. Diese Datei fasst das im Google Drive vorliegende SEO-Wissen zu LIGANOVA zusammen. **Wichtiger Hinweis vorab:** Das gesamte ausgewertete Material stammt aus den Jahren **2021 und 2022**. Es liegen **keine aktuellen Daten** (2023–2026) und **keine GEO-/KI-Sichtbarkeitsdaten** im Ordner vor. Alle Befunde sind entsprechend als historischer Stand zu lesen.

## Überblick

- **Wer:** LIGANOVA (Stuttgart) ist eine Agentur/Group im Bereich **Brand Experience, Retail Experience und Experiential Marketing** — physische und „phygitale" Markenerlebnisse am Point of Sale, Pop-up-Stores, Shop-in-Shop, Events, AR/VR/Mixed Reality, 3D/Motion Design sowie Nachhaltigkeit im Handel.
- **Branche:** Marken-/Erlebnis-Marketing-Agentur (B2B), Schwerpunkt Retail/Fashion/Premium-Marken (referenzierte Kundenprojekte u. a. adidas, Land Rover, Nespresso, Bucherer, Jelmoli).
- **Domains (im Ordner vertreten):**
  - `liganova.com` — Hauptdomain (DE + EN-Inhalte, Portfolio, News/Presse)
  - `greencampaigncycle.com` (GCC) — Nachhaltigkeits-/Sub-Brand mit eigener Keyword- und Struktur-Arbeit
  - `career.liganova.com` — Karriere-Subdomain
  - Erwähnt, ggf. außerhalb des Mandats: `liganovaproduction-usa.com` (nur „ggf. Kurzanalyse" im Reporting)
- **Agenturkontakt EOM:** PM **Felix Scheub** (Keyword-/Metadaten-Task 2021), Reporting durch **Daniel** (2022).

## Mandat & Gewerke

Das Mandat war **breiter als reines SEO** und umfasste laut Ordnerstruktur und Reporting:

- **SEO** (On-Page, Content, Technik, Keyword-/Metadaten-Arbeit) — Ordner `5.0_SEO`
- **SEA** (Google Ads, u. a. Brand-Kampagne, responsive Suchanzeigen, GCC-Kampagnen) — Ordner `6.0_SEA`
- **Content** (Texterstellung zu Leistungsseiten) — Ordner `7.0_Content`
- **LinkedIn Ads** (Follower-Ads, Lead-Gen) — im Reporting erwähnt
- **Webtracking/Analytics** (GA, GSC, Looker/Data-Studio-Dashboard) — Ordner `4.0_Webtracking`, `3.0_Reportings`

Quelle: Ordnerstruktur Kundenordner; `LIGANOVA Reporting` (Doc, Stand Juli 2022, modifiziert 2022-08-02).

## SEO-Status & Befunde (mit Quelle + Datum)

### 1. Sichtbarkeit & Rankings (Stand Juli 2022)
- **Befund:** Sichtbarkeit von `liganova.com` laut Reporting „in den letzten Monaten steigend". Sistrix-Keyword-Zählung (erweiterte Datenbasis, DE): **Top-10 = 204** (Vormonat 258), **Top-100 = 559** (Vormonat 667).
- **Begründung/Einordnung:** Der Rückgang der Keyword-Anzahl wurde als unkritisch bewertet — verloren gingen vor allem **irrelevante Keywords** (z. B. Fremd-Markennamen wie „nike"), bei denen die Nutzerintention ohnehin nicht zu LIGANOVA passt.
- Quelle: `LIGANOVA Reporting`, Juli 2022 (Sistrix DE, GSC, GA).

### 2. Search-Console-Performance (Juli 2022 vs. Vorjahr)
- **Befund:** Organische **Klicks −2,4 %**, **Impressionen +48,1 %** (YoY). Analytics: **+5,4 % Nutzer** YoY.
- **Begründung:** Stark steigende Impressionen bei leicht rückläufigen Klicks deuten auf wachsende Reichweite/Sichtbarkeit, aber Optimierungsbedarf bei CTR (Title/Meta, Intent-Treffer).
- Quelle: `LIGANOVA Reporting`, Juli 2022 (GSC, GA).

### 3. Technische On-Page-Fehler — fehlende h1
- **Befund:** Audit-Sheet `20221219 LIGANOVA | Fehlende h1-Überschrift` listet **~44 URLs ohne h1-Überschrift** (News-/Pressemeldungen, Portfolio-Detailseiten, Imprint/Privacy, sowohl DE unter `/de/…` als auch EN-Pendants direkt unter Root).
- **Begründung:** Fehlende h1 schwächt die thematische Auszeichnung der Seite für Suchmaschinen und die Zugänglichkeit; betroffen sind v. a. Portfolio- und News-Seiten, die als Content-Assets ranken könnten.
- **Maßnahme:** Pro betroffener URL eine eindeutige, keyword-relevante h1 ergänzen.
- Quelle: Sheet `20221219 LIGANOVA | Fehlende h1-Überschrift` (Stand 2022-12-19).

### 4. Interne Verlinkung & Weiterleitungen
- **Befund:** Reporting nennt als laufende Doings „Nachkontrolle der **fehlerhaften internen Verlinkungen**" und „Analyse Problematik mit **internen Weiterleitungen**".
- **Maßnahme (lt. Plan):** Bereinigung fehlerhafter interner Links und Redirect-Ketten.
- Quelle: `LIGANOVA Reporting`, Juli 2022.

### 5. EN/DE-Parallelstruktur (Beobachtung aus den Daten)
- **Befund:** DE-Seiten liegen unter `/de/…`, die englischen Pendants teils direkt unter Root (`liganova.com/…`) — sichtbar an doppelten Inhalten in der h1-URL-Liste (z. B. `…/de/spenoki/` vs. `…/liganova-group-integrates-sustainability-startup-spenoki/`).
- **Begründung/Maßnahme (Empfehlung):** Sprachversionierung und hreflang/Canonical prüfen — die uneinheitliche Pfadlogik (DE mit Sprachpräfix, EN ohne) ist ein typisches Risiko für Duplicate-/Sprachzuordnungsprobleme. **Hinweis:** im Ordner liegt hierzu keine explizite hreflang-Analyse vor; dies ist eine abgeleitete Beobachtung, kein dokumentierter Audit-Befund.

### 6. Keyword- & Metadaten-Strategie (On-Page-Fundament)
- **Befund:** Zentrales Arbeitsdokument `LIGANOVA | Seitenübersicht für Keywords und Metadaten` (V1 2021-05, V2 2021-10, V3 mit Liganova-Feedback). Es definiert **neue Landingpages** für Leistungen und Skills mit Fokus-Keywords und Suchvolumen (Quelle SV: im Sheet ausgewiesen, ø monatl. SV).
- **Themen-Cluster & Beispiel-Fokus-KW (mit im Sheet hinterlegtem SV):**
  - Experience Solutions: *Pop Up Stores* (49.500), *Shop-in-Shop* (18.100), *Corporate Events* (12.100), *Multisensory Experiences* (590), *Phygital/Interactive Marketing* (5.400)
  - Skills: *Community Aufbau / e-community* (14.800), *Experiential Design* (9.900), *AR/VR & Mixed Reality* (u. a. *augmented reality marketing* 1.600), *3D & Motion Design* (motion 3d 1.600)
- **Begründung:** Hohe-Volumen-Begriffe wie „pop up stores" und „shop-in-shop" sind die kommerziell wertvollsten Anker für die Leistungsseiten.
- Quelle: `LIGANOVA | Seitenübersicht für Keywords und Metadaten - V2` (Stand 21.7.2021, modifiziert 2021-10-22).

### 7. Content-Erweiterung Leistungsseiten
- **Befund/Maßnahme:** Reporting nennt „Analyse Texterweiterung Seite **Experience Solutions**" und geplant „weitere Texterweiterung für **Point of Sale Campaigns**". Rückmeldungsdocs zu „Experience Solution Text" (2022-06-08) belegen redaktionellen Abstimmungsloop mit dem Kunden.
- Quelle: `LIGANOVA Reporting` (Juli 2022); `20220608 … Rückmeldung Experience Solution Text`.

### 8. Strukturierte Daten / Google for Jobs
- **Befund:** Eigenes Empfehlungsdoc `LIGANOVA - Empfehlung Google for Jobs` (2021-12) zur Karriere-Subdomain `career.liganova.com`.
- **Maßnahme:** Aufnahme in Google for Jobs (i. d. R. via JobPosting-Schema) — relevant für Recruiting-Sichtbarkeit.
- Quelle: Doc `LIGANOVA - Empfehlung Google for Jobs` (Stand 2021-12-17).

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im gesamten Kundenordner gibt es **kein Material zu AI Overviews, ChatGPT/Perplexity-Zitaten, LLM-Sichtbarkeit, Brand-Mentions in KI-Antworten oder llms.txt**. Das ist plausibel, da das dokumentierte Mandat 2021–2022 liegt, also vor dem Aufkommen generativer Suchergebnisse. Eine GEO-Bestandsaufnahme müsste neu erhoben werden (z. B. via Peec AI / Sistrix AI / DataForSEO LLM-Tools), liegt aber nicht im Scope der vorhandenen Dateien.

## Doc-Typen & Aufbau

Die Ablage folgt einer **nummerierten Gewerk-Struktur** statt der neueren EOM-Output-Architektur:

- `1.0_Orga`, `2.0_Meetings`, `3.0_Reportings`, `4.0_Webtracking`, `5.0_SEO`, `6.0_SEA`, `7.0_Content`, `BACKUP`
- In `5.0_SEO` und `7.0_Content` jeweils Unterordner pro Domain (`liganova.com`, `greencampaigncycle.com`, „Nachhaltige Website").
- Wiederkehrende Doc-Typen:
  - **Keyword-/Metadaten-Sheets** (versioniert V1/V2/V3, mit Kunden-Feedback-Fassung)
  - **Technische Audit-Sheets** (z. B. fehlende h1)
  - **Empfehlungs-/Rückmeldungs-Docs** (Google for Jobs, Domains, Textfreigaben)
  - **Reporting** als Google Doc (Fließtext-Summary + Verweis auf Data-Studio-/Looker-Dashboard) und als **Slides** (Jahresreporting „SEA, SEO – Recap und Ausblick")
- **Datei-Benennung:** Datumspräfix `YYYYMMDD` bzw. `YYYY-MM-DD` + `LIGANOVA |` + Thema.

## Schreibstil-Notizen

- **Reporting-Stil:** lockere, persönliche Kunden-Ansprache („Hallo zusammen", „Liebe Grüße, Daniel"), **Du-Anrede** im Reporting-Anschreiben (abweichend von der sonst empfohlenen Sie-Anrede).
- **Struktur des Monatsreports:** Summary → „Die Entwicklung im SEO / SEA / LinkedIn" → „Maßnahmen & Doings" (letzter Monat / aktueller Monat je Kanal).
- **KPI-Sprache:** Klicks, Impressionen, Nutzer, Leads, jeweils mit YoY/MoM-%; klare Einordnung statt nackter Zahlen (z. B. Erklärung, warum Keyword-Verluste unkritisch sind).
- **Metadaten-Vorgaben:** Meta-Title ca. 70 Zeichen / 512 px; Meta-Description ca. 155 Zeichen / 920 px (im Keyword-Sheet definiert).
- **Sprache:** Fachbegriffe oft englisch (Experience, Phygital, Skills), Inhalte gemischt DE/EN.

## Offene Punkte / Datenlücken

- **Aktualität:** Jüngste verwertbare Datei ist von **Dezember 2022**. Kein Material 2023–2026 — der dokumentierte SEO-Status ist veraltet. Aktiver Mandatsstatus unklar.
- **Keine GEO/KI-Daten** (s. o.).
- **Keine aktuellen technischen Crawl-Daten** (Broken Links, Redirects, hreflang, Core Web Vitals) als abgeschlossener Audit — nur Hinweise im Reporting.
- **Office-Dateien (.docx/.xlsx/.pptx):** im ausgewerteten Scope keine relevanten reinen Office-Dateien blockiert; ausgewertet wurden Google-native Formate.
- **Nicht im Detail ausgewertet** (als ältere/Nebenstränge eingestuft): GCC-Struktur- und Keyword-Sheets (2022), initiale Keyword-Recherche 2021-03, Jahresreporting-Slides 2022, „Rückmeldung zu den anderen Domains". Bei Bedarf nachladbar.
- **Suchvolumen-Werte** im Keyword-Sheet stammen aus 2021 und sind heute nicht mehr belastbar — vor Wiederverwendung neu erheben.

## Quellen (ausgewertete Dateien)

- `LIGANOVA | Seitenübersicht für Keywords und Metadaten - V2` (Sheet, Stand 21.7.2021, mod. 2021-10-22) — Keyword-/Metadaten-Strategie, Themencluster, SV.
- `LIGANOVA Reporting` (Doc, Juli 2022, mod. 2022-08-02) — Sichtbarkeit, GSC/GA-KPIs, SEO/SEA/LinkedIn-Doings.
- `20221219 LIGANOVA | Fehlende h1-Überschrift` (Sheet, 2022-12-19) — technischer On-Page-Befund (~44 URLs ohne h1).
- Ordnerstruktur Kundenordner (`5.0_SEO`, `7.0_Content`, `3.0_Reportings` gelistet) — Mandatsumfang, Doc-Typen, Domains.
- Weitere im Ordner gesichtete, nicht voll ausgewertete Dateien: `LIGANOVA - Empfehlung Google for Jobs` (2021-12), GCC-Keyword-/Struktur-Sheets (2022), Jahresreporting-Slides (2022).

---
Verwandte Hinweise: [[Über EOM]] · [[SEO-Methodik]] · [[Reporting-Standards]]
