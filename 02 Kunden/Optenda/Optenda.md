---
tags: [kunde, seo]
kunde: "Optenda"
stand-Datum: 2026-06-19
domain: optenda.de
sprachen: [de, en]
analyst: Ben (EOM)
---

# Optenda

> Wissensbasis für das SEO/GEO-Mandat. Quelle: Google-Drive-Kundenordner (`ben@eom.de`). Analyse-Logik: Befund → Begründung → Maßnahme. Nichts erfunden — fehlende/nicht zugängliche Daten sind offen markiert.
>
> **Wichtige Einordnung vorab:** Der ausgewertete Drive-Ordner enthält **kein klassisches SEO-Material** (keine Audits, Keyword-Sheets, Title/Meta-Konzepte, technischen Crawls, Content-Empfehlungen oder GEO-/KI-Analysen). Die drei vorhandenen Dateien drehen sich ausschließlich um das **GA4-Tracking-Konzept** beim Umstieg von Universal Analytics auf Google Analytics 4 sowie um eine **Projektstart-Checkliste**. Alle Dateien stammen aus **Ende 2022 / Anfang 2023** und sind damit nicht mehr aktuell. Diese Notiz fasst zusammen, was belegbar ist, und markiert die SEO-/GEO-Lücken offen.

## Überblick

- **Wer:** Optenda GmbH — Anbieter von **Software für Energiemonitoring und Energiedatenmanagement** (B2B). Produkte laut Tracking-Konzept: **Energy Monitor** und **CO2-Monitor** (jeweils mit „Test-Account"-Anforderung als zentraler Conversion), Metering-App, Erweiterungsmodule.
- **Branche:** Energiemanagement-/Energiemonitoring-Software (Industrie, Handel/Gewerbe/Filialen, Kommunen — erkennbar an den Zielseiten-URLs).
- **Domain:** `optenda.de` (WordPress — erkennbar an Strukturen wie `/energiemonitoring/software-energy-monitor/`, `/unternehmen/blog/`, Newsletter-Störer, Teaservideo-Klasse `mejs-overlay-button`).
- **Sprachen:** Deutsch (Hauptsprache) und Englisch. **Eigenvorgabe Kunde:** Die EN-Sprachversion soll **nicht** getrackt werden (Quelle: Trackingkonzept, Abschnitt 2.1).
- **Zielgruppen-Segmente (aus URL-Struktur):** Industrie (`/energiemonitoring-und-energieeffizienz-in-der-industrie/`), Handel/Gewerbe/Filialen (`/energiemonitoring-handel-gewerbe-filialen/`), Kommunen (`/energiemanagement-kommunen/`).

## Mandat & Gewerke

Belegbar aus der Drive-Ablage ist **nur ein abgeschlossenes Tracking-Projekt** sowie ein angelegter (überwiegend unbearbeiteter) Projektstart-Prozess:

- **Tracking-Konzept GA4** — Pauschal **960 €** (Quelle: Projektstart-Checkliste). Inhalt: IST-Aufnahme des UA-Trackings, SOLL-Konzept für GA4, Event-/Conversion-Mapping, Berichts-Empfehlungen (siehe „SEO-Status & Befunde"). **Ansprechpartnerin Kundenseite:** Lucie Mödl (Quelle: Checkliste).
- **Projektstart / Tools & Zugänge** — Standard-Onboarding-Checkliste angelegt, aber zum Stand der Datei **kaum bearbeitet** (siehe Befunde).
- **SEO-Gewerk** — In der Checkliste als Kategorie mit **127 Punkten** angelegt, davon **0 bearbeitet** (Quelle: Checkliste, Zeile „5) SEO"). **Es liegt im ausgewerteten Ordner kein einziges SEO-Deliverable vor.** → Ob ein SEO-Mandat über die Checklisten-Anlage hinaus tatsächlich startete, ist aus diesen Dateien **nicht belegbar**.

> Datenlücke: Laufzeit, aktueller Mandatsstatus und etwaige spätere SEO-/GEO-Arbeiten sind aus dem ausgewerteten Ordner nicht ersichtlich. Die jüngste Datei ist von 2023-01-20.

## SEO-Status & Befunde

**Es liegen keine SEO-Befunde im engeren Sinn vor** (keine Rankings, kein Suchvolumen, keine Sichtbarkeits-, On-Page- oder Backlink-Daten im Ordner — und ich erhebe hier bewusst keine, da nicht beauftragt/belegt). Die folgenden Punkte sind **SEO-relevante Beobachtungen aus dem Tracking-Material**, mit Befund → Begründung → Maßnahme.

### Conversion-Architektur der Website (Quelle: [[Optenda Trackingkonzept Google Analytics 4]], 2022-12-19)

- **Befund:** Die definierten Haupt-Conversions sind: **Test-Account CO2-Monitor**, **Test-Account Energy Monitor**, **Kontaktanfrage** (`generate_lead`), **Newsletter-Anmeldung**, plus extern: Terminbuchung und Webinar-Anmeldung. **Begründung:** Das sind die kommerziell wichtigsten Nutzeraktionen — relevant, weil SEO-Content auf genau diese Conversion-Pfade einzahlen muss. **Maßnahme (SEO):** Leistungs-/Landingpages der Segmente (Industrie/Handel/Kommunen) konsequent auf „Test-Account anfordern" und „Kontakt" als primäre CTA ausrichten; Conversion-starke URLs in der Keyword-Priorisierung bevorzugen.
- **Befund:** Test-Account- und Newsletter-Conversions werden über **Dankesseiten-Aufrufe** gemessen (`/danke-test-account-anfrage-co2-monitor/`, `/danke-test-account-anfrage-energy-monitor/`, `/danke-fuer-die-kontaktanfrage/`, `/danke-newsletter/`), nicht über Button-Klicks — bewusst, um echtes Absenden statt nur Klick zu erfassen. **Maßnahme (SEO):** Dankesseiten von Index/Crawling ausschließen (Noindex), damit sie nicht in der Suche erscheinen.

### Externe Conversions nicht trackbar (Quelle: Trackingkonzept, Abschnitt 3.1)

- **Befund:** **Terminbuchungen** (iframe-Kalender) und **Webinar-Anmeldungen** (laufen extern über edudip) sind **nicht sauber trackbar** — es entsteht eine Diskrepanz zwischen Button-Klick und tatsächlicher Anmeldung. **Begründung:** Conversion-Abwicklung findet außerhalb der eigenen Domain statt. **Maßnahme:** Falls Conversion-Attribution für SEO-/SEA-Reporting wichtig wird, Weiterleitung auf eigene Dankesseite mit DataLayer-Übergabe prüfen (im Konzept als Lösungsidee genannt).

### Telefonnummern/CTAs teils nicht verlinkt (Quelle: Trackingkonzept, Abschnitt 3.1, Optionale Events)

- **Befund:** Viele Telefonnummern (z. B. in Störern) sind **nicht verlinkt** und daher nicht trackbar. **Begründung:** Fehlende `tel:`-Verlinkung. **Maßnahme:** Telefonnummern und Kontakt-CTAs konsequent verlinken — verbessert Trackbarkeit **und** Usability/Mobile-UX (indirekter SEO-Nutzen).

### Content-/Seiten-Inventar (implizit aus den getrackten URLs)

- **Befund:** Vorhandene relevante Seitentypen u. a.: Startseite, Segment-Leistungsseiten (Industrie/Handel/Kommunen), Produktseiten (`/energiemonitoring/software-energy-monitor/`, Metering-App, `#Erweiterungsmodule`), `/energiedatenmanagement/`, Lizenzangebot, **Blog** (`/unternehmen/blog/` inkl. Artikeln wie `/optenda-unter-top-3-nachhaltigkeitsprojekte-2022/`), Über-uns, Stellenanzeigen, Webinar-Seiten. **Begründung:** Zeigt eine bereits vorhandene, segmentierte Content-Struktur mit Blog — gute Grundlage für ein späteres SEO-/Content-Mandat. **Maßnahme:** Bei SEO-Start dieses Inventar als Basis für Keyword-Mapping und Cluster-Bildung (Energiemonitoring, Energiedatenmanagement, Energiemanagement Kommunen) heranziehen.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im ausgewerteten Drive-Ordner gibt es kein Material zu AI Overviews, ChatGPT/Perplexity-Sichtbarkeit, LLM-Zitationen, `llms.txt` oder KI-Crawler-Zugriff. Das Thema war zum Erstellungszeitpunkt der Dateien (2022/2023) noch nicht Gegenstand des Projekts.

> Offen: GEO ist für einen erklärungsbedürftigen B2B-Software-Anbieter wie Optenda (Energiemonitoring, CO2-/Energiemanagement) ein naheliegendes Zukunftsfeld — derzeit aber ohne jegliche Datengrundlage. Vor Aussagen müsste eine eigene Erhebung (z. B. Peec AI / Sistrix AI / DataForSEO LLM) erfolgen.

## Doc-Typen & Aufbau

Im Ordner liegen drei Dateien, alle aus dem Onboarding-/Tracking-Kontext:

1. **„Optenda Trackingkonzept Google Analytics 4"** (Google Doc, 2022-12-19) — das inhaltliche Kernstück. Aufbau:
   - *1. IST-Bestandsaufnahme* (UA-Property `UA-185619504-1`, Datenansichten, Verweis-Ausschlüsse, interne IP-Filter, bestehende UA-Events & Zielvorhaben).
   - *2. SOLL GA4-Tracking* (Kundenvorgaben + Basis-Empfehlungen; GA4-Property `G-KBXT57DB1Q` bereits angelegt; Datenaufbewahrung 14 Monate, Google-Signals optional).
   - *3. Tracking-Möglichkeiten* (Event-Mapping UA→GA4, optionale Events, Conversions, nicht übernommene Events).
   - *4. Berichte* (Channels, Jahresübersicht, Einstiegs-/Ausstiegsseiten, Google-Ads-, GSC-Bericht; inkl. Hinweisen zu GA4-/Looker-/„Data Studio"-Limitierungen).
2. **„Optenda - GA4-Trackingtabelle"** (Google Sheet, 2023-01-20) — tabellarisches Event-/Conversion-Mapping: GTM-Tag → GA4-Eventname → Parameter (z. B. `e-mail_klick`, `telefonnummer_klick`, `scroll_25%/50%`, `startseite_button_header_klick`, `social_icons_klick`, `button_webinar_anmeldung_klick`) und Conversions (`test_account_co2_angefordert`, `test_account_energy_angefordert`, `generate_lead`, `newsletter_abonnieren`).
3. **„Optenda | Checkliste Projektstart, Tools & Zugänge, SEO | EOM Agency"** (Google Sheet, 2022-11-29) — Onboarding-Dashboard mit Punkte-Tracker je Phase (BizDev, Tools & Zugänge, Projektstart, Grundlegende Fragen, SEO). Ansprechpartnerin: Lucie Mödl; Tracking-Konzept mit 960 € beziffert.

## Schreibstil-Notizen

- **Sie-Anrede** in Kunden-Copy (EOM-Standard).
- **„KI" statt „AI"** durchgängig.
- Produktnamen exakt: **Energy Monitor**, **CO2-Monitor**, **Metering-App** (Schreibweise wie auf der Website/​im Konzept).
- Fachbegriffe der Domäne sauber führen: Energiemonitoring, Energiedatenmanagement, Energiemanagement (Kommunen), Energieeffizienz.
- Keine kundenspezifischen Title/Meta-Konventionen im Ordner belegt → bei SEO-Start mit `00 Kontext/`[[Schreibstil]] abgleichen und neu festlegen.

## Offene Punkte / Datenlücken

- **Kein SEO-Material vorhanden:** keine Audits, Keyword-Listen, Title/Meta, Crawls (Broken Links/Redirects/hreflang), Content-Empfehlungen oder Sichtbarkeits-/Backlink-Daten. SEO-Checklistenpunkte stehen auf **0 bearbeitet**.
- **Keine GEO-/KI-Sichtbarkeitsdaten.**
- **Alle Dateien veraltet** (2022/2023). Aktueller Mandats- und Website-Stand unbekannt.
- **Mandatsstatus unklar:** Ob über das Tracking-Konzept (960 €) hinaus ein laufendes SEO-Mandat besteht, ist aus dem Ordner nicht belegbar.
- **EN-Version:** bewusst nicht getrackt — für ein etwaiges SEO-Mandat wäre die Rolle der EN-Seiten (Index/hreflang/Scope) zu klären.
- **Empfehlung nächste Schritte (falls SEO beauftragt):** eigene Sichtbarkeits-/Keyword-Baseline erheben (Sistrix/GSC), Segment-Leistungsseiten auditieren, Blog-Content-Potenziale prüfen, GEO-Baseline anlegen. Alles erst nach Datengrundlage — hier nicht vorweggenommen.

## Quellen

Ausgewertete Dateien (Drive-Ordner Optenda, `ben@eom.de`):

- **Optenda Trackingkonzept Google Analytics 4** — Google Doc, geändert 2022-12-19 (`1FlSrV8z0YlC8yFGL-EV0xwZrEgadpLaqCuGHNF56Bqo`).
- **Optenda - GA4-Trackingtabelle** — Google Sheet, geändert 2023-01-20 (`1bV_Oh5GeqPe-VprB8Vc58iN9ukjTeHLmeGNf9k0arlc`).
- **Optenda | Checkliste Projektstart, Tools & Zugänge, SEO | EOM Agency** — Google Sheet, geändert 2022-11-29 (`1f6OVnGb8sVFZPUDJJQz9wTBR9SGrQjHDzF0nOHAkqvY`).

> Der Ordner enthielt **ausschließlich** diese drei Dateien. Weitere Unterordner (SEO, On-Page, Content, Technik, Reporting, GEO/KI, Audit, Keywords) waren **nicht vorhanden**.
