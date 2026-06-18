---
tags: [kontext, tools]
---

# Tools-Stack

## Datenquellen & Tools
- **Sistrix** — Sichtbarkeitsindex, Keywords Top-10/100, Wettbewerber, Optimizer. (MCP: `sistrix`)
- **Ahrefs** — Backlinks, Keywords, Site Audit, Rank Tracker, Brand Radar (AI-Visibility). (MCP: `Ahrefs`)
- **DataForSEO** — SERP, Keyword-Daten, Backlinks, Labs. (MCP: `dataforseo`) — Hinweis: bei NIBE **nicht freigeschaltet** (Fehler 40204), Backlinks dort via Sistrix.
- **Google Search Console (GSC)** — Klicks/Impressionen/CTR/Position, Brand vs. Non-Brand. (via Ahrefs `gsc-*` und GA4-MCP)
- **GA4** — Conversions, CPO, Schlüsselereignisse. (MCP: `GA4`)
- **Looker Studio** — Reporting-Dashboards (gemeinsamer Master).
- **Peec AI** — AI-Visibility-Tracking (Brand Mentions/Citations über LLM-Engines). (MCP: `Peec_AI`)
- **Wochen-Crawl** über `seo@eom.de` (technisches Audit, Health Score).
- **Toggl** — Zeiterfassung gegen Stundenbudget (z. B. VHV-Retainer).

## Konten / Postfächer
- `seo@eom.de` — Crawl-/Monitoring-Postfach
- `vhv@eom.de` — VHV-Sammelpostfach

## gws CLI — projekt-lokaler Workspace-Zugriff (Stand 18.06.2026)
Dieses Vault nutzt die **`gws` CLI** (`googleworkspace/cli`) für direkten Zugriff auf Drive/Gmail/Kalender/Sheets/Docs — **projekt-isoliert** mit eigenem Google-Account, getrennt von den globalen `ki@eom.de`-Connectors.
- **Account:** `ben@eom.de` (separater SEO-Account)
- **Config (gitignored):** `~/Desktop/brain/.gws/` — OAuth-Client + verschlüsselte Credentials (AES-256-GCM), kommt **nie** ins Repo
- **GCP-Projekt:** `eom-brain-seo-gws` (OAuth-Client „Desktop-App")
- **Nutzung:** Befehle nur mit gesetztem Scope ausführen:
  `GOOGLE_WORKSPACE_CLI_CONFIG_DIR="$HOME/Desktop/brain/.gws" gws <befehl>`
  (z. B. `gws drive files list`, `gws auth status`). Ohne diese Env-Variable greift `gws` nicht auf diesen Account zu.

## Verwandt
[[Reporting-Standards]] · [[Über EOM]]

---

## Verbindungen (Schritt 1) — Stand 18.06.2026
**SEO-Daten (live, getestet):** Sistrix ✅ (NIBE SI 0,0733 verifiziert), Ahrefs ✅, DataForSEO ✅ (außer NIBE-Backlinks), GA4 ✅, Peec AI ✅
**Google Workspace:** Drive ✅, Gmail ✅, Kalender ✅
**PM/CRM:** monday.com ✅, Apollo ✅, GitHub ✅, Shopify ✅
**Noch nicht verbunden (nicht SEO-kritisch):** Slack, Supabase, Windsor.ai (bei Bedarf authentifizieren)

## EOM-SEO-Skills & Agenten (Schritt 2)
**Maßgeschneiderte EOM-Agenten (Human-in-the-Loop):**
- `seo-stratege-sven` — strategischer SEO-Lead, orchestriert die Spezialisten
- `seo-technik` — technisches SEO (404, Redirects, CWV, Crawl)
- `seo-onpage` — Content/Redaktion, Ratgeber-Workflow mit Freigabe-Gates
- `seo-offpage` — Backlinks, Anchor-Texte, Link Intersect

**Skills (Auswahl):** seo, seo-audit, seo-technical, seo-content, seo-schema, seo-sitemap, seo-geo, seo-hreflang, programmatic-seo, ai-seo, blog-* (kompletter Blog-Workflow), schema-markup, brand-voice, copywriting

**Meta-Skill:** `skill-creator` (global installiert) — zum Bauen/Verbessern eigener Skills
