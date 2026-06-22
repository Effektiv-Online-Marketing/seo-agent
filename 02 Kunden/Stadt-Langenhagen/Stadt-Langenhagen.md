---
tags: [kunde, seo]
kunde: "Stadt-Langenhagen"
stand-Datum: 2026-06-19
---

# Stadt-Langenhagen

> Wissensbasis zusammengetragen aus dem Google-Drive-Kundenordner (Account `ben@eom.de`). Analyse-Logik: **Befund -> Begründung -> Maßnahme**. Es werden ausschließlich Inhalte aus den vorgefundenen Dateien wiedergegeben; nichts ergänzt oder geschätzt. Alle Quellen mit Datum in [[#Quellen]].

## Überblick

- **Wer:** Stadt Langenhagen — Kommunalverwaltung / öffentlicher Sektor in der Region Hannover (Niedersachsen).
- **Branche:** Öffentliche Verwaltung (kommunale Website, Bürgerservice, Standortvermarktung). Kein klassischer E-Commerce, sondern informations- und serviceorientierte Stadt-Website.
- **Domain:** `www.langenhagen.de`. Zusätzlich vorhandene Subdomains/Portale, die im Material auftauchen: `service.langenhagen.de` (Rathaus-Serviceportal), `branchenbuch.langenhagen.de`, `maengelmelder.langenhagen.de`, sowie die historische Subdomain `m.langenhagen.de`.
- **Technische Plattform:** Die Website läuft auf dem CMS/Dienstleister **Nolis** (vgl. [[#Quellen|Fragebogen]] und Weiterleitungsbefund auf `nolis.de`). EOM liefert Konzeption/SEO; die technische Umsetzung erfolgt durch Nolis.
- **Anlass des Mandats:** **Website-Relaunch** (Kick-off-Workshop 22.04.2020, Relaunch-Ziel „bis Ende 2020"). Die ausgewerteten SEO-Befunde stammen überwiegend aus der Phase **nach dem Relaunch** (Q4 2020 / Anfang 2021).

## Mandat & Gewerke

Aus den Dateinamen und Inhalten ableitbar (nicht erfunden):

- **Relaunch-Begleitung & Konzeption** der neuen `langenhagen.de` (Kick-off-Workshop 04/2020, Themen-/Notizdokumente, Sitemap-Konzeption).
- **Informationsarchitektur / Sitemap** — Seitentypen, Ressorts und Verteilerseiten-Struktur (Sitemap-Sheets 2020).
- **On-Page-SEO** — Title-Tag-/Meta-Description-Empfehlungen (dynamisch + manuell), Grundoptimierung zentraler Seiten.
- **Technisches SEO (Post-Relaunch-Audit)** — Canonical-Tags, Breadcrumb-Navigation, URL-Parameter, Weiterleitungen, 404-Handling, Duplicate Content.
- **SEA / Paid & Social** — Checkliste „Projektstart, Tools & Zugänge, SEO, SEA"; Slides „Social & Google Ads, Influencer" (09/2021); Recruiting-Ads über Meta (01/2025); Facebook-Pages-Zusammenlegung (09/2023).

Schwerpunkt des **SEO/GEO-relevanten** Materials liegt klar auf **technischem Post-Relaunch-SEO** und **On-Page (Title/Meta)** aus 2020/2021.

## SEO-Status & Befunde

### 1. Title-Tags & Meta-Descriptions fehlten/duplizierten nach Relaunch
- **Befund:** Direkt nach dem Relaunch lautete der Title-Tag **auf jeder Seite identisch „Stadt Langenhagen"**; Meta-Descriptions waren **nicht gepflegt**. (Quelle: *Empfehlung der dynamischen Meta-Daten*, 19.11.2020)
- **Begründung:** Google stuft identische, nicht zur Seite passende Titles als ungeeignet ein und generiert eigene Snippets; fehlende Descriptions führen zu automatisch gewählten, oft abgeschnittenen Textauszügen. Verlust an Relevanz- und CTR-Steuerung.
- **Maßnahme (EOM-Empfehlung):**
  - **Dynamische Default-Title-Tags und Default-Meta-Descriptions** systemseitig hinterlegen, damit jede Seite automatisch versorgt ist — bei gleichzeitiger Möglichkeit zur **manuellen Übersteuerung** durch Redakteure.
  - Zwei vorbereitete Varianten (je nach technischer Machbarkeit):
    - **Variante 1 — Title:** `{Name der Kategorie} | Stadt Langenhagen`; **Description:** „Stadt Langenhagen informiert: das Wichtigste aus der Region ✓ alles Wissenswerte zum Thema ‚{Kategorie}' ✓ immer aktuell ⇒ Jetzt informieren!"
    - **Variante 2 — Title:** `{Name der Kategorie} | Stadt Langenhagen`; **Description:** „Wichtiges aus der Region: Stadt Langenhagen über {Verteilerseite Ebene 2} ✓ alles Wissenswerte zum Thema ‚{Kategorie}' ⇒ Jetzt informieren!"
  - Ergänzend **manuell ausformulierte Title/Meta für zentrale Verteilerseiten** (Sheet *Empfehlung der Meta-Daten Verteilerseiten*, 08.12.2020) — siehe Stilmuster unter [[#Schreibstil-Notizen]].

### 2. Fehlerhafte / fehlende Canonical-Tags -> interner Duplicate Content
- **Befund:** Viele Seiten sind nach Relaunch über **mehrere URLs mit identischem Inhalt** erreichbar. Canonical-Tags fehlen teilweise oder **verweisen auf Parameter-URLs** (z. B. Serviceportal-Seiten verweisen per Canonical nicht auf sich selbst, sondern auf `?myMedium=1`-Varianten). Bei Hauptpunkten wie `…/rathaus-politik/` und `…/leben-in-langenhagen/` **fehlen Canonicals ganz**. (Quelle: *Alternative Empfehlung Canonical-Tags*, 25.01.2021)
- **Begründung:** Interner Duplicate Content; falsche Seiten werden als Original indexiert, was die SEO-Performance schwächt.
- **Maßnahme:** Canonical-Logik in den Templates korrigieren. In allen relevanten Seiten ausschließlich die **teilweise sprechende System-URL mit ID, aber ohne Parameter** als Canonical verwenden — entweder selbst-referenzierend oder auf die Originalseite verweisend. Canonicals dürfen **keine** Redirects (3xx), Nicht-200-Statuscodes (4xx/5xx) oder `noindex`-Seiten sein.

### 3. Breadcrumb-Navigation verlinkt Parameter-URLs (+ Selbstverlinkung)
- **Befund:** Breadcrumb-Punkte verlinken auf URLs **mit Parametern** statt auf die sauberen System-URLs; zusätzlich verlinkt der letzte Breadcrumb-Punkt auf sich selbst. (Quelle: *Alternative Empfehlung Breadcrumb-Navigation*, 25.01.2021)
- **Begründung:** Fördert internen Duplicate Content und schwächt die Stärkung relevanter Seiten über interne Verlinkung; Selbstverlinkung der aktuellen Seite bietet dem Nutzer keinen Mehrwert.
- **Maßnahme:** Breadcrumb-Links durchgängig auf die **System-URLs ohne Parameter** umstellen; den **letzten (aktiven) Breadcrumb-Punkt nicht verlinken**.

### 4. Falsch generierte Breadcrumb (Inhalt der zuvor besuchten Seite)
- **Befund:** Bei manchen Seiten wird **die Breadcrumb der vorher aufgerufenen Seite** angezeigt statt der eigenen (Beispiel: Seite „Interkultureller Erlebnispark" zeigt Breadcrumb von „Mietspiegel"). (Quelle: *Weitere Auffälligkeiten Part 2*, 15.01.2021)
- **Begründung:** Technischer Template-/Caching-Fehler; irreführende Orientierung für Nutzer und Suchmaschinen.
- **Maßnahme:** Breadcrumb-Generierung serverseitig korrigieren, sodass sie immer den Pfad der aktuellen Seite abbildet.

### 5. Weitere Post-Relaunch-Auffälligkeiten
(Quelle: *Weitere Auffälligkeiten Part 1*, 12.01.2021)
- **URLs mit Parametern und Zahlen in der Navigation** (z. B. `…silbersee-900000157-30890.html?naviID=…&brotID=…&rubrik=…`) -> auf saubere System-URLs umstellen.
- **Verwaiste Seiten**, die nicht in der Navigation verlinkt sind (z. B. `…/wohngeld-900000303-30890.html`) -> interne Verlinkung herstellen.
- **Uneinheitliche 404-Seiten** (z. B. `…/wietzepark.html` vs. `…/wietzepark/`) und **automatische JS-Weiterleitung von 404-Seiten auf die Startseite** -> abstellen, saubere/echte 404 ausliefern.
- **Falsche Weiterleitung alter URLs/Subdomains:** `https://m.langenhagen.de/` leitet auf `https://www.nolis.de/` (den Dienstleister) statt auf die eigene Domain -> auf `https://www.langenhagen.de/` umleiten.

### 6. Grundoptimierung zentraler Seiten
- **Befund/Maßnahme:** Separates Arbeits-Sheet *Grundoptimierung zentraler Seiten* (09.12.2020) mit ausformulierten **Title-Tags und Meta-Descriptions je Verteilerseite** über die Navigationsebenen 0–3 (Start, Rathaus & Politik, Leben in Langenhagen, Wirtschaft & Standort u. a.). Dient als On-Page-Umsetzungsliste für die wichtigsten Seiten.

## GEO / KI-Sichtbarkeit

**Keine GEO-/KI-Daten gefunden.** Im gesamten Kundenordner liegen keine Dokumente zu Generative Engine Optimization, AI Overviews, ChatGPT/Perplexity-Sichtbarkeit, LLM-Crawlern (GPTBot/ClaudeBot/PerplexityBot), `llms.txt` oder KI-Markenerwähnungen vor. Das Material datiert überwiegend 2020/2021 (jüngste Dateien 2023/2025 betreffen Paid Social/Recruiting, nicht GEO). Eine GEO-Bewertung ist auf Basis der vorhandenen Drive-Inhalte derzeit **nicht möglich**.

## Doc-Typen & Aufbau

Im Ordner wiederkehrende EOM-Deliverable-Typen für diesen Kunden:

- **Onboarding/Setup:** „Checkliste Projektstart, Tools & Zugänge, SEO, SEA" (Sheet); „Fragebogen Online-Marketing" (Doc).
- **Workshop-Doku:** Kick-off-Workshop Relaunch — „Notizzettel" und „THEMEN" (Docs), Material-/Workshop-Ordner.
- **Technische SEO-Empfehlungen (Audit-Stil):** je Thema ein eigenes kurzes Doc nach **IST -> SOLL**-Schema mit konkreten Beispiel-URLs (Canonical-Tags, Breadcrumb), bzw. **„Weitere Auffälligkeiten Part 1/2"** als nummerierte Befundlisten.
- **On-Page-Empfehlungen:** Title/Meta dynamisch (Doc mit Varianten) + Title/Meta-Tabellen (Sheets) je Verteilerseite.
- **Architektur:** Sitemap-Sheets („Seitentypen und Ressorts", „Sitemap 2020 v20").
- **Paid/Social:** Slides „Social & Google Ads, Influencer"; Preis-/Beratungs-Docs (Facebook-Pages-Merge 2023, Meta-Recruiting-Ads 2025).

Aufbau der Audit-Docs: Kurzer Erklärtext -> **IST** -> **SOLL** -> konkrete Beispiel-URLs -> EOM-Fußzeile (Adresse Hannover/Stuttgart).

## Schreibstil-Notizen

- **Sie-Anrede** durchgängig in der Kunden-Copy.
- **Meta-Description-Muster** der Stadt Langenhagen (aus den Title/Meta-Sheets), als wiederverwendbare Konvention:
  - Häkchen-Aufzählung mit **✓** als Trenner zwischen Nutzenpunkten.
  - Abschluss-CTA mit Pfeil-Emoji: **„⇒ Jetzt informieren!"**, „⇒ Jetzt entdecken!", „⇒ Jetzt mehr erfahren!"; teils themenspezifische Emojis (📞, 🚴, 💡, ▶).
  - Markenname **„Stadt Langenhagen"** und Ortsbezug **„in der Region" / „Region Hannover"** als feste Bausteine.
  - Beispiel (Start): *„Offizielle Anlaufstelle für Informationen der Stadt Langenhagen ✓ Anliegen? Wir helfen gerne weiter ✓ Meldungen, Bürgerservice & mehr ⇒ Jetzt informieren!"*
- **Title-Tag-Muster:** `{Thema/Kategorie} | Stadt Langenhagen` (Marke konsequent rechts, mit Pipe getrennt).
- Begriffskonvention im Vault: **„KI"** statt „AI".

## Offene Punkte / Datenlücken

- **Keine aktuellen SEO-Daten:** Keine Rankings, kein Sichtbarkeitsindex, keine Klick-/Impressions-/CTR-Zahlen (GSC/GA4), keine Keyword-Sheets mit Suchvolumen und keine Backlink-Daten im Ordner. Erfolgs-KPIs werden im Fragebogen erfragt, aber nicht beziffert. **Nicht aus Drive ableitbar — nicht geschätzt.**
- **Umsetzungsstand unbekannt:** Ob die technischen Empfehlungen (Canonicals, Breadcrumb, 404, Weiterleitungen) durch Nolis umgesetzt wurden, geht aus den Dateien nicht hervor.
- **Aktualität:** Kern-SEO-Material ist **2020/2021** — Stand der Website und Befunde können veraltet sein. Eine erneute technische Prüfung der heutigen `langenhagen.de` wäre nötig, um die Befunde zu verifizieren.
- **GEO/KI komplett offen** (siehe oben).
- **Office-Dateien nicht ausgewertet:** `Sitemap 2020 v20.xlsx` und `Sitemap - Seitentypen und Ressorts - 04112020.xlsx` sind `.xlsx` und über die CLI nicht exportierbar — nur per Dateiname als Architektur-/Sitemap-Artefakte erfasst.
- **Jüngste Aktivität** im Ordner ist Paid Social / Recruiting (2023/2025), nicht SEO/GEO — Hinweis darauf, dass der SEO-Schwerpunkt in der Relaunch-Phase lag.

## Quellen

Ausgewertete, Langenhagen-spezifische Dateien aus dem Drive-Kundenordner (Account `ben@eom.de`):

- *langenhagen.de | Empfehlung der dynamischen Meta-Daten* (Google Doc, 19.11.2020) — Title/Meta dynamisch, 2 Varianten.
- *langenhagen.de | Empfehlung der Meta-Daten Verteilerseiten* (Google Sheet, 08.12.2020) — ausformulierte Title/Meta je Verteilerseite.
- *Stadt Langenhagen | SEO | Grundoptimierung zentraler Seiten* (Google Sheet, 09.12.2020) — Title/Meta zentrale Seiten.
- *langenhagen.de | Weitere Auffälligkeiten | Part 1* (Google Doc, 12.01.2021) — Parameter-URLs, verwaiste Seiten, 404, Weiterleitungen.
- *langenhagen.de | Weitere Auffälligkeiten | Part 2* (Google Doc, 15.01.2021) — falsch generierte Breadcrumb.
- *langenhagen.de_ Alternative Empfehlung Canonical-Tags* (Google Doc, 25.01.2021) — Canonical-Logik IST/SOLL.
- *langenhagen.de_ Alternative Empfehlung Breadcrumb-Navigation* (Google Doc, 25.01.2021) — Breadcrumb-Verlinkung IST/SOLL.
- *Fragebogen-Stadt-Langenhagen* (Google Doc, 13.03.2020) — Anforderungen, Plattform Nolis, Tools (GA, GSC), Relaunch-Ziel.

Nur per Dateiname/Metadaten erfasst (nicht exportierbar oder nicht inhaltlich ausgewertet): *Sitemap 2020 v20.xlsx*, *Sitemap - Seitentypen und Ressorts - 04112020.xlsx*, *Checkliste Projektstart, Tools & Zugänge, SEO, SEA* (Sheet), *Social & Google Ads, Influencer | September 2021* (Slides), *Preis-Info: Facebook-Pages zusammenlegen | September 2023* (Doc), *Nachricht an Lorena Recruiting Ads Meta | Januar 2025* (Doc), Kick-off-Workshop-Notizen/THEMEN (04/2020).

---
Verwandte Konzepte: [[SEO-Methodik]] · [[Schreibstil]] · [[Technical]] · [[On-Page & Content]]
