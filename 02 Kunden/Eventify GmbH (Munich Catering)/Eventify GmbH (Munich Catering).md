---
tags: [kunde, seo]
kunde: "Eventify GmbH (Munich Catering)"
stand-Datum: 2026-06-19
---

# Eventify GmbH (Munich Catering)

> Wissensbasis-Notiz (EOM-intern). Aufbau: Befund → Begründung → Maßnahme. Sie-Anrede in Kunden-Copy, „KI" statt „AI". Daten ausschließlich aus den ausgewerteten Drive-Dateien; nichts geschätzt. Fehlende/nicht zugängliche Daten sind als Datenlücke markiert.

## Überblick

- **Marke / Produkt:** „Munich Catering" — Catering-Dienstleister mit lokalem Bezug zu München. Rechtsträger laut Mandatsbezeichnung: Eventify GmbH. (Hinweis: In den ausgewerteten Dateien wird durchgängig die Marke „Munich Catering" genannt; der Firmenname „Eventify GmbH" stammt aus der Mandatsbezeichnung, nicht aus den Drive-Dokumenten — siehe Datenlücken.)
- **Branche:** Catering / Event-Gastronomie, regional München. Google behandelt „Catering" als lokale Suche, daher Optimierung auf generische Keywords *und* auf „… München" parallel sinnvoll (Quelle: *Empfehlung zur Seiten-Navigation & Struktur*).
- **Domains:**
  - Live-Domain: `https://munich-catering.com/` (DE) und `https://munich-catering.com/en/` (EN).
  - Relaunch-Staging zum Auditzeitpunkt: `https://catering-lac.vercel.app/` (Vercel-Hosting; Quelle: *Relaunch SEO Audit 28.11.2025*).
- **Sprachen:** Deutsch (Default) + Englisch. EN-Seiten gestartet ~04.02.2025 (Quelle: *SEO-Klickzahlen Überblick*, 18.08.2025).
- **Zahlungs-/Shop-Funktion:** Es existiert ein Bestell-/Checkout-Flow inkl. Stripe-Anzahlung (Deposit), GA4-/GTM-Tracking, Kontoanlage und transaktionalen E-Mails — die Site ist also nicht nur Lead-Gen, sondern hat einen E-Commerce-artigen Bestellprozess (Quelle: *QA Findings*, 16.04.2026).

## Mandat & Gewerke

EOM betreut Munich Catering mit einem **kombinierten SEO- + SEA-Mandat** seit **Juni 2023** (Quelle: *SEO-Klickzahlen Überblick*).

Belegte Gewerke (aus Ordnerstruktur `02_Meetings`, `03_Reportings`, `04_Tracking`, `05_SEO`, `06_SEA`, `07_Content` und den Dokumenten):

- **SEO On-Page / Content:** laufende Erstellung neuer Leistungs-Landingpages (Texterstellung im Vault als `.docx`), Title/Meta, Überschriftenstruktur, Formular-Optimierung.
- **SEO Technik:** Relaunch-Begleitung (Audit, Crawl, Redirect-Liste, hreflang/Canonical/robots/Sitemap, strukturierte Daten), QA der neuen Site.
- **SEA:** Google-Ads-Kampagnen DE + EN (inkl. Messe-Kampagne EN, PMax), laufende Optimierung (Quelle: *Reporting Dezember 2025*).
- **Tracking & Analytics:** GA4/GTM/Stripe-Tracking, Measurement-Protocol-Setup, Cookie-Banner-Spezifikation (Quelle: *Tracking & Analytics Implementation Briefing*, *QA Findings*, *Tracking Feedback*).
- **Reporting:** Monatsreports via Looker-Studio-Dashboard (`lookerstudio.google.com/s/mIV5l-Cv_Mw`), monatliche Zusammenfassung DE/EN.
- **Content/Kreativ:** Spot/Video-Assets (Ordner `07_Content`).

Aktuelle Phase (Stand der jüngsten Dateien, Q1–Q2 2026): **Website-Relaunch** auf neues System (Staging auf Vercel), parallel laufender Ausbau der Leistungsseiten. Ansprechpartner kundenseitig laut Reportings: „Leo"; im Reporting genannte Empfänger u. a. „Leo".

## SEO-Status & Befunde

### Sichtbarkeit & organische Performance

- **Befund:** Allgemeine Sichtbarkeit laut Sistrix „momentan noch sehr gering"; Rankings mit „Ausschlägen und Entwicklungen" (Quelle: *Reporting Dez 2025*, 21.01.2026).
- **Befund (GSC, Dez 2025 vs. Vormonat):** Klicks **+2,7 %**, Impressionen **+33,1 %**. GA4: organische Nutzer **−13,8 %** ggü. Vormonat (Quelle: *Reporting Dez 2025*).
- **Befund (Langfrist, Stand 18.08.2025):** Letzte 6 Monate vs. die 6 Monate davor: **>500 Klicks** und **~78.000 Impressionen** mehr (DE). EN seit Start (04.02.2025): **229 Klicks**, **>17.000 Impressionen**. Seit Start der Zusammenarbeit (Juni 2023): **+36 Top-10-Keywords**, **+331 Top-100-Keywords** (Quelle: *SEO-Klickzahlen Überblick*).
- **Top-5 organische Suchanfragen (ohne Brand, Dez 2025):** arabisches catering · catering italienisches buffet · catering munich · catering münchen ost · gastro verleih in der nähe (Quelle: *Reporting Dez 2025*).
- **Begründung:** Sichtbarkeit wächst, ist aber für die generischen Geld-Keywords noch nicht etabliert. **Maßnahme (lt. EOM):** Fokus weiter auf Aufbau neuer Leistungsseiten.

### Technische Befunde aus dem Relaunch-Audit (Staging, 28.11.2025)

Quelle durchgehend: *Munich Catering Relaunch SEO Audit 20251128* (Staging `catering-lac.vercel.app`). Diese Punkte sind vor dem Go-Live abzustellen.

- **KRITISCH – Sprachversionen ohne eigene URL:** Übersetzung ändert die URL nicht (dynamische Auslieferung), es gibt keine eigenständig indexierbaren URLs je Sprache. Ohne JavaScript wird nur die **EN-Version** ausgespielt. → Indexierung & Sichtbarkeit beider Sprachen gefährdet. **Maßnahme:** Eigene URLs je Sprache (z. B. `/` DE, `/en` EN), danach hreflang.
- **hreflang fehlt:** Erst nach eigenen Sprach-URLs umsetzbar; jede Version muss sich selbst und die andere wechselseitig referenzieren.
- **robots.txt fehlt** → keine Crawler-Steuerung/Sitemap-Verweis. **Maßnahme:** robots.txt anlegen, auf Sitemap verweisen.
- **XML-Sitemap fehlt** → erschwert vollständige Indexierung nach Relaunch. **Maßnahme:** `sitemap.xml` bereitstellen.
- **Canonical-Tags fehlen** → Risiko Duplicate Content (Parameter, Trailing Slashes, Protokolle). **Maßnahme:** selbstreferenzierende Canonicals im `<head>`.
- **Strukturierte Daten fehlen** komplett. **Maßnahme:** JSON-LD für **Organization** (global), **LocalBusiness** (lokaler Catering-Bezug) und **FAQ** (auf FAQ-Seiten).
- **404-Fehler:** Footer verlinkt `/terms` und `/privacy`, die (noch) nicht existieren.
- **Überschriftenstruktur fehlerhaft:** doppelte H1, gebrochene Hierarchie (H1→H4), h-Tags zu Styling-Zwecken und im Footer. **Maßnahme:** genau eine H1/Seite, saubere H1→H4-Hierarchie, keine h-Tags im Footer.
- **Bilder zu groß / nicht weboptimiert** → Ladezeit & Core Web Vitals. **Maßnahme:** WebP, korrekte Dimensionen, Lazy Loading.
- **Title & Meta-Description noch nicht gepflegt** auf der neuen Site. **Maßnahme:** bestehende, optimierte Meta-Daten aus dem Crawl-Export der Live-Site übernehmen, um Rankings nicht zu gefährden.
- **CMS-Anforderungsliste** für SEO-Pflege dokumentiert (individuelle Meta-Daten, JSON-LD global + pro Seite, Alt-Texte, Akkordeons, Canonicals, noindex, automatische XML-Sitemap, Bild-Komprimierung, sprechende URLs, H1–H4, hreflang, Breadcrumbs, Redirect-Management, individuelle 404-Seite).

### Tracking-/QA-Befunde Relaunch (16.04.2026)

Quelle: *QA Findings and Cookie Banner Specification 260416* (E2E-Test mit Bestellung MCA-2600-16, Gesamtwert 312,81 €, Deposit 62,56 €).

- **Finding 1:** `purchase`-Event feuert **zu früh** — beim Klick „Continue to Payment", bevor die Stripe-Anzahlung erfolgt ist. **Maßnahme:** Bestellabsenden → `generate_lead` (lead_type: order_request); `purchase` erst nach erfolgreicher Stripe-Zahlung (gleiche transaction_id), Wert = Gesamtbestellwert (nicht Deposit); Storno → `refund`.
- **Finding 2:** Nach erfolgreicher Stripe-Zahlung (Rücksprung `?paid=1`) wird **kein** Conversion-Event registriert; der spezifizierte Measurement-Protocol-Call aus dem Webhook läuft offenbar nicht. **Maßnahme:** Webhook/MP-Call prüfen (Erreichbarkeit, client_id-Übergabe, api_secret/measurement_id, HTTP-Status), `purchase` von dort feuern.
- **Finding 3:** Optionales clientseitiges Backup-Event auf `?paid=1` empfohlen — bevorzugt **Variante A** (`payment_confirmed`, getrennt ausgewertet, keine Kollision mit serverseitigem `purchase`).
- **Verifiziert OK:** contact_form_submit, generate_lead (Step 1+4), quote_form_step (Step 2+3), view_item_list, view_cart, begin_checkout.
- **Weitere UX/Lokalisierungs-Bugs:** DE-Formular Step 4 zeigt EN-Untertitel; E-Mail im Checkout nicht vorbefüllt; Telefon-Validierung lehnt nationales Format ab; „My Orders" zeigt alles als „Pending"; transaktionale E-Mails kommen auf Englisch trotz DE-Bestellung.

### Cookie-Banner-Spezifikation (Relaunch)

- **Befund/Vorgabe:** Custom-Cookie-Banner (in-house, kein Usercentrics-Lizenz mehr), **rein visuell** — kein Script-Blocking/Consent-Gating, nur UI + Persistenz (`localStorage` `cookie_consent_v1`, 12 Monate). Kategorien: Essential (ON, fix), Funktional/Statistik/Marketing (OFF default). **Offene Punkte für Dev:** Herkunft eines zweiten GA4-Cookies `_ga_MLLT4F7KPF`; verwaiste `uc_*`-Keys (Usercentrics-Reste). Fehlende Rechtsseite: `/impressum` (404) muss angelegt werden; `/datenschutz` und `/agb` existieren.
- **Hinweis (intern):** Ein „rein visuelles" Cookie-Banner ohne tatsächliches Consent-Gating ist datenschutzrechtlich heikel — als offener Punkt vermerkt, nicht als Empfehlung von EOM zu lesen.

## GEO / KI-Sichtbarkeit

- **Begrenzte GEO-Substanz vorhanden.** Es liegt **keine** GEO-Messung (z. B. Peec AI, Sistrix AI, AI-Overview-/LLM-Citation-Tracking) im Kundenordner vor — also **keine Daten zur KI-Sichtbarkeit** von Munich Catering in ChatGPT/Perplexity/AI Overviews.
- Das einzige KI-nahe Dokument ist *Tool-Empfehlungen ChatBot für Munich Catering* (07.05.2025): eine **Marktübersicht von Chatbot-/Live-Chat-Tools** (HubSpot Chatbot, Userlike, moinAI, ProProfs, Freshchat, Tidio, Crisp) zur Lead-Qualifizierung auf der Website — also On-Site-Conversational-Tooling, **nicht** GEO/Answer-Engine-Optimierung.
- Indirekt GEO-relevant aus dem Audit: empfohlene **strukturierte Daten** (Organization/LocalBusiness/FAQ) und eine saubere, indexierbare Sprach-/URL-Struktur sind Grundvoraussetzungen, um in KI-Antworten zitierfähig zu sein. Ein dediziertes GEO-Gewerk ist bislang nicht dokumentiert.

## Doc-Typen & Aufbau

Im Kundenordner wiederkehrende Deliverable-Typen:

- **Empfehlungs-Docs** (Google Docs): „Munich Catering | Empfehlung …" (z. B. neue Landingpage, Navigation/Struktur, Messe Catering, Grill Catering, Kaffeemaschine mieten, Karriere-Seite). Aufbau: kurze Einleitung → Befund → konkrete Umsetzungsempfehlung, häufig mit Beispiel-URLs und Suchvolumen-Annotationen.
- **Landingpage-Texte** (`.docx`, Office — nur per Name auswertbar): „Munich Catering _ Text … Landingpage" (Barista mieten, Canapés, Bio, Geburtstag, Office, Lunchbox, Pizza, Privat). Jüngste: Barista/Canapés (03.06.2026).
- **Keyword-Recherche** (Sheets): „KWR Übersicht Leistungen" (zuletzt 21.04.2026), „KWR Leistungsseiten" — strukturiert je Landingpage: *Seite / Keyword / SV / Prio / Anmerkungen / Status* (erstellt / on hold).
- **Technik-/Relaunch-Docs:** Relaunch SEO Audit (DE+EN), QA Findings, List of Errors, Relaunch Feedback (mehrere Termine), Redirect List, html-Crawl (`.xlsx`), Content Migration Findings.
- **Tracking-Docs:** Implementation Briefing, Tracking Feedback.
- **Reportings** (Docs): monatlich, „Munich Catering Reporting – <Monat> <Jahr>", als Anschreiben mit Looker-Link, Summary SEA (DE/EN-KPIs), Summary SEO (GSC/GA4/Sistrix), „Maßnahmen & Doings" (letzter Monat + geplant).

## Schreibstil-Notizen

- **Reportings:** lockere, persönliche Anrede („Hallo Leo,"), Ich-/Wir-Perspektive des Beraters, Unterschrift mit Vornamen (z. B. „Sharia"). KPI-Sprache mit %-Vergleichen zu Vor-Monat/Vor-Jahr, Klammerverweise auf Dashboard-Seiten („s. Seite 9"). Abschluss mit Dank für die Zusammenarbeit.
- **Empfehlungs-/Audit-Docs:** sachlich, strukturiert, **Befund → Begründung → Empfehlung**; technische Empfehlungen mit konkreten Code-/URL-Beispielen (hreflang, Canonical, JSON-LD). Kritikalität wird markiert („⇒ Dies ist ein kritisches Problem").
- **KWR-Konvention:** „SV." = monatliches durchschnittliches Suchvolumen; lokale vs. generische Keyword-Variante explizit unterschieden.
- **Footer/Branding:** EOM – Effektiv Online-Marketing GmbH, Hannover (teils + Stuttgart), GF Ernest Mavriqi.
- **Sprache:** überwiegend Deutsch; technische QA-/Tracking-Docs teils auf Englisch.

## Offene Punkte / Datenlücken

- **Firmenname vs. Marke:** „Eventify GmbH" erscheint in den Drive-Dokumenten nicht; dort durchgängig „Munich Catering". Zuordnung des Rechtsträgers nicht aus den Dateien belegt.
- **Keine GEO-/KI-Sichtbarkeitsdaten** im Ordner (kein Peec/Sistrix-AI-Tracking, keine AI-Overview-/LLM-Citation-Auswertung).
- **Office-Dateien (`.docx`/`.xlsx`) nicht exportierbar** und daher nur per Namen gewertet: alle Landingpage-Texte, der html-Crawl (`munich-catering html-Crawl-251128.xlsx`), die Redirect-Liste-Quelle. Inhalt der konkreten LP-Texte und der Crawl-Issues nicht im Detail erfasst.
- **Keine eigenen Tool-Abfragen** (Sistrix/Ahrefs/GSC/DataForSEO) durchgeführt — alle Zahlen stammen aus den EOM-Dokumenten zum jeweiligen Stand; aktuelle Live-Werte können abweichen.
- **Relaunch-Status unklar:** Ob der Vercel-Relaunch zwischen Nov 2025 und Q2 2026 live gegangen ist und ob die Audit-Kritikpunkte (Sprach-URLs, hreflang, robots, Sitemap, Canonicals, Schema) behoben sind, ist aus den Dateien nicht abschließend belegt.
- **Datenschutz-Risiko Cookie-Banner** (rein visuell, ohne echtes Consent-Gating) — offener rechtlicher Punkt, in den Docs nicht final geklärt.

## Quellen (ausgewertete Dateien)

Alle aus Drive-Ordner *Eventify / Munich Catering* (`1ovcGokWS5sgQqZbInZ2I8ZIPvUlOBtPW`), Account `ben@eom.de`:

- *Munich Catering Relaunch SEO Audit 20251128* (Doc, 28.11.2025) — technisches Relaunch-Audit Staging.
- *Munich Catering – QA Findings and Cookie Banner Specification 260416* (Doc, 16.04.2026) — Tracking-QA + Cookie-Banner-Spec.
- *Munich Catering Reporting – Dezember 2025* (Doc, 21.01.2026) — Monatsreport SEA/SEO + Doings.
- *Munich Catering – SEO-Klickzahlen Überblick* (Doc, 18.08.2025) — Langfrist-GSC-/Keyword-Entwicklung.
- *Munich-Catering | Empfehlung zur Seiten Navigation/Struktur* (Doc, 25.10.2024) — Seitenarchitektur + Keyword-Mapping mit SV.
- *Munich Catering | KWR Übersicht Leistungen* (Sheet, zuletzt 21.04.2026) — Keyword-Recherche je Leistungsseite (SV, Prio, Status).
- *Tool-Empfehlungen ChatBot für Munich Catering* (Doc, 07.05.2025) — On-Site-Chatbot-Toolvergleich (einziges KI-nahes Dokument).

Verwandt: [[Über EOM]] · [[SEO-Methodik]] · [[Reporting-Standards]] · [[Schreibstil]]
