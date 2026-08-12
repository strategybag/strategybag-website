#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import json, urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "insights.json"

SEARCHES = [
    ("AI + MARKETING", '"AI marketing" OR "AI brand strategy"'),
    ("BRAND STRATEGY", '"brand strategy" OR "brand equity" OR "brand value"'),
    ("INNOVATION", '"product innovation" marketing OR commercialization marketing')
]

PREFERRED = [
    "Harvard Business Review","McKinsey","MIT Sloan","Forbes",
    "Fast Company","Fortune","Adweek","Marketing Week","The Drum"
]

def current_items():
    try:
        data = json.loads(OUT.read_text(encoding="utf-8"))
        return {x.get("category"): x for x in data if isinstance(x, dict)}
    except Exception:
        return {}

def fetch(category, query):
    params = urllib.parse.urlencode({"q":query,"hl":"en-US","gl":"US","ceid":"US:en"})
    req = urllib.request.Request(
        "https://news.google.com/rss/search?" + params,
        headers={"User-Agent":"Mozilla/5.0 STRATEGY-BAG"}
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        root = ET.fromstring(r.read())

    items = []
    for node in root.findall(".//item"):
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        raw = (node.findtext("pubDate") or "").strip()
        src = node.find("source")
        source = (src.text or "").strip() if src is not None else "News source"
        if not title or not link:
            continue
        try:
            date = datetime.strptime(raw,"%a, %d %b %Y %H:%M:%S %Z").strftime("%b %d, %Y")
        except Exception:
            date = ""
        items.append({
            "category":category,
            "title":title,
            "source":source,
            "date":date,
            "url":link,
            "summary":""
        })

    preferred = [i for i in items if any(p.lower() in i["source"].lower() for p in PREFERRED)]
    pool = preferred or items
    return pool[0] if pool else None

old = current_items()
new = []
for category, query in SEARCHES:
    try:
        item = fetch(category, query)
    except Exception:
        item = None
    if item is None:
        item = old.get(category)
    if item:
        new.append(item)

if len(new) == 3:
    OUT.write_text(json.dumps(new, indent=2), encoding="utf-8")
