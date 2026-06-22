---
tags: [kunde, seo]
kunde: "VIER"
stand-Datum: 2026-06-19
---

# VIER

> Wissensdatei auf Basis des zugänglichen Google-Drive-Materials (Account ben@eom.de). Die meisten Drive-Dateien sind PDFs (Angebote) oder Office-Formate, die nicht maschinell exportierbar sind; Grundlage dieser Datei sind die drei exportierbaren Quellen (Matomo-Audit-Doc, Projektinfo-Sheet, Budget-Sheet). Quellen am Ende gelistet.

## Überblick

- **Kunde:** VIER (Marke „VIER", Domain [vier.ai](https://www.vier.ai/)).
- **Branche:** KI-/Software-Anbieter für Kundenservice & Conversational AI (Produkte u. a. **VIER Copilot**, **VIER Engage**, **Smart Dialog Chat**, **Smart Dialog Voice**; thematische Marken-Claims „VIERliebtAI", „VIERliebtNews"). Ableitbar aus Tracking-Zielen, Whitepaper-Themen (EU AI Act, „Effizienz mit KI") und Google-Ads-Kampagnennamen.
- **Domain/Sprachen:** `vier.ai` mit deutscher und englischer Sprachversion (`/en/`). Belegt durch den Matomo-Befund zum DE→EN-Sprachwechsel.
- **Ansprechpartner (operativ):** Jessica Viebach-Mall (Jessica.Viebach-Mall@vier.ai). **Entscheider:** Bastian Bakeberg. (Quelle: Projektinfo-Sheet)
- **Pipedrive-Deal:** eom.pipedrive.com/deal/1429.

> **Wichtige Einordnung:** Das vorliegende Drive-Material beschreibt **kein klassisches SEO-/Content-/GEO-Mandat**, sondern ein **Tracking-/Analytics-/CRO-Mandat** (Matomo, Google Consent Mode, Conversion-Übergabe an Google Ads, Datenanalyse & CRO). Reine SEO-/GEO-Deliverables (Keyword-Recherche, Title/Meta, technisches Crawl-Audit, AI-Overview-/LLM-Sichtbarkeit) sind im Ordner **nicht** vorhanden. Das ist offen so zu benennen.

## Mandat & Gewerke

Aus Budget- und Projektinfo-Sheet erkennbare laufende/abgerechnete Leistungen:

- **Matomo-Beratungspaket** (2 Sitzungen, ~5 Std.) — Beratung zum bestehenden Matomo-Tracking + Erstellung eines Tracking-Konzepts (einmalig, ~8–10 Std.).
- **Erstellung eines Reporting-Berichts der Tracking-KPIs** (einmalig, ~8 Std.).
- **Laufende Retainer-Leistung „Datenanalyse & CRO"** mit je ~10 Std./Monat (Mai–Oktober gelistet). Umsetzung der Maßnahmen durch **EOM**.
- **A/B-Testing** als nachgelagerter CRO-Schritt vorgesehen (Tool-Umsetzung durch VIER, sobald Vorarbeiten erledigt sind).

Schwerpunkt also: **Web-Analytics-Qualität (Matomo)**, **Conversion-Tracking**, **Consent Mode**, **Kampagnen-/Google-Ads-Anbindung** und darauf aufbauend **CRO**. Start der Maßnahmen: „Sofort". Bisherige Maßnahmen anderer Dienstleister: laut Sheet nicht relevant.

## SEO-Status & Befunde

Es liegen **keine klassischen SEO-Befunde** (Crawl, Indexierung, Title/Meta, Rankings, Backlinks, Content-Audit) im Ordner vor. Die belastbaren technischen Befunde stammen aus dem **Matomo-Audit** (Quelle: „Matomo Audit VIER", Google Doc, Tests 23.–25.09., Doc-Stand 2025-09-30) und betreffen Tracking/Datenqualität. Logik: Befund → Begründung → Maßnahme.

- **Doppelte Conversion-Erfassung bei Downloads.** *Befund:* Klick auf „Whitepaper herunterladen" (ungegatetes Whitepaper „Effizienz mit KI") löste gleichzeitig die Ziele „Whitepaper Download" UND „Broschüren Download" aus. *Begründung:* Ereignisaktion unterscheidet Whitepaper/Broschüre nicht sauber. *Maßnahme (EOM):* Trigger so anpassen, dass die Ereignisaktion nicht „Whitepaper" enthält.
- **Event-Anmeldung feuert falsch.** *Befund:* Nach Absenden eines **Newsletter**-Formulars auf der Event-Seite wurde fälschlich das Ziel „Event-Anmeldung" ausgelöst; ein echtes Event-Formular existiert aktuell nicht. *Maßnahme:* Tag so anpassen, dass es nicht bei Newsletter-Anmeldungen auslöst.
- **Whitepaper-Download wird gar nicht als Ziel erfasst.** *Befund:* Formulare „Entscheidungshilfe VIER EU AI Act Journey" und „EU AI Act" lösten kein Ziel aus. *Begründung:* Der „Senden"-Button trägt die Klick-Klasse `submitButton`, die nicht im Trigger hinterlegt ist. *Maßnahme:* `submitButton` in den Trigger aufnehmen.
- **Newsletter-Abo nur teilweise getrackt.** *Befund:* Anmeldung über die News-Seite (VIERliebtNews) wurde als Ziel erfasst, über die Startseite (VIERliebtAI) **nicht**. Zusätzlich kamen Bestätigungs-Mails verzögert (~10 Min.) oder gar nicht an. *Maßnahme:* Trigger zusammenfassen, damit Newsletter-Abos seitenübergreifend tracken.
- **Formularübermittlungen unvollständig.** *Befund:* Am 24.09. abgesendetes Kontaktformular und am 25.09. abgesendetes Whitepaper-Formular „EU AI Act" tauchen in der Formularübersicht nicht auf; nicht alle Formulare erscheinen im Ereignisbericht. *Maßnahme:* Trigger anpassen, um alle Formulare abzudecken.
- **Video-Interaktionen nicht/teilweise getrackt.** *Befund:* Video-„Plays" werden weder im Echtzeitbericht noch in der Medienübersicht als Plays erfasst; im Ereignisbericht nur ein Teil. (offener Klärungspunkt)
- **In-Page-Klicks nicht erfasst.** *Befund:* Klicks auf Buttons/Tabs/Menüpunkte, die innerhalb der Seite navigieren (z. B. „Whitepaper anfordern"-Anker, Produktseiten-Tabs), werden nicht als Klicks erfasst. *Maßnahme:* offene Rückfrage an VIER, welche Elemente getrackt werden sollen (Klassen/IDs prüfen).
- **Neue vs. wiederkehrende Besucher unzuverlässig.** *Befund:* Wiederkehrende Nutzer wurden trotz gleichem Gerät nicht durchgängig erkannt; **keine User ID** eingerichtet. *Maßnahme:* VIER prüft Setzen der Matomo-Cookies `_pk_ses`, `_pk_ref`, `_pk_uid` und Übergabe einer User ID im Data Layer; EOM prüft die Cookie-Logik; ggf. Custom-Dimensions-Workaround.
- **Google Consent Mode nur teilweise korrekt.** *Befund:* Default (keine Zustimmung) und Vollzustimmung korrekt; bei **selektiver** Zustimmung setzt das Update-Tag jedoch alle Parameter auf `granted`, weil der Trigger „Google Ads Consent granted" nur den Google-Ads-Consent abfragt. *Maßnahme (EOM):* Trigger anpassen, damit dienst-selektive Zustimmung berücksichtigt wird.
- **Kampagnen-Tracking / Google-Ads-Übergabe korrekt.** *Befund:* `mtm_`-Parameter (campaign/kwd/source/medium/content) auf Kontoebene und in den Kampagnen (`pmax-ai-gateway`, `pmax-vier`, `search-brand-VIER`, `search-product-Copilot`, `-engage`, `-smart-dialog-chat`, `-smart-dialog-voice`) korrekt definiert; Parameter- und Conversion-Übergabe getestet. *Maßnahme:* Empfehlung, statt zwei nur **einen** Conversion-Export laufen zu lassen (Produktinteresse & Kontaktformular tauchen doppelt auf).
- **Interne Suche** wird korrekt mit Suchbegriffen erfasst (kein Handlungsbedarf).
- **Heatmaps & Session Recordings** am 23.09. definiert, am 25.09. noch keine Aufnahmen, keine Konsolen-Fehler — EOM prüft Ursache.
- **Geolokalisierung** nur auf Länderebene; für Stadt/Region PHP-GeoIP-Datenbank empfohlen (schnell umsetzbar) bzw. Server-Modul (genauer).
- **A/B-Testing / CRO-Voraussetzungen:** weder in Matomo noch per Drittanbieter-Tool eingerichtet.

> **DE/EN-Hinweis (einziger genuin SEO-/Tracking-naher Befund):** Beim Wechsel von der deutschen zur englischen Seite zeigt das Klickereignis korrekt `/en/`, das Seitenaufruf-Ereignis aber **nicht** die richtige `/en/`-URL. Relevant für saubere sprachgetrennte Auswertung (und potenziell hreflang-/URL-Konsistenz). Quelle: Matomo-Audit.

## GEO / KI-Sichtbarkeit

**Keine GEO-Daten gefunden.** Im Ordner liegen keine Analysen zu AI Overviews, LLM-Zitierfähigkeit, ChatGPT/Perplexity/Copilot-Sichtbarkeit oder KI-Traffic vor. Inhaltlich ist VIER selbst ein KI-Anbieter (Conversational AI, „VIER Copilot"), und es existieren KI-bezogene Whitepaper (EU AI Act, „Effizienz mit KI") sowie eine Brand-Kampagne „VIERliebtAI" — das ist thematisch GEO-relevant, aber es wurde **keine** GEO-Messung oder -Optimierung beauftragt/dokumentiert. Potenzielles Ausbaufeld, derzeit ohne Datengrundlage.

## Doc-Typen & Aufbau

Vorliegende Deliverable-Typen im Kundenordner:

- **Google Doc — Audit:** „Matomo Audit VIER". Aufbau: Inhaltsverzeichnis mit Seitenverweisen → Abschnitte je Tracking-Aspekt (Seitenaufrufe, Conversions je Ziel, Seiten-Events, Besucher-Unterscheidung, Consent Mode, interne Suche, Kampagnen-Tracking, Heatmaps, Geolokalisierung, A/B-Testing) → abschließende **„Nächste Schritte"** mit klarer Aufgabenteilung (Anpassung durch EOM / Anpassung durch VIER / Rückfragen). Stark screenshot-gestützt (im Text-Export nur als „  " sichtbar). Fußzeile mit EOM-Impressum.
- **Google Sheet — Projektinfos:** „VIER | Allgemeine Projektinfos | EOM Agency". Standardisierter EOM-Fragebogen (Info/Notizen-Spalten): Deal-Link, Domain, Ansprechpartner/Entscheider, Zeiten pro Leistung, Start, Umsetzer, Länder/Wettbewerber/KPIs (überwiegend leer), plus Fortschritts-Zähler (60 Punkte gesamt, 9 bearbeitet).
- **Google Sheet — Budget:** „VIER - Offenes Budget". Spalten Leistung / Zeit intern; Farb-Konvention **grün = abgerechnet**; getrennte Blöcke „geplant" vs. „geleistet".
- **PDFs — Angebote/Bestellung** (Unterordner „Angebote"): mehrere `Angebot-25xxxx-33028`-Dateien (2024–2025) + `Bestellung_30001897.pdf`. **Nicht auswertbar** — PDF-Download/Export schlägt mit Backend-Fehler fehl; Inhalt nur über Dateinamen/Deal-Code (33028) erschließbar.

Konventionen: Doc-Benennung im EOM-Stil mit Pipe-Trennern (`VIER | <Typ> | EOM Agency`). Markup im Doc über Farbe/Screenshots, das im reinen Text-Export verloren geht.

## Schreibstil-Notizen

- **Audit-Tonalität:** sachlich, „wir"-Form gegenüber dem Kunden („wir haben überprüft …"), teils Du-Nähe in den Audit-Formulierungen („eure Daten", „bei euch"). In abgabefähiger Kunden-Copy gilt jedoch die EOM-Regel **Sie-Anrede** und **„KI" statt „AI"** — das vorhandene Doc weicht stellenweise davon ab (Du-Form, „AI").
- **Analyse-Logik** im Audit folgt faktisch Befund → (Begründung) → Maßnahme, mündend in eine explizite „Nächste Schritte"-Verteilung.
- **Title/Meta-Konvention:** im Material **nicht erkennbar** (kein On-Page-/Title-Meta-Deliverable vorhanden).
- Marken-/Produktschreibweise: Eigenname **VIER** durchgehend versal; Produkte „VIER Copilot", „VIER Engage", „Smart Dialog Chat/Voice"; Kampagnen-Claims als CamelCase-Hashtag-Stil „VIERliebtAI", „VIERliebtNews".

## Offene Punkte / Datenlücken

- **Angebots-PDFs nicht lesbar** (Backend-Fehler beim Download) — genauer Leistungs-/Honorar-Scope und Vertragsumfang daher nur indirekt belegt.
- **Kein SEO-Kernmaterial:** keine Keyword-Recherche, kein technisches Crawl-/Indexierungs-Audit, keine Title/Meta-Konzepte, keine Rankings/Sichtbarkeitsindex-Daten, keine Backlink-Analyse.
- **Kein GEO-/AI-Visibility-Material** (siehe oben).
- **Projektinfo-Sheet überwiegend leer:** Ziele/KPIs, Wettbewerber, saisonale Besonderheiten, Content-Verantwortung, Reporting-Wünsche, Projektteam — nicht ausgefüllt (51 von 60 Punkten offen).
- **Wirksamkeit der Audit-Maßnahmen:** Es liegt kein Nachweis vor, dass die für 09/2025 verteilten Tracking-Fixes inzwischen umgesetzt/verifiziert wurden (kein Folge-Report im Ordner).
- **Reporting-Bericht der Tracking-KPIs** ist beauftragt (~8 Std.), aber als Deliverable im Ordner **nicht** auffindbar.

## Quellen

Ausgewertete Drive-Dateien (Ordner-ID `1UAm_SsHgzjJ0aBdHJbi-7_mSbMQjxNLR`, Account ben@eom.de):

- **Matomo Audit VIER** — Google Doc (modifiziert 2025-09-30) — vollständig ausgewertet.
- **VIER | Allgemeine Projektinfos | EOM Agency** — Google Sheet (2024-06-05) — ausgewertet (CSV).
- **VIER - Offenes Budget** — Google Sheet (2025-12-03) — ausgewertet (CSV).
- **Angebote/** (Unterordner) — 5× `Angebot-25xxxx-33028` PDFs + `Bestellung_30001897.pdf` (2024–2025) — **nicht auswertbar** (PDF-Download per gws schlug fehl), nur per Dateiname/Deal-Code berücksichtigt.

Verwandt: [[Über EOM]], [[SEO-Methodik]], [[Reporting-Standards]], [[Tools-Stack]]
