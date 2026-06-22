---
tags: [kunde, seo]
kunde: "Schwäbische Zeitung"
stand-Datum: 2026-06-19
---

# Schwäbische Zeitung

> [!info] Kurzcharakter
> Kein klassisches Audit-Mandat, sondern ein **Content-Produktions-Mandat**: EOM schreibt SEO-Ratgeberartikel für den Bereich **Bauen & Wohnen** des Publishers Schwäbisch Media (schwaebische.de). Die Artikel werden im Namen lokaler Werbekunden der Schwäbischen (Handwerker, Bauunternehmen, Kommunen) erstellt und auf `schwaebische.de/ratgeber/bauen-und-wohnen/` veröffentlicht.

## Überblick

- **Wer:** Schwäbisch Media / Schwäbische Zeitung — Regionalverlag im südlichen Baden-Württemberg (Schwerpunkt Ravensburg / Oberschwaben). Tritt EOM gegenüber als **Auftraggeber & Vermittler** auf; die eigentlichen fachlichen Ansprechpartner sind die Werbekunden des Verlags.
- **Branche:** Publisher / Medienhaus mit Content-Marketing-Vermarktung an regionale KMU.
- **Domain:** `schwaebische.de`, redaktioneller Content-Hub `schwaebische.de/ratgeber/bauen-und-wohnen/` mit thematischen Unterverzeichnissen (`/hausbau/`, `/garten-und-balkon/`, `/kueche-und-bad/`, `/renovieren-und-sanieren/`, `/mobilitaet/`, `/wohnen-und-schlafen/`).
- **Hauptansprechpartner (Verlag):** Tobias Baunach (tobias.baunach@regio-tv.de) — koordiniert Kunden, Interviewtermine und Freigaben.
- Quelle: [[#Quellen|„2025 Projektinfos Schwäbische"]] (Stand zuletzt 31.07.2025) und Ordnerstruktur im Drive-Kundenordner.

## Mandat & Gewerke

- **Kernleistung:** Texterstellung von SEO-optimierten Ratgeberartikeln für „Bauen & Wohnen".
- **Volumen / Kommerzielles:** Paket über **150 Texte für 109.331,26 €**; Zeitrahmen 750–950 h; Toggl-Projekt „schwaebische.de – Texterstellung 150 Texte" ab März 2024. Quelle: „2025 Projektinfos Schwäbische".
- **Gewerke-Schwerpunkt:** **On-Page & Content** (Keyword-Recherche → Briefing → Experteninterview → Text → Title/Meta/Teaser). Klassisches technisches SEO, Off-Page/Backlinks oder ein laufendes Monatsreporting sind **nicht** Teil des Mandats (keine entsprechenden Deliverables im Ordner gefunden).
- **Folge-/Zusatzpakete:** „03_Nachoptimierungen" (Überarbeitung bestehender Bauco-Artikel, Anfang 2024), aktuelles **„Paket 20 Texte"** (zuletzt geändert 15.12.2025) — d. h. das Mandat läuft fort bzw. wurde verlängert.
- **Prozess (laut Projektinfos):** Tobias meldet neuen (Werbe-)Kunden → KWR/Kickoff → Themen-Freigabe durch Kunden → Briefing inkl. Interviewfragen → Interview (von Tobias aufgezeichnet, via JIRA bereitgestellt) → Texterstellung (Autor: Lukas Becker) → QS durch PM → Freigabe-Schleife mit Kunde → Ablage in SharePoint + JIRA-Verlinkung.
- **Tool-Kette des Mandats:** JIRA (Textabstimmung), SharePoint (Ablage), Monday (internes Board), Toggl (Zeit), Sistrix (Meta-Längenprüfung), zuletzt NotebookLM + ChatGPT (Strukturierung, siehe Schreibstil-Notizen).

### Endkunden hinter dem Mandat (Werbekunden der Schwäbischen)
Aus dem Unterordner `00_Kunden_Schwäbische` (je eigener Ordner): **Bauco** (mit Abstand größter Auftraggeber, Immobilien/Bau), Warema, Schellinger, Rhomberg, Fachmann Bommer, Thermostone, Wiehl Treppen, **Stadt Ravensburg**, Solmotion, Kreissparkasse Ravensburg, Reuter der Maler, Pfaff Garagen, Haller Infrarot, Plana Küchen RV, Karl Traub, Garten Müller, Baur Immobilien, Sto, GaLaBau, Beckmann.
- Die frühen Texte (001–095) sind nahezu alle **Bauco**-Themen (Immobilienbewertung, Hausverkauf, Garten, Garagen, Sanierung). Quelle: Dateinamen in `02_Texterstellung`.

## SEO-Status & Befunde

> [!warning] Wichtigster Befund — flächendeckende Ranking-Verluste 2024 → 2025
> **Befund:** Im Report „Ranking Verluste Top-10 KWs – 2024" (Spreadsheet, zuletzt geändert 16.04.2025; Vergleich Sistrix-Positionen **08.01.2024 vs. 06.01.2025**) sind **rund 352 Keywords** gelistet, die binnen eines Jahres aus den Top-10 nach unten gerutscht sind. **13 Keywords** sind ganz aus dem messbaren Bereich gefallen (Spalte „>100" bzw. leer).
> **Begründung:** Betroffen ist breit der gesamte `ratgeber/bauen-und-wohnen`-Cluster — von Einzelartikeln (z. B. „checkliste für häuslebauer" Pos. 4 → 44; „alles über dämmstoffe" Pos. 4 → 24; „dieffenbachia raumklima" Pos. 7 → 30) bis zu Kategorieseiten (z. B. „bauen ratgeber" Pos. 6 → 16, „bau wohnen" Pos. 3 → 8). Das Muster (viele kleine bis große Abstürze gleichzeitig) deutet auf nachlassende Aktualität/Wettbewerb und ggf. Google-Core-Update-Effekte hin — eine eindeutige Ursache lässt sich aus dem Sheet allein **nicht** belegen.
> **Maßnahme (aus dem Mandat ableitbar, nicht erfunden):** Genau dieses Sheet diente als Grundlage für **Nachoptimierungen** (zweite Datei „Ranking Verluste Top10 KWs – geordnet nach URLs" gruppiert die Verluste je URL → priorisierte Content-Updates). Konkrete umgesetzte Maßnahmen sind im Vault-Material nicht dokumentiert.
> Quelle: „Ranking Verluste Top-10 KWs – 2024" & „… geordnet nach URLs" (Ordner `06_Reporting & Analyse`, Stand 04/2025).

- **Content-Lücken-Logik in der KWR:** Im aktuellen KWR-Sheet wird je Keyword geprüft „Inhalte auf BuW zum KW?" — durchgängig **„nein"** bzw. nur tangentiale Treffer. Befund: Es werden gezielt Themen gewählt, zu denen schwaebische.de **noch nicht** rankt (Lückenfüllung statt Kannibalisierung). Quelle: „Schwäbische | Paket 20 Texte – Übersicht & KWR" (Stand 15.12.2025).
- **Suchvolumen-Bandbreite (aktuelles Paket):** Die 20 geplanten Texte mischen bewusst hohe und niedrige Volumina, z. B. „badezimmer deko" (SV 6.600), „feng shui schlafzimmer" (Haupt-KW-Cluster bis 4.200), bis hin zu Nischen wie „fahrrad überwintern" (30) oder „e-auto laden im winter" (30). Das entspricht exakt der dokumentierten Methodik (Gleichgewicht aus hohem/niedrigem SV). Quelle: KWR-Sheet + „SEO Grundlagen Paper".
- **Regionalitäts-Hebel:** In der KWR explizit vermerkt, dass Regionalität (Baden-Württemberg) als Differenzierung eingebaut wird (z. B. „e bike unterwegs laden" → eigener BW-Absatz, „wäre mit regionaler Karte besonders wertvoll"). Befund: lokaler Bezug wird als Ranking-Vorteil des Regionalverlags genutzt.

> [!note] Datenherkunft
> Alle Positions- und SV-Werte oben stammen aus den von EOM erstellten Sheets (Basis Sistrix). Es wurden für diese Notiz **keine** eigenen Live-Rankings, Suchvolumina oder Backlink-Daten erhoben oder geschätzt.

## GEO / KI-Sichtbarkeit

- **Keine GEO-/KI-Sichtbarkeits-Daten gefunden** (kein Peec-AI-/Brand-Radar-Report, keine AI-Overview-/LLM-Citation-Auswertung, keine `llms.txt`-Prüfung im Kundenordner).
- **GEO-relevante Signale in der Produktionsmethode** (indirekt, kein Tracking): Die aktuelle „Anleitung: Schwäbische Texte" (Stand 26.11.2025) schreibt vor, **NotebookLM** zur Strukturableitung aus den Top-Google-Ergebnissen und **ChatGPT** (Projekt „Schwäbische 20 Texte") zur Texterstellung zu nutzen, sowie verpflichtend einen **„Das Wichtigste in Kürze"-Block direkt nach der Einleitung** einzubauen. Dieser Answer-First-/Zusammenfassungs-Block ist ein klassisches GEO/AEO-Muster (zitierfähige Kurzantwort) — er wird hier aber als Schreibkonvention genutzt, **nicht** als gemessene KI-Sichtbarkeit.
- **Offen / Chance:** Für ein Publisher-Mandat dieser Größe wäre eine GEO-Auswertung (Werden die `/ratgeber/`-Artikel in AI Overviews / ChatGPT / Perplexity zitiert?) naheliegend, ist aber bisher nicht Teil des Scopes.

## Doc-Typen & Aufbau

Im Kundenordner wiederkehrende Deliverable-Typen:

1. **KWR-Sheets** (`04_KWR`, `08_Paket 20 Texte`): Spalten Titel · Haupt-/Neben-Keywords (Haupt-KW blau) · SV · „Inhalte auf BuW?" · Anmerkungen · Doc-Link · „Rausgesendet?".
2. **Text-Docs** (`02_Texterstellung`): Benennung `EOM | Text <Nr> - <Endkunde-Nr> - <Thema>` (z. B. „EOM | Text 049 - Bauco-116 - Hauswert ermitteln …"). Marker `{ST}` und `V2` für Versionen.
3. **Nachoptimierungs-Docs** (`03_Nachoptimierungen`): `EOM | N-OP <Nr> - <Endkunde-Nr> - <Thema>` + begleitendes „Ausrichtung/Nachoptimierung"-Sheet.
4. **Reporting-Sheets** (`06_Reporting & Analyse`): Ranking-Verlust-Tabellen (nach KW und nach URL) + „Agency Tabellen Vorlage".
5. **Prozess-/Wissens-Docs** (`01_Orga`, `05_Infos zu Kunden`, `07_Weitere Themen`): Projektinfos, Kick-Off-Protokolle, „SEO Grundlagen Paper für Verkauf", „Anleitung: Schwäbische Texte".
6. **Briefings** (`02_Texterstellung/Briefings`) inkl. Interviewfragen, abgeleitet aus der Artikelgliederung.

> [!caution] Format-Hinweis
> Die neuesten Texte im „Paket 20 Texte" liegen als **.docx** vor (z. B. „Text Nr. 18 – Vliestapete tapezieren.docx") und sind per gws **nicht** als Text exportierbar — Inhalt hier nur über Dateinamen/KWR-Sheet erfasst, nicht im Volltext gelesen.

## Schreibstil-Notizen

- **Sie-Anrede**, Ratgeber-/Service-Ton („So gelingt …", „Darauf sollten Sie achten", „X Tipps für …").
- **Pflicht-Struktur:** Einleitung → **„Das Wichtigste in Kürze"** → keyword-tragende H-Überschriften (Haupt- & Nebenkeywords möglichst in den Headings). Quelle: „Anleitung: Schwäbische Texte".
- **E-E-A-T über Experteninterviews:** Fachlichkeit und „einzigartige Stimme" des jeweiligen Endkunden fließen per Interview ein — bewusst als Ranking-/Vertrauensfaktor positioniert. Quelle: „SEO Grundlagen Paper".
- **Title/Meta/Teaser:** Meta-Beschreibungen werden mit Keywords formuliert und im **Sistrix-Tool auf Pixel-/Zeichenlänge** geprüft; zusätzlich kurzer **Teaser-Text (1–2 Sätze)**. Quelle: „Anleitung: Schwäbische Texte".
- **Längen-/Dichte-Kontrolle:** Zielwortzahl wird mit „Wörter zählen" geprüft, danach Keyword-Dichte. Keyword-Abdeckung wird im KWR-Sheet je Text dokumentiert; Lesbarkeit hat Vorrang vor erzwungener Vollabdeckung (mehrfach in den Anmerkungen vermerkt).
- **KI** statt „AI" (Vault-Konvention).

## Offene Punkte / Datenlücken

- **Keine GEO-/KI-Sichtbarkeitsmessung** vorhanden (s. o.).
- **Keine technischen SEO-Checks** im Ordner (Crawl, Broken Links, Redirects, hreflang, Core Web Vitals) — Mandat ist reiner Content.
- **Kein laufendes Monatsreporting** (Klicks/Impressionen/CTR aus GSC, SI-Verlauf) — nur die einmalige Ranking-Verlust-Analyse 04/2025.
- **Ursache der Ranking-Verluste 2024→2025 unbelegt** (Core Update? Aktualität? Wettbewerb?) — bräuchte Sistrix-Sichtbarkeitsverlauf + GSC zur Verifikation.
- **Neueste Texte (.docx) nicht im Volltext geprüft** — nur Titel/Keywords.
- **Mandatsstatus aktuell unklar:** Projektinfos enden Juli 2025 (~20 Texte offen, Klärungstermin 24.07.2025 mit Elisa, 10 Texte für Sto gestrichen); parallel existiert ein „Paket 20 Texte" bis Dez. 2025. Wie beide zueinander stehen (Restabwicklung vs. Anschlussauftrag), ist nicht dokumentiert.

## Quellen

Ausgewertete Dateien (Google Drive, Account ben@eom.de):

- **2025 Projektinfos Schwäbische** (Doc, `01_Orga`, Stand 31.07.2025) — Mandat, Volumen, Prozess, Endkunden-Status. *(Volltext gelesen)*
- **Anleitung: Schwäbische Texte** (Doc, `02_Texterstellung`, Stand 26.11.2025) — aktuelle Produktionsmethode (NotebookLM/ChatGPT, Struktur, Meta-Prüfung). *(Volltext gelesen)*
- **2025-03-11 Recherche & Ideen – SEO Grundlagen Paper für Verkauf** (Doc, `07_Weitere Themen`) — Methodik & Schreibstil-Logik. *(Volltext gelesen)*
- **Ranking Verluste Top-10 KWs – 2024** (Sheet, `06_Reporting & Analyse`, Stand 16.04.2025) — ~352 KW-Verluste, Sistrix 01/2024 vs. 01/2025. *(CSV ausgewertet)*
- **Ranking Verluste Top10 KWs – geordnet nach URLs** (Sheet, `06_Reporting & Analyse`, Stand 15.04.2025) — dieselben Verluste je URL gruppiert (Nachoptimierungs-Priorisierung). *(per Name/Kontext gewertet)*
- **Schwäbische | Paket 20 Texte – Übersicht & KWR** (Sheet, `08_Paket 20 Texte`, Stand 15.12.2025) — 20 aktuelle Themen, Haupt-/Neben-KWs, SV, Content-Gap-Check. *(CSV ausgewertet)*

Ergänzend strukturell gesichtet (nicht im Volltext): Ordnerlisten `00_Kunden_Schwäbische`, `02_Texterstellung` (~95 Bauco-Texte), `03_Nachoptimierungen`, `04_KWR`, `05_Infos zu Kunden`.

---
*Hinweis: Diese Notiz ist die lokale Wissensfassung. Es wurden keine Quelldateien in Drive verändert.*
