#!/usr/bin/env python3
"""
Refresh STRATEGY BAG's three homepage insight links from Google News RSS.

No API key is required. The script intentionally links to the original
publisher through Google News rather than copying article content.
"""
from pathlib import Path
from datetime import datetime
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "insights.json"

SEARCHES = [
    ("AI + MARKETING", '"AI marketing" OR "AI brand strategy"'),
    ("BRAND STRATEGY", '"brand strategy" OR "brand equity" OR "brand value"'),
    ("INNOVATION", '"product innovation" marketing OR commercialization marketing'),
]

PREFERRED_SOURCES = [
    "Harvard Business Review", "McKinsey", "MIT Sloan", "Forbes",
    "Fast Company", "Fortune", "Adweek", "Marketing Week", "The Drum"
]

def google_news(category, query):
    params = urllib.parse.urlencode({
        "q": query,
        "hl": "en-US",
        "gl": "US",
        "ceid": "US:en"
    })
    url = f"https://news.google.com/rss/search?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 STRATEGY-BAG-site"})
    with urllib.request.urlopen(req, timeout=30) as response:
        xml = response.read()

    root = ET.fromstring(xml)
    items = []
    for node in root.findall(".//item"):
        title = (node.findtext("title") or "").strip()
        link = (node.findtext("link") or "").strip()
        raw_date = (node.findtext("pubDate") or "").strip()
        source_node = node.find("source")
        source = (source_node.text or "").strip() if source_node is not None else ""

        if not title or not link:
            continue

        try:
            parsed = datetime.strptime(raw_date, "%a, %d %b %Y %H:%M:%S %Z")
            display_date = parsed.strftime("%b %d, %Y")
        except Exception:
            display_date = ""

        items.append({
            "category": category,
            "title": title,
            "source": source or "News source",
            "date": display_date,
            "url": link,
            "summary": ""
        })
    return items

selected = []
for category, query in SEARCHES:
    try:
        results = google_news(category, query)
    except Exception as exc:
        print(f"{category}: {exc}")
        results = []

    preferred = [
        item for item in results
        if any(source.lower() in item["source"].lower() for source in PREFERRED_SOURCES)
    ]
    pool = preferred or results
    if pool:
        selected.append(pool[0])

# Do not erase the working homepage if a network/RSS fetch fails.
if selected:
    OUTPUT.write_text(json.dumps(selected[:3], indent=2), encoding="utf-8")
    print(f"Wrote {len(selected[:3])} insight items.")
else:
    print("No usable stories found; leaving existing insights.json unchanged.")
