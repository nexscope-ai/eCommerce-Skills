---
name: product-differentiation-ebay
version: 1.0.0
author: Nexscope AI
description: "eBay product differentiation strategy tool. Analyze competitor weaknesses, extract pain points from negative feedback, identify unique selling points, and generate actionable differentiation strategies. Includes eBay-specific seller feedback analysis. No API key required."
metadata: {"nexscope":{"emoji":"🎯","category":"ecommerce"}}
---

# Product Differentiation — eBay 🎯

Develop winning product differentiation strategies for eBay marketplace.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation-ebay -g
```

## Features

- **Competitor Matrix** — Side-by-side listing comparison
- **Pain Point Mining** — Extract issues from negative feedback
- **USP Extraction** — Identify selling points from positive feedback
- **Differentiation Opportunities** — Find gaps in the market
- **Positioning Strategy** — Market positioning recommendations
- **Action Plan** — Prioritized improvement roadmap

## eBay-Specific Analysis

| Dimension | Method | Output |
|-----------|--------|--------|
| Seller Feedback | Feedback score analysis | Trust signals |
| Item Specifics | Attribute comparison | Missing features |
| Shipping Options | Delivery comparison | Speed advantage |
| Return Policy | Policy comparison | Buyer confidence |
| Best Offer | Price flexibility | Negotiation edge |

## Progressive Analysis Levels

| Level | Required Data | Unlocked Analysis |
|-------|---------------|-------------------|
| **L1 Basic** | Listing info | Basic comparison matrix |
| **L2 Pain Points** | + Competitor feedback | Pain point analysis |
| **L3 USP** | + Your feedback | Selling point extraction |
| **L4 Complete** | + Market data | Full strategy & action plan |

## Usage

### Interactive Mode

```bash
python3 scripts/analyzer.py
```

### With Parameters

```bash
python3 scripts/analyzer.py '{
  "your_item_id": "123456789012",
  "competitor_ids": ["234567890123", "345678901234"],
  "category": "Consumer Electronics"
}'
```

## Output Example

```
🎯 eBay Product Differentiation Report

Listing: Wireless Earbuds Pro
Category: Consumer Electronics
Competitors Analyzed: 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 COMPETITOR COMPARISON

Attribute       | You  | Comp A | Comp B | Comp C
─────────────────────────────────────────────────
Price           | $45  | $40    | $50    | $38
Shipping        | Free | $5     | Free   | Free
Returns         | 30d  | 14d    | 30d    | None
Feedback Score  | 99%  | 97%    | 98%    | 95%
Best Offer      | ✅   | ❌     | ✅     | ❌

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😤 TOP PAIN POINTS

1. 🔴 Slow shipping (mentioned 38x)
2. 🔴 Item not as described (mentioned 25x)
3. 🟡 Poor packaging (mentioned 18x)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ YOUR ADVANTAGES

1. ⭐ Higher feedback score (99%)
2. ⭐ Free shipping included
3. ⭐ Best Offer enabled

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ACTION PLAN

Priority | Action                    | Impact
─────────────────────────────────────────────
HIGH     | Highlight fast shipping   | +12% CVR
HIGH     | Add more item photos      | +8% CVR
MEDIUM   | Extend return policy      | +5% trust
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/) — AI tools for e-commerce sellers.**
