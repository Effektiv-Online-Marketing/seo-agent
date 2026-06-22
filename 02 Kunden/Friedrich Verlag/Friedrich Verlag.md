---
tags: [kunde, seo]
kunde: "Friedrich Verlag"
stand-Datum: 2026-06-19
---

# Friedrich Verlag

> [!info] Kurz-Einordnung
> Langjähriger EOM-Kunde (10+ Jahre). **SEO ist aktuell kein aktives Gewerk** — das laufende Mandat (Stand 2026) ist ausschließlich **Social Ads** (Meta inkl. Shopping + TikTok, vereinzelt LinkedIn). SEO lief historisch ca. 2 Jahre, wurde aber eingestellt; zuletzt extern durch einen Freelancer betreut. Dieses Dokument fasst das im Drive auffindbare SEO/GEO-Wissen zusammen und benennt die Datenlücken offen.

---

## Überblick

- **Wer/Branche:** Friedrich Verlag GmbH — Bildungs-/Fachverlag für Lehr- und Lernmaterial (Grundschule, Sekundarstufe, Referendare/Studierende, Schulleitung; daneben Pflege-Fachsegment). Geschäftsmodell stark **abo-getrieben** (Jahres-/Ref-Abos, Probe-Abos, Fachzeitschriften) plus Einzelprodukte (Lernspiele, Fachbücher, Sondermaterial).
- **Domain:** `https://www.friedrich-verlag.de/`
- **Technik-Setup (laut Projektübergabe, 11/2025):** Zwei Systeme — **TYPO3** für alles außerhalb von `/shop/`, **Magento** für das `/shop/`-Verzeichnis. Auf das Magento-Backend hat EOM **keinen Zugang** (vom Kunden auch nicht gewünscht).
- **Saisonalität (für SEO/Content-Timing relevant):** Beste Monate Ende August/September (Schulstart), gut Oktober/November (Schulstart Süd, Black Week). Schwach Mai–Juli sowie oft Januar/Dezember. Februar/März mittel (didacta-Rabatte, 2. Schulhalbjahr).
- **Ruf-/Produktthema (kontextrelevant für E-E-A-T/Content):** Laut interner Übergabe gilt das Abo-Modell bei Lehrkräften/Referendaren als "knebelig"; Mitbewerber bieten teils gleiche/bessere Inhalte ohne Bindung und günstiger. Produktqualität "wird besser". Diese Wahrnehmung ist für Content-Vertrauenssignale und Reputationsthemen einzuordnen.

## Mandat & Gewerke

- **Aktuelles Mandat (2026):** Social Ads (Meta + TikTok, vereinzelt LinkedIn) + teilweise Tracking. PM-Wechsel Julia → Katharina (Stand 11/2025). Umsetzung Meta/TikTok: Sharia (mit Freelancer-Support Anna-Lena).
- **Historische Gewerke bei EOM (10+ Jahre):** SEA (~9 Jahre, **2024 gekündigt**), Tracking (~8 Jahre), **SEO (~2 Jahre)**, CRO (~1 Jahr), Social Ads (~6 Jahre), einmalig Social-Strategie (Meta) sowie einmalige Affiliate-/Off-Page-Maßnahmen.
- **SEO-Status laut Übergabe:** *"Haben wir vor viiiielen-vielen Jahren auch mal für FV gemacht; letzter Stand: Betreuung durch Freelancer Daniel Schneider."* → SEO liegt also derzeit **nicht** bei EOM.
- **Zielhierarchie (Conversions, gilt v. a. für Ads, aber als Content-Prioritätsgeber nutzbar):**
  1. Verkäufe Jahres-/Ref-Abos (höchste Prio)
  2. Verkäufe Probe-Abos
  3. Leads (z. B. White Paper)
  4. Verkäufe Einzelprodukte (Lernspiele, Fachbücher, Sondermaterial; Shopping-relevant)
- **KPI-Vorgabe:** Keine harten Zielwerte, aber klare Regel: Alle Maßnahmen müssen einen **positiven ROI** haben (eigenes ROI-Reporting ab Januar 2025).
- **Quelle:** [[FV | Projektübergabe Friedrich Verlag | November 2025]] (Google Sheet, 2025-11-12).

## SEO-Status & Befunde

> [!warning] Datenstand
> Es liegen **keine aktuellen** SEO-Audits, Rankings oder Sichtbarkeits-Reports im Drive. Die jüngsten SEO-Artefakte stammen aus **2018 bzw. 2021**. Reportings ab 2025/2026 sind ausschließlich **Social-Ads-Reports**, kein SEO. Die folgenden Befunde sind daher historisch zu verstehen und vor jeder Maßnahme neu zu verifizieren (Sistrix/GSC/Ahrefs).

**Befund 1 — On-Page-Potenziale auf Kategorie-/Hub-Seiten (Quelle: 2018, On-Page-Sheet)**
- *Begründung:* Mehrere stark frequentierte Zielseiten waren laut Analyse "nicht optimiert" und hatten kaum/keine relevanten Rankings, obwohl sie zu den meistaufgerufenen Seiten gehörten.
- Genannte Seiten mit Chancen:
  - `/klasse-leiten/` — keine relevanten Rankings, nicht optimiert, aber unter den Top-Aufrufen (90 Tage)
  - `/referendare-studierende/` — Top-Aufrufe, "großes Potenzial im Bereich der Schwellenkeywords", nicht optimiert
  - `/sekundarstufe/klassenfuehrung/` und `/sekundarstufe/schulleitung/` — kaum Rankings, nicht optimiert
  - `/grundschule/spielpaedagogik/` — Schwellenkeyword-Potenzial, nicht optimiert (als "wenig Relevanz" markiert)
- *Maßnahme (zu re-validieren):* On-Page-Optimierung der Hub-/Kategorieseiten (Title/Meta, H-Struktur, Content-Tiefe) priorisiert nach Traffic × Schwellenkeyword-Nähe — beginnend bei `/referendare-studierende/` und `/klasse-leiten/`, da diese Reichweite + Conversion-Nähe (Referendare = Fokus-Zielgruppe) verbinden.
- *Quelle:* [[OnPage Optimierungen - Potenziale]] (Sheet, Stand 2018-02-09), verknüpft mit altem Basecamp-Task.

**Befund 2 — Shop-/Content-Doppelstruktur (TYPO3 vs. Magento)**
- *Begründung:* Inhalte existieren parallel als Content-/Themenseite (z. B. `/grundschule/musik/`) und als Shop-Seite (`/shop/grundschule/musik`). Das birgt klassische Risiken: Keyword-Kannibalisierung, unklare kanonische Zuordnung, gespaltene interne Verlinkung — verschärft dadurch, dass `/shop/` (Magento) für EOM nicht zugänglich ist.
- *Maßnahme (zu re-validieren):* Bei künftiger SEO-Aufnahme Canonical-/Intent-Mapping zwischen TYPO3-Hub und Magento-Shop-Seite prüfen.
- *Quelle:* URL-Paare im On-Page-Sheet (2018) + Backend-Beschreibung in der Übergabe (2025).

**Befund 3 — Crawl-/Indexierungsrisiko historisch real eingetreten (kritisch)**
- *Begründung:* Laut Übergabe wurde **serverseitig der Google-Crawler temporär vom Zugriff auf die Website ausgeschlossen** — "war kritisch für ALLES (SEO, SEA, …)".
- *Maßnahme:* Bei jeder SEO-Reaktivierung zuerst Crawlability/Indexierbarkeit (robots.txt, Statuscodes, Server-/Bot-Filter) prüfen, bevor On-Page-Arbeit beginnt.
- *Quelle:* [[FV | Projektübergabe Friedrich Verlag | November 2025]].

**Befund 4 — Tracking-/Consent-Instabilität (datenseitig)**
- *Begründung:* Tracking & Consent werden zunehmend von Friedrich selbst bzw. wechselnden Freelancern/Agenturen verändert, oft ohne EOM-Kenntnis. Das gefährdet die nachweisbare Performance-Messung (Ads wie auch organisch).
- *Maßnahme:* Für valide SEO-/Performance-Datenbasis Tracking-Governance klären; GSC als belastbare organische Quelle priorisieren.
- *Quelle:* Übergabe 2025-11.

**Vorhandene Alt-Artefakte (nur Bestandsnachweis, nicht ausgewertet/veraltet):**
- XML-Sitemap-Crawl `friedrich-verlag-internal_all.csv` (2021-04-14)
- Meta-Daten für YT-Bumper (2021-10-26)
- Reportings-Unterordner 2015–2018 (alt)

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im gesamten gesichteten Kundenordner existieren keine Dateien zu AI Overviews, GEO/AEO, LLM-Sichtbarkeit, ChatGPT/Perplexity-Citations oder llms.txt. Das Thema KI taucht nur strategisch-allgemein im EOM-Strategie-Scan (2026-03) auf ("KI verändert interne und externe Prozesse sowie das Kundenverhalten fundamental") — **ohne** Friedrich-spezifische GEO-Analyse oder -Maßnahme.

> Empfehlung (nicht beauftragt): Bei einer SEO-Reaktivierung wäre ein GEO-Baseline-Check sinnvoll, da Bildungs-/Referendariats-Fragen ("Was muss ich als Referendar im ... beachten?") typische informationsgetriebene Prompts sind, bei denen FV als Fachverlag als Quelle kandidieren könnte. Aktuell **keine Datengrundlage** dafür im Vault.

## Doc-Typen & Aufbau

Im Kundenordner dominieren (nach Aktualität):
- **Social-Ads-Reportings** (Google Docs, monatlich, 2025–2026) — *Hauptdeliverable des aktuellen Mandats*; teils mit "SHORT"-Variante.
- **ROI-Reporting / Sheet** (ab Januar 2025) — ROI-Nachweis als Kern-KPI-Logik.
- **Projektübergabe** (Sheet, 11/2025) — strukturierte Wissensübergabe (Ansprechpartner, Zugänge, Tools, Saisonalität, Tasks).
- **EOM Strategie-Scan** (Slides, 03/2026) — generisches EOM-Beratungsangebot (Potenzialanalyse, 990 € einmalig), kein FV-spezifischer Audit.
- **Historische SEO-Artefakte** (Sheets/CSV, 2018/2021): On-Page-Potenziale, Sitemap-Crawl, YT-Meta.
- Weitere Gewerke-Ordner: SEA (Offboarding 2024), CRO, Social Ads/Shopping/Media, Tracking, Kampagnenkalender, Zielgruppen-Studie (YouGov 2018).

## Schreibstil-Notizen

- **Kundenansprache:** **"Du"** (laut Übergabe ausdrücklich Du, nicht Sie) — Ausnahme zur sonstigen EOM-Sie-Konvention in Kunden-Copy; bei FV-spezifischer Kommunikation beachten.
- Interne EOM-Doku zu FV ist sehr direkt/ehrlich gehalten (Stärken/Schwächen offen benannt).
- Zielgruppen-Tonalität: Lehrkräfte, Referendare/Studierende, Schulleitung — fachlich, entlastungsorientiert ("Zeit sparen", "Klasse leiten").
- **KI** statt "AI" durchgängig.

## Offene Punkte / Datenlücken

- **Kein aktueller SEO-Audit / keine Sichtbarkeitsdaten** im Drive (jüngstes SEO-Material 2018/2021). Rankings, SI, Backlinks, GSC-Daten müssten frisch erhoben werden — hier **nicht** geschätzt.
- **SEO derzeit nicht im EOM-Mandat** — laut Übergabe extern (Freelancer Daniel Schneider). Unklar, ob/wie aktiv.
- **Magento-`/shop/`-Bereich** für EOM nicht zugänglich → technische SEO-Tiefe dort eingeschränkt.
- **Office-Dateien** (`.xlsx`: Kampagnenkalender 2021/2023, Aktionsübersicht 2020) nicht exportierbar → nur per Name eingeordnet, Inhalt nicht ausgewertet.
- **Kein GEO/AI-Sichtbarkeits-Material** vorhanden.
- Technik-Ansprechpartner aktuell unklar (mehrere Agenturen beteiligt, nicht alle bekannt) → erschwert technische SEO-Umsetzung.

## Quellen (ausgewertete Dateien)

- **FV | Projektübergabe Friedrich Verlag | November 2025** — Google Sheet, modified 2025-11-12 (Mandat, Technik, Saisonalität, SEO-Historie, kritische Fehler). *Hauptquelle.*
- **OnPage Optimierungen - Potenziale** — Google Sheet, modified 2018-02-09 (On-Page-Befunde Kategorie-/Hub-Seiten). *Historisch.*
- **FV_Strategie Scan - 202603** — Google Slides, modified 2026-03-02 (generisches EOM-Strategie-Scan-Angebot, kein FV-Audit).
- Ordner-Sichtung: SEO/ (Crawls 2021, Reportings 2015–2018), REPORTINGS/ (2025/2026 = Social Ads), Strategie/ — bestätigt: kein aktuelles SEO-/GEO-Material.
- Nur per Name eingeordnet (nicht exportierbar/alt): XML-Sitemap-Crawl CSV (2021-04-14), Kampagnenkalender `.xlsx` (2021/2023), Aktionsübersicht `.xlsx` (2020).

> Drive-Kundenordner-ID: `1TybKnrn6SeqU_kM9bQhoE7nfniE63A8M` (Account ben@eom.de)
