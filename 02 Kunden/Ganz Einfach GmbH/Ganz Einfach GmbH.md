---
tags: [kunde, seo]
kunde: "Ganz Einfach GmbH"
stand-Datum: 2026-06-19
---

# Ganz Einfach GmbH

> Kunden-Wissensbasis (SEO & GEO). Aufbau nach EOM-Logik: **Befund → Begründung → Maßnahme**.
> Quellen siehe Abschnitt [[#Quellen]]. Stand: 2026-06-19.

## Überblick

- **Kunde / Betreiber:** Ganz Einfach GmbH. Tritt im SEO-Mandat unter der Marke **Brandson** auf.
- **Branche:** E-Commerce / Online-Shop für Haushalts-, Klein- und Elektrogeräte (Ventilatoren, Luftkühler, Heizlüfter, Wetterstationen, Bewässerung, Werkzeug, Outdoor & Hobby). Vergleichbares Sortiment wie Klarstein.
- **Sortimentsgröße:** Laut Kunde ca. **3.000 Artikel**; mehrere Eigen-/Hausmarken (genannt: Brandson, Arendo, Prime sowie zahlreiche kleinere Marken).
- **Domains:**
  - **brandson.de** — neuer Shopware-Shop, zum Erhebungszeitpunkt kurz vor Launch (Live-Gang geplant Ende/Anfang der Woche um den 16.06.2026). Aktuell **keine SEO-Sichtbarkeit** (Nulllinie), da nie live.
  - **brandson-equipment.com** — Alt-/Bestandsseite auf **Squarespace** (Staging-Referenz: felix-schmidt-dg58.squarespace.com). Trägt aktuell den Großteil des organischen Traffics; eher Katalog-Charakter mit Verlinkung zu Marktplätzen.
  - **ganzeinfach.de** — Firmen-/Marken-Hintergrund (u. a. alte Feedback-Mail feedback@ganzeinfach.de).
- **Regionen:** DACH. brandson.de mit drei Länder-Pfaden: `/` (DE), `/at` (AT), `/ch` (CH), aktuell einsprachig deutsch.
- **CMS:** Neuer Shop = **Shopware**; Altseite = **Squarespace** (Domain liegt nicht bei Squarespace, sondern beim Hosting-/Domain-Dienstleister, vermutlich 1&1; Zugriff über interne IT).

## Mandat & Gewerke

EOM betreut Brandson/Ganz Einfach in einem **laufenden SEO-/GEO-Mandat** mit aktuellem Fokus auf den **Shop-Relaunch und die Domain-Migration**. Erkennbare Gewerke aus den Unterlagen:

- **Technical SEO:** Relaunch-Begleitung, Domain-Migration brandson-equipment.com → brandson.de, GSC-Einrichtung, hreflang, Canonicals/Trailing Slash, Sitemap/robots, Tracking-Prüfung nach Go-Live.
- **On-Page / Content:** Title-/Meta-Templates, Überschriften-Struktur (H1), Produkt-/Kategorietexte, Duplicate-Content-Prüfung, perspektivisch Ratgeber-/FAQ-Seiten.
- **Keyword-/Themenrecherche:** Cluster-Recherche, Start mit Oberkategorie „Ventilatoren & Luftqualität".
- **GEO / KI-Sichtbarkeit:** als nächster Schritt im Mandat eingeplant (Status-Quo-Erhebung steht noch aus).
- **SEA & Tracking:** eigene Ordner „03. SEA" und „02. Tracking" im Drive vorhanden (nicht Teil dieser SEO-Erfassung, aber Hinweis auf breiteres Mandat).

Drive-Ablage des Kunden ist nach Gewerken sortiert: `01. Angebote`, `02. Tracking`, `03. SEA`, `04. Brandson SEO`, `05. Meetings`, `06. Reportings` (Reportings-Ordner aktuell **leer**).

Beteiligte (aus Meeting): EOM-seitig Hannes Ühss, Johanna Knebel, Roxeanne Rieck; Kundenseite „Can & Markus" sowie weitere Ansprechpartner (nvurus@ganzeinfach.de). Aufgaben werden in **Monday** dokumentiert.

## SEO-Status & Befunde

Quelle für die Befunde: *SEO- & GEO-Strategie* (Google Doc, Juni 2026) und *2026-06 Crawl brandson-equipment.com* (Sheet), sofern nicht anders genannt. Priorisierung 1 = hoch, 3 = niedrig (vom Analysten im Strategiedoc vergeben).

### Ausgangslage / Sichtbarkeit
- **Befund:** brandson.de hat keine Sichtbarkeit (neue Domain); brandson-equipment.com ist die von Google indexierte Hauptdomain und das primäre Ergebnis bei der Suche nach „Brandson". Die Altseite zeigte historisch wiederkehrende kurzfristige Sichtbarkeits-Peaks (laut Doc in der Spitze bis ~6.000 monatliche SEO-Klicks). *(Quelle: Strategie-Doc, Juni 2026.)*
- **Begründung:** Es existiert bereits etablierte **Markenbekanntheit** mit echten Brand-Suchanfragen (z. B. „brandson turmventilator" ~300/Monat DE, „brandson heizlüfter", „brandson ventilator"). Brand-Keywords sind schwer von Wettbewerbern angreifbar.
- **Maßnahme:** Diese Brand-Basis beim Relaunch erhalten und gezielt von brandson-equipment.com auf brandson.de transferieren.

### Befund 1 — Google Search Console Domain Property (Prio 1)
- **Befund:** Für beide Domains existiert (noch) keine eingerichtete GSC-Domain-Property.
- **Begründung:** GSC ist der einzige Kanal mit proprietären Google-Daten (Klicks, Impressionen, Position) und Voraussetzung für ein sauberes Migrations-Monitoring.
- **Maßnahme:** GSC-Domain-Property für brandson.de **und** brandson-equipment.com anlegen; Nutzer **ganzeinfach.eom@gmail.com** zufügen. Spätestens zum Live-Gang.

### Befund 2 — Domain-Migration brandson-equipment.com → brandson.de (Prio 1)
- **Befund:** Der Großteil des SEO-Traffics in DE/AT/CH landet auf der Altdomain. Beim Launch des neuen Shops droht ein Domain-Konflikt (Google weiß nicht, welche Domain ranken soll).
- **Begründung:** Ohne saubere URL-genaue Weiterleitung droht im Worst Case ein Neustart bei null (Rankings über Wochen/Monate weg). Eine reine Komplett-Weiterleitung der Domain ist „Pokern".
- **Maßnahme:** Dreischritt — (1) GSC-Property einrichten, (2) **Redirect-Map** für alle relevanten URLs erstellen (1:1 auf die jeweils existierende Zielseite im neuen Shop) und Umzug in GSC über das Tool zur Adressänderung melden, (3) Weiterleitungen technisch hinterlegen (vermutlich beim Hosting-/Domain-Dienstleister, da die Squarespace-Domain extern liegt). Migration **auf einen Schlag**. Die Redirect-Map wird im Sheet *2026-06 Crawl brandson-equipment.com* aufgebaut (Spalte „Neue URL & Weiterleitung"); Stand 2026-06-19 sind dort erst wenige Ziele gepflegt (z. B. `/` → brandson.de, `/kontakt` → `/service/kontakt-kundenservice`), der Großteil ist noch „TBD".

### Befund 3 — Überschriften (Prio 2)
- **Befund:** Auf **Kategorie-Seiten** ist die Hauptüberschrift häufig als `<h2>`/`<h3>` statt `<h1>` ausgezeichnet; zusätzlich gibt es in mehreren Templates **leere Überschriften** (Ober­kategorie- und Produktseiten). Produktseiten-H1 sind bereits korrekt.
- **Begründung:** Eine eindeutige H1 ist ein zentrales On-Page-Signal; leere Überschriften erzeugen unsaubere Struktur.
- **Maßnahme:** Kategorie-Hauptüberschrift auf `<h1>` umstellen; leere Überschriften aus den Templates entfernen.

### Befund 4 — hreflang (Prio 2)
- **Befund:** Alle drei Länder-URLs (`/`, `/at`, `/ch`) werden mit **`de-DE`** ausgezeichnet; kein `x-default`. AT- und CH-Seiten sind aktuell 1:1-Kopien der DE-Seite.
- **Begründung:** Falsche Sprach-/Regionsauszeichnung verhindert korrektes Geo-Targeting; identische Inhalte führen zu **Duplicate Content** → AT/CH werden ggf. nicht/teilweise indexiert.
- **Maßnahme:** AT-URL als `de-AT`, CH-URL als `de-CH` auszeichnen; `x-default` auf die DE-URL legen. Mittelfristig AT/CH mit markt-spezifischem Content differenzieren (Aufwand → in Folge-JF zu klären).

### Befund 5 — Meta Title & Descriptions (Prio 2)
- **Befund:** Title/Description-Längen teils außerhalb der Google-Vorgaben (Abschneiden/Umschreiben). Produkt-Titel folgen dem Muster `Name | Anzahl | Artikel-Nr`, teils mit **doppelter Farbangabe** und teils mit vorangestelltem Markennamen „Brandson". Kategorie-Titel oft nur **ein Wort**. Einige Unterseiten mit **leerer Meta Description**. **404-Seite** trägt den Meta-Title „Ganz Einfach".
- **Begründung:** Title/Description sind die SERP-Basis; zu kurz/zu lang/leer = verschenktes CTR-Potenzial; uneinheitliche 404-Titel verhindern 404-Monitoring.
- **Maßnahme – Templates (für Shopware):**
  - Produkt-Seite: `{productsName} (Artikel-Nr)` — zweite Farbangabe und Anzahl raus, Artikel-Nr in Klammern, mit wichtigstem Keyword statt Marke starten.
  - Kategorie-Seite: `{productsCategory} günstig online bestellen | Brandson`.
  - Leere Descriptions befüllen; 404-Title auf „Seite nicht gefunden" o. ä. ändern (Basis für 404-Monitoring).

### Befund 6 — Canonical & Trailing Slash (Prio 3)
- **Befund:** URLs sind sowohl mit als auch ohne Trailing Slash erreichbar; Canonical zeigt bereits korrekt auf die Variante ohne Slash.
- **Begründung:** Google ignoriert Canonicals gelegentlich → Restrisiko Duplicate Content.
- **Maßnahme:** Trailing-Slash-Varianten global per **301** auf die Variante ohne Slash weiterleiten.

### Befund 7 — XML-Sitemap in robots.txt (Prio 3)
- **Befund:** Sitemap ist nicht in der robots.txt verlinkt.
- **Maßnahme:** `Sitemap: https://www.brandson.de/sitemap.xml` ans Ende der robots.txt ergänzen.

### Befund 8 — Produkt-/Kategorietexte & Duplicate Content (On-Page)
- **Befund (aus „SEO Check – Name & Beschreibung"):** Mehrere ähnliche Produkte teilen sich identische Beschreibungen (Beispiele Produkt-IDs 307596/307594/307595; 306858/306859/306857/306856); mind. ein Produkt mit fehlerhafter Zuordnung (Tabelle bewirbt 2er-Set, Shop führt Einzelprodukt — ID 1430); doppelte Leerzeichen in Texten (z. B. ID 307346).
- **Begründung:** Identische Texte = Duplicate Content; falsche Zuordnungen schaden Nutzervertrauen und Datenqualität.
- **Maßnahme:** Beschreibungen je Produktvariante (Set/Farbe) individualisieren; fehlerhafte Einträge korrigieren und auf Systematik prüfen; doppelte Leerzeichen bereinigen. Zusätzlich: aussagekräftige Meta Title/Description je Ober-/Haupt-/Produktkategorie + SEO-Kategorietexte (Kurzbeschreibung oben, Langtext + FAQ unten) — sofern Shopware Freitextfelder erlaubt.

### Wettbewerb (Befund, eingeschränkt belegbar)
- **Befund:** Verglichene Domains: de.dreo.com, rowenta.de/at/ch, klarstein.de/at/ch. brandson-equipment.com liegt im DACH-Vergleich am unteren Ende (laut Strategie-Doc ~1.500 monatliche SEO-Klicks / ~80 rankende Keywords; im Crawl-Sheet bewegen sich Werte in ähnlicher Größenordnung). Dyson.de erhält laut Doc knapp 1 Mio. Klicks/Monat (Premium-Marke, breiter Kategoriebaum → nur bedingt vergleichbar). Klarstein als direktester Wettbewerber mit deutlichem Vorsprung. Backlink-Profil im Mittelfeld, aber mit hohem Spam-Anteil.
- **Begründung:** Großer Abstand v. a. durch Markenbekanntheit und Sortimentsbreite der Wettbewerber.
- **Maßnahme:** Auf Brand-Basis aufbauen, Rankings der bestehenden Keywords verbessern, Sortiment entlang nachgefragter Kategorien (siehe Wettbewerber-Top-Produkte) ausbauen. Top-Traffic-Kategorien der Wettbewerber zur Orientierung: Klarstein (mobile Klimaanlage, Eiswürfelmaschine, Dunstabzugshaube), Rowenta (Akku-Staubsauger, Wischsauger, Nasssauger), Dreo (Turmventilator, Heizlüfter, Ventilatoren), WMF (Wasserkocher, Besteck, Pfanne).
- **Hinweis (Datenlücke):** Konkrete Sichtbarkeits-/Klickzahlen der Wettbewerber stammen aus Tool-Screenshots im Doc und sind hier nur referenziert, nicht eigenständig verifiziert.

### Stärkste Bestands-URLs (aus Crawl-Sheet, als Migrations-Priorität)
Traffic-Werte (Tool-Schätzung, Monatsbasis) und Top-Keyword/Position aus *2026-06 Crawl brandson-equipment.com* (~325 URLs erfasst):
- `/produkte-standventilatoren` — Traffic ~1.320; Top-KW „standventilator" (SV 22.000, Pos. 7).
- `/produkte-turmventilatoren` — Traffic ~822; Top-KW „turmventilator" (SV 29.000, Pos. 12). Redirect-Ziel im Sheet „TBD".
- `/` (Startseite) — Traffic ~120; Brand „brandson" (SV 100, Pos. 1) → Ziel brandson.de.
- `/turmventilator-weiss` — ~112; „brandson turmventilator" (SV 1.200, Pos. 5).
- `/turmventilator-coolgrau` — ~70; „brandson turmventilator" (SV 1.200, Pos. 7).
- `/keramik-heizluefter-weiss-2000w` — ~31; „brandson heizlüfter" (SV 80, Pos. 1).
- **Maßnahme:** Diese URLs in der Redirect-Map mit höchster Priorität 1:1 auf die passenden Zielseiten in brandson.de mappen.

## GEO / KI-Sichtbarkeit

- **Befund:** Brandson wird laut Strategie-Doc in den gängigen KI-Tools **deutlich seltener erwähnt** als Wettbewerber (Vergleich genannt: klarstein.de, rowenta.de vs. brandson-equipment.com). Eine eigene, belastbare GEO-Status-Erhebung liegt **noch nicht** vor — sie ist als nächster Schritt im laufenden Mandat eingeplant.
- **Begründung:** Markenbekanntheit, Autorität und SEO-Traffic wirken direkt auf die KI-Sichtbarkeit; bei niedriger Brand-Stärke ist auch die Erwähnung in LLMs gering.
- **Maßnahme:** GEO-Status-Quo erheben (z. B. via Peec AI / Brand-Radar-Tooling), priorisierte Handlungsempfehlungen ableiten. **Keine eigenen GEO-Messdaten gefunden** — Werte stehen noch aus.

## Doc-Typen & Aufbau

Im Drive-Kundenordner (Ordner „04. Brandson SEO" + Shortcut „EOM SEO" + „05. Meetings/JF Notizen") vorhanden:

- **Strategie-Dokument** (Google Doc): „2026-06 – Brandson SEO/GEO-Strategie" — gegliedert in 1) SEO-Status Quo, 2) Technische Analyse (Findings mit Prio 1–3 + UX-Block), 3) Wettbewerbsanalyse, 4) Keyword-/Themenrecherche, 5) GEO-Status & -Potenzial. Durchsetzt mit Tool-Screenshots (im Text-Export nur als Platzhalter sichtbar).
- **Crawl-/Redirect-Sheet** (Google Sheet): „2026-06 – Crawl brandson-equipment.com" — Spalten URL | Traffic | Keywords | Top-Keyword | Top-KW-Suchvolumen | Top-KW-Position | Neue URL & Weiterleitung. Dient als Basis der Redirect-Map (~325 URLs).
- **On-Page-Check** (Google Doc): „SEO Check_Name & Beschreibung" — Prüfung Produkt-Titel/-Beschreibungen auf Duplicate Content, Fehler, Formatierung + Empfehlungen zu Kategorietexten/Meta.
- **Office-Anhang** (nicht exportierbar, nur per Name gewertet): „Brandson_Titel_USP_Beschreibung_Duplikate.xlsx" — Quelltabelle der Produkt-Titel/USP/Beschreibungen inkl. Duplikat-Markierung.
- **Meeting-Notiz** (Google Doc, Gemini): „Ganz Einfach x EOM – SEO-Strategie – 2026/06/16" — Zusammenfassung + Next Steps + Volltranskript des JF.
- **Content-/Themenstruktur** (Shortcut-Ordner „EOM SEO"): Kategorie-Ordner 1. Ventilatoren, 2. Luftqualität, 3. Bewässerung, 4. Geräte & Technik, 5. Wohnen & Haushalt, 6. Haustechnik, 7. Outdoor & Hobby, 8. Werkstatt & Baustelle, Logos — Arbeitsstruktur für Keyword-Recherche/Content je Kategorie.

Aufbau-Logik durchgängig **Befund → Begründung → Maßnahme** mit Priorisierung (1–3); UX-Hinweise separat vom reinen SEO-Impact ausgewiesen.

## Schreibstil-Notizen

- **Anrede:** „ihr/euch" im Strategie-Doc (kollegial-direkt gegenüber dem Kunden), Sie-Anrede in shop-/nutzerseitiger Copy (z. B. „Bitte wählen Sie eine Filiale").
- **„KI" statt „AI":** Im Strategie-Doc taucht „AI-Tools" auf — für EOM-Vault-Texte konsequent **KI** verwenden.
- **Ton:** erklärend, mit Klammer-Definitionen und Anleitungs-Links (z. B. „was ist ein Trailing Slash?"), pragmatisch („lieber elementar etwas da, dann nachjustieren").
- **Priorisierung sichtbar:** Jedes Finding mit Prio 1–3; Aufwand-/Entscheidungspunkte offen benannt und in Folge-Termine (JF) verschoben.
- **Marken-Konvention für Title:** Kategorie-Title-Template endet auf `| Brandson`; Markenname im Produkt-Title bewusst nach vorne-Keyword verschoben.

## Offene Punkte / Datenlücken

- **GSC noch nicht eingerichtet** → keine proprietären Google-Performance-Daten (Klicks/Impressionen/Position) verfügbar; alle Traffic-/Keyword-Zahlen stammen aus Drittanbieter-Tools (Schätzwerte).
- **Reportings-Ordner leer** → kein laufendes Reporting im Drive ablegt (Stand 2026-06-19).
- **GEO-Status-Quo fehlt** → keine eigenen KI-Sichtbarkeitsdaten; nur qualitative Aussage „seltener erwähnt".
- **Redirect-Map unvollständig** → im Crawl-Sheet überwiegend „TBD" in der Zielspalte; Migration noch nicht abgeschlossen.
- **Entscheidung Shop-Struktur offen** → ein großer Sammel-Shop (ganzeinfach) vs. spezialisierte Marken-Shops (Brandson/Arendo/Prime) wurde **vertagt**; Risiko Duplicate Content bei Mehrfachlistung gleicher Artikel.
- **Technische Umsetzbarkeit der Redirects** → Domain liegt extern (nicht bei Squarespace), interne IT/Hosting-Dienstleister muss umsetzen; Zuständigkeit/Weg noch zu klären.
- **AT/CH-Differenzierung** → aktuell Kopien; eigener Content für AT/CH noch nicht entschieden (Aufwand).
- **Office-XLSX** „Brandson_Titel_USP_Beschreibung_Duplikate.xlsx" nicht maschinell ausgewertet (kein Export möglich) — Inhalt nur über den abgeleiteten „SEO Check" bekannt.
- **Keyword-Recherche-Doc** „2026-06 Keyword Recherche Brandson" (im Strategie-Doc verlinkt) wurde hier nicht separat geöffnet/ausgewertet.

## Quellen

Ausgewertete Dateien (Google Drive, Account ben@eom.de, Ordner „Ganz Einfach GmbH"), Stand 2026-06-19:

1. **2026-06 – Brandson SEO/GEO-Strategie** (Google Doc) — Status Quo, technische Findings (Prio 1–3), Wettbewerb, Keyword-Cluster, GEO. *(Modified 2026-06-16)*
2. **2026-06 – Crawl brandson-equipment.com** (Google Sheet) — ~325 Bestands-URLs mit Traffic/Top-KW/SV/Position + Redirect-Ziel-Spalte. *(Modified 2026-06-16)*
3. **SEO Check_Name & Beschreibung** (Google Doc) — On-Page-Prüfung Produkt-Titel/-Beschreibungen, Duplicate Content, Kategorietext-Empfehlungen. *(Modified 2026-05-12)*
4. **Ganz Einfach x EOM – SEO-Strategie – 2026/06/16** (Google Doc, Gemini-Notiz) — Meeting-Zusammenfassung, Next Steps, Transkript. *(Modified 2026-06-17)*
5. **Brandson_Titel_USP_Beschreibung_Duplikate.xlsx** (Office, nur per Name gewertet — nicht exportierbar) — Quelltabelle Produkt-Titel/USP/Beschreibung mit Duplikat-Markierung.
6. **Ordnerstruktur** „EOM SEO" (Kategorie-Ordner) + Kundenordner-Hauptebene (01.–06.) — als Kontext für Gewerke und Content-Struktur.

Verwandte Notizen: [[Über EOM]] · [[SEO-Methodik]] · [[Tools-Stack]]
