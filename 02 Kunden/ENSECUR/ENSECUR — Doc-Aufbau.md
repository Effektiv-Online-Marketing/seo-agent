---
tags: [kunde, ensecur, doc-aufbau, vorlage]
status: aktiv
quelle: Lokaler ENSECUR-Export (EOM-Empfehlung Copilot-Landingpage inkl. Senior-SEO-Review von Ben), gelesen 19.06.2026
---

# ENSECUR — Doc-Aufbau

Der EOM-Empfehlungs-Doc-Aufbau am ENSECUR-Beispiel beschrieben. Basis: das eine gelesene Original-Doc (Copilot-Datenschutz-Landingpage). Ergänzt [[ENSECUR]] und [[ENSECUR — Schreibstil]]; Methodik-Bezug: [[SEO-Methodik]]; Format-Verwandtschaft: [[NIBE — Doc-Aufbau]] (gleiches 3-Farben-Markup).

> Datenbasis dünn: nur **ein** Doc-Typ belegt (Content-/Landingpage-Empfehlung). Anders als bei NIBE/HERMA sind Technik-Audit-, Reporting- und Strategie-Doc-Typen für ENSECUR **nicht belegt** → hier bewusst nur der belegte Typ dokumentiert.

Allen Docs gemeinsam:
- **Fußzeile fix:** „EOM – Effektiv Online-Marketing GmbH / Bödekerstraße 85 in 30161 Hannover / Registergericht Hannover HRB 204938, Geschäftsführer Ernest Mavriqi."
- Master-Logik **Befund → Begründung → Maßnahme** (Änderungen am Markup begründet, offene Fachpunkte als Rückfrage markiert).
- Kollaboration im Doc; **Senior-SEO-Gegenlese durch Ben** als Kommentar-Thread.

---

## 1) Content-/Landingpage-Empfehlung (der belegte Typ)
Beispiel: *Empfehlung zur Landingpage „Microsoft Copilot und Copilot Chat datenschutzgerecht einführen"*

**Aufbau:**
1. **Titel** — „Empfehlung zur Landingpage „[Thema]"".
2. **`URL Vorschlag:`** — vollständige Ziel-URL (z. B. `https://www.ensecur.de/microsoft-copilot-datenschutz/`).
3. **1. Keywords**
   - **Hauptkeyword** mit **`SV`** (z. B. `microsoft copilot datenschutz` — SV 100).
   - **Nebenkeywords** als Liste, je mit `SV` (z. B. `copilot dsgvo` SV 50, `dsfa copilot` SV 10, `microsoft copilot risiken` SV 10).
4. **2. Metas**
   - **Meta-Titel:** `Thema | ENSECUR` (Brand-Suffix am Ende, ENSECUR groß).
   - **Meta-Beschreibung:** Sie-Anrede, Nutzen + Leistung, **`►`-Glyph**, **Schluss-CTA** („… ► Erstgespräch anfragen").
5. **3. Content** — mit **3-Farben-Legende** oben, dann der Vorschlag mit **inline H1/H2/H3** in Live-Reihenfolge.
6. **Footer** — fixe EOM-Fußzeile.
7. **Senior-SEO-Review-Block** als Kommentar-Thread von Ben (s. u.).

### 3-Farben-Legende (fix, oben im Content-Teil)
```
Content-Anpassungen: Gelb
Neuer Content: Grün
Hinweise: [Knalliges Gelb]
Gelöscht: Durchgestrichen
```
- **[Regieanweisungen in eckigen Klammern]** strikt von Live-Copy trennen, z. B.
  `[CTA: Erstgespräch vereinbaren → https://www.ensecur.de/kontakt/]`.
- Begründungen inline beim Element, z. B. „'365' entfernt, damit die Überschrift sich von der M365-Seite abgrenzt."

### H-Struktur (belegtes Muster für eine Beratungs-/Leistungs-Landingpage)
```
H1: [Leistung] datenschutzgerecht einführen
  → Antwort-Absatz (direkte Antwort auf die Kernfrage) + [CTA]
H2: Wann Unterstützung sinnvoll ist            (Sorgen-/Auslöser-Fragen als Bullets)
H2: Welcher Weg passt zu Ihrem Vorhaben?       → ZWEI-BOX-MUSTER (s. u.)
H2: So unterstützen wir Sie bei …              (Body nicht leer lassen!)
H2: So läuft die Begleitung typischerweise ab
  H3: 1. … H3: 2. … H3: 3. … H3: 4.           (Prozess-Schritte)
H2: Was Sie am Ende in der Hand haben          (Ergebnis-/Deliverable-Liste)
H2: [Branchen-/Sonderfall-Abschnitt]           (z. B. kirchliche Einrichtungen — Sub-Pillar-Kandidat)
H2: Für wen diese Leistung besonders geeignet ist
H2: Was diese Begleitung umfasst – und was nicht
  H3: Enthalten …   H3: Nicht enthalten …      (klare Scope-Abgrenzung)
H2: [Cross-Sell-Anker]                          (2–3 Sätze + Link zur Pillar, kein 2. Produktversprechen)
H2: Warum [Thema] mit ENSECUR                   (Trust/E-E-A-T, USP-Differenzierung)
H2: Interesse an …?                             (Erstgespräch-CTA-Block)
H2: Häufig gestellte Fragen zu …               → FAQ (s. u.)
```

### Zwei-Box-Muster (Didaktik — belegt)
Unter „Welcher Weg passt zu Ihrem Vorhaben?" zwei H3 als kartenartige Boxen mit identischem Innenraster:
```
Box A (H3): [Variante 1 — niedrigschwellig regeln]
  Für wen dieser Weg gedacht ist · Typische Fragen · Typisches Ergebnis · [CTA]
Box B (H3): [Variante 2 — vertieft absichern, z. B. DSFA]
  Für wen dieser Weg gedacht ist · Typische Anwendungsfälle · Typisches Ergebnis · [CTA]
```
Empfehlung (Bens Prio 2): Boxen visuell trennen, **unterschiedliche CTA-Ziele + UTM-Parameter**, damit in Analytics sichtbar wird, welcher Weg Anfragen bringt.

### FAQ (belegt)
- Als **H2 „Häufig gestellte Fragen zu …"** + je Frage ein **H3**.
- **GEO-Regel:** Antwort-Satz zuerst, dann Bulletliste (Listen-Snippet-Kandidaten kennzeichnen).
- Muss die **snippet-relevante Ja/Nein-Frage** enthalten (belegt: „Ist Microsoft Copilot DSGVO-konform?").
- **FAQPage-JSON-LD** ist Pflicht (Tech-Backlog) — sonst Snippet-Potenzial verschenkt.

**Mini-Skelett:**
```
Empfehlung zur Landingpage „[Thema]"
URL Vorschlag: https://www.ensecur.de/...
1. Keywords  → Haupt (KW + SV) / Neben (Liste KW + SV)
2. Metas     → Meta-Titel „… | ENSECUR" / Meta-Beschreibung mit ► + CTA
3. Content   → Legende (Gelb/Grün/[Knalliges Gelb]/Durchgestrichen)
   H1 + Antwort-Absatz → H2-Kette inkl. Zwei-Box → FAQ (H3)
Footer (EOM Hannover, HRB 204938)
— Senior-SEO-Review (Ben): Stark gemacht / Prio 1 / Prio 2 / Prio 3 / Einordnung / Größte Hebel
```

---

## 2) Senior-SEO-Review-Block (wie Ben gegenliest)
Belegter Kommentar-Thread von Ben am Ende des Empfehlungs-Docs. **Prio-Logik:**

1. **„Stark gemacht"** — was schon gut ist (Suchintention klar, Keyword-Mapping inkl. Long-Tail, USP-Differenzierung, H-Hierarchie/Zwei-Box, FAQ inkl. snippet-relevanter Frage). Erst Lob/Bestätigung, dann Kritik.
2. **Prio 1 — schnell, hoher Impact:** sofort umsetzbare On-Page-Hebel.
   - Beispiele aus dem Doc: H1 entschlacken; Title vs. H1 trennen (DSFA rein); **fehlende interne Verlinkung** (mind. 3 Cross-Links: Pillar, DSGVO-Beratungsseite, Rücklink); **E-E-A-T sichtbar** (Autorenkasten, Aktualisierungsdatum); **FAQPage-JSON-LD**.
3. **Prio 2 — mittelfristig:** UX/Struktur/Content-Tiefe.
   - Beispiele: Boxen visuell + UTM trennen; FAQ snippet-fähiger (Antwort zuerst); zu spezifische H2 als eigene Sub-Pillar auslagern; leere H2 mit Body füllen.
4. **Prio 3 — Architektur:** Cluster-/Pillar-Struktur.
   - Beispiele: bei wachsendem Volumen zwei Pillar-Pages + Hub gegen Kannibalisierung; Cross-Sell-H2 nur als Anker (2–3 Sätze + Link); regelmäßiges **PAA-Mining** der FAQ.
5. **„Einordnung"** — Markt/Wettbewerb/Lead-Realismus: SV-Höhe, Long-Tail-Kumulation, Topical-Authority-Logik, realistischer Zeithorizont (6–12 Monate), Wettbewerbsintensität, woher die Differenzierung kommt.
6. **„Größte Hebel"** — 3–4 Punkte als Fazit (hier: H1 entschlacken, fehlende interne Verlinkung, FAQ-Schema, E-E-A-T-Block).

**Prinzip:** Prio nach **Impact × Aufwand** (Prio 1 = schnell + hoher Impact). On-Page vor UX vor Architektur. Jeder Punkt nennt das **Warum** (z. B. „sonst verschenkt ihr Linkjuice und Topical-Authority"). Schema-/Technik-Punkte gehen explizit in den **Tech-Backlog** (EOM/Entwickler).

---

## Quell-Landkarte (ENSECUR)
- **Drive:** Ben wertet Dateien **nur im Ordner „SEO Agent Ben"** aus (nicht in jedem Agency-Ordner). Aktuell **1 Doc** dort → Datenbasis dünn.
- **Belegter Doc-Typ:** Content-/Landingpage-Empfehlung (1) mit Senior-SEO-Review (2).
- **Nicht belegt** (anders als NIBE/HERMA): Technik-/Crawl-Auswertung, Reporting, Strategie-/GEO-Schulungs-Doc → erst bei breiterer Datenbasis ergänzen.
</content>
