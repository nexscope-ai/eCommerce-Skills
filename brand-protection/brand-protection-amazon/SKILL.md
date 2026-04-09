---
name: brand-protection-amazon
version: 1.0.0
description: "Amazon brand protection toolkit. Detect hijackers, counterfeits, and unauthorized sellers. Includes MAP violation monitoring, trademark abuse detection, complaint templates for Brand Registry, and test buy evidence collection guides. No API key required."
metadata: {"nexscope":{"emoji":"🛡️","category":"ecommerce"}}
---

# Brand Protection — Amazon 🛡️

Protect your brand from hijackers, counterfeits, and unauthorized sellers on Amazon.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection-amazon -g
```

## Features

- **Hijacker Detection** — Find unauthorized sellers on your listings
- **Price Monitoring** — MAP violation alerts
- **Counterfeit Signals** — Review-based fake detection
- **Trademark Abuse** — Title/keyword infringement detection
- **Complaint Templates** — Brand Registry, C&D letters
- **Test Buy Guide** — Evidence collection procedure

## Detection Dimensions

| Dimension | Method | Risk Level |
|-----------|--------|------------|
| Hijackers | Seller count monitoring | 🔴 High |
| Price Violations | Below MAP detection | 🔴 High |
| Counterfeit | Review keyword analysis | 🔴 High |
| Trademark | Title pattern matching | ⚠️ Medium |

## Risk Levels

| Level | Description | Action |
|-------|-------------|--------|
| 🔴 High | Immediate threat to brand | Take action within 24h |
| ⚠️ Medium | Potential concern | Monitor and investigate |
| ✅ Low | Normal activity | Continue monitoring |

## Input Configuration

```json
{
  "brand_name": "YourBrand",
  "trademark_number": "US12345678",
  "brand_registry": true,
  "authorized_sellers": ["A1B2C3D4E5F6G7"],
  "protected_asins": ["B08XXXXXX1"],
  "min_price": 29.99
}
```

## Usage

### Hijacker Detection

```bash
python3 scripts/detector.py
```

### Generate Complaint Templates

```bash
# Brand Registry complaint
python3 scripts/templates.py complaint

# Cease & Desist letter
python3 scripts/templates.py cease-desist

# Test buy guide
python3 scripts/templates.py testbuy
```

## Output Example

```
🛡️ Brand Protection Report

Brand: YourBrand
ASINs Monitored: 5
Analysis Date: 2024-01-15

━━━━━━━━━━━━━━━━━━━━━━━━

🔴 HIGH RISK ALERTS

ASIN: B08XXXXXX1
├── 3 unauthorized sellers detected
├── Lowest price: $19.99 (MAP: $29.99)
└── Action: File Brand Registry complaint

━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ COUNTERFEIT SIGNALS

Reviews mentioning "fake": 5
Reviews mentioning "not authentic": 2
Recommendation: Order test buy
```

## Complaint Templates Included

| Template | Use Case |
|----------|----------|
| Brand Registry | Report to Amazon |
| Cease & Desist | Direct seller contact |
| Test Buy Report | Evidence documentation |
| DMCA Takedown | Copyright infringement |

## Action Workflow

```
Monitor Listings
      ↓
Detect Violation
      ↓
Collect Evidence (Test Buy)
      ↓
Generate Complaint
      ↓
Submit to Amazon / Send C&D
      ↓
Track Resolution
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
