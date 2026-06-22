---
tags: [kunde, seo]
kunde: "LUXHAUS"
stand: 2026-06-19
analyst: Ben (EOM)
quelle-drive: "13pTqM5W1tAvM61WxItdxCJ3CkHCtOZJ5"
---

# LUXHAUS

> [!warning] Einordnung vorab
> Der LUXHAUS-Drive-Ordner enthält **kein SEO- und kein GEO/KI-Material**. Die vorhandenen Deliverables drehen sich ausschließlich um **Conversion-Tracking, Analytics-Setup und einen Website-Relaunch** (GTM, GA4, Google Ads, Meta, LinkedIn). Für ein vollständiges SEO/GEO-Wissensprofil fehlt die Datengrundlage im Drive — siehe [[#Offene Punkte / Datenlücken]].

## Überblick

- **Kunde:** LUXHAUS — Hersteller individueller Fertighäuser (Holz-/Architektenhäuser, Premium-Segment). Branche: Fertighausbau / Bauen & Wohnen DACH.
- **Domain:** `https://www.luxhaus.de/` (deutschsprachig, Markt DE). Keine weiteren Sprach-/Länderversionen aus den Docs ableitbar.
- **Betreuende Agentur:** EOM – Effektiv Online-Marketing GmbH (Hannover/Stuttgart).
- **Aktueller Stand des Mandats:** Im Zentrum steht ein **Website-Relaunch** mit anschließender Tracking-Neuaufsetzung. Jüngste Aktivität: GTM-Installationsdoc (Stand 2026-06-11), Relaunch-Tracking-Prüfung (2025-12-05).

## Mandat & Gewerke

Aus den Docs erkennbare Leistungen (alle im Bereich **Tracking & Analytics**, nicht SEO):

- **Google-Tag-Manager-Implementierung** (Container `GTM-NZG99B7V`) inkl. Installationsanleitung für die Website (Quelle: „LUXHAUS - Google Tag Manager Installation", Doc, 2026-06-11).
- **Conversion-/Event-Tracking-Setup** über GA4, Google Ads, Meta und LinkedIn (Quelle: „LUXHAUS Relaunch – Tracking Überprüfung", Doc, 2025-12-05).
- **Tracking-QA nach Relaunch:** Prüfung, welche Events nach dem Relaunch korrekt feuern und welche fehlerhaft sind (Quelle: „LUXHAUS - Tracking Umsetzung - Fehler & Anpassung auf Website", Doc, 2025-11-28).
- **Geplante Folgeschritte (laut Doc):** Dashboard-Erstellung, ggf. Einbindung von **Server-Side Tagging (SST)**, ggf. Optimierung des **Consent-Management (CMP)**.
- Zwei Angebots-PDFs (Ordner „Angebot/SST" 2026-01-22, „Tracking Umsetzung & Dashboard Erstellung" 2025-06-13) bestätigen Angebotsstand: **Tracking-Umsetzung + Dashboard** sowie **Server-Side Tagging**. Inhalt nur per Dateiname auswertbar — Download nicht möglich (siehe Datenlücken).

> Es liegt **kein SEO-Mandat** (Audit, Keyword, On-Page, Off-Page, Reporting) im Ordner vor.

## SEO-Status & Befunde

Keine SEO-spezifischen Daten im Drive (kein Audit, keine Keyword-Recherche, keine Sistrix/GSC/Ahrefs-Auswertung, keine Title/Meta-Empfehlungen). Es lassen sich aber **website-/technik-nahe Befunde** aus dem Tracking-QA ableiten, die SEO/UX-Relevanz haben:

- **Befund:** Auf der Ansprechpartner-Seite (`/ansprechpartner/steiner-maximilian#kontakt`) ist beim E-Mail-Link keine `mailto:`-URL hinterlegt, sondern nur ein Anker (`…#`). **Begründung:** Der Klick öffnet keine Mailfunktion → Conversion-/UX-Verlust. **Maßnahme:** korrekten `mailto:`-Link hinterlegen. _(Quelle: Tracking-Fehler-Doc, 2025-11-28; im Relaunch-Doc als `link_email` als gelöst markiert — Status prüfen.)_
- **Befund:** Formular Terminanfrage (`/terminanfrage`) hat einen Konfigurationsfehler beim Wunschtermin-Feld; nach „Absenden" erscheint eine Fehlermeldung und es erfolgt **keine Weiterleitung auf die Dankesseite**. **Begründung:** Fraglich, ob Anfragen überhaupt erfolgreich abgesendet werden → potenzieller Lead-Verlust. **Maßnahme:** Fehler beheben, Nutzer auf Dankesseite weiterleiten. _(Quelle: Tracking-Fehler-Doc, 2025-11-28.)_
- **Befund:** Ansprechpartner-Kontaktformular hat **keine Dankesseite mehr** (war beim Erst-Setup vorhanden). **Begründung:** Ohne Dankesseite kann nur der Button getrackt werden → unsaubere Conversion-Messung (auch fehlgeschlagene Sends zählen). **Maßnahme:** Dankesseite als Conversion-Trigger einrichten. _(Quelle: Tracking-Fehler-Doc, 2025-11-28.)_
- **Befund (Inhalt entfernt):** Seite `/plus/broschuere-anfordern` ist nicht mehr verfügbar (von LUXHAUS bewusst gelöscht). **SEO-Relevanz:** gelöschte URLs → Redirect-/404-Prüfung sinnvoll (im Doc nicht behandelt). **Maßnahme:** Redirect-Konzept prüfen (nicht Teil des aktuellen Mandats). _(Quelle: Relaunch-Doc, 2025-12-05.)_
- **Befund:** Im Consent-Banner steht „Marketing Cookies" doppelt; GA4 und Hotjar gehören zu „Statistik", Google Ads fehlt. **Maßnahme:** Kategorien bereinigen/zusammenfassen. _(Quelle: beide Tracking-Docs.)_
- **Befund:** Im Terminvereinbarungs-Formular lassen sich im Nachrichtenfeld keine Leerzeichen eingeben. **Maßnahme:** Eingabevalidierung korrigieren. _(Quelle: beide Tracking-Docs.)_

**Erfolgreich umgesetzte Conversion-Events (Relaunch-QA, 2025-12-05):** `ansprechpartner_vcard`, `link_email`, Baugrundstück finden (`/service/grundstuecksboerse` / `/grundstueck`), Lieblingshausformular, Preisbeispiel anfordern (`/haeuser/fertighaus-preise`), Checkliste anfordern (`/gute-gruende/individuell-bauen`), Garagen-Broschüre, Finanzierungsservice, Infomaterial (`/infos-anfordern`), Terminanfrage, `ansprechpartner_kontakt`. Hauptconversions laufen auf GA4, Google Ads, Meta, LinkedIn.

**Nicht umsetzbar:** `ansprechpartner_pdf` (Visitenkarte nur als vCard, kein PDF), `ansprechpartner`-Lupensuche (kein trackbares Element vorhanden), `link_pdf` (keine PDF-Links auf der Seite gefunden).

> Diese Befunde sind **Content-/URL-/UX-Signale**, die für ein späteres SEO-Mandat nützlich sind (Formular-/Conversion-Pfade, gelöschte URLs, wichtige Landingpages wie `/haeuser/fertighaus-preise`, `/infos-anfordern`, `/terminanfrage`), aber sie sind **keine** SEO-Auswertung.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im Drive existiert nichts zu AI Overviews, LLM-Zitierfähigkeit, ChatGPT/Perplexity/Copilot, KI-Traffic oder Peec-AI-Tracking. Für LUXHAUS ist bislang keine GEO-Arbeit dokumentiert.

## Doc-Typen & Aufbau

Vorhandene Deliverable-Typen im Ordner:

| Typ | Datei | Aufbau |
|---|---|---|
| Google Doc | LUXHAUS Relaunch – Tracking Überprüfung (2025-12-05) | Listen-/Statusstruktur: „Umgesetzt & funktioniert" → „Nicht umsetzbar" → „Offene Themen" → „Nächste Schritte" → „Aufgefallen". Events mit URL + Danke-Seite. |
| Google Doc | Tracking Umsetzung - Fehler & Anpassung auf Website (2025-11-28) | Befund-Listen mit eingerückter **Empfehlung** je Punkt — folgt implizit dem Befund→Maßnahme-Schema. |
| Google Doc | LUXHAUS - Google Tag Manager Installation (2026-06-11) | Knappe Implementierungs-/Anleitungsseite mit GTM-Code-Snippets (Head + Body-noscript), Container-ID `GTM-NZG99B7V`. |
| PDF | Angebot-251584-21027 (SST, 2026-01-22) | Angebot Server-Side Tagging — nur per Name auswertbar. |
| PDF | Angebot-241400-21027 (Tracking Umsetzung & Dashboard, 2025-06-13) | Angebot Tracking + Dashboard — nur per Name auswertbar. |

**Konventionen:** Alle Docs mit EOM-Footer (EOM – Effektiv Online-Marketing GmbH, HRB 204938). Dateibenennung mit Präfix „LUXHAUS …". Tracking-Docs arbeiten mit konkreten Live-URLs inkl. Danke-Seiten-Pfaden als Conversion-Trigger.

## Schreibstil-Notizen

- **Tonalität:** sachlich, prozessorientiert, dokumentierend; klare Befund-→-Empfehlung-Struktur. Sie-Anrede in kundengerichteten Anleitungen (GTM-Doc: „Kopieren Sie … fügen Sie ein").
- **Begriffe:** Conversion/Event, Dankesseite als Trigger, Tags, Consent-Banner/CMP, Server-Side Tagging (SST).
- **Title/Meta-Konvention:** **nicht ableitbar** — es liegt kein On-Page-/Title-Meta-Deliverable vor.

## Offene Punkte / Datenlücken

- **Kein SEO-Material:** kein Audit, keine Keyword-Recherche, keine technische SEO-Prüfung (Crawl/Redirects/hreflang/Broken Links), keine Reportings, keine Title/Meta-Empfehlungen.
- **Kein GEO/KI-Material:** keine AI-Visibility-Daten.
- **Angebots-PDFs nicht lesbar:** Der Drive-Download der beiden PDFs (`Angebot-251584` SST, `Angebot-241400` Tracking/Dashboard) schlug wiederholt mit „Internal error" (500, backendError) fehl — Inhalte nur per Dateiname gewertet, nicht verifiziert. Erneut versuchen, sobald die Drive-API stabil ist.
- **Tracking-Restpunkte (laut Docs offen):** Meta-Conversions im Events-Manager bestätigen, LinkedIn Conversion-IDs in Tags ergänzen (erweiterter Werbekonto-Zugriff nötig), Server-Side-Tagging-Entscheidung, CMP-Optimierung, Dashboard-Erstellung; Tracking zusätzlicher Formularseiten (`/fertighaus`, `/lieblingshaus`, `/planungsgutschein`, `/empfehlung`, `/baufamilienbefragung`, Newsletter, Kundendienst) zu klären.
- **Empfehlung:** Falls ein SEO/GEO-Mandat angestrebt wird, fehlt die Grundlage komplett — ein technischer + On-Page-Erstaudit und eine GSC/Sistrix-Basisanalyse für `luxhaus.de` wären der Startpunkt (nicht im aktuellen Scope).

## Quellen

Ausgewertete Drive-Dateien (Ordner `LUXHAUS`, FOLDER_ID `13pTqM5W1tAvM61WxItdxCJ3CkHCtOZJ5`):

1. **LUXHAUS Relaunch – Tracking Überprüfung** — Google Doc, geändert 2025-12-05 *(gelesen)*
2. **LUXHAUS - Tracking Umsetzung - Fehler & Anpassung auf Website** — Google Doc, geändert 2025-11-28 *(gelesen)*
3. **LUXHAUS - Google Tag Manager Installation** — Google Doc, geändert 2026-06-11 *(gelesen)*
4. **Angebot-251584-21027 (1).pdf** (Ordner Angebot/SST) — PDF, geändert 2026-01-22 *(nur per Name; Download fehlgeschlagen)*
5. **Angebot-241400-21027 (3).pdf** (Ordner Angebot/Tracking Umsetzung & Dashboard) — PDF, geändert 2025-06-13 *(nur per Name; Download fehlgeschlagen)*

Ordnerstruktur: `Angebot/` (SST, Tracking Umsetzung & Dashboard) und `Tracking/` (GTM, 2 Tracking-Docs).
