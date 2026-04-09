---
name: etsy-seo
version: 1.0.0
author: Nexscope AI
description: "Etsy SEO analyzer and optimizer. Improve search visibility with title optimization, tag analysis, description scoring, and keyword research. Includes SEO scoring (0-100), long-tail keyword suggestions, and prioritized action plans. No API key required."
metadata: {"nexscope":{"emoji":"🔍","category":"ecommerce"}}
---

# Etsy SEO 🔍

Analyze and optimize Etsy listings for better search visibility.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill etsy-seo -g
```

## Features

- **SEO Score** — 0-100 comprehensive rating
- **Title Optimization** — Keyword placement, length analysis
- **Tag Analysis** — 13 tag optimization, long-tail suggestions
- **Description Analysis** — First 160 chars, keyword density
- **Attribute Check** — Completeness validation
- **Keyword Research** — Category-based suggestions
- **Action Plan** — Prioritized improvement roadmap

## SEO Scoring Weights

| Dimension | Weight | Max Score |
|-----------|--------|-----------|
| Title | 30% | 100 |
| Tags | 25% | 100 |
| Description | 20% | 100 |
| Attributes | 15% | 100 |
| Images | 10% | 100 |

## Etsy Tag Rules

| Rule | Specification |
|------|---------------|
| Quantity | Max 13 tags |
| Length | Max 20 characters each |
| Format | Multi-word phrases allowed |
| Strategy | Long-tail + synonyms + attributes |

## Title Best Practices

```
[Core Keyword] + [Attributes] + [Material/Style] + [Use Case/Occasion]

✅ Good:
"Personalized Name Bracelet, Custom Gold Bracelet for Women, Birthday Gift"

❌ Bad:
"Beautiful Handmade Bracelet"
```

## Usage

### Interactive Mode

```bash
python3 scripts/analyzer.py
```

### With Listing Data

```bash
python3 scripts/analyzer.py '{
  "title": "Handmade Silver Ring",
  "tags": ["silver ring", "handmade jewelry"],
  "description": "Beautiful handmade ring...",
  "category": "Jewelry"
}'
```

### Demo Mode

```bash
python3 scripts/analyzer.py --demo
```

## Output Example

```
🔍 Etsy SEO Analysis Report

Listing: Personalized Name Bracelet
Category: Jewelry > Bracelets

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 SEO SCORE: 72/100 ⚠️

Title:       85/100 ████████░░
Tags:        65/100 ██████░░░░
Description: 70/100 ███████░░░
Attributes:  80/100 ████████░░
Images:      60/100 ██████░░░░

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 TITLE ANALYSIS

Current: "Handmade Silver Bracelet"
Length: 24/140 characters ⚠️ Too short

Issues:
• Missing core keyword at start
• No personalization keywords
• Missing occasion/gift keywords

Suggested:
"Personalized Silver Bracelet, Custom Name Bracelet, Birthday Gift for Her"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏷️ TAG ANALYSIS

Used: 8/13 tags ⚠️ Add 5 more

Current Tags:
✅ silver bracelet
✅ handmade jewelry
⚠️ bracelet (too generic)

Suggested Tags:
+ personalized bracelet
+ custom name jewelry
+ birthday gift for women
+ anniversary gift
+ minimalist bracelet

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 ACTION PLAN

Priority | Action                      | Impact
──────────────────────────────────────────────
HIGH     | Rewrite title with keywords | +15 score
HIGH     | Add 5 more tags             | +10 score
MEDIUM   | Optimize first 160 chars    | +8 score
LOW      | Add more product photos     | +5 score
```

## Keyword Research

The tool suggests keywords based on:
- Category trends
- Competitor analysis
- Search volume indicators
- Long-tail variations

## Optimization Workflow

```
Analyze current listing
      ↓
Score each dimension
      ↓
Identify gaps
      ↓
Generate suggestions
      ↓
Prioritize actions
      ↓
Track improvements
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
