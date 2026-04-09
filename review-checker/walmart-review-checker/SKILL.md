---
name: walmart-review-checker
version: 1.0.0
description: "Walmart review authenticity analyzer. Detect fake reviews, suspicious patterns, and rating manipulation. Includes WFS verified badge analysis, incentivized review detection, and Walmart-specific red flag identification. No API key required."
metadata: {"nexscope":{"emoji":"🔍","category":"ecommerce"}}
---

# Walmart Review Checker 🔍

Review authenticity analyzer for Walmart — detect fake reviews, suspicious patterns, and feedback manipulation.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill walmart-review-checker -g
```

## Features

- **Authenticity Score** — 0-100 comprehensive rating
- **WFS Verified Badge Analysis** — Check fulfillment verification patterns
- **Incentivized Review Detection** — Identify paid/incentivized reviews
- **Walmart-specific Red Flags** — Platform-specific warning signs
- **Progressive Analysis** — More data = deeper insights

## Walmart-Specific Detection

| Signal | Description |
|--------|-------------|
| WFS Badge | Verified fulfillment patterns |
| Incentivized | "Received free product" indicators |
| Review timing | Clustered reviews in short periods |
| Generic comments | Templated review patterns |

## Risk Levels

| Score | Level | Description |
|-------|-------|-------------|
| 70-100 | ✅ Low Risk | Reviews appear authentic |
| 50-69 | ⚠️ Medium Risk | Some concerns found |
| 30-49 | 🔴 High Risk | Multiple red flags |
| 0-29 | 💀 Critical | Likely manipulated reviews |

## Usage

### Paste Reviews

```
Check these Walmart reviews:

5 stars - Great product, fast shipping from WFS!
5 stars - Exactly as described, love it!
1 star - Arrived damaged.
```

### JSON Input

```bash
python3 scripts/analyzer.py '[
  {"content": "Great product!", "rating": 5, "date": "2024-01-15", "wfs_verified": true},
  {"content": "Amazing!", "rating": 5, "date": "2024-01-15", "wfs_verified": false}
]'
```

### Demo Mode

```bash
python3 scripts/analyzer.py --demo
```

## Output Example

```
📊 Walmart Review Authenticity Report

Product: Example Product
Reviews: 25
Analysis Level: L3

━━━━━━━━━━━━━━━━━━━━━━━━

Authenticity Score: 74/100 ✅

Low Risk - Reviews appear authentic.

━━━━━━━━━━━━━━━━━━━━━━━━

Detection Results

✅ Time Clustering: Normal
✅ WFS Verified Ratio: 68% (healthy)
⚠️ Generic Comments: 12%
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
