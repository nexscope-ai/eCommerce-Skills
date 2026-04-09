---
name: brand-protection-ebay
version: 1.0.0
description: "eBay brand protection toolkit. Detect unauthorized sellers, counterfeits, and VeRO violations. Includes price monitoring, trademark abuse detection, VeRO complaint templates, and enforcement guides. No API key required."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — eBay 🛡️

Protect your brand from unauthorized sellers and counterfeits on eBay.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection-ebay -g
```

## Features

- **Unauthorized Seller Detection** — Find sellers without authorization
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Feedback-based fake detection
- **Trademark Abuse** — Listing title/description infringement
- **VeRO Complaint Templates** — eBay's rights owner program
- **Enforcement Guide** — Step-by-step takedown process

## eBay-Specific Detection

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Unauthorized Sellers | Seller ID monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Feedback keyword analysis | 🔴 High |
| Trademark | Title pattern matching | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Immediate threat | File VeRO within 24h |
| ⚠️ Medium | Potential concern | Monitor and investigate |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "trademark_number": "US12345678",
  "vero_enrolled": true,
  "authorized_sellers": ["seller_id_1", "seller_id_2"],
  "protected_item_ids": ["123456789012"],
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
# VeRO complaint
python3 scripts/templates.py vero

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Test buy guide
python3 scripts/templates.py testbuy
```

## Output Example

```
🛡️ eBay Brand Protection Report

Brand: YourBrand
Items Monitored: 8
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

Item: 123456789012
├── Unauthorized seller detected
├── Price: $15.99 (MAP: $29.99)
└── Action: File VeRO complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ COUNTERFEIT SIGNALS

Feedback mentioning "fake": 3
Feedback mentioning "not genuine": 2
Recommendation: Order test buy
```

## VeRO Program

eBay's Verified Rights Owner Program allows brand owners to:
- Report counterfeit listings
- Remove trademark violations
- Protect intellectual property

## Action Workflow

```
Monitor Listings
      ↓
Detect Violation
      ↓
Collect Evidence
      ↓
File VeRO Complaint
      ↓
Track Removal
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
