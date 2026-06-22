---
tags: [kunde, seo]
kunde: "BDEW Bundesverband der Energie- und Wasserwirtschaft e.V."
stand-Datum: 2026-06-19
---

# BDEW Bundesverband der Energie- und Wasserwirtschaft e.V.

> [!warning] Datenlage
> Der Google-Drive-Kundenordner enthält **kaum SEO/GEO-Material**. Vorhanden sind im Wesentlichen: eine GA4-Tracking-Analyse (Google Doc, 30.01.2024) sowie Orga-Dokumente (Angebot-PDF, unterzeichnetes NDA). Es gibt **keine** Audits, Keyword-Sheets, Content-/Title-Meta-Empfehlungen, technischen Crawl-Reports oder GEO-/KI-Unterlagen im Ordner. Diese Notiz ist daher bewusst knapp gehalten und beruht fast vollständig auf der GA4-Tracking-Analyse. Befunde mit Quelle + Datum sind unten markiert; alles Übrige ist als Datenlücke offen benannt.

## Überblick

- **Wer:** BDEW Bundesverband der Energie- und Wasserwirtschaft e.V. — Spitzen- bzw. Branchenverband der Energie- und Wasserwirtschaft in Deutschland.
- **Branche:** Energie- und Wasserwirtschaft (Verband/Interessenvertretung). Verbands-/Informationswebsite, kein klassischer E-Commerce.
- **Domain:** `bdew.de` (in der GA4-Analyse mehrfach genannt, u. a. Screaming-Frog-Crawl der `bdew.de` und „sämtliche Seiten der bdew.de"). Quelle: BDEW – Tracking-Analyse GA4, 30.01.2024.
- **Mandatsverhältnis:** EOM (Effektiv Online-Marketing GmbH) ist der ausführende Dienstleister; NDA unterzeichnet (NDA_BDEW_unterzeichnet.pdf), Angebot dokumentiert (Angebot-231298-11046.pdf, 13.12.2023).

## Mandat & Gewerke

Auf Basis des Ordnerinhalts lässt sich nur **ein** konkretes Gewerk belegen:

- **Tracking / Web-Analyse (GA4):** Analyse und Fehleridentifikation des GA4-Trackings nach der UA→GA4-Umstellung, inkl. Abgleich GA4 ↔ Universal Analytics ↔ Matomo und Looker-Studio-Prüfung. Quelle: BDEW – Tracking-Analyse GA4, 30.01.2024.

Weitere klassische SEO-Gewerke (On-Page/Content, Technik, Off-Page, GEO/KI, laufendes Reporting) sind im Ordner **nicht** belegt — siehe [[#Offene Punkte / Datenlücken]].

## SEO-Status & Befunde

Es liegt **kein SEO-Audit** vor. Die folgenden Befunde stammen ausschließlich aus der Tracking-Analyse und betreffen die Mess-/Datengrundlage (Voraussetzung für jedes spätere SEO-Reporting), nicht Rankings oder Sichtbarkeit.

**Quelle für alle folgenden Befunde:** BDEW – Tracking-Analyse GA4 (Google Doc), Stand 30.01.2024.

- **Befund:** Nach der GA4-Umstellung wurden in GA4 rund **50 % weniger Nutzer** als in UA angezeigt. **Begründung:** Auslöser des Mandats; deutliche Datendiskrepanz zwischen den Tools. **Maßnahme (EOM-Analyseergebnis):** Ursache liegt voraussichtlich **nicht** in der aktuellen GA4-Einbindung, sondern in einer fehlerhaften UA-Implementierung ab Beginn des Parallelbetriebs; aktuell kein akuter Handlungsbedarf.
- **Befund:** GA4 trackte **erst ab Ende Oktober 2023** Seitenaufrufe (`page_view`); davor 0 Aufrufe im Seitenbericht. Auch `session_start` und `user_engagement` stiegen ab Ende Okt. 2023 stark. **Begründung:** Initial fehlerhafte GA4-Implementierung, im Okt. 2023 offenbar nachgebessert. **Maßnahme:** Klärung mit BDEW, welche konkreten Anpassungen im Okt. 2023 vorgenommen wurden (nicht mehr nachvollziehbar).
- **Befund:** In **UA** unnatürliche Werte — Absprungrate ~0,96 % (05/23), Seitenaufrufe ~doppelt so hoch wie einzelne Seitenaufrufe (379.552 vs. 166.523), viele Nutzer ohne Sitzung. **Begründung:** Deutet auf doppelt ausgelösten PageView / doppelte UA-Einbindung über die gesamte bdew.de. **Maßnahme:** Bestätigt die Diagnose „UA fehlerhaft, GA4 valide".
- **Befund (Plausibilisierung):** Nutzerzahlen UA 12/22 vs. GA4 12/23 ähnlich (GA4: 48.365 Nutzer / 88.798 Sitzungen; UA: 54.710 / 90.282). Matomo 12/23: 89.732 Sitzungen / 63.364 Nutzer — Sitzungen nahe an GA4. **Begründung:** Stützt, dass die aktuellen GA4-Daten valide sind. **Maßnahme:** GA4 als künftige Datenbasis nutzbar.
- **Grundlegende Checks (alle bestanden):** Tracking-Implementierung/Quellcode korrekt; Consent-Banner-Auswahl wird korrekt umgesetzt; Echtzeitbericht trackt korrekt; Tracking-Code auf allen Seiten der bdew.de vorhanden (Screaming-Frog-Crawl); Looker Studio ohne Datenabweichung.

**Offene technische To-dos aus der Analyse (Anhang, für sauberes Reporting relevant):**

- **Befund:** Interner Datenfilter in GA4 nicht wirksam — IP-Adressen der BDEW-Mitarbeiter sind nicht hinterlegt (unter Datenstreams > Tag-Einstellungen > Interner Traffic), Datenfilter greifen daher nicht. **Maßnahme:** Interne IPs definieren, damit interner Traffic ausgeschlossen wird (war in UA eingerichtet).
- **Befund:** Interne Suche wird laut Einstellungen ausgewertet, **funktioniert aber noch nicht**; Parameter `search_term` fehlt. **Maßnahme:** Interne Suche aktivieren und `search_term` als benutzerdefinierte Dimension anlegen.
- **Befund:** Keine benutzerdefinierten Dimensionen/Metriken in der Property angelegt. **Begründung:** Ohne diese lassen sich Ereignis-Parameter historisch nicht in Standard-/Custom-Reports auswerten. **Maßnahme:** Custom Dimensions nachziehen (z. B. `search_term`, `page_location`).

**Empfehlung (EOM):** Einbindung von GA4 über den **Google Tag Manager (GTM)** — einfachere Event-/Tag-Pflege und Prüfung über den GTM-Vorschaumodus.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im Kundenordner liegen keinerlei Unterlagen zu KI-Sichtbarkeit, AI Overviews, LLM-Zitierfähigkeit, `llms.txt`, KI-Crawler-Zugriff (GPTBot/ClaudeBot/PerplexityBot) o. Ä. Eine Aussage zur GEO-Performance von bdew.de ist auf Basis des Ordners **nicht** möglich.

## Doc-Typen & Aufbau

Im Ordner vorhandene Dokumenttypen:

- **Tracking-/Web-Analyse-Report** (Google Doc): klare Gliederung — Aufgabenstellung/Problematik → Analyse der Daten und Tools (Grundlegende Checks, Looker Studio, GA4, Universal Analytics, Matomo) → Ergebnis/Empfehlung → Anhang mit weiteren GA4-Hinweisen. Folgt erkennbar dem EOM-Muster Befund → Begründung → Empfehlung.
- **Orga-Dokumente** (PDF): Angebot, unterzeichnetes NDA — nicht inhaltlich SEO/GEO-relevant, nur für die Mandatsakte.
- **Unterordner:** `1.0_Orga` (enthält die beiden PDFs).

## Schreibstil-Notizen

Beobachtet im GA4-Report (EOM-Hausstil, konsistent mit Vault-Vorgaben):

- **Wir-Perspektive** der Agentur gegenüber dem Kunden („Wir empfehlen…", „Wir gehen stark davon aus…").
- **Befund → Begründung → Maßnahme/Empfehlung** durchgängig; Auffälligkeiten mit konkreten Zahlen belegt.
- Checklisten mit ✔ für bestandene Prüfungen; klare Trennung von Hauptbefund und „nicht relevanten" Hinweisen (Anhang).
- Sachlich-technische Sprache, deutsche Fachbegriffe, vorsichtige Formulierungen bei Unsicherheit („voraussichtlich", „Vermutung").
- Hinweis für Kunden-Copy: Sie-Anrede und „KI" statt „AI" gemäß Vault-Standard (im vorliegenden internen Analyse-Doc nicht einschlägig).

## Offene Punkte / Datenlücken

- **Kein SEO-Audit / keine On-Page-Analyse** im Ordner (Title/Meta, Content, interne Verlinkung, Struktur).
- **Keine Keyword-Recherche / kein Keyword-Sheet.**
- **Keine technischen SEO-Reports** (Crawl-Auswertung bzgl. Indexierung, Broken Links, Redirects, hreflang, Core Web Vitals). Der erwähnte Screaming-Frog-Crawl diente nur der Prüfung der Tracking-Code-Abdeckung, nicht einer SEO-Bewertung.
- **Kein laufendes SEO-Reporting** (GSC-Klicks/Impressionen/CTR/Position, Sichtbarkeitsindex).
- **Keine Off-Page-/Backlink-Daten.**
- **Keine GEO-/KI-Sichtbarkeitsdaten.**
- **Offene Sachfragen aus der Analyse:** Welche Tracking-Anpassungen wurden im Okt. 2023 vorgenommen? Wurden die GA4-To-dos (interne IP-Filter, interne Suche/`search_term`, Custom Dimensions, GTM-Migration) umgesetzt? — nicht im Ordner dokumentiert.
- **Domain-Scope/Sprachversionen** von bdew.de nicht im SEO-Kontext dokumentiert.

## Quellen

Ausgewertete Dateien (Google Drive, Account `ben@eom.de`, Kundenordner-ID `1VNOr_qiZ18G_ocd5GubongM_zKkdT03t`):

- **BDEW – Tracking-Analyse GA4** (Google Doc), modifiziert 30.01.2024 — Hauptquelle dieser Notiz.
- `1.0_Orga/Angebot-231298-11046.pdf` (PDF), 13.12.2023 — Orga, nur per Name gewertet (nicht inhaltlich gelesen).
- `1.0_Orga/NDA_BDEW_unterzeichnet.pdf` (PDF), 12.01.2024 — Orga, nur per Name gewertet (nicht inhaltlich gelesen).

Verwandt: [[Über EOM]] · [[SEO-Methodik]] · [[Tools-Stack]]
