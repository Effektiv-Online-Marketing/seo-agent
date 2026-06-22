---
tags: [kunde, seo]
kunde: "HELMA"
stand-Datum: 2026-06-19
---

# HELMA

> [!info] Schnellkontext
> HELMA ist ein deutscher Bauträger/Hausbau-Konzern (Eigenheimbau, Wohnungsbau, Ferienimmobilien, Finanzierung). EOM betreut seit Jahren das SEO über mehrere Geschäftsbereiche und separate Domains. Es gab eine **Insolvenz von HELMA** und einen Übergang in einen **Notbetrieb** (2024); zuletzt eine **Projektübergabe (Juni 2025)** auf einen Investor-Kontext. Dieses Dossier fasst den aus Google Drive zugänglichen Wissensstand zusammen. Nicht alle Dateien sind exportierbar (Office-/Slide-Formate), entsprechende Lücken sind unten offen benannt.

## Überblick

**Wer/Branche:** HELMA ist ein Anbieter im Bereich Hausbau / Bauträger im DACH-Raum mit mehreren Geschäftsbereichen (Gewerken). Conversions/Ziele laut Übergabe: AG = Beauftragung für Hausbau, WB = Verkauf von Objekten (Neubau, Häuser und Wohnungen). *(Quelle: Helma - Projektübergabe, 2025-06-06)*

**Geschäftsbereiche & Domains** *(aus Ordnerstruktur + Übergabe + Meta-Sheets)*:
- **HAG** – HELMA Eigenheimbau AG → `https://www.helma.de/`
- **HWB** – HELMA Wohnungsbau GmbH → `https://www.helma-wohnungsbau.de/`
- **HFI** – HELMA Ferienimmobilien GmbH → `https://www.helma-ferienimmobilien.de/`
- **HBF** – Hausbau-Finanz (Finanzierungsvermittlung)
- **HFE / Energieautark** – Energieautarke Häuser, eigene Domain → `https://www.helma-energieautark.de/` (neue Businessline ab 2023)

**Backend/Technik:** Typo3 als CMS. Technik wurde von **HDNET** betreut; EOM hatte keinen direkten Technik-Kontakt, HELMA vermittelte. Seiten wurden überwiegend von HELMA selbst erstellt; EOM nahm „kleine Anpassungen" (Metas, Bilder etc.) vor. *(Quelle: Projektübergabe, 2025-06-06)*

## Mandat & Gewerke

EOM-Leistungen für HELMA (laut „Aufgaben EOM seit Notbetrieb", 2024-07-17 und Projektübergabe 2025):
- **Technisches Monitoring:** regelmäßige Crawls aller HELMA-URLs, Prüfung über Sistrix + Google Search Console; Analyse von 404-Seiten, Indexierungsproblemen; Ableitung von Handlungsempfehlungen für HDNET.
- **Rankings-/Traffic-Monitoring:** Überwachung Sichtbarkeit, Rankings und organischer Klicks; Nachoptimierung bei Auffälligkeiten.
- **On-Page/Content:** Schwellenkeyword-Optimierungen, Ratgeber-/Textoptimierungen, Erstellung von Meta-Daten für neue Referenzprojekte, Teaser-Texte (Pressebereich).
- **Strukturierte Daten:** laufender Test + Analyse von Rich-Snippets für Projekt-Seiten (WB/FI) und deren Effekt auf die Klickrate.
- **Spezial-Doings je GB:** AG = Aktualisierung „alter" Text-Optimierungs-Tasks + Crawl nach Erwähnungen ehemaliger Mitarbeiter/geschlossener Musterhäuser; FI = größere Optimierung Ostsee-/Nordsee-URLs sowie Verzeichnis `/nordrhein-westfalen/`.

**Zusammenarbeit/Setup** *(Projektübergabe 2025)*:
- PM/Ansprechpartner EOM: Roxi · SEO: Constantin · Kunde: Herr Maier (Sie-Anrede).
- Tools im Einsatz: Search Console, Google Analytics, Tag Manager, **Sistrix** + **Sistrix Optimizer**, **Monday** (PM + Kommunikation). Looker Studio für Reporting.
- Sistrix-Optimizer-Projekte vorhanden für HWB und AG, **Keywords aber nicht sauber gepflegt** → Empfehlung in der Übergabe: neues Projekt mit echten Fokus-Keywords anlegen.
- Aufgabenform: Schwellenkeyword-Optimierungen im externen Monday-Board; sonstige Themen per Mail mit Herrn Maier.
- Selbstständigkeits-Niveau: nur kleine Änderungen durfte EOM selbst umsetzen; künftiger Prozess (nach Insolvenz/Investor) noch ungeklärt.

## SEO-Status & Befunde

> Befund → Begründung → Maßnahme. Daten ausschließlich aus den Drive-Dokumenten; keine eigenen Rankings/SV-Schätzungen.

**1. Technische Fehler / kaputte Conversion-Pfade (HWB).**
Befund: Verlinkte „Katalog-bestellen"- und Kontaktseiten liefern 404 (z. B. `helma-wohnungsbau.de/kontakt/katalog-bestellen.html`); zudem vermischen sich AG- und WB-Seiten über die Site-Navi (404-Kette beim Wechsel zwischen Bereichen), und auf der WB-Fehlerseite wird im Störer fälschlich auf HAG verlinkt. Begründung: 404 auf transaktionalen Seiten kosten direkt Conversions und Nutzervertrauen. Maßnahme: defekte Links/Störer/Buttons systematisch prüfen und korrigieren (Aufgabe für HDNET). *(Quelle: HELMA Check, 2022-03-23)*

**2. Tracking-/Messlücken.**
Befund: Klicks, die in neuem Fenster öffnen, werden nicht weiter getrackt; GA-Event „Klicks Hauptnavigation" mit falschem Label (CSS-Selektor unzuverlässig, feuert mal falsch, mal gar nicht). Begründung: verfälschte Verhaltensdaten erschweren Optimierungsentscheidungen. Maßnahme: Navi-Tracking überarbeiten oder (laut interner Notiz) verzichten, da Navigationsklicks ohnehin über Seitenaufrufe sichtbar. *(Quelle: HELMA Check, 2022-03-23)*

**3. Trust-/E-E-A-T-Signale unzureichend platziert.**
Befund: Auszeichnungen/Preise/Urkunden sind auf den GB-Seiten schwer auffindbar, meist nur auf Startseiten. Begründung: gerade auf transaktionalen Seiten schaffen sichtbare Trust-Elemente Conversion-Vertrauen – in einer Branche, in der Käufer sich teils lebenslang verschulden. Maßnahme: Auszeichnungen sichtbar auf transaktionalen Seiten (ggf. global im Header), USP-Icons statt Fließtext, dedizierte Vorteils-/Ablauf-Unterseiten (Vorbild Heinz von Heiden); konkrete, differenzierende USPs statt Floskeln. *(Quelle: HELMA - Trust Elemente, 2023-05-25)*

**4. Lokale Landingpages ohne aktuelles Angebot.**
Befund: Lokale LPs („Haus bauen in xy", „Bauunternehmen in xy") existieren für Standorte, an denen HELMA teils keine Projekte mehr hat. Begründung: fehlende Projekte → schlechte Nutzersignale (Absprünge), die das Ranking belasten. Maßnahme: LPs ohne Perspektive deaktivieren/zusammenlegen – mit Kunde abzustimmen. *(Quelle: Projektübergabe, 2025-06-06)*

**5. Eigennamen-Problematik (Haus-Modelle = Städtenamen).**
Befund: HELMA-Hausmodelle tragen Städtenamen (z. B. `…/einfamilienhaeuser.html` mit Modell „Lübeck"), wodurch diese automatisch befüllten Seiten für „Haus in xy" ranken und Verwirrung stiften. Begründung: Keyword-Kannibalisierung/falsche Zuordnung gegenüber den eigentlichen lokalen LPs. Maßnahme: dokumentiert als bekannte Einschränkung; Seiten sind automatisiert befüllt und nicht direkt anpassbar. *(Quelle: Projektübergabe, 2025-06-06)*

**6. SEO-Strategie im Notbetrieb (Priorisierung).**
Befund/Maßnahme: Fokus auf Optimierung transaktionsorientierter Seiten (Schwellenkeyword-Optimierung bzw. größere Optimierungen mit Seitenzusammenlegungen/Textoptimierungen) je GB; CTR-/Meta-Optimierung und internes Verlinkungskonzept nachrangig (Verlinkungskonzept zurückgestellt, da unklar war, welche Seiten bleiben). Konkrete Optimierungsbereiche: helma.de = „Haus bauen in …", „Bauunternehmen in …", „Grundstücke in …", Ratgeber; HWB = „Aktuelle Projekte", „Bauträger in …", Haustypen; HFI = Ostsee/Nordsee + `/nordrhein-westfalen/`. *(Quelle: HELMA - SEO Maßnahmen Notbetrieb, 2024-08-06)*

**Positiv vermerkt:** Der Bauwissen-/Ratgeberbereich performt laut Übergabe konstant gut; auch lokale LPs („Haus bauen/kaufen in xy") liefen ordentlich. *(Quelle: Projektübergabe, 2025-06-06)*

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Sichtbarkeitsdaten im Kundenordner gefunden.** In den ausgewerteten Dateien gibt es keine Hinweise auf AI Overviews, ChatGPT/Perplexity-Tracking, llms.txt, AI-Crawler-Steuerung oder Brand-Mention-Monitoring in LLMs. Die SEO-Arbeit ist durchgängig klassisch (Sistrix-Sichtbarkeit, GSC-Rankings/Klicks, On-Page, technische Crawls). Falls GEO künftig Thema wird, fehlt hier jegliche Baseline.

## Doc-Typen & Aufbau

Typische Deliverable-Typen im HELMA-Ordner:
- **Übergabe-/Projektdokumente** (Sheets): zentrale Projektübergabe mit Ansprechpartnern, Tools, Zugängen, Conversions, Besonderheiten (z. B. „Helma - Projektübergabe", „Übergabe an Jelena/Elisa").
- **Keyword-Recherchen** (Sheets): Spalten `LP | KW | SV`, gruppiert nach Ziel-Landingpage (Beispiel Energieautark, 2023).
- **Title/Meta-Sheets** (Sheets): Spalten `URL | Title | Description` (Beispiel Energieautark Meta-Daten, 2024).
- **Technik-/Crawl-Checks** (Sheets, teils .xlsx): „Linkfehler", „Gecrawlt – zurzeit nicht indexiert", „Duplikat – nicht als kanonisch festgelegt", „Fehlende URLs in Sitemaps", „http erreichbare URLs", geschlossene Standorte.
- **On-Page-/Content-Empfehlungen** (Docs): Alt-Texte, Trust-Elemente, strukturierte Daten, GMB-Empfehlungen, Inhalts-Ideen für LPs.
- **Reporting**: eigener Ordner „Reportings" (Monatsstruktur, z. B. Dezember 2022 / Januar 2023) + Looker Studio; SEA in separatem Ordner.

## Schreibstil-Notizen

- **Sie-Anrede** durchgängig in Kunden-Copy und gegenüber dem Kunden (Herr Maier). *(Projektübergabe)*
- **Title/Meta-Konvention (Energieautark-Beispiele):** Marke „HELMA" prominent im Title, oft Muster `<Nutzen> von HELMA – <Claim>`. Descriptions beginnen meist mit Imperativ („Entdecken Sie …", „Erleben Sie …", „Profitieren Sie …"), enthalten das **►-Zeichen** vor dem CTA und schließen mit kurzem CTA („► Mehr erfahren", „► Jetzt informieren", „► Kontaktieren Sie uns"). *(Quelle: HELMA Energieautark - Meta Daten, 2024-04-19)*
- **Inhaltlich/Tonalität:** ehrliche, transparente Kommunikation als Leitprinzip (Baubranche, hohe Investition, kritische Zielgruppe). Konkrete, differenzierende USPs statt Floskeln wie „x Jahre Erfahrung". Nutzer „nicht die Katze im Sack kaufen lassen" – Abläufe (Bauzeit, Festpreis, Zahlungsmodalitäten, Bauleitung) offen erklären. *(Quelle: Trust-Elemente, 2023-05-25)*
- **Content-Aufbau LPs (Energieautark):** Grundlagen erklären → Vorteile je Zielgruppe → Kacheloptik mit Haustypen → frühe interne Verlinkung; Zielgruppen-spezifische Abschnitte (Wohnungsbaugenossenschaften, Energieversorger, Banken, private Investoren). *(Quelle: Energieautarke Häuser - Ideen Inhaltliche Themen LPs, 2023-10-02)*

## Offene Punkte / Datenlücken

- **Kein GEO/KI-Material** vorhanden (siehe oben) – keine Baseline zu AI-Sichtbarkeit.
- **Keine aktuellen Sichtbarkeits-/Ranking-Zahlen** im Vault erfassbar; konkrete Sistrix-/GSC-Werte stehen in Tools, nicht in den gelesenen Docs (bewusst nicht geschätzt).
- **Office-Formate (.xlsx) nicht exportierbar**, daher nur per Dateiname gewertet: z. B. „HELMA_Alle GF_Site Search 2022.xlsx", „HAG - Gecrawlt – zurzeit nicht indexiert 08.12.23.xlsx" – Inhalte ungelesen.
- **Crawls-Ordner & SEO-Unterordner** enthalten viele weitere Detail-Sheets (Linkfehler, Indexierung, Bannertexte) – nur Top-Treffer gesichtet, nicht vollständig ausgewertet.
- **Statusunsicherheit durch Insolvenz/Notbetrieb:** Mandatsumfang nach Übergabe Juni 2025 (Investor) und welche GB/Domains aktiv bleiben, ist aus den Docs nicht abschließend ersichtlich.
- **Energieautark-Domain:** unklar, ob `helma-energieautark.de` nach Insolvenz weiterbesteht; Meta-/KW-Material ist von 2023/2024.

## Quellen (ausgewertete Dateien)

Alle aus Google Drive, Ordner `HELMA` (ID `1mT57oRPol8eJ3TxUnU9sQ1Atvy2tieV-`), Account ben@eom.de:

| Datei | Typ | Stand |
|---|---|---|
| Helma - Projektübergabe (Ordner „Übergabe") | Sheet | 2025-06-06 |
| HELMA - SEO Maßnahmen - Notbetrieb 2024 - aktualisiert | Doc | 2024-08-06 |
| HELMA - Aufgaben EOM seit Notbetrieb - 17.07.2024 | Doc | 2024-07-17 |
| HELMA Check | Doc | 2022-03-23 |
| HELMA - Trust Elemente | Doc | 2023-05-25 |
| HELMA - Energieautarke Häuser - Vorschläge/Ideen Inhaltliche Themen LPs | Doc | 2023-10-02 |
| HELMA - Keywordrecherche Energieautarke Häuser | Sheet | 2023-11-10 |
| HELMA Energieautark - Meta Daten | Sheet | 2024-04-19 |
| Ordnerstruktur Kundenordner + Unterordner (SEO, Crawls, Reportings, Energieautark) | Drive-Listing | 2026-06-19 |

Verwandt: [[Über EOM]] · [[SEO-Methodik]] · [[Schreibstil]] · [[Tools-Stack]]
