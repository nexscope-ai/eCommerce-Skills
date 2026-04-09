---
name: brand-protection-walmart
version: 1.0.0
author: Nexscope AI
description: "Walmart brand protection toolkit. Detect unauthorized sellers, counterfeits, and MAP violations. Includes Walmart Brand Portal reporting, WFS seller monitoring, and complaint templates. No API key required."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — Walmart 🛡️

Protect your brand from unauthorized sellers and counterfeit products on Walmart Marketplace.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection-walmart -g
```

## Features

- **Unauthorized Seller Detection** — Find sellers without authorization
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Review-based fake detection
- **Trademark Abuse** — Listing title/description infringement
- **Walmart Brand Portal** — Official reporting templates
- **WFS Monitoring** — Track fulfillment-verified sellers

## Walmart-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Unauthorized Sellers | Seller ID monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Review keyword analysis | 🔴 High |
| Trademark | Title pattern matching | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Immediate threat | Report within 24h |
| ⚠️ Medium | Potential concern | Investigate further |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "trademark_number": "US12345678",
  "brand_portal_enrolled": true,
  "authorized_sellers": ["seller_id_1", "seller_id_2"],
  "protected_item_ids": ["123456789"],
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
# Walmart Brand Portal report
python3 scripts/templates.py brand-portal

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Test buy guide
python3 scripts/templates.py testbuy
```

## Output Example

```
🛡️ Walmart Brand Protection Report

Brand: YourBrand
Items Monitored: 10
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Item: 123456789
├── 2 unauthorized sellers detected
├── Lowest price: $17.99 (MAP: $29.99)
└── Action: File Brand Portal complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ COUNTERFEIT SIGNALS

Reviews mentioning "fake": 4
Reviews mentioning "not original": 1
Recommendation: Order test buy
```

## Walmart Brand Portal

Walmart's Brand Portal allows brand owners to:
- Report counterfeit listings
- Remove unauthorized sellers
- Monitor brand health metrics

## Action Workflow

```
Monitor Walmart Listings
      ↓
Detect Violation
      ↓
Collect Evidence
      ↓
File Brand Portal Report
      ↓
Track Resolution
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
