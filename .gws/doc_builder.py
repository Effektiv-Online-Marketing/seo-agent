#!/usr/bin/env python3
"""EOM Google-Docs Builder fuer interne-Verlinkungs-Deliverables.

Liest ein Dokument-Modell (JSON: Liste von Bloecken) und erzeugt eine
Google-Docs-batchUpdate-Requestliste. Faerbung wird ueber EXAKT berechnete
Zeichen-Ranges als echte backgroundColor gesetzt -> niemals Inline-HTML/CSS.

Block-Format:
  {"type": "title|h1|h2|h3|normal", "runs": [[text, style], ...]}
Run-Styles:
  ""  normaler Text
  "b" fett (Label)
  "y" Ankertext  -> gelb
  "g" neuer Content -> gruen
  "o" Anpassung Bestand -> orange

Aufruf: python3 doc_builder.py <model.json> <out_requests.json>
"""
import json
import sys

GREEN = {"red": 0.8549, "green": 0.9176, "blue": 0.8275}   # #d9ead3
ORANGE = {"red": 0.9765, "green": 0.7961, "blue": 0.6118}  # #f9cb9c
YELLOW = {"red": 1.0, "green": 0.851, "blue": 0.4}         # #ffd966
BLACK = {"red": 0.0, "green": 0.0, "blue": 0.0}

NAMED = {"title": "TITLE", "h1": "HEADING_1", "h2": "HEADING_2",
         "h3": "HEADING_3", "normal": "NORMAL_TEXT"}
BG = {"y": YELLOW, "g": GREEN, "o": ORANGE}


def build(blocks):
    full_text = ""
    para_styles, normal_ranges, heading_ranges = [], [], []
    bg_runs, bold_runs = [], []
    idx = 1
    for block in blocks:
        ptype = block["type"]
        para_start = idx
        for text, style in block["runs"]:
            rstart = idx
            full_text += text
            idx += len(text)
            if style in BG:
                bg_runs.append((rstart, idx, BG[style]))
            elif style == "b":
                bold_runs.append((rstart, idx))
        full_text += "\n"
        idx += 1
        para_styles.append((para_start, idx, NAMED[ptype]))
        (heading_ranges if ptype in ("title", "h1", "h2", "h3")
         else normal_ranges).append((para_start, idx))

    req = [{"insertText": {"location": {"index": 1}, "text": full_text}}]
    for s, e, n in para_styles:
        req.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e},
                    "paragraphStyle": {"namedStyleType": n}, "fields": "namedStyleType"}})
    for s, e in normal_ranges:
        req.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e},
                    "textStyle": {"weightedFontFamily": {"fontFamily": "Montserrat", "weight": 400},
                                  "fontSize": {"magnitude": 12, "unit": "PT"}},
                    "fields": "weightedFontFamily,fontSize"}})
    for s, e in heading_ranges:
        req.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e},
                    "textStyle": {"foregroundColor": {"color": {"rgbColor": BLACK}}},
                    "fields": "foregroundColor"}})
    for s, e, color in bg_runs:
        req.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e},
                    "textStyle": {"backgroundColor": {"color": {"rgbColor": color}}},
                    "fields": "backgroundColor"}})
    for s, e in bold_runs:
        req.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e},
                    "textStyle": {"bold": True}, "fields": "bold"}})
    return full_text, req


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as fh:
        blocks = json.load(fh)
    text, requests = build(blocks)
    with open(sys.argv[2], "w", encoding="utf-8") as fh:
        json.dump({"requests": requests}, fh, ensure_ascii=False)
    print(f"blocks={len(blocks)} chars={len(text)} requests={len(requests)}")
