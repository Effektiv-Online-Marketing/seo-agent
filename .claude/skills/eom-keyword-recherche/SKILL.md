---
name: eom-keyword-recherche
description: Erstellt EOM-Keyword-Recherchen im verbindlichen Standardablauf mit Live-Sistrix-Daten, gebrandetem Google Sheet, Google-Doc-Zusammenfassung und lokaler Vault-Notiz. Nutze diesen Skill immer bei Anfragen wie "mach eine KWR", "mach eine Keyword-Recherche", "Keyword Recherche für", "Seed-Keyword", "Keyword-Cluster", "mach das ins Sheet", "such mir Keywords", "Themenrecherche", "baue mir eine KWR", "mach eine SEO-Recherche" oder wenn ein Nutzer Kunde, Domain und Keyword nennt, auch wenn Vorlage, Drive oder Sistrix nicht ausdrücklich erwähnt werden.
---

# EOM — Keyword-Recherche

Du erstellst eine **EOM-Keyword-Recherche** im verbindlichen Standardablauf. Ziel ist immer derselbe Output-Typ:
- **gebrandeter Google Sheet**
- **Google-Doc-Zusammenfassung**
- **lokale Vault-Notiz**

Arbeite standardmäßig autonom. Stoppe nur, wenn ein Pflichtinput fehlt, der Kunden-Scope unklar ist oder **kein Live-Sistrix-Zugriff** möglich ist.

## Zuerst laden (Pflicht)
Lies vor jeder KWR mindestens diese Dateien:
- `CLAUDE.md`
- `00 Kontext/SEO-Methodik.md`
- `00 Kontext/Schreibstil.md`
- `04 Ressourcen/Keyword-Recherche/Keyword-Recherche.md`
- `04 Ressourcen/EOM-Standards/Doc-Sheet-Slide-Aufbau.md`
- `02 Kunden/<Kunde>/<Kunde>.md`

Falls vorhanden, zusätzlich laden:
- `02 Kunden/<Kunde>/<Kunde> — Doc-Aufbau.md`
- `02 Kunden/<Kunde>/<Kunde> — Schreibstil.md`

## Pflichtinput
Wenn nicht schon klar im Prompt enthalten, hole genau diese drei Angaben ein:
- `Kunde`
- `Domain`
- `Seed-Keyword`

## Hartes Gate: Sistrix
**Ohne Live-Sistrix keine KWR.**

Das bedeutet:
- Prüfe zu Beginn, ob **echter Live-Zugriff auf Sistrix** möglich ist.
- Nutze vorhandene Drive-Dokumente, alte KWRs oder lokale Notizen **nicht** als Ersatz für die Datenerhebung.
- Wenn Sistrix nicht live erreichbar ist, **sofort stoppen** und klar sagen, dass die KWR ohne echte Sistrix-Daten nicht erstellt wird.
- Keine Fallback-Quelle für SV, CPC, Competition oder Rankings verwenden, wenn der Sistrix-Schritt blockiert ist.

## Tooling & Ausführung (Pflicht)
Alle Drive-Deliverables laufen über die **gws-CLI als `ben@eom.de`**, nicht über den MCP-Drive-Connector (der sieht die EOM-Vorlagen oft nicht).
- Jeder gws-Aufruf mit Prefix: `GOOGLE_WORKSPACE_CLI_CONFIG_DIR="$HOME/Desktop/brain/.gws"`.
- Account prüfen: `gws drive about get --params '{"fields":"user(emailAddress)"}'` → muss `ben@eom.de` sein.
- Vorlagen kopieren: `gws drive files copy`. Inhalt setzen: `gws sheets ... values update` / `... batchUpdate` und `gws docs documents batchUpdate`.
- Bei allen Drive-Calls `"supportsAllDrives":true` mitgeben.
- **KRITISCH — `--params` vs. `--json` trennen:** Die gws-CLI trennt **Query-Parameter** (`--params`) vom **Request-Body** (`--json`). Body-Felder gehören IMMER in `--json`, sonst werden sie still ignoriert (Datei landet als „Kopie von …"/„Untitled" im Drive-Root):
  - `drive files create` (Ordner): `--params '{"supportsAllDrives":true,"fields":"id"}'` + `--json '{"name":"…","mimeType":"application/vnd.google-apps.folder","parents":["<PARENT>"]}'`.
  - `drive files copy`: `--params '{"fileId":"<VORLAGE>","supportsAllDrives":true,"fields":"id"}'` + `--json '{"name":"<Dateiname>","parents":["<ZIELORDNER>"]}'`.
  - `drive files update` (umbenennen/verschieben): `--params '{"fileId":"…","addParents":"<NEU>","removeParents":"<ALT>","supportsAllDrives":true}'` + `--json '{"name":"…"}'`.
  - `sheets values update`: `--params '{"spreadsheetId":"…","range":"…","valueInputOption":"RAW"}'` + `--json '{"range":"…","majorDimension":"ROWS","values":[…]}'`.
  - `sheets/docs batchUpdate`: ID in `--params`, `{"requests":[…]}` in `--json`.
- **Nach jedem `copy`/`create` verifizieren:** `gws drive files get` mit `fields:"name,mimeType,parents"` → Name korrekt? Liegt es im richtigen Ordner (nicht im Root `0A…`)? Erst dann weiterarbeiten.

**Vorlagen-IDs:**
- KWR-Sheet: `1NPggycrxyBidt2n1dcSgeEhEmGJPJ81JADru1SjpoNw` (Tab `Vorlage`, sheetId `1081565111`, 4 eingefrorene Kopfzeilen).
- EOM-Doc: `1IKD7nruTswvy3-AD8Uk63RpmkPIglgXCs2dE7o6CGqM` (Branding + Montserrat in allen Named Styles).

**Drive-Ablage:** Zentraler Basisordner `1wIAbiC48F_VD4Bnf5n_5mGhrUDJhMnpT` → Kundenordner (suchen oder anlegen) → Gewerk-Unterordner `On-Page` (für KWR). Beide bei Bedarf per `gws drive files create` (mimeType `application/vnd.google-apps.folder`) anlegen.

## Workflow (in dieser Reihenfolge)
1. **Scope bestätigen**
   - Kunde, Domain, Seed-Keyword, Markt/Land und kundenspezifische Einschränkungen prüfen.
   - Beispiel NIBE: nur `/de-de`, nur DE-Daten.

2. **Live-Sistrix-Daten ziehen**
   - Seed-Keyword prüfen (`mcp__sistrix__keyword_seo_metrics`).
   - Pre-Check: rankt die Domain bereits? Pro Cluster-Keyword `mcp__sistrix__keyword_seo` mit `domain=<Domain>` → echte Position der Domain je Keyword.
   - Top-Ranker je Keyword: `mcp__sistrix__keyword_seo` mit `limit=1` → Platz-1-Domain.
   - Für jedes Keyword: `SV` (= Sistrix-Traffic-Schätzung), `Competition`, `CPC`, `Intent`, `Funnel`, eigenes Ranking, Top-Ranker.
   - Nichts schätzen: Werte unter Messschwelle als `k.A.`, nicht abgefragte Rankings als `n. erhoben` markieren.

   **2a — Fragen- & Long-Tail-Ernte (Pflicht, erweitert den Keyword-Satz):**
   - Den Seed nicht nur in offensichtliche Cluster zerlegen, sondern echte Suchphrasen nachziehen: `mcp__sistrix__domain_ideas` (Keyword-Ideen zur Domain) und je Top-Keyword `mcp__sistrix__keyword_seo_serpfeatures` für PAA-/SERP-Feature-Signale.
   - Gezielt Fragen- und Long-Tail-Varianten aufnehmen (Was/Wie/Warum/Kosten/Unterschied/Vergleich), **sofern sie eine echte Sistrix-Messung haben**. Ohne Live-Wert → nicht in die KWR.
   - Diese Treffer durchlaufen dieselbe Metrik-Erhebung (SV, Competition, Intent, Ranking, Top-Ranker) wie die Seed-Cluster. Long-Tail mit klarer Informations-/Fragenintention für die Content-Empfehlung markieren.

   **2b — Competitor-Gap (Pflicht, findet fehlende Keywords):**
   - Wettbewerber bestimmen: `mcp__sistrix__domain_competitors_seo` für die Kundendomain.
   - Keyword-Lücken aufdecken: `mcp__sistrix__domain_opportunities` / `mcp__sistrix__domain_ideas` → relevante Keywords, für die Wettbewerber ranken und die Kundendomain (noch) nicht.
   - Nur Gaps mit echtem Live-SV und thematischer Passung zum Scope aufnehmen. Gap-Keywords im Sheet klar kennzeichnen (eigener Block am Ende oder Klartext-Hinweis „Gap vs. <Wettbewerber>" im Keyword-Eintrag).

3. **Vorhandene Drive-Artefakte suchen**
   - Prüfe, ob es zum Thema bereits KWRs, Docs oder Sheets im Kundenordner gibt.
   - Nutze diese nur für **Benennung, Ablage und historischen Kontext**, nicht als Ersatz für die Live-Daten.

4. **Gebrandeten Sheet anlegen**
   - KWR-Vorlage (ID oben) per `gws drive files copy` in den `On-Page`-Unterordner kopieren. Dateiname: `<Kunde> | KWR – <Thema>`.
   - **Rows 1-3 leer lassen, Header beginnt immer in Zeile 4** (Tab `Vorlage`, Daten ab Zeile 5). Keine Meta-Zeilen oberhalb des Headers.
   - Standardspalten (A-H): `Keyword`, `SV`, `Competition (0-100)`, `CPC (€)`, `Intent`, `Funnel-Stufe`, `<Kunde> Ranking`, `Top-Ranker`.
   - Werte per `gws sheets spreadsheets values update` (Range `Vorlage!A4:H<n>`, `valueInputOption:RAW`) schreiben.
   - Formatierung per `gws sheets spreadsheets batchUpdate`:
     - `repeatCell` → **Montserrat** über den ganzen Tabellenbereich, Header-Zeile zusätzlich `bold`.
     - **Header-Zeile (Zeile 4) IMMER weißer Text** (`foregroundColor` rgb 1/1/1): Die Vorlage hat in Zeile 4 einen dunkelblauen EOM-Hintergrund (rgb ~0,01/0,18/0,51); schwarzer Default-Text ist darauf unlesbar. Pflicht bei jeder KWR.
     - `updateCells` → **Notiz an die `SV`-Header-Zelle**: „SV = Sistrix Traffic-Schätzung (Klicks/Mon., mobil-gewichtet), kein klassisches Suchvolumen; k.A. = unter Messschwelle."
     - `autoResizeDimensions` für die Spalten A-H.
   - Sortierung empfohlen: Ziel-Keywords nach SV absteigend, dann Grenz-/Nicht-Ziel-Keywords (z. B. Shop-Intent) klar gekennzeichnet ans Ende.

5. **Google-Doc-Zusammenfassung anlegen oder aktualisieren**
   - **EOM-Doc-Vorlage (ID oben) per `gws drive files copy`** in den `On-Page`-Unterordner kopieren (nie leer anlegen). Dateiname: `<Kunde> — Keyword-Recherche <Thema>`.
   - Inhalt per `gws docs documents batchUpdate` einfügen. Aufbau nach EOM-Methodik:
     1. `Key Takeaways`
     2. `Phase 0: Pre-Check`
     3. `SERP-Analyse`
     4. `Keyword-Cluster & Suchvolumen`
     5. `Wettbewerber-Analyse / Content-Benchmark`
     6. `Keyword-Kategorisierung`
     7. `Content-Empfehlung` (jeder Punkt als **Befund → Begründung → Maßnahme**)
     8. `Datenquellen & Methodik`
   - **Formatierung (Pflicht):**
     - Titel/Überschriften per `namedStyleType` (`TITLE` / `HEADING_1` / `HEADING_2`).
     - **Im DOC bleiben Titel + Überschriften SCHWARZ** (`foregroundColor` rgb 0/0/0). Nicht weiß setzen — im Doc steht hinter den Überschriften kein dunkler Hintergrund. (Nur im SHEET wird die Header-Zeile weiß, siehe Schritt 4.)
     - Fließtext explizit auf **Montserrat, Größe 12 PT** (`weightedFontFamily` + `fontSize`), da der NORMAL-Default der Vorlage 11/Light ist.
     - **Kernbefunde fett + gelb markieren** (`updateTextStyle` mit `bold:true` + `backgroundColor` Gelb, z. B. rgb 1/0.95/0.4): Quick-Wins, Wettbewerbsbefunde, wichtigste Rankings, Nicht-Ziel-Keywords.
     - In `Content-Empfehlung` die Einleitung **`Maßnahme:` fett** setzen.
   - Index-Mathematik sauber halten: Volltext **einmal** per `insertText` einfügen, danach Style-Requests auf die berechneten Ranges anwenden.
   - Immer mit **Quelle + Datum + Analyst** arbeiten.

6. **Lokale Vault-Notiz anlegen**
   - Pfad:
     - `02 Kunden/<Kunde>/<Kunde> — KWR <Thema>.md`
   - Mindestinhalt:
     - `Kontext`
     - `Drive-Deliverables` (Sheet-Link **und** Doc-Link + Ablagepfad)
     - `Live-Daten & Rankings` (kompakte Tabelle: Keyword, SV, Competition, eigenes Ranking, Top-Ranker; Quick-Wins + Wettbewerbsbefund hervorheben)
     - `Kernerkenntnisse`
     - `Datenlage / Einschränkung` (Quelle, Datum, SV-Hinweis, was als `k.A.`/`n. erhoben` markiert ist)
   - Keine alten „keine Live-Metrikquelle"-Hinweise stehen lassen, wenn live erhoben wurde.

## KWR-Logik
- **Analyse-Logik immer:** Befund -> Begründung -> Maßnahme.
- **Kernschritte der Recherche:**
  - Pre-Check: rankt die Domain fürs Seed-Keyword?
  - SERP-Analyse: PAA, SERP-Features, Top-Ranker, Intent-Mix
  - Keyword-Cluster + Suchvolumen
  - Fragen-/Long-Tail-Ernte (echte Sistrix-Treffer, kein Raten)
  - Competitor-Gap: Keywords, für die Wettbewerber ranken und die Domain nicht
  - BOFU / MOFU / TOFU
  - erste Content-/Seitenempfehlung

## Schreib- und Datenregeln
- Sie-Anrede in der Kundenkopie.
- **„KI" statt „AI"**.
- **Keine erfundenen Zahlen.**
- SV, CPC, Competition, Rankings und Wettbewerber nur aus Live-Sistrix oder daraus ableitbaren, sauber belegten Live-Befunden.
- **`SV` ist die Sistrix-Traffic-/Klick-Schätzung pro Monat (mobil-gewichtet), kein klassisches Google-Suchvolumen** — im Sheet (SV-Header-Notiz), Doc und Notiz so kennzeichnen.
- Fehlende Daten offen benennen: `k.A.` für Werte unter der Sistrix-Messschwelle, `n. erhoben` für nicht abgefragte Rankings. Keine Platzhalter erfinden.
- Immer **Quelle, Erhebungsdatum und Analyst** nennen.

## Drive- und Benennungslogik
- Kundenordner im zentralen Drive suchen oder anlegen.
- Passenden Gewerk-Unterordner nutzen, wenn die Kundenlogik bereits einen hat.
- Falls kein klarer KWR-Unterordner existiert, einen sinnvollen bestehenden SEO-/Strategie-Kontext nutzen statt willkürlich abzulegen.
- Lokale Vault-Notiz bleibt Pflicht, auch wenn Drive-Deliverables erstellt wurden.

## Output am Ende
Liefere dem Nutzer immer:
- den Link zum **gebrandeten Sheet**
- den Link zum **Google Doc**
- den Pfad zur **lokalen Vault-Notiz**
- einen kurzen Ergebnisblock mit:
  - Seed-Keyword
  - wichtigste Erkenntnis
  - Datenquelle
  - Datum
  - Analyst

## Nicht tun
- Kein Ahrefs-, DataForSEO- oder Drive-Fallback, wenn Sistrix live fehlt.
- Keine Tabellenüberschrift in Zeile 1.
- Keine Zusatzzeilen zwischen leerem Kopfbereich und Header, wenn die Vorlage oben Platz für Branding braucht.
- Keine KWR nur im Sheet abliefern.
- Keine KWR ohne lokale `.md`-Fassung im Vault abschließen.
- **Nie eine halbe KWR (z. B. nur Cluster ohne Live-Zahlen) als reine `.md` ablegen** — bei fehlendem Live-Sistrix stattdessen sofort stoppen und das offen sagen.
- **Output ist immer dreiteilig: gebrandeter Sheet + formatiertes Doc (mit Markierungen) + Vault-Notiz.** Ein Teil fehlt = KWR nicht fertig.
- Doc nie ohne Named Styles, Montserrat-12-Fließtext und gelb/fett markierte Kernbefunde abgeben.
- Drive-Deliverables nie über den MCP-Connector erzwingen, wenn die Vorlage fehlt — gws-CLI als `ben@eom.de` nutzen.
