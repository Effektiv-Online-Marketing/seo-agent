---
tags: [kunde, seo]
kunde: "Juppen"
stand-Datum: 2026-06-19
---

# Juppen

> Wissensbasis aus dem Google-Drive-Kundenordner (Account `ben@eom.de`), erstellt am 2026-06-19. Logik durchgehend: **Befund → Begründung → Maßnahme**. Es wurde nichts geschätzt; nicht zugängliche Daten sind offen als Datenlücke markiert.

## Überblick

- **Wer:** Schuhhaus Juppen — stationärer Schuh-Einzelhändler mit Online-Shop. Filialen in **Düsseldorf und Ratingen** (Quelle: Briefing Startseitentext, Feb 2021).
- **Branche:** E-Commerce / Schuhe (Marken-Multibrand-Shop für Damen-, Herren- und Kinderschuhe).
- **Domain:** `https://www.juppen.de` (Quelle: Briefing Startseitentext; OnPage-Empfehlungen 2022).
- **Markenkern im Sortiment u. a.:** Gabor, Paul Green, Timberland, Joop, On (Running), El Naturalista, Maripé, INUIKII/IKKII, NIS (New Italia Shoes), Galizio Torresi, Birkenstock, Converse, Nike, Vans, Haflinger u. v. m. (Quelle: OnPage-Empfehlungen 2022-01-31; 404-Listen 2021).
- **Verbund / Mehrmarken-Konstellation:** Juppen gehört offenbar zu einer Händlergruppe zusammen mit **GISY** und **Prange**. Die EOM-Empfehlung zu „On" hält ausdrücklich fest, dass Keyword- und Optimierungs-Überschneidungen zwischen GISY, Prange und Juppen unkritisch sind, solange sich die **Fließtexte je Shop unterscheiden** (Quelle: „Empfehlung Marke On", 2021-03-11). Im EOM-Vault existiert ein eigener Kundenordner [[GISY-Schuhe.de]].
  - *Begründung:* Erklärt, warum On-Page-Empfehlungen teils auf Basecamp-Projekt „gisy-schuhe-de" verlinken (siehe OnPage-Sheet 2022).

## Mandat & Gewerke

EOM betreute Juppen als laufendes SEO-Mandat mit Monatsreporting. Belegte Gewerke (aus Drive-Ordnerstruktur `5.0 SEO`, `8.0 Content`, `3.0 Reportings`, `10.0 Crawls`):

- **Technisches SEO** (Schwerpunkt 2020–2022): Crawl-Analysen (Screaming Frog), 404-/Soft-404-Bereinigung, Status-Codes der Sitemap, Canonical-Tags, doppelte h1/Titles, Indexbereinigung, interne Verlinkung, Pagespeed.
- **On-Page & Content:** Title-/Meta-/h1-Optimierung sowie Content- und Verlinkungs-Empfehlungen für Marken- und Kategorieseiten; Startseitentext-Briefing.
- **Reporting:** Monatliche Reports als Looker-/Data-Studio-PDF (Januar 2021 bis Dezember 2022 lückenlos im Drive).
- **SEA & Social Media:** eigene Drive-Ordner (`6.0 SEA`, `7.0 Social Media`) vorhanden — **nicht ausgewertet** (außerhalb des SEO/GEO-Scopes dieser Erfassung).
- **Relaunch:** eigener Ordner `9.0 Relaunch` + Hinweis im Milestones-Doc auf Conversion-Tracking-Setup für einen Relaunch (Datenlücke, siehe unten).

*Aktualitäts-Hinweis:* Der jüngste belegbare Arbeitsstand ist ein **Screaming-Frog-Crawl vom 25.02.2025** (`10.0 Crawls`, `.seospider`-Datei, binär, nicht exportierbar). Alle inhaltlich lesbaren Deliverables stammen aus **2020–2022**. Ob das Mandat 2025 noch aktiv ist, lässt sich aus den Dateien nicht zweifelsfrei ableiten (siehe Datenlücken).

## SEO-Status & Befunde (mit Quelle + Datum)

### Technische Befunde (durchgängiges Thema: Crawling-/Index-Hygiene)

- **Befund:** Wiederkehrende **404-Fehler** in großem Umfang, auch über die XML-Sitemap ausgespielt. Belegt durch eine Serie von Deliverables: „404 in Sitemap" (2021-08-11), „Status Codes Sitemap URLs" (2021-04 bis 2021-06), „Rankingverluste aufgrund von 404-Fehlern" (2021-07-14), „404 Fehler – Juni 2022" sowie Search-Console-Exporte `juppen-404-sc-25052022` und `juppen-soft-404-sc-25052022`.
  - *Begründung:* 404-URLs in der Sitemap und auf indexierten Produkt-/Kategorie-URLs verschwenden Crawl-Budget und führten laut Deliverable-Titel zu **konkreten Rankingverlusten**. Betroffen waren u. a. zahlreiche Produkt-Detailseiten (z. B. Gabor-, Birkenstock-, Vans-, Nike-, Converse-Artikel) sowie ganze Marken-/Kategorie-URLs wie `/haflinger/damenschuhe`, `/havaianas`, `/romika`, `/verba` (Quelle: „Rankingverluste durch 404", 2021-07-14).
  - *Maßnahme:* Sitemap auf 200er-URLs bereinigen; ausgelaufene Produkt-URLs sauber per **301 auf passende Kategorie/Marke** weiterleiten statt 404; Soft-404 (z. B. „Da ist etwas schief gelaufen"-Seiten) eliminieren. Bei einem aktuellen Mandat den 2025er-Crawl gegen die alten 404-Muster prüfen (Wiederkehr typisch bei Produkt-Lebenszyklen im Schuh-E-Commerce).

- **Befund:** Fehlerseiten mit h1 **„Da ist etwas schief gelaufen"** (2021-01 / 2021-07) — Soft-404 / fehlerhafte Templates.
  - *Begründung:* Solche Seiten liefern teils 200-Status mit Fehler-Content → Index-Verschmutzung.
  - *Maßnahme:* Korrekten 404/410-Status sicherstellen, aus Index entfernen.

- **Befund:** **Mehrfache / fehlende Canonical-Tags**, u. a. „Parameter-URLs ohne Canonical-Tag" (Feb 2021) und „Mehrfache Canonical-Tags" (2021-04-12).
  - *Begründung:* Parameter-URLs (Filter/Sortierung) ohne sauberen Canonical erzeugen Duplicate Content und Index-Aufblähung — im Schuh-Shop mit vielen Filterkombinationen kritisch.
  - *Maßnahme:* Eindeutigen, selbstreferenzierenden Canonical je Kanon-URL; Parameter-URLs auf die Kanon-Variante kanonisieren.

- **Befund:** **Doppelte h1-Überschriften** (Deliverable-Serie Jan 2021) und **doppelte Titles** (April 2021).
  - *Begründung:* Mehrere h1 pro Seite bzw. identische Titles über viele Seiten schwächen die thematische Eindeutigkeit. Hinweis aus dem Startseiten-Briefing: oberhalb des eigentlichen Textes wurden **Slider-Textpassagen fälschlich als h2** ausgezeichnet → gestörte Überschriften-Hierarchie.
  - *Maßnahme:* Genau eine h1 je Seite; nur den eigentlichen Content mit h-Tags strukturieren (nicht Slider/Layout-Elemente); Titles unikalisieren.

- **Befund:** Bedarf an **Indexbereinigung** (Deliverable 2021-02-22) und Optimierung der **internen Verlinkung** (Doc 2021-01-27).
  - *Begründung:* Zu viele dünne/duplizierte URLs im Index; Linkpower wird nicht gezielt auf Prio-Seiten verteilt.
  - *Maßnahme:* Noindex/Konsolidierung dünner URLs; interne Links aus Startseite/Content gezielt auf Prio-Kategorien & Top-Marken (siehe On-Page).

- **Befund:** **Pagespeed-Optimierungsbedarf** (Doc „Pagespeed-Optimierung Juppen", 20.11.2020).
  - *Maßnahme:* (Inhalt des Docs nicht im Detail ausgewertet) — bei aktuellem Mandat Core Web Vitals / INP neu erheben, da der Befund > 5 Jahre alt ist.

- **Befund:** **Defekte Backlinks** dokumentiert (Sheet „Juppen – Defekte Backlinks", 2021-06-11).
  - *Begründung:* Verweisende Domains zeigen auf nicht mehr existente URLs → verlorene Linkkraft.
  - *Maßnahme:* Defekte Ziel-URLs per 301 auf passende Live-Seiten retten.

### On-Page / Content-Befunde

- **Befund:** Title/Meta/h1 vieler **Marken- und Kategorieseiten** waren schematisch („… Markenschuhe online entdecken im Juppen Shop") und teils ungenau (z. B. h1 „Konstantin Starke Herrenschuhe" auf der **On-Herrenschuhe**-Seite — Template-/Pflegefehler). Belegt im großen OnPage-Sheet (2022-01-31) und in der On-Empfehlung (2021).
  - *Begründung:* Generische, sich wiederholende Metas nutzen Suchvolumen schlecht aus und differenzieren Seiten nicht.
  - *Maßnahme (EOM-Konvention, siehe unten):* Title nach Muster **„[Marke] Schuhe: jetzt bequem online kaufen bei Juppen"**, Meta-Description mit USP-Trust-Signalen (Kauf auf Rechnung, Versand mit DHL, kostenlose Rücksendungen) + CTA.

- **Befund:** Viele Marken-/Kategorieseiten hatten **keinen oder zu dünnen Fließtext** (z. B. INUIKII, NIS, El Naturalista Herren, Galizio Torresi, Maripé), während andere bereits gut ausgebaut waren (Gabor, Joop, Paul Green, Timberland) (Quelle: OnPage-Sheet 2022-01-31).
  - *Begründung:* Ohne keyword-relevanten Content fehlt Ranking-Substanz für teils hohe Suchvolumina (z. B. „gabor" SV 60.500, „paul green" SV 49.500, „timberland" SV 110.000 — Werte aus EOM-Sheet übernommen, nicht selbst erhoben).
  - *Maßnahme:* Markentexte mit Zwischenüberschriften (Keyword-haltig) aufbauen; Duplicate zwischen „Marke allgemein" und „Marke Damen/Herren" vermeiden; bei „On" Texte zwischen GISY/Prange/Juppen unterscheiden.

- **Befund:** **Startseite** — Überschriften-Hierarchie und interne Verlinkung optimierbar; Fokus-KWs „juppen schuhe", „schuhe düsseldorf"; erweiterte KWs „schuhe online kaufen/-shop" (Quelle: Briefing Startseitentext, Feb 2021).
  - *Maßnahme:* h1-Vorschlag „Markenschuhe online kaufen: Juppen Schuhe Düsseldorf"; Startseite verlinkt auf Damen-/Herren-/Kinderschuhe & Top-Marken (Linkpower-Verteilung); interne Links farblich erkennbar machen (waren nur fett).

### Performance / Reporting

- **Befund / Datenlücke:** Lückenlose Monatsreports **Jan 2021 – Dez 2022** liegen als PDF vor, sind aber **reine Looker-/Data-Studio-Bildexporte** — bei der Auswertung (Dez-2022-Report) ließ sich **kein maschinenlesbarer Text/KPIs** extrahieren.
  - *Begründung:* Keine belastbaren Klick-/Impressions-/Positions-/SI-Zahlen aus den Dateien ableitbar.
  - *Maßnahme:* Für aktuelle KPI-Aussagen GSC/Sistrix direkt anziehen (siehe Datenlücken); keine Zahlen aus den PDFs zitieren, ohne sie visuell zu prüfen.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im gesamten Kundenordner existieren keine Dokumente zu AI Overviews, ChatGPT/Perplexity-Zitaten, LLM-Sichtbarkeit, Brand-Mentions oder `llms.txt`. Das Mandat liegt zeitlich (2020–2022) vor der GEO-Welle. → Falls das Mandat aktiv ist: GEO-Baseline (z. B. Peec AI / Sistrix AI / Ahrefs Brand Radar) als Erst-Erhebung anlegen.

## Doc-Typen & Aufbau

Beobachtete, wiederkehrende Deliverable-Formate im Drive:

- **Technische Befund-Sheets** (Google Sheets): pro Issue ein Sheet mit URL-Liste + Status/Problem, oft mit Datum im Dateinamen (`Juppen - JJJJ-MM-TT - <Issue>`). Teils mit „Anmerkungen EOM" und „ARBEITSDATEI/ARBEITSTABELLE"-Varianten.
- **OnPage-Empfehlungs-Sheets** (Matrix): Spalten je URL/Marke; Zeilen = Zielkeywords (mit SV), Title-Tag IST/SOLL, Meta IST/SOLL, h1 IST/SOLL, Content-Empfehlung, interne-Verlinkungs-Empfehlung.
- **Content-/Marken-Empfehlungs-Docs** (Google Docs): persönliche Anrede („Hallo Andrea"), je URL ein Block mit Keywords+SV, Title/Meta/h1 IST→SOLL, mögliche H2 inkl. Beispiel-Anrissen, WDF*IDF-Begriffsliste, interne Verlinkung; Abschluss mit EOM-Signatur (Hannover/Stuttgart).
- **Briefing-Docs** (z. B. Startseitentext): Frage-Logik (Was/Wo/Warum), Keyword-Set, Überschriften-Vorschläge, WDF*IDF-Liste, Verlinkungs-Hinweise.
- **Reportings** (PDF, monatlich): Looker/Data-Studio-Export.
- **Crawls**: Screaming-Frog `.seospider` + CSV-Export.

## Schreibstil-Notizen

- **Anrede:** Sie-Form in Kunden-Copy; persönliche, kollegiale Du-Ansprache der Ansprechpartnerin in Empfehlungs-Docs („Hallo Andrea", „Wenn die Vorschläge so für dich passen…").
- **Title-Konvention (juppen-spezifisch, Stand 2022):** `[Marke/Produkt] Schuhe: jetzt bequem online kaufen bei Juppen` (Varianten: „für Damen/Herren", „hier/ganz bequem"). Ablösung der alten Floskel „… online entdecken im Juppen Shop".
- **Meta-Description-Konvention:** Trust-/USP-Stack mit Symbolen: `► Kauf auf Rechnung ✓ Schneller Versand mit DHL ✓ Kostenlose Rücksendungen ✓ Jetzt hier entdecken & shoppen!`. Auf Marken-Landingpages teils Emojis (👟) + ✓-Häkchen.
- **Content-Prinzip:** Marke-allgemein vs. Marke-Damen/Herren inhaltlich klar trennen (Duplicate vermeiden); Keyword-haltige Zwischenüberschriften; WDF*IDF-gestützte Begriffsabdeckung; interne Verlinkung immer mit dem Hauptkeyword der Zielseite.
- **Begrifflichkeit im Vault:** „KI" statt „AI".

## Offene Punkte / Datenlücken

- **Mandatsstatus 2023–2025 unklar:** Inhaltliche Deliverables enden 2022; einziger jüngerer Beleg ist ein Crawl vom **25.02.2025** (binär, nicht lesbar). Aktivität/Scope aktuell verifizieren.
- **Reportings nicht maschinenlesbar:** Monatsreports sind Bild-PDFs → keine KPI-Extraktion möglich. Für SI/Klicks/Impressionen GSC/Sistrix direkt nutzen.
- **Office-/Numbers-/.seospider-Dateien nicht exportierbar:** `.xlsx`, `.numbers`, `.seospider` (u. a. der 2025er-Crawl) wurden nur per Dateiname gewertet.
- **Keine Live-Tool-Daten erhoben:** Es wurden bewusst **keine** aktuellen Rankings/SV/Backlinks geschätzt. Suchvolumen-Angaben in dieser Notiz sind **Zitate aus den EOM-Sheets (2021/2022)**, nicht neu erhoben.
- **Keine GEO/KI-Baseline vorhanden** (siehe oben).
- **Relaunch/Tracking:** Milestones-Doc nennt „Ausfall des Trackings seit 01.10.20" und Conversion-Tracking-Aufgaben für einen Relaunch — Details/Abschluss unbekannt (Platzhalter „xx" im Doc).
- **Ansprechpartnerin:** In Empfehlungs-Docs als „Andrea" adressiert; vollständige Kontaktdaten nicht in den ausgewerteten Dateien.

## Quellen (ausgewertete Dateien)

Google Drive, Kundenordner Juppen (`1tJ2abQ3dc45asxepgS1zWFFwLnogSBAe`), Account `ben@eom.de`:

- `2.0 Meetings / Projekt-Milestones & Notizen Juppen` (Doc) — Tracking-Ausfall, Relaunch-Hinweise.
- `5.0 SEO / OnPage Optimierungen / Juppen – Briefing Startseitentext – Februar 2021` (Doc) — Startseiten-Struktur, Fokus-KWs, WDF*IDF.
- `8.0 Content / OnPage Optimierungen / 2022-01-31 Juppen | OnPage Empfehlungen` (Sheet) — Title/Meta/h1/Content-Matrix über ~22 Marken-/Kategorie-URLs (jüngstes lesbares On-Page-Deliverable).
- `5.0 SEO / OnPage Optimierungen / 2021-03-11 Juppen | Empfehlung Marke On` (Doc) — Marken-Content-Empfehlung; Beleg für GISY/Prange/Juppen-Verbund.
- `5.0 SEO / Juppen – 2021-07-14 – Rankingverluste aufgrund von 404-Fehlern` (Sheet) — 404-URL-Liste mit Ranking-Bezug.
- `3.0 Reportings / 2022 / Juppen_Reporting_Dezember 2022.pdf` — jüngster Monatsreport (Bild-PDF, nicht textextrahierbar).
- Ergänzend per Ordner-/Dateiname gewertet: Crawl `25.02.2025 …seospider` (`10.0 Crawls`), 404-/Soft-404-SC-Exporte (Mai/Juni 2022), Canonical-/h1-/Title-/Index-/interne-Verlinkungs-Deliverables (2021), Pagespeed-Doc (2020), „Defekte Backlinks" (2021).

Siehe auch: [[GISY-Schuhe.de]] (Schwester-Mandat im selben Händlerverbund).
