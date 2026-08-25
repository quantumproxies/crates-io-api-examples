"""Minimal Rust crates (crates.io) API call — one typed row per crate.

Docs & schema: https://quanticdata.io/collectors/crates-io-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/crates_io/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "serde",
        "max_results": 10
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("name"), row.get("description"), row.get("version"))
print(f"{len(data['results'])} crates, cost ${data['cost']}")
