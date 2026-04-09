---
name: amazon-review-checker
version: 1.0.0
description: "Amazon review authenticity analyzer. Detect fake reviews, suspicious patterns, and rating manipulation. Includes time clustering detection, content similarity analysis, rating distribution checks, and verified purchase validation. Progressive analysis with L1-L4 depth levels. No API key required."
metadata: {"nexscope":{"emoji":"🔍","category":"ecommerce"}}
---

# Amazon Review Checker 🔍

Review authenticity analyzer — detect fake reviews, suspicious patterns, and rating manipulation.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill amazon-review-checker -g
```

## Features

- **Authenticity Score** — 0-100 comprehensive rating
- **Suspicious Pattern Detection** — Time clustering, content similarity, rating anomalies
- **Fake Review Flagging** — Mark high-risk reviews with explanations
- **Progressive Analysis** — More data = deeper insights

## Progressive Analysis Levels

| Level | Required Data | Unlocked Analysis |
|-------|---------------|-------------------|
| **L1 Basic** | Review content | Similarity, length, keywords |
| **L2 Advanced** | + Review date | Time clustering detection |
| **L3 Deep** | + Star rating | Rating distribution analysis |
| **L4 Complete** | + VP status | Verified purchase validation |

## Detection Dimensions

| Dimension | Weight | Method |
|-----------|--------|--------|
| Time Clustering | 25% | Sliding window + burst detection |
| Content Similarity | 20% | N-gram + Jaccard similarity |
| Rating Distribution | 20% | Chi-square test vs natural distribution |
| VP Ratio | 15% | Compare to category benchmark |
| Review Length | 5% | Entropy analysis |
| Suspicious Keywords | 5% | Keyword pattern matching |

## Risk Levels

| Score | Level | Description |
|-------|-------|-------------|
| 70-100 | ✅ Low Risk | Reviews appear authentic |
| 50-69 | ⚠️ Medium Risk | Some concerns found |
| 30-49 | 🔴 High Risk | Multiple red flags |
| 0-29 | 💀 Critical | Likely mass fake reviews |

## Usage

### Method 1: Paste Reviews

Paste reviews directly in conversation:

```
Check these reviews:

5 stars - Great product! Works perfectly.
5 stars - Amazing! Best purchase ever.
1 star - Not as described.
```

### Method 2: JSON Input

```bash
python3 scripts/analyzer.py '[
  {"content": "Great product!", "rating": 5, "date": "2024-01-15", "verified_purchase": true},
  {"content": "Amazing!", "rating": 5, "date": "2024-01-15", "verified_purchase": false}
]'
```

### Method 3: Demo Mode

```bash
python3 scripts/analyzer.py --demo
```

## Output Example

```
📊 Review Authenticity Report

ASIN: B08XXXXX
Reviews: 10
Analysis Level: L4

━━━━━━━━━━━━━━━━━━━━━━━━

Authenticity Score: 66/100 ⚠️

Medium Risk - Some concerns found.

━━━━━━━━━━━━━━━━━━━━━━━━

Detection Dimensions

🔴 Time Clustering: 70/100
   Max 6 reviews within 48h

✅ Content Similarity: 24/100
   Found 0 highly similar review groups

━━━━━━━━━━━━━━━━━━━━━━━━

High-Risk Reviews (Top 3)

1. Risk 75% - "Perfect!"
   Reason: Too short, non-VP, templated 5-star

🔍 Want more accurate analysis? Add:
• Reviewer info → Unlock "Account Profile Analysis"
```

## Interaction Flow

```
User Input (any format)
        ↓
Smart field detection
        ↓
Analyze with available data
        ↓
Results + depth suggestions
        ↓
User continues or ends
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
