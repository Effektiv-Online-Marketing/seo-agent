---
name: eom-onpage-empfehlung
description: Erstellt EOM-OnPage-Empfehlungen als abgabefähiges, gebrandetes Google Doc (EOM-Vorlage, Montserrat) plus lokale Vault-Notiz. Eine OnPage-Empfehlung ist eine copy-paste-fertige Seitenempfehlung (Title/Meta + ausformulierter Content), kein reines Audit. Nutze diesen Skill bei Anfragen wie "mach eine OnPage-Empfehlung", "Empfehlung zu /<seite>", "optimiere die Seite <URL>", "mach ein Beispiel für <URL>", "Title und Content für <URL>", "OnPage für <Kunde>" oder wenn jemand Kunde + URL nennt und eine Seitenoptimierung will.
---

# EOM — OnPage-Empfehlung

Du erstellst eine **EOM-OnPage-Empfehlung** im verbindlichen Standardablauf. Ziel-Output ist immer:
- **gebrandetes Google Doc** (EOM-Vorlage, Montserrat) als abgabefähige Seitenempfehlung
- **lokale Vault-Notiz**

Eine OnPage-Empfehlung ist eine **fertige, copy-paste-fähige Seitenempfehlung** (Befund -> Begründung -> Maßnahme steckt implizit drin: die Empfehlung *ist* die Maßnahme), kein Audit-Bericht.

Arbeite autonom. Stoppe nur, wenn ein Pflichtinput fehlt, der Kunden-Scope unklar ist oder die Ziel-URL nicht erreichbar ist.

## Zuerst laden (Pflicht)
- `CLAUDE.md`
- `00 Kontext/SEO-Methodik.md`
- `00 Kontext/Schreibstil.md`
- `04 Ressourcen/Audit-Vorlagen/OnPage-Empfehlung Vorlage.md` (Master-Schema + Doc-Link)
- `02 Kunden/<Kunde>/<Kunde>.md`

Falls vorhanden zusätzlich:
- `02 Kunden/<Kunde>/<Kunde> — Schreibstil.md`
- kundenspezifischer Title/Meta-Skill (z. B. `hannoversche-title-meta`, `nibe-title-meta`), wenn der Kunde eigene Konventionen hat.

## Pflichtinput
Wenn nicht klar im Prompt enthalten, hole ein:
- `Kunde`
- `Ziel-URL`
- `Ziel-Keyword` (wenn nicht genannt: aus URL/Seite ableiten und bestätigen)

## Datenquellen: lesen vs. schreiben (KRITISCH)
- **Schreiben IMMER als `ben@eom.de`** über die gws-CLI in den **zentralen Basis-Shared-Drive** `1wIAbiC48F_VD4Bnf5n_5mGhrUDJhMnpT`.
- Der Kundenordner **„1 - Kunden" (`1G37IASKRJceHM2fmcRHq9uMpzFJc1Oe-`, ozan/ernest) ist NUR Infoquelle**: dort lesen/Beispiele ziehen, **nie hineinschreiben** oder Ordner/Dateien anlegen.
- Die MCP-Drive-Tools (`mcp__claude_ai_Google_Drive__*`) laufen als `ozan` und werden **nur zum Lesen/Suchen** genutzt, nie zum Erstellen. Siehe Memory `feedback-drive-ben`.

## Live-Seite erfassen (Pflicht, nichts erfinden)
Ziel-URL mit `WebFetch` ziehen und erfassen:
- Ist-`title` und Ist-`meta description` (soweit erkennbar)
- H1, alle H2/H3 in Reihenfolge
- USPs/Vorteile, Tarif-/Leistungsbausteine, harte Fakten (Zahlen, Alter, Fristen, Summen)
- vorhandene CTAs/Buttons

Inhalte und Fakten der Empfehlung **aus der Live-Seite ableiten**. Keine Zahlen/Leistungen erfinden. Optional zur Schärfung der Suchintention Top-10-SERP/semantische Begriffe heranziehen (z. B. `mcp__dataforseo__serp_organic_live_advanced`), wenn verfügbar.

## Tooling & Ausführung (Pflicht)
- Jeder gws-Aufruf mit Prefix: `GOOGLE_WORKSPACE_CLI_CONFIG_DIR="$HOME/Desktop/brain/.gws"`.
- Account prüfen: `gws drive about get --params '{"fields":"user(emailAddress)"}'` → muss `ben@eom.de` sein.
- Bei allen Drive-Calls `"supportsAllDrives":true` mitgeben.
- **`--params` (Query) vs. `--json` (Body) trennen** (sonst landet die Datei als „Untitled" im Root):
  - `drive files create` (Ordner): `--params '{"supportsAllDrives":true,"fields":"id"}'` + `--json '{"name":"…","mimeType":"application/vnd.google-apps.folder","parents":["<PARENT>"]}'`.
  - `drive files copy`: `--params '{"fileId":"<VORLAGE>","supportsAllDrives":true,"fields":"id,owners(emailAddress)"}'` + `--json '{"name":"<Dateiname>","parents":["<ZIELORDNER>"]}'`.
  - `docs documents batchUpdate`: ID in `--params`, `{"requests":[…]}` in `--json`.
- **Nach jedem `copy`/`create` verifizieren** (`gws drive files get`, `fields:"name,parents,owners(emailAddress)"`): richtiger Name, richtiger Ordner, im Shared Drive ist `owner=None` ok (nicht ozan).

**Vorlagen-IDs:**
- EOM-Doc-Vorlage: `1IKD7nruTswvy3-AD8Uk63RpmkPIglgXCs2dE7o6CGqM` (Branding + Montserrat in allen Named Styles).
- Referenz-OnPage-Vorlage (befüllt, als Muster): `1ghZDhaX7kDEv4ogqEV3OLKOC2DYr89Om6i3_PeDa26w`.

**Drive-Ablage:** Basis-Shared-Drive `1wIAbiC48F…` → Kundenordner (suchen oder per `gws drive files create` anlegen) → Gewerk-Unterordner `On-Page` (anlegen, falls fehlt).

## Workflow (in dieser Reihenfolge)
1. **Scope bestätigen** — Kunde, Ziel-URL, Ziel-Keyword, Markt/Land, kundenspezifische Einschränkungen.
2. **Infos lesen** — Live-Seite (WebFetch). Optional: bestehende OnPage-Beispiele des Kunden in „1 - Kunden" (read-only) für Stil/Benennung ansehen.
3. **Ablage vorbereiten** — im Basis-Shared-Drive Kundenordner + `On-Page` suchen/anlegen.
4. **Doc anlegen** — EOM-Doc-Vorlage per `gws drive files copy` in den `On-Page`-Ordner kopieren. Dateiname: `<Kunde> | Empfehlung zu /<seite>`.
5. **Inhalt einfügen** — per `gws docs documents batchUpdate` (Struktur + Formatierung siehe unten).
6. **Lokale Vault-Notiz** — `02 Kunden/<Kunde>/<Kunde> — Empfehlung zu <seite>.md` anlegen.
7. **Output liefern** — Doc-Link, lokaler md-Pfad, kurzer Ergebnisblock.

## Doc-Aufbau (verbindliche Struktur)
**Kopf**
- Aktuelle URL (+ ggf. URL nach Relaunch)
- Ziel-Keyword
- Platzierung / Navigation (wo sitzt die Seite)
- Interne Verlinkung (von welchen Seiten CTA-/Textlinks hierher)
- Hinweis Ist-Title (Status quo)

**1. Metas**
- `Meta-Titel:` Keyword-Varianten vorne + Brand hinten (~ max 60 Zeichen)
- `Meta-Beschreibung:` Nutzen + USP/Trust-Haken (✓) + CTA (►), ~ max 155 Zeichen

**2. Content** (ausformulierte Copy, nicht nur Stichpunkte)
- `<h1>` Hauptüberschrift mit Ziel-Keyword + Subline
- Einleitungsabsatz mit Keyword + `[Verlinkung zu …]`
- `[Bild]`-Platzhalter mit Alt-Text-Hinweis
- mehrere `<h2>`-Blöcke (nach Suchintention/PAA): Subline -> `[Bild]` -> Fließtext (semantische Begriffe) -> CTA
- Conversion-Blöcke am Ende mit konkretem `CTA-Button: <Text> [Link: …]`
- FAQ-Block (`<h2>`) mit Empfehlung FAQPage-Schema

## Formatierung (Pflicht)
- Titel/Überschriften per `namedStyleType` (`TITLE` / `HEADING_1` / `HEADING_2`) — dann stimmen Montserrat-Gewicht + Größe (26/16/14) automatisch.
- **Im Doc bleiben Titel + Überschriften SCHWARZ** (kein dunkler Hintergrund dahinter). Nicht weiß setzen.
- Fließtext explizit auf **Montserrat, Größe 12 PT** (`weightedFontFamily` + `fontSize`) — Vorlagen-Default ist 11/Light.
- **Meta-Labels (`Meta-Titel:`, `Meta-Beschreibung:`) fett.**
- **Abstände wie im Muster:** zwischen den Blöcken Leerzeilen (leere Absätze) einfügen.
- Index-Mathematik sauber: Volltext **einmal** per `insertText` (Index 1) einfügen, dann Style-Requests auf berechnete Ranges. Empfohlen: Requests mit kleinem Python-Helper bauen (Liste aus `(text, style)` -> kumulative Start-Indizes -> `updateParagraphStyle`/`updateTextStyle`), per `--json "$(cat …)"` an `batchUpdate`.

## Lokale Vault-Notiz (Pflicht)
Pfad: `02 Kunden/<Kunde>/<Kunde> — Empfehlung zu <seite>.md`. Mindestinhalt:
- Frontmatter (`tags`, `status`, `erstellt`, `kunde`, `url`, `keyword`)
- `Google Doc (Deliverable)`-Link + Ablagepfad (Basis-Shared-Drive)
- `Kopf`, `1. Metas`, `2. Content (Struktur)`
- `Verifizierte Fakten (Live-Seite)` mit Quelle + Datum
- Verweis `[[OnPage-Empfehlung Vorlage]]`

## Schreib- und Datenregeln
- Sie-Anrede in der Kundenkopie.
- **„KI" statt „AI"**, kundenspezifische Title/Meta-Konventionen beachten.
- **Keine Gedankenstriche (—)** in Texten (Ozans Stil).
- **Keine erfundenen Fakten/Zahlen** — alles aus der Live-Seite oder belegten Live-Quellen.
- Fehlende Infos offen benennen statt erfinden.

## Output am Ende
- Link zum **Google Doc**
- Pfad zur **lokalen Vault-Notiz**
- kurzer Ergebnisblock: Ziel-URL, Ziel-Keyword, Meta-Titel-Empfehlung, wichtigste Content-Maßnahme, Quelle + Datum

## Nicht tun
- Nie in „1 - Kunden" (ozan) schreiben oder dort Ordner/Dateien anlegen — nur lesen.
- Nie über den MCP-Drive-Connector erstellen — immer gws als `ben@eom.de`.
- Kein leeres Doc anlegen — immer die EOM-Vorlage kopieren.
- Doc nie ohne Named Styles, Montserrat-12-Fließtext und Block-Abstände abgeben.
- Keine OnPage-Empfehlung ohne lokale `.md`-Fassung abschließen.
- Keine Fakten/Zahlen schätzen, die nicht auf der Seite stehen.
