# EOM KWR Skill Design

## Ziel
Ein wiederverwendbarer Projektskill, der EOM-Keyword-Recherchen immer im gleichen Ablauf erstellt:
- Live-Sistrix als Pflichtquelle
- gebrandeter Google Sheet
- Google-Doc-Zusammenfassung
- lokale Vault-Notiz

## Trigger
Der Skill soll bei Anfragen wie `KWR`, `Keyword-Recherche`, `Keyword Recherche`, `Seed-Keyword`, `Cluster`, `mach das ins Sheet` oder ähnlichen SEO-Recherchewünschen triggern.

## Feste Regeln
- Ohne Live-Sistrix wird hart gestoppt.
- Keine Fallback-Quelle für Metriken.
- Die Sheet-Vorlage beginnt praktisch erst mit dem Header ab Zeile 4.
- Zu jeder KWR gehören immer Drive-Artefakte und eine lokale `.md`-Fassung im Vault.

## Bevorzugte Outputs
- Sheet: `<Kunde> | KWR – <Thema>`
- Doc: `<Kunde> — Keyword-Recherche <Thema>`
- Vault: `02 Kunden/<Kunde>/<Kunde> — KWR <Thema>.md`

## Warum diese Form
- Sie bildet den EOM-Standard besser ab als ein reiner Sheet-Workflow.
- Sie hält die Arbeit im Drive nutzbar und im Vault auffindbar.
- Sie verhindert improvisierte Fallbacks bei fehlenden SEO-Daten.
