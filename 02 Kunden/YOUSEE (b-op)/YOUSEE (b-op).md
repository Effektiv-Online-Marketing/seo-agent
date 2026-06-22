---
tags: [kunde, seo]
kunde: "YOUSEE (b-op)"
stand-Datum: 2026-06-19
---

# YOUSEE (b-op)

## Überblick

**Wer:** YOUSEE ist ein Anbieter von Augenlaser- und Linsenchirurgie (Augenkliniken) in der DACH-Region. Gegründet 2018, Mutterklinik ist iroc. Prof./Dr. Theo Seiler gilt als "Erfinder des ersten Augenlaserverfahrens" — zentraler USP und Trust-Anker.
**Branche:** Healthcare / Augenchirurgie (Augenlasern, Linsenimplantat/ICL). Lokales/regionales Geschäft mit Lifestyle- und Medizin-Charakter. Hauptziel der Website: **Terminbuchung** (Erst-/Kurzuntersuchung).
**Standorte:** Schweiz (Zürich, Basel, Bern) plus neuer Standort **Düsseldorf** (erster DE-Standort, Eröffnung Januar, bei Stand der Übergabe noch nicht offiziell eröffnet, nur angeteasert). Perspektivisch weitere DE-Standorte, ggf. Österreich — Fokus bleibt DACH (Sprachbarriere/Regulierung sonst).
**Agentur-Konstellation:** EOM ist die SEO-Agentur. Direkter Kunde/Marketing ist die Agentur **b-op** (daher der Klammerzusatz). b-op übernimmt Corporate Design, Online-Marketing und Texterstellung und versteht sich als "Anwalt" von YOUSEE. Die **Technik sitzt in Serbien** (Strahinja, Nemanja; englischsprachig, Kommunikation läuft über Marcel/b-op).

### Domain-Situation (zentral für das Verständnis)
Historisch existieren mehrere Standort-Domains:
- [[youseezueri.ch]] (Zürich) — performt von den Bestandsdomains am besten
- [[youseebasel.ch]] (Basel)
- [[youseebaern.ch]] (Bern)
- **[[yousee.clinic]]** — soll die **künftige Hauptdomain** für alle Standorte (CH + DE) werden; bislang nur wenige Seiten und kaum organische Sichtbarkeit.

## Mandat & Gewerke

- **Kern-Mandat:** SEO-Begleitung eines **Relaunchs** auf die konsolidierte Domain `yousee.clinic` (Sprachverzeichnisse `/de/`, `/ch/`, darunter Leistungs- und Standortseiten). Conversion/Ziel laut Übergabe explizit: "Relaunch".
- **Gewerke EOM:** technisches SEO (Crawling/Indexierung, Weiterleitungen, hreflang, Canonicals, Sitemap/robots.txt), Website-/URL-Struktur-Konzept, Keyword-Recherche, SEO-Basics (Title/Meta/H1), Content-Empfehlungen & QS, lokale SEO (LocalBusiness/MedicalBusiness), Tracking-Konzept (GA4) sowie **SEO-Schulung der serbischen Technik** (Seminar Juli 2025 inkl. Quizze).
- **Arbeitsteilung:** YOUSEE/Technik baut Seiten auf Basis der EOM-Empfehlungen; **EOM prüft die Umsetzung** (Metas, H1, Canonicals etc.). EOM hat **keinen Zugang zum Alt-Backend**; neues Backend wird **Strapi**.
- **Tooling:** Google Search Console (alle Domain-Properties), Google Analytics, Sistrix + Sistrix Optimizer, Monday (Kommunikation & PM). Kein Looker Studio. Ansprache: Duzen.
- **Ansprechpartner Kunde:** Dunja Ben Hadj Hassen (Managing Partner & Head of Marketing, b-op), Marcel Dykiert (Team Marketing, b-op — Haupt-Kontakt), Benni (YOUSEE-Marketing, selten). PM bei EOM: Roxi; SEO: Anne.

## SEO-Status & Befunde

> Hinweis: Keine eigenen Live-Rankings/Backlinks/SV in dieser Datei geschätzt. Zahlen unten stammen direkt aus den ausgewerteten EOM-Dokumenten.

**Sichtbarkeit (Quelle: SEO-Konzept EOM, Sistrix, Stand Doc 11/2024):**
- `yousee.clinic` hat **nahezu keine Sichtbarkeit** (SI CH 0,0001) — wenige Seiten, daher erwartbar. Befund: schwacher Startpunkt für die geplante Hauptdomain.
- Keyword-Bestand CH (Sistrix, Stand Doc): Top-10 / Top-100 — youseezueri.ch 22/205, youseebasel.ch 25/227, youseebaern.ch 487/176 (Wert für baern.ch im Doc auffällig, ggf. Tippfehler in Vorlage), yousee.clinic 6/32.
- Wettbewerber CH mit höchster Sichtbarkeit: **clearvision-laser.ch (1,03)** und **betterview.ch (0,96)**, dahinter focuslaser.ch (0,44); YOUSEE-Domains klar darunter.
- **Begründung:** Bestandsdomains tragen die Sichtbarkeit; die Zieldomain muss diese beim Umzug per sauberen 301-Weiterleitungen erben, sonst drohen Verluste.

**Technische Befunde (Quelle: SEO-Konzept EOM 11/2024 + SEO Audit Relaunch, Sheet zuletzt 11/2025):**
- **robots.txt schließt aktuell alle Crawler aus** — kritisch; muss zum Go-Live geöffnet werden (mit Sitemap-Referenzen je Sprache). → Maßnahme: produktive robots.txt mit `sitemap_de/en/ch.xml`.
- **XML-Sitemap:** alte `yousee.clinic`-Sitemap war eine 404; vorhandene Sitemap nicht dynamisch. → Maßnahme: dynamische Sitemap je Sprache, in GSC + robots.txt hinterlegen, nur indexierbare 200-URLs.
- **H1 / Überschriften werden per JavaScript geladen** → erschwert Erfassung bei verzögertem Rendering; teils fehlende H1. → Maßnahme: H1 unique je Seite, idealerweise im HTML.
- **Canonicals:** fehlerhafter Canonical gefunden mit verdoppelter URL (`…b-op.com/de/yousee-clinics.website.int.b-op.com/videos`); Beispiel youseezueri.ch `/augenklinik-zurich` zeigt per Canonical auf eine 404 (`/contact`) → nicht indexierbar. → Maßnahme: Selbst-Canonical je Seite/Sprachversion, Duplicate-Content (Parameter-URLs) automatisiert kanonisieren.
- **hreflang:** noch nicht vollständig gesetzt; Selbstreferenz + wechselseitige Verweise je Sprachversion (z. B. `de-CH`, `en-US`) erforderlich; Canonical darf hreflang nicht übersteuern. (Eigene Prüf-Sheets vorhanden: "hreflang check", "hreflang Check pro Seite", 03/2025.)
- **Weiterleitungen:** Weiterleitungskonzept CH→`yousee.clinic` mit Vermeidung von Ketten (Beispiel: alte 301 von `/augenlasern` auf neues Ziel `/augenlasern/methoden` umhängen). Eigene Sheets: "Weiterleitungsketten beheben" (02/2025), "Weiterleitungsziele 404-Seiten" (V1/V2). HTTP-Status-Exporte (httpstatus.io, 02/2025) im Technik-Ordner.
- **Canonical-Spezialfall Zürich (07/2025):** GSC meldet "Google verwendet andere URL als im Canonical angegeben" — eigenes Prüf-Sheet vorhanden.
- **Fehlerseiten:** 404 auf youseezueri.ch wegen weißer Schrift unlesbar; auf basel/baern/clinic gar keine 404-Seite eingerichtet. → Maßnahme: hilfreiche 404 aufbauen.
- **Meta Descriptions:** fehlen/unoptimiert; Empfehlung: CTR-orientierte Titles/Descriptions mit korrekter Länge, Sonderzeichen, CTA.
- **Internal Linking:** ausformulierte Seiten haben i. d. R. ausreichend In-/Outlinks; Empfehlung: interne Links im semantischen Cluster setzen.

**Struktur-/Content-Befunde:**
- Empfohlene URL-Struktur (freigegeben b-op, Dez. 2024): `/augenlasern` (+ `/ablauf`, `/preise-deutschland`, `/preise-schweiz`, `/methoden/{lasik,trans-prk,femto-lasik,smile-klex,prk,monovision}`, `/ablauf/{voruntersuchung,nach-der-op}`), `/linsenimplantation` (+Preise), `/ueber-uns/warum-yousee`, `/standorte` mit `/ch` (Basel/Bern/Zürich) und `/de/duesseldorf`.
- Domain-Entscheidung: **`yousee.clinic`** als Hauptdomain (branchenrelevante TLD `.clinic`, von Google wie generische TLD behandelt, keine Länderbindung, etablierte Marke). `yousee.com` ist vergeben/zu teuer.
- Standortseiten: zunächst **eine URL pro Stadt** (Team/Räume per Sprunglinks gebündelt), Vorbild care-vision.de; Ausbau nach Relaunch mit ersten Daten.
- Content-Lücken mit Keyword-Potenzial (erste KWR aus Konzept, Quelle Sistrix/EOM): "Ablauf" (augen lasern ablauf SV 320), "Nach der OP" (augen lasern danach SV 210), Methoden (lasik SV 6600, femto-lasik 2900, prk 1900, klex 880, monovision 480, icl implantation 170), Voruntersuchung (SV 40/30/20). Detail-KWR-Sheets vorhanden: LASIK, Femto-LASIK, Standort Düsseldorf, Startseite DE.
- **Rechtlicher Hinweis Content:** "SMILE" darf aus rechtlichen Gründen nicht verwendet werden → bei YOUSEE "KLEx/KLEKs".

**Projektstatus (Übergabe 09/2025):** Relaunch eingeleitet, aber **noch nicht umgesetzt**. Düsseldorf noch nicht offiziell eröffnet (nur angeteasert, Kurzuntersuchungen buchbar). Anfangs zogen Technik-Seiten ohne Weiterleitungen um — wiederholtes Hin und Her; trotz Schulung muss die Technik eng beaufsichtigt werden. Offene Doings: Prüfung umgesetzter Seiten (Metas/H1/Canonicals), Weiterleitungskonzept, Sitemap, robots.txt, Indexierbarkeit. **Prio: Relaunch.**

## GEO / KI-Sichtbarkeit

**Keine GEO-Daten gefunden.** In den ausgewerteten Dokumenten (SEO-Konzept, Relaunch-Audit, Termin-Notizen, Projektübergabe, Tracking-Konzept) gibt es **keine Inhalte zu AI Overviews, ChatGPT/Perplexity-Sichtbarkeit, LLM-Optimierung, AEO/GEO oder llms.txt**. Das Mandat ist bislang klassisch ausgerichtet (technisches SEO + Relaunch + lokale SEO). Der einzige KI-nahe Bezug ist eine allgemeine **SEO-Technik-Schulung** für das Entwicklerteam (Juli 2025), nicht GEO/AI-Visibility für YOUSEE. → Offener Ansatzpunkt: Im Healthcare-/Augenlaser-Umfeld (stark informationsgetriebene, beratungsintensive Suchanfragen) ist AI-Sichtbarkeit perspektivisch relevant; aktuell jedoch keine Datengrundlage im Vault.

## Doc-Typen & Aufbau

Der Drive-Ordner ist nach Projektphasen organisiert:
- **01 SEO Konzept:** Agenda, Termin-Notizen (b-op), **SEO Audit Relaunch** (Sheet, 11/2025), SEO-Konzept als Präsentation (ALT + EOM-Version).
- **02 Relaunchbegleitung yousee.clinic:** Unterordner **Content**, **KWR** (Keyword-Recherche-Sheets je Thema/Standort + Sistrix-CSV-Exporte), **Technik** (hreflang-Checks, Weiterleitungs-/404-Sheets, httpstatus.io-Exporte, Canonical-Sheet Zürich), **Website-Struktur**; plus freigegebenes **URL-Struktur-Sheet** (Dez. 2024).
- **SEO Technik Schulung:** Seminar-Präsentationen (DE) + 5 Quizze (Slides + Google Forms) + Schulungs-Doc.
- **Einzeldateien:** Angebot (PDF 10/2024), **Tracking-Konzept & GA4-Setup** (Doc, zuletzt 12/2025), zwei **Projektübergabe-SEO**-Sheets (zuletzt 09/2025 bzw. 10/2025).

Muster: Konzepte als Google Slides, operative SEO-Arbeit als Google Sheets (eine Datei je Teilaufgabe — viele kleine, fokussierte Sheets), Steuerung/Tasks in Monday.

## Schreibstil-Notizen

- **Sprache:** Deutsch, **Duzen** (Kundenwunsch). Title-/Description-Beispiele aus dem Konzept verwenden "du/dir".
- **Tonalität YOUSEE:** Qualität & Aufklärung statt Preis-Druck. Patienten sollen über **Leistung/Qualität** überzeugt werden, nicht über Rabatte; ethischer Anspruch (Patienten werden auch abgelehnt). Angst nehmen durch **aufklärenden Content + Trust-Signale**.
- **Trust-/E-E-A-T-Hebel:** Theo Seiler als Erfinder des Augenlaserns, Experten-/Autorenaufbau mit Ärzten, Kooperationen mit Unikliniken, geplante TÜV-/ISO-Zertifizierung (mit Düsseldorf), Verbandsmitgliedschaften — content-fähig.
- **Begriffs-Guardrail:** "SMILE" vermeiden → "KLEx/KLEKs".
- **CTA-Logik:** alles auf **Terminbuchung** (Kurz-/Voruntersuchung) ausgerichtet; je Standort eigenes Buchungstool (eigener Server), künftig ein zentrales Tool → Zwischenseite für nicht-standortspezifische Verlinkung nötig.

## Offene Punkte / Datenlücken

- **Office-/Slides-Inhalte teilweise nicht maschinell ausgewertet:** Präsentationsinhalte wurden über den Text-Export gelesen (Sprechertext-Reihenfolge teils unsauber); das PDF-Angebot und die Tracking-/GA4-Doc-Details wurden nicht vollständig erfasst.
- **Keine Live-Daten im Vault:** aktuelle Rankings/Sichtbarkeit/Backlinks/Indexierungsstand nach Relaunch unbekannt — Sistrix/GSC nicht hier abgefragt (bewusst nicht geschätzt).
- **Relaunch-Stand unklar:** Übergabe 09/2025 sagt "noch nicht umgesetzt"; ob `yousee.clinic` inzwischen live konsolidiert ist, ist aus den Dokumenten nicht belegt.
- **GEO/AI-Visibility:** keinerlei Grundlage vorhanden (siehe oben).
- **Auffällige Zahl** im Konzept (youseebaern.ch Top-10 = 487) wirkt wie ein Vorlagen-/Tippfehler — nicht verifiziert.
- Zweites Projektübergabe-Sheet (Version ohne Datum, 10/2025-Stand) nicht separat ausgewertet (inhaltlich Dublette zur 09/2025-Version angenommen).

## Quellen

Ausgewertete Drive-Dateien (Ordner-ID 1t859JKKun3eKC0gByXz6uZ0G7ihydujF):
- YOUSEE – SEO-Konzept – EOM (Slides, 11/2024)
- YOUSEE – SEO Audit Relaunch (Sheet, zuletzt 11/2025)
- YOUSEE – Projektübergabe SEO 09/2025 (Sheet)
- YOUSEE – Notizen aus Termin (Benny + b-op) – Jelena (Doc, 11/2024)
- yousee.clinic – URL-Struktur zum Relaunch – Freigabe b-op (Sheet, 12/2024)
- Ordnerlistings: 01 SEO Konzept, 02 Relaunchbegleitung (Content/KWR/Technik/Website-Struktur), SEO Technik Schulung
- Nur per Dateiname gewertet (nicht im Detail exportiert): Tracking-Konzept & GA4-Setup (Doc), Angebot-PDF (10/2024), KWR-Sheets (LASIK/Femto-LASIK/Düsseldorf/Startseite DE), Technik-Sheets (hreflang, Weiterleitungen, 404, Canonical Zürich), httpstatus.io-Exporte, Schulungs-Quizze.
