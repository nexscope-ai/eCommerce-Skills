---
name: ebay-review-checker
version: 1.0.0
description: "eBay review and feedback authenticity analyzer. Detect fake reviews, suspicious seller feedback patterns, and buyer manipulation. Includes time clustering detection, content similarity analysis, and eBay-specific red flag identification. No API key required."
metadata: {"nexscope":{"emoji":"🔍","category":"ecommerce"}}
---

# eBay Review Checker 🔍

Review and feedback authenticity analyzer for eBay — detect fake reviews, suspicious patterns, and feedback manipulation.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill ebay-review-checker -g
```

## Features

- **Seller Feedback Analysis** — Analyze seller feedback authenticity
- **Buyer Feedback Patterns** — Detect suspicious buyer behavior
- **eBay-specific Red Flags** — Platform-specific warning signs
- **Progressive Analysis** — More data = deeper insights

## eBay-Specific Detection

| Signal | Description |
|--------|-------------|
| Feedback timing | Clustered feedback in short periods |
| Generic comments | "A+++" or "Great seller" patterns |
| Account age | New accounts leaving multiple feedbacks |
| Transaction patterns | Unusual buying/selling patterns |

## Risk Levels

| Score | Level | Description |
|-------|-------|-------------|
| 70-100 | ✅ Low Risk | Feedback appears authentic |
| 50-69 | ⚠️ Medium Risk | Some concerns found |
| 30-49 | 🔴 High Risk | Multiple red flags |
| 0-29 | 💀 Critical | Likely manipulated feedback |

## Usage

### Paste Feedback

```
Check this seller feedback:

Positive - Great seller, fast shipping! A+++
Positive - Excellent transaction, thank you!
Positive - Perfect! Would buy again.
Negative - Item never arrived.
```

### JSON Input

```bash
python3 scripts/analyzer.py '[
  {"content": "A+++ seller!", "rating": "positive", "date": "2024-01-15"},
  {"content": "Fast shipping", "rating": "positive", "date": "2024-01-15"}
]'
```

## Output Example

```
📊 eBay Feedback Authenticity Report

Seller: example_seller
Feedback Count: 50
Analysis Level: L3

━━━━━━━━━━━━━━━━━━━━━━━━

Authenticity Score: 72/100 ✅

Low Risk - Feedback appears authentic.

━━━━━━━━━━━━━━━━━━━━━━━━

Detection Results

✅ Time Clustering: Normal
⚠️ Generic Comments: 15% (slightly high)
✅ Account Diversity: Good
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/) — AI tools for e-commerce sellers.**
