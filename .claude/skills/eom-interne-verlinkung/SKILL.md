---
name: eom-interne-verlinkung
description: Erstellt EOM-Deliverables für interne Verlinkungen (neue Ratgeber/Seiten aus Bestandsseiten verlinken) im verbindlichen Vorlagen-Format mit echter Orange/Grün/Gelb-Markierung via Google-Docs-API (niemals Inline-HTML/CSS), vollen Quell-URLs und live-belegten Passagen. Nutze diesen Skill bei Anfragen wie "interne Verlinkung", "Verlinkungsvorschläge", "intern verlinken", "neue Seite aus Bestandsseiten verlinken", "Linkempfehlungen", "Anker setzen", "wo soll ich auf den neuen Ratgeber verlinken", "Textanpassungen für interne Links".
---

# EOM — Interne Verlinkung (Linkempfehlungen für neue Seiten)

Du baust ein **internes-Verlinkungs-Deliverable**: aus welchen Bestandsseiten auf eine oder mehrere neue (oft noch nicht online stehende) Zielseiten verlinkt werden soll — inkl. Quell-URL, exaktem Abschnitt, Bestandstext-Zitat und fertig formuliertem Einbau-Satz mit sprechendem Ankertext.

Output ist immer:
- **ein Google Doc im EOM-Vorlagen-Format** (gebrandet, Montserrat, echte Farb-Markierung)
- **eine lokale Vault-Notiz**

## Zuerst laden
- `CLAUDE.md`, `00 Kontext/Schreibstil.md`, `00 Kontext/SEO-Methodik.md`
- `02 Kunden/<Kunde>/<Kunde>.md` (Scope, Schreibstil, CMS-Modell)

## HARTE REGELN (aus Kundenfeedback — diese Fehler dürfen NIE wieder passieren)

1. **Entitäten nicht gleichsetzen.** Prüfe, ob Begriffe wirklich dasselbe Thema sind. Beispiel-Fehler: **Wohnwagen (= Anhänger) ≠ Wohnmobil (= selbstfahrend)** — andere Zielgruppe. Niemals von einer thematisch *ähnlichen, aber anderen* Seite verlinken. Prüfe zuerst, ob der Kunde überhaupt passenden Bestandscontent hat; wenn nicht, sind die Empfehlungen **neuer Content**.
2. **Immer die volle Quell-URL** ausgeben (`https://www.…/pfad`), nie nur einen H2-Hinweis.
3. **KEIN Inline-HTML/CSS im Doc.** Keine `<span style=…>`, kein `<a href=…>`, keine `background-color`-Strings als Text. Farben werden ausschließlich als **echte `backgroundColor` über die Docs-API** gesetzt → via `scripts/doc_builder.py`.
4. **Farb-Legende (Vorlagen-Standard):** Anpassung am Bestand = **orange**, neuer Content = **grün**, Ankertext = **gelb**. Legende oben ins Doc, Farbwörter selbst eingefärbt.
5. **Datenbeleg pflicht.** Jede Quellseite + jeder zitierte Abschnitt stammt aus Live-Abruf (Sitemap + Seitenfetch). Nichts erfinden — kein erfundenes Zitat, kein erfundener Abschnitt.
6. **Interne Briefings = nur das Ergebnis.** Keine ausschweifenden Erklärungen, keine Wiederholungen. Kompakt, belegt, abgabefertig.
7. **Ankertext** sprechend, keyword-tragend, variierend, Sie-Anrede. „KI" statt „AI".
8. **Bereits geplante Links nicht doppeln** (z. B. Produktseite→Ratgeber, Querverlinkung der neuen Seiten untereinander) — explizit ausnehmen.

## Vorlagen-Format (Gold-Standard, Referenz-Doc `17FQpzaxZFlZXFxWrSl2LuD1EcYZB3Ur-OLjiScWAOgs`)
1. **Titel:** `<Kunde> | Empfehlung interne Verlinkungen – <Thema>`
2. **Intro:** kurz, was folgt (Bestandsseiten + konkreter Abschnitt je Empfehlung).
3. **Farb-Legende** (orange/grün/gelb als eingefärbte Wörter).
4. **Hinweis zur Datenbasis** (Entitäten-Klärung, ob Bestandscontent existiert, Quellen + Datum + Analyst, was bereits separat geplant ist).
5. **Annahme zu Ziel-URLs**, falls Zielseiten noch offline (Platzhalter, 1× anpassbar).
6. **Pro Empfehlung (H2):** `Quell-URL:` (voll) · `Abschnitt:` (zitierte H2) · `Bestehender Text (Auszug):` (echtes Zitat) · `Empfehlung (neuer Content / Anpassung am Bestand):` Einbau-Satz mit grün/orange + gelbem Ankertext.

## Konnektoren (geprüft — so läuft es am besten)
- **Drive/Docs:** **gws-CLI als `ben@eom.de`** (nicht MCP-Connector — der sieht EOM-Vorlagen oft nicht). Prefix: `GOOGLE_WORKSPACE_CLI_CONFIG_DIR="$HOME/Desktop/brain/.gws"`. `--params` = Query, `--json` = Body strikt trennen. Nach `copy`/`create` per `gws drive files get` verifizieren.
- **Live-Seiten/Sitemap:** `curl` (Sitemap, robots) + `WebFetch` (H2-Struktur + wörtliche Passagen). Kein Schätzen.
- **Optional Daten:** Sistrix-MCP für SV/Relevanz der Quell-/Zielthemen, wenn Priorisierung nötig.
- **Rendering:** `scripts/doc_builder.py` (Python) — Modell als **Python-Daten mit Single-Quote-Delimitern** bauen (vermeidet das JSON-Quote-Escaping-Problem mit „ ", das früher das Doc zerschoss), `build(blocks)` → `{"requests":[…]}` → `gws docs documents batchUpdate`.

## Workflow
1. **Scope:** Kunde, Zielseite(n)/neue Ratgeber, Markt, bereits geplante Links (ausnehmen). Entitäten klären (Regel 1).
2. **Bestand erheben (live):** `https://www.<domain>/sitemap.xml` ziehen → relevante Bestandsseiten filtern. Je Top-Quelle `WebFetch`: H2-Liste + wörtliches Zitat des passendsten Abschnitts.
3. **Mapping:** je Zielseite 1–3 starke, *defensible* Quellseiten. Jede Quell-Sektion nur einmal belegen. Typ je Insert bestimmen: neuer Absatz (grün) oder Anpassung vorhandenen Satzes (orange); Ankertext (gelb).
4. **Doc bauen:**
   - EOM-Vorlage kopieren: `gws drive files copy` (Vorlage-ID `1IKD7nruTswvy3-AD8Uk63RpmkPIglgXCs2dE7o6CGqM`) in Kunden→`On-Page`-Ordner. Dateiname `<Kunde> — Empfehlung interne Verlinkung <Thema>`. Verifizieren.
   - Modell als Python-Bloecke (siehe `scripts/doc_builder.py`-Doc), `build()` → reqs.json → `gws docs documents batchUpdate`.
5. **Verifizieren (Pflicht-Gate):**
   - Text-Export `grep -cE '<span|<a href|background-color|style='` → **muss 0** sein.
   - `gws docs documents get` Hintergrund-Runs zählen (`grep -c rgbColor`) → > 0 (Farben echt gesetzt).
6. **Vault-Notiz:** `02 Kunden/<Kunde>/<Kunde> — Interne Verlinkung <Thema>.md` (Doc-Link, Ablagepfad, Empfehlungstabelle mit vollen URLs, Befunde, offene Punkte, Quellen+Datum+Analyst).

## Output am Ende (intern = nur Ergebnis)
- Doc-Link
- Pfad zur Vault-Notiz
- Kompakte Empfehlungstabelle: Quell-URL · Abschnitt · Ziel · Typ (grün/orange) · Ankertext
- Quelle + Datum + Analyst

## Nicht tun
- Kein Inline-HTML/CSS, keine Tabellen-Hacks, keine `<span>`-Strings.
- Keine Wohnmobil-/themenfremden Quellen für Wohnwagen-/Anhänger-Themen (Entitäten-Fehler).
- Keine erfundenen Zitate/Abschnitte/URLs.
- Keine ausschweifenden Erklärtexte bei internen Briefings.
- Doc nicht über MCP-Connector erzwingen, wenn Vorlage fehlt — gws-CLI als ben.
- Deliverable nicht ohne lokale `.md`-Fassung abschließen.
