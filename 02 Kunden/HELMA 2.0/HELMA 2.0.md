---
tags: [kunde, seo]
kunde: "HELMA 2.0"
stand: 2026-06-19
quelle: "Google Drive Kundenordner (Account ben@eom.de)"
---

# HELMA 2.0

> Analyse-Logik im Vault: **Befund → Begründung → Maßnahme.** Sie-Anrede in Kunden-Copy, "KI" statt "AI". Es wird nichts erfunden — fehlende/nicht zugängliche Daten sind offen markiert.

## Überblick

**Befund:** HELMA ist ein deutscher **Massivhaus-Bauträger** ("Stein-auf-Stein"-Bauweise) mit über 40 Jahren Erfahrung, Unternehmenssitz und Musterhauspark in **Lehrte** (Niedersachsen). Zentrale juristische Einheit ist die **HELMA Eigenheimbau AG**; eine 100-%-Tochter ist die **Helma Immobilien GmbH** (Bauträger/Direktvertrieb von Immobilien, u. a. Vertriebsgebiet Leipzig in Sachsen). Branche: Hausbau / Immobilien (Eigenheime, Eigentumswohnungen, Doppel-/Reihenhäuser, Grundstücke, Kapitalanlage).

**Domains / Sprachen (aus den Doc-URLs ableitbar):**
- `helma.de` — Hauptdomain Hausbau/Eigenheime (z. B. `/eigenheime/bauunternehmen-berlin.html`, `/eigenheime/bauunternehmen-chemnitz.html`)
- `helma-wohnungsbau.de` — Immobilien/Wohnungsbau (z. B. `/aktuelle-projekte/sachsen.html`, `/aktuelle-projekte/sachsen-anhalt.html`)
- Sprache: **Deutsch (DE)**, regionale Landingpages je Bundesland/Stadt. URL-Struktur mit `.html`-Endung deutet auf **TYPO3** als CMS hin (siehe Mandat).

**Begründung:** Alle ausgewerteten Deliverables tragen den EOM-Footer und referenzieren ausschließlich `.de`-URLs mit regionalem Zuschnitt; das Tochter-/Mutterverhältnis und die Vertriebsgebiete sind in den Content-Empfehlungen explizit beschrieben.

## Mandat & Gewerke

Aus dem Übergabedokument ([[#Quellen|Übergabe_Marketing]] + EOM-Anmerkung) und den Content-Deliverables erkennbar:

- **SEO (administrativ + operativ) bei EOM:** "Google-Konten / SEO → administrative Betreuung über EOM sichergestellt." EOM hat Zugriff auf Google Analytics und **Looker Studio** (kann Reports anpassen), **Analytics ist bereits in Betreuung enthalten**.
- **On-Page / Content:** EOM übernimmt **Umsetzung neuer Landingpages** und **Anpassung bestehender Landingpages**; inhaltliche/textliche Erstellung über EOM möglich. Belegt durch die laufende Serie **Schwellenkeyword-Recherche & N-OP-Empfehlung** (regionale Landingpages).
- **Technik (CMS):** Website auf **TYPO3**, technische Betreuung über externen Dienstleister **HDNET**; EOM hat **Backend-CMS-Zugang** und kann Anpassungen vornehmen. Tickets über **JIRA** (HDNET) und **Monday** (EOM-Abstimmung).
- **Consent/Tracking:** **Cookiebot** im Einsatz; EOM hat Zugang und kann Anpassungen vornehmen.
- **Begleitend (nicht EOM-Kerngewerk):** Social Media über *yoursquares*, Newsletter zurückgestellt (CRM-Schnittstelle erforderlich), Grafik teils inhouse/Freelancer.

**Maßnahme/Hinweis:** SEO-Schwerpunkt des Mandats liegt aktuell klar auf **regionaler On-Page-/Content-Optimierung** (Schwellenkeywords) plus **Reporting via Looker/Analytics**. Es fehlen im Ordner laufende technische Audits, Crawls, Backlink- oder Sichtbarkeits-Reportings — diese sind hier nicht belegt (siehe Datenlücken).

## SEO-Status & Befunde

Alle Befunde stammen aus den vier **Schwellenkeyword-/N-OP-Empfehlungen** (Google Docs, Aug.–Sep. 2025). "SV" = Suchvolumen-Angabe **aus dem Doc** (Quelle/Tool im Doc nicht genannt — nicht von EOM nachgeschätzt).

**Befund 1 — Regionale Landingpages mit klarem Schwellenkeyword-Fokus.** Vier optimierte Seiten:

| Seite | URL | Hauptkeyword | SV (lt. Doc) | Datum |
|---|---|---|---|---|
| Bauunternehmen Berlin | helma.de/eigenheime/bauunternehmen-berlin.html | bauunternehmen berlin | 1.000 | 2025-09-10 |
| Bauunternehmen Chemnitz | helma.de/eigenheime/bauunternehmen-chemnitz.html | bauunternehmen chemnitz | 170 | 2025-09-03 |
| Immobilien Sachsen | helma-wohnungsbau.de/aktuelle-projekte/sachsen.html | immobilie sachsen kaufen | 110 | 2025-08-28 |
| Immobilien Sachsen-Anhalt | helma-wohnungsbau.de/aktuelle-projekte/sachsen-anhalt.html | immobilien sachsen-anhalt kaufen | 30 | 2025-09-03 |

**Begründung:** Jede Seite adressiert ein Hauptkeyword + 2–4 Nebenkeywords (z. B. Berlin: "massivhausanbieter berlin" SV 170, "bauunternehmen in berlin" SV 140; Sachsen: "haus kaufen sachsen" SV 1.000, "immobilie sachsen" SV 390). **Maßnahme (bereits empfohlen):** Title/Meta + H1/H2 + Fließtext auf das Haupt- und die Nebenkeywords ausrichten.

**Befund 2 — Title/Meta-Optimierung: Marke + Keyword nach vorn.** Durchgängiges Muster: das **Hauptkeyword wandert in den Titel-Anfang**, Marke "HELMA" wird ergänzt, Description erhält Trust-/USP-Signale + Checkmarks + CTA.
- Beispiel Berlin: alt *"Ihr Bauunternehmen in Berlin für Massivhäuser | HELMA"* → neu *"Bauunternehmen Berlin & Massivhausanbieter | HELMA"*.
- Beispiel Sachsen: alt *"Immobilien oder Grundstücke in Sachsen kaufen: Eigentumswohnungen"* → neu *"Immobilien kaufen in Sachsen: Große Auswahl bei HELMA"*.
**Begründung:** Keyword-Frontloading + Markennennung stärken Relevanz und CTR. **Maßnahme:** neue Metas im CMS einpflegen (durch EOM/HDNET).

**Befund 3 — Content-Neufassung mit höherer Keyword-Dichte und Suchintent-Bezug.** Die Empfehlungen ersetzen "von der Stange"-Einleitungen durch keyword-tragende H1/H2 (z. B. "Immobilien in Sachsen-Anhalt kaufen – dort wohnen, wo andere Urlaub machen", "Hauskauf Sachsen-Anhalt – provisionsfrei direkt vom Bauträger"). USP-Anker durchgängig: **provisionsfrei / Direktvertrieb / Bauträger aus erster Hand / 40+ Jahre Erfahrung / Massivbau**.
**Begründung:** Die alten Texte waren tourismus-/erlebnislastig und keyword-arm; die neuen Versionen verankern Such-Keywords semantisch und transportieren Conversion-Treiber. **Maßnahme:** Texte mit Markup (grün = neu, gelb = angepasst, rot = entfällt) ins CMS übertragen.

**Befund 4 — Markenkonsistenz prüfen.** In den Texten tauchen unterschiedliche Firmennamen auf ("Helma Immobilien GmbH", "HELMA Eigenheimbau AG", an einer Stelle "Helma Hausbau GmbH"/"HELMA Hausbau AG"). **Maßnahme:** Firmenbezeichnungen vor Veröffentlichung gegen die korrekten Rechtsformen prüfen (Konsistenz/E-E-A-T-Signal, vermeidet falsche Entitätssignale).

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten im Kundenordner gefunden.** Es liegen keine Deliverables zu AI Overviews, ChatGPT/Perplexity/Copilot-Zitaten, LLM-Traffic, Brand-Radar/Peec-Tracking oder `llms.txt` vor. Die ausgewerteten Dokumente sind reine klassische On-Page-/Keyword-Empfehlungen.

**Hinweis (Potenzial, nicht belegt):** Die Q&A-artigen H2-Überschriften in der Chemnitz-Seite ("Wer ist HELMA und was macht uns als Bauunternehmen Chemnitz besonders?") sind grundsätzlich GEO-/Antwort-freundlich strukturiert — bislang aber kein dokumentiertes GEO-Mandat.

## Doc-Typen & Aufbau

**Deliverable-Typ im Ordner:** ausschließlich **Google Docs** des Typs *"Schwellenkeyword-Recherche & N-OP-Empfehlung"* (4 Stück) + 1 Übergabe-Dokument (Word `.docx`, nicht exportierbar) und dessen EOM-Anmerkung (Google Doc). Keine Sheets, keine Slides.

**Standard-Aufbau der N-OP-Empfehlung (sehr konsistent):**
1. **Kopf:** Titel + Ziel-**URL**.
2. **1. Keywords** — Hauptkeyword (mit SV) + Nebenkeywords (mit SV).
3. **2. Metas** — *Meta-Titel aktuell* vs. *Meta-Titel neu*; *Meta-Description aktuell* vs. *neu*.
4. **3. Content** — Vorher/Nachher mit **Farb-Markup-Legende**: grün = neu, gelb = angepasst, rot = entfällt. Strukturiert mit `<h1>`/`<h2>`-Auszeichnung.
5. **Footer:** EOM – Effektiv Online-Marketing GmbH (Hannover/Stuttgart), HRB 204938, GF Ernest Mavriqi.

**Hinweis:** Das Farb-Markup (grün/gelb/rot) ist nur im Google Doc sichtbar, nicht im Textexport — beim Anlegen neuer Docs manuell setzen (vgl. Vault-Drive-Konvention).

## Schreibstil-Notizen

- **Tonalität:** durchgehende **Sie-Anrede**, warm-einladend, vertrauensbildend; emotionale Hooks ("dort wohnen, wo andere Urlaub machen", "Traum vom Eigenheim"). Conversion-USPs werden wiederholt verankert: *provisionsfrei*, *Direktvertrieb / aus erster Hand*, *über 40 Jahre Erfahrung*, *Massivbau / Stein-auf-Stein*, *Rundum-sorglos / alles aus einer Hand*.
- **Title-Konvention:** **Hauptkeyword vorn**, Marke "HELMA" hinten mit Pipe (`… | HELMA`) oder integriert ("… bei HELMA"). Titel werden mit Mehrwertergänzung ausgespielt (z. B. "& Massivhausanbieter").
- **Meta-Description-Konvention:** USP-Aufzählung mit **✓-Checkmarks**, abschließender **CTA mit ► / ➧-Pfeil** ("► Mehr erfahren!", "➧ Jetzt informieren!").
- **Überschriften:** keyword-tragende H1/H2; teils im Frage-Antwort-Stil (Chemnitz).

## Offene Punkte / Datenlücken

- **Keine technischen SEO-Deliverables** im Ordner: keine Crawls, Broken-Links, Redirects, hreflang-, Indexierungs- oder Core-Web-Vitals-Checks (Technik läuft über HDNET).
- **Keine Sichtbarkeits-/Ranking-/Backlink-Reports** und keine Monatsreports vorhanden — obwohl Looker Studio + Analytics laut Übergabe in EOM-Betreuung sind. Reportings liegen vermutlich außerhalb dieses Ordners.
- **SV-Quelle/Tool nicht dokumentiert** (Sistrix/Ahrefs/DataForSEO?) und **kein Erhebungsdatum** der Keyword-Zahlen in den Docs — Werte stammen 1:1 aus den Docs, nicht nachgeschätzt.
- **`Übergabe_Marketing.docx`** ist Office-Format und ließ sich nicht als Text exportieren; Inhalt nur über die EOM-Anmerkungsfassung (Google Doc) erschlossen.
- **Markennamen-Inkonsistenz** (Eigenheimbau AG / Hausbau AG / Immobilien GmbH) klären.
- **Kein GEO-/KI-Mandat** dokumentiert.

## Quellen

Ausgewertete Drive-Dateien (Kundenordner `1h5xoCwfE2FDk1VMS2XnDMCdtjnyjwA-J`, Account `ben@eom.de`):

1. **Helma.de | Schwellenkeyword-Recherche & N-OP-Empfehlung "Bauunternehmen Berlin"** — Google Doc, 2025-09-10
2. **Helma.de | Schwellenkeyword-Recherche & N-OP-Empfehlung "Bauunternehmen Chemnitz"** — Google Doc, 2025-09-03
3. **Helma Wohnungsbau | Schwellenkeyword-Recherche & N-OP-Empfehlung "Sachsen"** — Google Doc, 2025-08-28
4. **Helma Wohnungsbau | Schwellenkeyword-Recherche & N-OP-Empfehlung "Sachsen-Anhalt"** — Google Doc, 2025-09-03
5. **Übergabe_Marketing_Anmerkung EOM** — Google Doc, 2025-04-11 (Mandat/Gewerke)
6. **Übergabe_Marketing.docx** — Word (nicht exportierbar, nur per Name/Anmerkungsfassung gewertet), 2025-04-11

Verwandt: [[Über EOM]], [[SEO-Methodik]], [[Schreibstil]]
