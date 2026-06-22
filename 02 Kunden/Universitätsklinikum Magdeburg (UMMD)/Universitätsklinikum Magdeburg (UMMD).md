---
tags: [kunde, seo]
kunde: "Universitätsklinikum Magdeburg (UMMD)"
stand-datum: 2026-06-19
domains:
  - www.med.ovgu.de
  - www.lungenklinik-lostau.de
  - www.klinikum-cracau.de
  - www.mvz-cracau.de
mandatstyp: Web-Analytics / Tracking (Matomo)
---

# Universitätsklinikum Magdeburg (UMMD)

> [!warning] Einordnung des Mandats
> Der UMMD-Kundenordner enthält **kein klassisches SEO- oder GEO-Material** (keine Audits, keine Keyword-Recherchen, keine Title/Meta-Optimierung, keine technischen Crawl-Reports, keine AI-Visibility-Daten). Das bei EOM laufende Mandat ist ein **Web-Analytics-/Tracking-Projekt rund um Matomo** (Self-Hosted). Diese Wissensdatei dokumentiert daher den Tracking-Scope ehrlich als das, was vorliegt — und markiert die SEO/GEO-Lücken offen.

## Überblick

- **Kunde:** Universitätsmedizin Magdeburg (UMMD), Universitätsklinikum / medizinische Fakultät der Otto-von-Guericke-Universität. Öffentlicher Gesundheits-/Bildungssektor.
- **Hauptdomain:** `www.med.ovgu.de`. Weitere getrackte Domains derselben Trägergruppe:
  - `www.lungenklinik-lostau.de` (Lungenklinik Lostau)
  - `www.klinikum-cracau.de` (Klinikum Cracau)
  - `www.mvz-cracau.de` (MVZ Cracau)
- **Sprache:** Deutsch (DACH/DE).
- **CMS-Landschaft:** Egotec CMS für `med.ovgu.de`; TYPO3 für Klinikum Cracau, MVZ Cracau und Lungenklinik Lostau. (Quelle: Matomo-Doku V1.2, 08.01.2026)
- **EOM-Rolle:** „Partneragentur" für Wartung, Optimierung und Bugfixing des Trackings. Projektleitung Roxeanne Rieck; Web Analyst Anna-Lena Eggensberger (vorher auch Roxeanne Rieck genannt). (Quelle: Matomo-Doku V1.2)

## Mandat & Gewerke

Erkennbar aus Angeboten und Leistungsnachweis (alles **Tracking/Analytics**, kein SEO/GEO):

- **Angebot 251491** (Stand 03/2025): Matomo Standard-Tracking-Umsetzung inkl. Fehleranalyse & -behebung (16 Std.) + Erstellung eines Tracking-Konzepts. Maßnahmen: Kick-Off, Konzepterstellung, VPN-Aufwände inkl. Technik-Abstimmung UMMD, Einrichtung Standard-Tracking, PM. Gesamt ~19,25 Std.
- **Angebot 251524** (Stand 05/2025): Umsetzung des Tracking-Konzepts (18 Std.). Maßnahmen: Abstimmungscall, Umsetzung (13,25 Std.), Funktionsprüfung (2,5 Std.), PM. Gesamt ~18,25 Std.
- **Angebot 251572** (Stand 11/2025): weiteres Angebot (PDF nicht exportierbar, nur per Name gewertet).
- **Leistungsnachweise** März–Juni 2025 als Sheet vorhanden.

**Befund → Begründung → Maßnahme:** Das Mandat ist auf Webanalyse (Matomo Self-Hosted) fokussiert. → Begründung: Sämtliche Deliverables (Trackingkonzept, Matomo-Doku, Tracking-Ordner, VPN-Zugang) und Angebote drehen sich um Datenerfassung, nicht um Sichtbarkeit/Ranking. → Maßnahme: SEO-/GEO-Leistungen müssten separat scoped werden; aktuell keine Beauftragung erkennbar.

## SEO-Status & Befunde

Es liegen **keine SEO-Befunde** (technisch / On-Page / Content) im Ordner vor. Stattdessen relevante **Analytics-/Tracking-Befunde**, die mittelbar für späteres SEO-Reporting wichtig sind:

- **Consent-bedingte Datenlücke:** Matomo startet erst nach CCM19-Einwilligung (`CCM19.consentStateChanged`, DLV `ccm19_Matomo = true`, Hostname ≠ „intranet"). → Begründung: DSGVO-konform, aber Conversions/Traffic systematisch untererfasst. → Maßnahme: Bei jeder KPI-Auswertung Consent-Bias mitdenken; ggf. Consent-Rate als Kontext-Metrik führen. (Quelle: Matomo-Doku V1.2, 08.01.2026)
- **Defekte/instabile Event-Tags (Status-Kapitel C):**
  - „Klicks zurück zur Startseite" — funktioniert beim Text-Klick, beim Bild-Klick **nicht** zuverlässig.
  - „Klick auf Direktlinks" — **funktioniert nicht durchgängig**.
  - „Bildboxlink" und „Bildblock" — **funktionieren nicht**, obwohl CSS-Klasse übereinstimmt.
  - „ubux_linkblock" (Kurzinfo-Link) — **überzählt** (gleiche Klasse auch bei anderen Elementen, z. B. E-Mail-Adressen).
  - „Box_gerahmt" (Bewerbungs-Button) und „Ubox_head_link" — **nicht immer ausgelöst**.
  → Begründung: Inhalts-Element-Selektoren im Egotec-Template sind nicht eindeutig. → Maßnahme: Selektoren/Klassen schärfen, dedizierte Events statt generischer Klassen-Trigger. (Quelle: Matomo-Doku V1.2, Kapitel 9/C)
- **Standardmäßig nicht erfassbar (Setup nötig):** 404-/Fehlerseiten, interne Tools, YouTube-Video-Performance (Plugin Media Analytics ~179 €/Jahr), Terminbuchungstool im iFrame (nur wenn Matomo im iFrame implementierbar). → Maßnahme: für SEO-relevantes Reporting (404-Monitoring!) gezielt nachrüsten. (Quelle: Trackingkonzept, 29.05.2025)
- **Search Console nicht angebunden:** GSC-Daten in Matomo nur via kostenpflichtigem Plugin „Search Engine Keywords Performance" (~179 €/Jahr). → Begründung: Ohne GSC-Anbindung keine Keyword-/Impressions-/CTR-Sicht in Matomo. → Maßnahme: Voraussetzung für jegliches SEO-Reporting; aktuell nicht beauftragt.

## GEO / KI-Sichtbarkeit

**Keine GEO-Daten gefunden.** Im Ordner existiert nichts zu AI Overviews, LLM-Zitierfähigkeit, KI-Traffic, ChatGPT/Perplexity/Copilot, llms.txt oder Brand-Mentions. GEO ist für UMMD bislang weder beauftragt noch dokumentiert.

## Doc-Typen & Aufbau

Vorliegende Deliverable-Typen:

- **Google Doc — „Universitätsmedizin Magdeburg Trackingkonzept"** (29.05.2025): gegliedert in 1) IST-Bestandsaufnahme, 2) SOLL-Tracking (Basis-Tracking + Plugin-Empfehlungen mit Preisen/Links), 3) Tracking-Möglichkeiten (Allgemeines, Kontaktaufnahmen, Socials, Navigation, optionale Custom Reports). Aufbau: KPI-Listen + Empfehlung je Plugin mit Kosten und Use-Case. EOM-Footer (Hannover/Stuttgart, HRB) am Ende.
- **Google Doc — „Doku-Matomo-Entw. V1.2"** (08.01.2026, Autor kundenseitig: Christian Maleike-Fitza): formale Systemdokumentation mit Änderungsverlauf-Tabelle, Inhaltsverzeichnis, Kapiteln (Systemübersicht, Tag Manager, Datenschutz/Consent, Rollen & Rechte, offene Punkte, Anhang mit Tag/Trigger/Variablen-Listen und Parameter-Status). Sehr strukturiert, versioniert, freigabebasiert.
- **Google Sheet — „UMMD Leistungsnachweise März–Juni 2025"**: Angebots-/Stundenaufstellung (Leistung, Stunden, Maßnahmen, Summen).
- **PDF — 3× Angebote** (251491, 251524, 251572): nicht exportierbar (kein Docs-Editors-Format), nur per Name/Datum gewertet.
- **Office-/Binär-Dateien** (`.docx`-Kopie der Matomo-Doku, `.dmg` AnyConnect-VPN-Client, `.zip` Sicherheitszertifikat, VPN-Anleitung): Infrastruktur/Zugang, kein SEO-Inhalt.

**Markup/Konventionen:** Tracking-Logik durchgängig als „Befund → Empfehlung/Maßnahme" mit Plugin-Links und Preisen; Tag-Naming-Konvention „Übergreifend <Aktion>" sowie Ereigniskategorie / Ereignisaktion / Ereignisname als feste Event-Triplet-Struktur.

## Schreibstil-Notizen

- **Tonalität:** sachlich-dokumentarisch, Sie-Anrede, „Nutzer:innen" (Gendern im kundenseitigen Doc). EOM-Konzept eher beratend-erklärend (Empfehlung + Begründung + Kosten).
- **Begrifflichkeit:** „KI" wäre konform — kommt im Material aber nicht vor (kein KI/GEO-Thema).
- **Title/Meta-Konvention:** **nicht ableitbar** — es liegt kein On-Page-/SEO-Material vor, aus dem eine Title/Meta-Konvention hervorginge.

## Offene Punkte / Datenlücken

- **Kein SEO-Scope vorhanden:** keine Audits, Keywords, Title/Meta, Content-Empfehlungen, Crawl-/Broken-Link-/Redirect-/hreflang-Checks. Falls SEO gewünscht: separates Mandat nötig.
- **Kein GEO/KI-Material** (s. o.).
- **Angebots-PDFs nicht maschinell lesbar** — Detailpositionen aus 251491/251524 nur über das Leistungs-Sheet, 251572 gar nicht inhaltlich erfasst.
- **GSC-Anbindung fehlt** in Matomo → ohne sie kein organisches Suchreporting möglich.
- **Tag-Bugs offen** (Bildbox/Bildblock/Direktlinks/Kurzinfo-Überzählung) — Datenqualität für Interaktions-KPIs eingeschränkt.
- **Mehr-Domain-Setup:** vier Domains in einer Matomo-Instanz; Mandanten-Segmentierung pro Subdomain laut Doku „geplant", noch nicht durchgängig umgesetzt.

## Quellen

| Datei | Typ | Stand |
|---|---|---|
| Universitätsmedizin Magdeburg Trackingkonzept | Google Doc | 29.05.2025 |
| Doku-Matomo-Entw. V1.2 | Google Doc | 08.01.2026 |
| UMMD – Leistungsnachweise März–Juni 2025 | Google Sheet | 17.06.2025 |
| Angebot-251491-32007 (1) | PDF (nicht exportierbar) | 03/2025 |
| Angebot-251524 | PDF (nicht exportierbar) | 05/2025 |
| Angebot-251572-32007 (1) | PDF (nicht exportierbar) | 11/2025 |
| Anleitung VPN-Zugang Med. Uni Magdeburg + AnyConnect/Zertifikat | Doc / dmg / zip | 10–11/2025 |

Verwandt: [[Reporting-Standards]], [[Tools-Stack]]
