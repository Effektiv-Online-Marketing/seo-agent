---
tags: [onpage, interne-verlinkung, vhv]
status: final
erstellt: 2026-06-22
kunde: VHV Versicherung
analyst: Ben (EOM)
---

# VHV — Interne Verlinkung Wohnwagen-Ratgeber (Führerschein, TÜV, Gewicht)

**Google Doc (Deliverable):** https://docs.google.com/document/d/10Jsza_3YwuKyok1Fl2pnq0pPUlo-AR7VpEkLAVG9pSA/edit
**Ablage Drive:** Basis-Ordner → `VHV` → `On-Page` (Account `ben@eom.de`). Im Vorlagen-Format (Hannoversche-Referenz-Doc), echte Orange/Grün/Gelb-Markierung via Docs-API, kein Inline-CSS.

## Aufgabe
Interne Verlinkungen aus Bestandsseiten auf 3 neue, noch nicht online stehende Ratgeber: **Wohnwagen Führerschein, Wohnwagen TÜV, Wohnwagen Gewicht**. Bereits separat eingeplant (nicht gedoppelt): Produktseite → Ratgeber und Querverlinkung der 3 Ratgeber untereinander.

## Wichtiger Befund (korrigiert)
- **Wohnwagen = Anhänger ≠ Wohnmobil** (selbstfahrend, andere Zielgruppe). Wohnmobil-Seiten sind daher **keine** Quelle.
- vhv.de hat **keine** eigene Wohnwagen-/Anhänger-Seite und **keinen** Wohnwagen-Bezug in den Auto-Ratgebern → Empfehlungen sind fast alle **neuer Absatz (grün)**, nur 1× Bestands-Anpassung (orange) an der bereits vorhandenen HU-Erwähnung.

## Empfehlungen (4 Quellseiten, 6 Anker — alle mit voller URL)
| # | Quellseite (volle URL) | Abschnitt | Ziel | Typ |
|---|---|---|---|---|
| 1 | https://www.vhv.de/auto-versicherung/ratgeber/fahranfaenger | „Begleitetes Fahren und Probezeit" | Führerschein | neu (grün) |
| 2 | https://www.vhv.de/auto-versicherung/ratgeber/kfz-zulassung | „Kfz-Zulassung – perfekt vorbereitet" | Gewicht + Führerschein | neu (grün) |
| 3 | https://www.vhv.de/auto-versicherung/ratgeber/kfz-zulassung | „diese Unterlagen sind wichtig" (HU schon erwähnt) | TÜV | Anpassung (orange) |
| 4 | https://www.vhv.de/auto-versicherung/ratgeber/gebrauchtwagenkauf | „Besichtigen und Probe fahren" | TÜV + Gewicht | neu (grün) |

Abdeckung: Führerschein 2 Anker · TÜV 2 · Gewicht 2. Jede Empfehlung enthält Quell-URL, exakten Abschnitt, zitierten Bestandstext und den fertig formulierten Einbau-Satz mit sprechendem Ankertext.

## Offen / Hinweise
- **Ziel-URLs** der 3 Ratgeber sind Annahme (`/auto-versicherung/ratgeber/wohnwagen-…`), da noch offline. Bei abweichenden finalen URLs → Anker einmalig anpassen.
- VHV ohne CMS-Schreibzugriff → Übergabe an Neoskop; EOM liefert Text + Platzierung. Anker müssen kundenseitig als echte Links gesetzt werden.

## Quellen & Stand
- vhv.de-Sitemap (`https://www.vhv.de/sitemap.xml`) + Live-Abruf der 4 Quellseiten am 2026-06-22.
- Vorlage/Format: Hannoversche-Referenz-Doc `17FQpzaxZFlZXFxWrSl2LuD1EcYZB3Ur-OLjiScWAOgs`.
- Render-Mechanik: `.gws/doc_builder.py` (Docs-API-Farb-Runs). Analyst: Ben (EOM), Stand 2026-06-22.
