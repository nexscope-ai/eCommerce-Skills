---
name: profit-margin-calculator-shopify
version: 1.0.0
description: "Shopify/DTC profit margin calculator for sellers. Calculate cost breakdowns including ad spend, CAC, payment processing fees, and 3PL costs. Includes LTV/CAC analysis and DTC-specific benchmarks. No API key required."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — Shopify/DTC 💰

Calculate product profitability for Shopify and DTC stores — cost breakdowns, profit margins, and CAC/LTV analysis.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator-shopify -g
```

## Cost Components

| Cost Item | Description | Notes |
|-----------|-------------|-------|
| Product Cost | FOB purchase price | - |
| Inbound Shipping | To 3PL warehouse | - |
| 3PL Fulfillment | ShipBob/Deliverr etc. | - |
| **Payment Processing** | 2.9% + $0.30 | Shopify Payments |
| **Advertising** | 20-40% | Main cost ⚠️ |
| Return Cost | Return processing | - |
| Customer Shipping | If free shipping offered | Optional |

## DTC Characteristics

- **No platform commission**: Only payment processing fees
- **High ad spend ratio**: 20-40%, main cost driver
- **Requires high margins**: 60%+ gross margin to support ads
- **Focus on LTV/CAC**: Recommended >3

## Key Metrics

| Metric | Recommended |
|--------|-------------|
| Gross Margin | >60% |
| Net Margin | >20% |
| LTV/CAC | >3 |
| Repeat Rate | Higher = better |

## Usage

```bash
python3 scripts/calculator.py

python3 scripts/calculator.py '{"selling_price": 49.99, "ad_spend_ratio": 0.20, "product_cost": 12}'
```

## Output Example

```
💰 **Shopify/DTC Profit Analysis Report**

Selling Price         $49.99   100.0%
────────────────────────────────────────
Product Cost          -$12.00    24.0%
3PL Fulfillment       -$4.50     9.0%
Payment Processing    -$1.75     3.5%
Advertising           -$10.00    20.0%  ⬅️ Main cost
...
────────────────────────────────────────
Net Profit            $18.59    37.2%

💡 Max Affordable CAC: $10.00
```

## DTC Golden Ratios

```
DTC Health Formula:
├── Gross Margin > 60%
├── Ad Spend < 30%
├── Fulfillment < 15%
├── Net Margin > 15%
└── LTV/CAC > 3
```

## vs Amazon

| Item | Amazon | Shopify/DTC |
|------|--------|-------------|
| Platform fee | 8-15% | 0% |
| Payment fee | Included | 2.9% + $0.30 |
| Ad spend | 10-20% | 20-40% |
| Margin need | 40%+ | 60%+ |
| Traffic | Platform | Self-built |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

