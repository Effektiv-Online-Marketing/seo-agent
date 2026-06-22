---
tags: [kunde, seo]
kunde: "LPKF"
stand-Datum: 2026-06-19
---

# LPKF

> [!info] Hinweis zum Datenstand
> Diese Wissensdatei basiert ausschließlich auf den im Google-Drive-Kundenordner vorhandenen Dokumenten. Das sichtbar dokumentierte Mandat reicht von 2018 bis **September 2023**; danach wurde die Zusammenarbeit laut Dokumentenlage **pausiert** (siehe [[#Mandat & Gewerke]]). Aktuelle Live-Daten (Sistrix/GSC/Ahrefs) wurden für diese Erfassung **nicht** abgerufen — alle Zahlen stammen aus den ausgewerteten Dateien und sind mit Quelle + Datum belegt.

## Überblick

- **Wer:** LPKF Laser & Electronics SE — börsennotierter Hersteller von Lasersystemen und Laserprozesslösungen mit Sitz in Garbsen/Hannover.
- **Branche:** Industrie / Maschinenbau, B2B, international. Geschäftsfelder umfassen u. a. Laser-Kunststoffschweißen (Laser Plastic Welding), PCB-Prototyping (In-House PCB Prototyping / Research), Laser Depaneling (Nutzentrennung von Leiterplatten), Stencil-Laser (SMT-Schablonen), AMP Technology (2.5D/3D IC, Antenna-in-Package), LTP (digitaler Keramik-/Glasdruck) und Photovoltaik.
- **Hauptdomain:** `lpkf.com` (mehrsprachig: DE, EN, JA, KO). USA-Domain: `lpkfusa.com`.
- **Domain-Landschaft:** stark zersplittert mit zahlreichen Subdomains/Microsites (siehe [[#Subdomain- & Microsite-Strategie]]).

## Mandat & Gewerke

EOM betreute LPKF langjährig mit Schwerpunkt **technisches SEO** und **On-Page/Content** sowie **Reporting**.

- **Technical SEO:** Crawls (Screaming Frog), interne Weiterleitungen/Redirect-Ketten, 404-Management, Canonical-/Parameter-Handling, hreflang, strukturierte Daten, Disavow.
- **On-Page/Content:** Title/Meta-Empfehlungen je Seitenbereich, H1-Struktur, Alt-Texte, interne Verlinkung zur Stärkung von Produktseiten, Keyword-Sets je Geschäftsfeld/Microsite.
- **Reporting:** Monatliches Looker-/Data-Studio-Dashboard (Link im Mai-Report: `datastudio.google.com/s/tAeT3dGRCoQ`), PDF-Export an den Kunden (Ansprechpartner kundenseitig: **Herr Lippold**; EOM-seitig u. a. Jana Heckerott).
- **Tracking:** GA4-Trackingkonzept / Ist-Analyse (2023-06).
- **Schnittstellen:** Technische Umsetzung liegt bei der **Technikagentur Burg Digital**; CMS ist **TYPO3**. EOM liefert Empfehlungen, die Umsetzung erfolgt durch Kunde/Burg Digital.
- **Status (Stand 2023-09):** Laut „Maßnahmen LPKF 2024" wollte EOM „bevor wir die Zusammenarbeit **pausieren**" die wichtigsten Baustellen übergeben — das Mandat ruht damit ab Ende 2023 (zumindest in der vorliegenden Dokumentation).

## SEO-Status & Befunde

### Reporting-KPIs (Quelle: „LPKF Reporting Mai 2023", 2023-06-07)

- **Sichtbarkeitsindex DE (Sistrix):** Mobile 0,307 → 0,284 (30.04.→31.05.); Desktop 0,325 → 0,329.
- **Sichtbarkeitsindex US (Sistrix):** Mobile 0,0107 → 0,0122; Desktop 0,0158 → 0,0127. → US-Sichtbarkeit auf sehr niedrigem Niveau und instabil.
- **Keyword-Rankings DE:** Top-10 von 722 (April) auf 741 (Mai) leicht verbessert; Top-100 von 3.120 auf 2.674 gesunken.
- **GSC organisch EN (`lpkf.com`):** Mai 2023 5.271 Klicks (Vorjahr 5.957), 169.027 Impressionen (+4,1 % YoY), CTR 3,12 % (Vorjahr 2,4 %).
- **GSC organisch DE (`lpkf.com`):** Mai 2023 2.433 Klicks (−42,5 % YoY von 4.604), 121.030 Impressionen (+2,3 % YoY), CTR 2,01 %. → **Auffälliger Klick-Einbruch DE bei steigenden Impressionen** = CTR-/Relevanzthema.

### Technische Befunde

**Befund 1 — hreflang fehlerhaft (Japanisch).**
Domainweit wird die japanische Sprachversion als `hreflang="jp-JP"` ausgezeichnet.
*Begründung:* Der korrekte ISO-639-1-Sprachcode ist `ja`, nicht `jp`; falscher Code wird von Suchmaschinen ignoriert, das japanische Publikum erhält ggf. die falsche Sprachversion.
*Maßnahme:* In TYPO3 (über Burg Digital) die Sprachverknüpfung anpassen, sodass durchgängig `hreflang="ja-JP"` ausgegeben wird.
*(Quelle: „Maßnahmen LPKF 2024", 2023-09)*

**Befund 2 — extreme URL-Inflation durch Parameter.**
Von über **11.000** gecrawlten URLs auf `lpkf.com` enthalten über **2.000 (>20 %) Parameter** (z. B. `?country=Deutschland&cHash=…` auf Messen-/Kontaktseiten).
*Begründung:* Filteroptionen verlinken auf jeweils neue Parameter-URLs statt nur den Seiteninhalt zu ändern → exponentiell viele Quasi-Duplikate, Crawl-Budget wird verschwendet, wichtige Inhalte werden ggf. nicht indexiert.
*Maßnahme:* Entweder Filter technisch so umbauen, dass keine neuen URLs entstehen, oder selbstreferenzierende Canonicals von Parameter-URLs auf die Ausgangs-URL setzen (Backend/Burg Digital).
*(Quelle: „Maßnahmen LPKF 2024", 2023-09; vgl. ältere Analyse „Parameter-URLs mit selbstreferenzierenden Canonicals", 2019-08)*

**Befund 3 — interne Weiterleitungen & 404-Fehler (Eigenleistung möglich).**
213 fehlerhafte interne Weiterleitungen (u. a. interne HTTP-Links statt HTTPS), 67 von Screaming Frog gemeldete Weiterleitungsketten, 44 interne 404-Fehler auf der Hauptdomain.
*Begründung:* Interne Redirect-Ketten und 404s verschwenden Crawl-Budget und verwässern interne Linkkraft; laut EOM-Einschätzung der „Task mit dem stärksten Effekt" und ohne weitere Freigabe umsetzbar.
*Maßnahme:* Interne Links auf finale HTTPS-Zielseiten umbiegen, Ketten auflösen, 404-Ziele weiterleiten.
*(Quelle: „Mögliche Tasks für die nächsten Wochen", 2023-08; vgl. „20221213 LPKF | Neue 404-Fehler", „2022-02-14 Defekte Links")*

**Befund 4 — Kannibalisierung lpkf.com ↔ lpkfusa.com.**
Nach dem CMS-Umzug von `lpkfusa.com` (Herbst 2022) rapider Rückgang des Sistrix-Sichtbarkeitsindex; kurzer Anstieg im Juli 2023 bereits wieder rückläufig.
*Begründung:* Beim Relaunch wurden große Teile der Hauptdomain ohne USA-spezifische Aufbereitung auf `lpkfusa.com` kopiert; alte Inhalte wurden auf `app.lpkfusa.com` verschoben → Rankings entfielen oder verschoben sich zur Hauptdomain.
*Maßnahme (inhaltlich):* Altinhalte von `app.lpkfusa.com` zusammenführen/umziehen, Duplicate Content kontrollieren, Landingpages mit echtem USA-Bezug (lokale Referenzen/Ansprechpartner) anreichern, lokale Branchen-Backlinks aufbauen.
*Maßnahme (technisch):* Interne Weiterleitungen direkt nach Umzug, strukturierte Daten, möglichst Hosting mit US-IP.
*(Quelle: „Maßnahmen LPKF 2024", 2023-09; „20230404 Notizen lpkfusa.com")*

**Befund 5 — Duplicate Content zwischen Hauptdomain und Subdomains.**
Identische/sehr ähnliche Seiten manuell unter mehreren URLs angelegt; konkretes Beispiel: identische „Service Packages"-Seiten auf `stencillaser.lpkf.com/en/products/service-packages` und `laser-depaneling.lpkf.com/en/products/service-packages`.
*Begründung:* Suchmaschinen können nicht erkennen, welche URL relevant ist; Sichtbarkeit splittet sich.
*Maßnahme:* Subdomain-spezifisches Fokusthema in den Texten verankern (z. B. „stencil laser systems" statt „laser depaneling systems"); bei Haupt-/Subdomain-Dubletten die Hauptdomain-URL auf das Subdomain-Äquivalent weiterleiten, solange die Inhalte ausgelagert bleiben.
*(Quelle: „Dupe Content zwischen Hauptdomain und Subdomains", 2023-06; Tabelle „20230614 Duplicate Content Hauptdomain und Subdomains")*

### Subdomain- & Microsite-Strategie

EOM-Kernempfehlung: **Microsites/Subdomains in die Hauptdomain eingliedern.**
*Begründung:* Suchmaschinen behandeln Subdomains als eigenständige Domains; dadurch geht der „Vererbungseffekt" interner und externer Links verloren — externe Links zeigen meist auf `lpkf.com`, die Subdomains erhalten kaum „Empfehlungen". Zusätzlich wird Content auf den Microsites unnötig auf mehrere sehr ähnliche Unterseiten (Technologie vs. Vorteile) aufgeteilt → Kannibalisierung, unklare Relevanz.
*Maßnahme:* Microsite-Inhalte meist auf eine Seite reduzieren und in die Hauptdomain integrieren; Subdomains nur bei zwingender technischer Notwendigkeit oder thematisch komplett eigenständigem Geschäftsbereich.
*(Quelle: „Empfehlung zu Subdomains", 2023-01)*

Bekannte Subdomains (Stand 2023-01):
- `de.lpkf.com` / `en.lpkf.com` — Support-Seiten + **Knowledge-Center (hohes SEO-Potenzial)**
- `amp-technology.lpkf.com`
- `ltp.lpkf.com`
- `laser-depaneling.lpkf.com`
- `lasermicronics.lpkf.com` — Dienstleistungen, **darf bestehen bleiben**
- `stencillaser.lpkf.com` (aus Dupe-Content-Doc)
- `app.lpkfusa.com` (Alt-Inhalte der USA-Domain)

### Keyword-Fokus (Quelle: „202306 Zentrale Keywords", 2023-07; SV = Suchvolumen lt. Dokument)

Keyword-Sets sind pro Geschäftsfeld/Microsite organisiert:
- **Laser Depaneling DE:** nutzentrennen (70), nutzentrennung (70), depaneling (40), leiterplatten trennen (20).
- **Laser Depaneling EN:** pcb laser cutting (110), depaneling pcb (90), pcb depaneling (90), laser depaneling (20).
- **Laser Micronics:** metall laserschneiden (210).
- **Stencil Laser EN:** stencil laser cutting (1.300), smt stencil (1.300), stencil manufacturing (210), precision metal cutting (210).
- **AMP Technology EN:** mmwave antenna (720), antenna in package (390), 3d integrated circuit (210), 2.5D IC (70).
- **LTP EN:** digital ceramic printing on glass (140), digital glass printing machine (50). **LTP DE:** digitaldruck auf glas (90), keramischer digitaldruck auf glas (20).
- **LPKF (Kern) DE:** kunststoffschweißen (2.900), laserschweißen kunststoff (110). **EN:** laser plastic welding (720), plastic laser welding (720).

> Höchste Volumina im Set: „kunststoffschweißen" (2.900, DE), „stencil laser cutting"/„smt stencil" (je 1.300, EN), „laser plastic welding" (720, EN).

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im gesamten Kundenordner existieren keine Dokumente zu AI Overviews, ChatGPT/Perplexity/LLM-Sichtbarkeit, llms.txt oder generativer Suche. Das dokumentierte Mandat endete (Pause) im Herbst 2023, also vor der breiten Etablierung von GEO-Reporting. Für eine GEO-Bewertung von LPKF lägen aktuell **keine Vault-Quellen** vor — dies wäre bei Reaktivierung des Mandats neu aufzusetzen (z. B. Brand-Mentions/Citations-Tracking über Peec AI oder Sistrix AI).

## Doc-Typen & Aufbau

Der Ordner folgt einer klaren Ablage-Logik:
- **Numerierte Hauptordner:** `00 ORGA/PM`, `01 SEO`, `02 TRACKING`, `REPORTINGS`, `MEETINGS`, `RELAUNCH-2018`, `BACKUP`.
- **`01 SEO`** ist nach **Geschäftsfeld/Domain** untergliedert (LPKF Hauptdomain, LPKFUSA, LASER MICRONICS, Laser-Depaneling, diverse Microsites, Arralyze, Vitrion, LTP) plus Querschnittsordner (`Crawls`, `hreflang`, `Domainübergreifend`, `OnPage Empfehlungen`, `Rankings`).
- **`REPORTINGS`** nach Jahr (2017–2023), Monatsreports als PDF/Doc.
- **Doc-Typen:** Empfehlungs-Briefe (Google Docs, Brief-Form an Herrn Lippold), Analyse-Tabellen (Sheets: 404-Listen, Redirects, Title/Meta, H1, Duplicate Content), Crawl-Exporte, Title/Meta-Sheets je Seitenbereich, strukturierte-Daten-Snippets (.txt).
- **Benennung:** überwiegend `YYYYMMDD LPKF | <Thema>` bzw. `LPKF: <Thema>` — datiert und thematisch eindeutig.

## Schreibstil-Notizen

- Empfehlungen sind als **persönliche Briefe** formuliert: Anrede „Guten Tag Herr Lippold," + Grußformel, durchgängig **Sie-Anrede**.
- Genderschreibweise mit Sternchen („Nutzer*innen", „Besucher*innen", „Ansprechpartner*innen").
- **Befund → Begründung → Maßnahme**-Logik ist erkennbar, technische Sachverhalte werden für Nicht-Techniker mit Analogien erklärt (Crawl-Budget = „Akku"; Link-Vererbung = „Empfehlung").
- Klare Trennung von **inhaltlichen** und **technischen** Maßnahmen (Bullet-Blöcke).
- Hinweis-Konvention für Versand: „Beim Versenden auf Markierungen, fettgedruckte Textpassagen und Anhang achten!" — Farb-/Fett-Markup wird im Doc gesetzt (vgl. Vault-Regel zu Grün/Gelb-Markup).
- Signatur: „EOM – Effektiv Online-Marketing GmbH".

## Offene Punkte / Datenlücken

- **Mandatsstatus unklar:** Dokumentation endet 2023-09 mit „Pause"-Ankündigung. Ob/seit wann reaktiviert — nicht aus dem Ordner ersichtlich.
- **Keine aktuellen Live-Daten** in dieser Erfassung erhoben (Sistrix-SI, GSC, Ahrefs, Rankings). Reporting-Zahlen sind Stand Mai 2023.
- **Office-Dateien** (`.xlsx`) wie „lpkf.com-Titles Meta Descriptions" wurden nur per Dateiname gewertet (nicht exportierbar); Inhalte nicht eingesehen.
- **Reportings 2024+** nicht vorhanden → bestätigt die Mandatspause.
- **GEO/KI komplett offen** (siehe oben).
- **Umsetzungsstand der Empfehlungen** (hreflang, Parameter-Canonicals, Subdomain-Integration) nicht dokumentiert — abhängig von Burg Digital/TYPO3.
- **Mehrere Eigenmarken/Domains** (Arralyze, Vitrion, LASER MICRONICS, LTP, lpkfusa.com) — jeweils eigene SEO-Logik, hier nur soweit erfasst, wie für die Hauptdomain relevant.

## Quellen (ausgewertete Dateien)

Alle aus Drive-Ordner `01 SEO` bzw. dessen Unterordnern, Account `ben@eom.de`:

1. **„202308 LPKF | Maßnahmen LPKF 2024"** (Google Doc, 2023-09-01) — hreflang, Parameter-URLs, lpkf.com↔lpkfusa.com-Kannibalisierung.
2. **„202308 LPKF | Mögliche Tasks für die nächsten Wochen"** (Google Doc, 2023-08-11) — interne Redirects (213), Ketten (67), 404 (44), Alt-Texte, Disavow.
3. **„202306 LPKF | Zentrale Keywords"** (Google Doc, 2023-07-10) — Keyword-Sets je Geschäftsfeld inkl. SV.
4. **„20230619 LPKF | Dupe Content zwischen Hauptdomain und Subdomains"** (Google Doc, 2023-06-19) — Duplicate-Content-Empfehlung.
5. **„20230103 LPKF | Empfehlung zu Subdomains"** (Google Doc, 2023-01-09) — Subdomain-/Microsite-Strategie.
6. **„LPKF Reporting Mai 2023"** (Google Doc, 2023-06-07) — Sistrix-SI, GSC-KPIs DE/EN/US.
7. Ordnerstruktur `01 SEO`, `02 TRACKING`, `REPORTINGS`, `Domainübergreifend` (Listung, 2026-06-19) — Doc-Typen, Domain-Landschaft, „LPKF - Ist-Analyse - GA4 Trackingkonzept" (2023-06, per Name gewertet).

Verknüpft: [[NIBE]] · [[VHV Versicherung]] (Vergleichskunden für Methodik)
