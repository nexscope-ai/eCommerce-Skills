---
name: brand-protection-tiktok
version: 1.0.0
author: Nexscope AI
description: "TikTok Shop brand protection toolkit. Detect unauthorized sellers, counterfeit products, and affiliate abuse. Includes TikTok IP Protection reporting, influencer misuse detection, and complaint templates. No API key required."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — TikTok Shop 🛡️

Protect your brand from unauthorized sellers and counterfeit products on TikTok Shop.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection-tiktok -g
```

## Features

- **Unauthorized Seller Detection** — Find sellers without authorization
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Review-based fake detection
- **Affiliate Abuse** — Unauthorized influencer promotion
- **TikTok IP Protection** — Official reporting templates
- **Content Takedown** — Video/post removal requests

## TikTok-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Unauthorized Sellers | Shop monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Review/comment analysis | 🔴 High |
| Affiliate Abuse | Creator content scan | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Active infringement | Report within 24h |
| ⚠️ Medium | Potential concern | Investigate further |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "tiktok_shop_id": "your_shop_id",
  "trademark_number": "US12345678",
  "authorized_affiliates": ["creator_id_1", "creator_id_2"],
  "min_price": 29.99
}
```

## Usage

### Detection

```bash
python3 scripts/detector.py
```

### Generate Complaint Templates

```bash
# TikTok IP Protection report
python3 scripts/templates.py ip-report

# Seller complaint
python3 scripts/templates.py seller-complaint

# Content takedown
python3 scripts/templates.py content-takedown
```

## Output Example

```
🛡️ TikTok Shop Brand Protection Report

Brand: YourBrand
Shops Monitored: 5
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Shop: fake_seller_123
├── Selling counterfeit products
├── Price: $9.99 (MAP: $29.99)
└── Action: File TikTok IP report

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ AFFILIATE ABUSE

Creator: @unauthorized_creator
├── Promoting without authorization
├── Commission rate: 25%
└── Action: Contact creator / Report
```

## TikTok IP Protection

TikTok's Intellectual Property Protection program allows brand owners to:
- Report counterfeit listings
- Remove unauthorized content
- Block infringing sellers

## Action Workflow

```
Monitor TikTok Shop
      ↓
Detect Violation
      ↓
Collect Evidence
      ↓
File IP Report
      ↓
Track Removal
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
