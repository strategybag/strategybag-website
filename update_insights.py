#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "insights.json"

SEARCHES = [
    ("AI + MARKETING", '"AI marketing" OR "AI brand strategy"'),
    ("BRAND STRATEGY", '"brand strategy" OR "brand equity" OR "brand value"'),
    ("INNOVATION", '"product innovation" marketing OR commercialization marketing'),
]

PREFERRED = [
    "Harvard Business Review", "McKinsey", "MIT Sloan", "Forbes",
    "Fast Company", "Fortune", "Adweek", "Marketing Week", "The Drum"
]

def existing_items():
    try:
        data = json.loads(OUTPUT.read_text(encoding="utf-8"))
        return {x.get("category"): x for x in data if isinstance(x, dict)}
    except Exception:
        return {}

def fetch(category, query):
    params = urllib.parse.urlencode({"q": query, "hl":"en-US", "gl":"US", "ceid":"US:en"})
    url = "https://news.google.com/rss/search?" + params
    req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0 STRATEGY-BAG"})
    with urllib.request.urlopen(req, timeout=25) as response:
        root = ET.fromstring(response.read())

    results = []
    for node in root.findall(".//item"):
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        raw_date = (node.findtext("pubDate") or "").strip()
        source_node = node.find("source")
        source = (source_node.text or "").strip() if source_node is not None else "News source"
        if not title or not link:
            continue
        try:
            dt = datetime.strptime(raw_date, "%a, %d %b %Y %H:%M:%S %Z")
            date = dt.strftime("%b %d, %Y")
        except Exception:
            date = ""
        results.append({
            "category": category,
            "title": title,
            "source": source,
            "date": date,
            "url": link,
            "summary": ""
        })
    preferred = [r for r in results if any(p.lower() in r["source"].lower() for p in PREFERRED)]
    return (preferred or results)[0] if (preferred or results) else None

old = existing_items()
new = []
for category, query in SEARCHES:
    try:
        item = fetch(category, query)
    except Exception as exc:
        print(category, exc)
        item = None
    if item is None:
        item = old.get(category)
    if item is not None:
        new.append(item)

# Only overwrite when all three categories are present.
if len(new) == 3:
    OUTPUT.write_text(json.dumps(new, indent=2), encoding="utf-8")
    print("Updated all 3 insight cards.")
else:
    print("Could not obtain all 3 categories; existing insights.json left unchanged.")
