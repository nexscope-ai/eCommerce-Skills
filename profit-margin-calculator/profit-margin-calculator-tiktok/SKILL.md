---
name: profit-margin-calculator-tiktok
version: 1.0.0
description: "TikTok Shop profit margin calculator for sellers. Calculate cost breakdowns including affiliate commissions, platform fees, and FBT costs. Includes return rate analysis for impulse buying patterns. No API key required."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — TikTok Shop 💰

Calculate product profitability for TikTok Shop sellers — cost breakdowns, profit margins, and affiliate commission analysis.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator-tiktok -g
```

## Cost Components

| Cost Item | Description | Notes |
|-----------|-------------|-------|
| Product Cost | FOB purchase price | - |
| Inbound Shipping | To FBT warehouse | - |
| FBT Fulfillment | Fulfillment by TikTok | Optional |
| **Platform Fee** | 5% | Lower ✅ |
| **Affiliate Commission** | 10-30% | Main cost ⚠️ |
| Advertising | TikTok Ads | - |
| Return Cost | Higher return rate | 5-15% |

## TikTok Characteristics

- **Low platform fee**: Only 5%
- **High affiliate commission**: 10-30%, main cost driver
- **High return rate**: Impulse buying, 5-15% returns
- **Short viral cycle**: Need fast inventory turnover

## Usage

```bash
python3 scripts/calculator.py

python3 scripts/calculator.py '{"selling_price": 19.99, "creator_commission_rate": 0.15, "product_cost": 5}'
```

## Output Example

```
💰 **TikTok Shop Profit Analysis Report**

Selling Price         $19.99   100.0%
────────────────────────────────────────
Product Cost          -$5.00    25.0%
FBT Fulfillment       -$3.50    17.5%
Platform Fee (5%)     -$1.00     5.0%
Affiliate Commission  -$3.00    15.0%  ⬅️ Main cost
...
────────────────────────────────────────
Net Profit            $4.54    22.7%
```

## TikTok Fee Structure

| Fee Type | Rate | Notes |
|----------|------|-------|
| Platform Fee | 5% | Lower than Amazon |
| Affiliate Commission | 10-30% | Varies by influencer tier |
| FBT Fulfillment | ~$3-5/order | Similar to FBA |
| Return Processing | ~$2-3/return | Higher return rate |

## Key Considerations

1. **Affiliate costs are variable** — Top influencers demand higher rates
2. **Plan for returns** — Budget 5-15% return rate
3. **Fast turnover needed** — Viral products have short cycles
4. **Lower platform fees** — 5% vs Amazon's 8-15%

## vs Amazon

| Item | Amazon | TikTok |
|------|--------|--------|
| Platform fee | 8-15% | 5% |
| Affiliate | N/A | 10-30% |
| Return rate | 5-10% | 5-15% |
| Traffic | Search | Content |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
