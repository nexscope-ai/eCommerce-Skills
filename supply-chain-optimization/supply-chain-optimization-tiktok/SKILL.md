---
name: supply-chain-optimization-tiktok
version: 1.0.0
description: "Supply Chain Bottleneck Analyzer for TikTok Shop sellers. Diagnose cash flow, inventory turnover, affiliate commissions, and return rates. Includes FBT cost analysis, influencer payout optimization, and viral product lifecycle management. No API key required for basic analysis."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — TikTok Shop 📦

Supply chain bottleneck analyzer for TikTok Shop sellers. Diagnose cash flow, inventory, affiliate costs, and return rates.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization-tiktok -g
```

## Platform Characteristics

| Feature | TikTok Shop | vs Amazon |
|---------|-------------|-----------|
| Fulfillment | FBT / Self-ship | FBA |
| Commission | 2-8% (category) + 2% transaction | 8-15% |
| Payment cycle | 7-15 days | 14 days |
| Traffic source | Content-driven | Search-driven |
| Return rate | Higher (impulse buying) | Medium |

## Cost Structure (TikTok Shop)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping
├── FBT Fulfillment / Self-ship
├── Platform Fee (2%)
├── Referral Fee (2-8%)
├── Affiliate Commission (10-30%)  ← TikTok-specific
├── Advertising (Spark Ads)
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "tiktok": {
        "gross_margin": {
            "healthy": 0.45,    # Need to cover affiliate commission
            "warning": 0.35,
            "danger": 0.25
        },
        "shipping_ratio": {
            "healthy": 0.05,
            "warning": 0.08,
            "danger": 0.12
        },
        "inventory_days": {
            "healthy": 30,      # TikTok viral cycle is short
            "warning": 45,
            "danger": 60
        },
        "cash_cycle": {
            "healthy": 60,      # Fast payment
            "warning": 90,
            "danger": 120
        },
        "net_margin": {
            "healthy": 0.15,    # After affiliate split
            "warning": 0.08,
            "danger": 0.03
        },
        # TikTok-specific metrics
        "return_rate": {
            "healthy": 0.10,    # <10% healthy
            "warning": 0.20,
            "danger": 0.30
        },
        "affiliate_ratio": {
            "healthy": 0.20,    # Affiliate commission ratio
            "warning": 0.30,
            "danger": 0.40
        }
    }
}
```

## TikTok-Specific Costs

### Affiliate Commission

```
Livestream selling: 10-30% commission
Short video promotion: 10-25% commission
Top influencers: May require upfront fees
```

### Return Costs

```
TikTok return rates typically higher than traditional e-commerce (impulse buying)
Must account for:
├── Return shipping cost
├── Product damage/loss
└── Restocking fees
```

## Input Data

```
**Sales (TikTok-specific)**
• Average Selling Price: $___
• FBT Fulfillment Fee: $___/unit
• Platform Fee: 2% (fixed)
• Referral Fee: ___%
• Affiliate Commission Rate: ___% (if applicable)
• Spark Ads Spend Ratio: ___%

**Risk (TikTok-specific)**
• Return Rate: ___%
• Return Processing Cost: $___/unit
```

## API Integration

### TikTok Shop API

```bash
export TIKTOK_APP_KEY="xxx"
export TIKTOK_APP_SECRET="xxx"
export TIKTOK_ACCESS_TOKEN="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Order API |
| Products | Product API |
| Logistics | Logistics API |
| Affiliates | Affiliate API |

## Bottleneck Diagnosis Focus

TikTok Shop-specific bottlenecks:

1. **High affiliate commission** → Profit erosion
2. **High return rate** → Hidden costs
3. **Slow inventory turnover** → Short viral cycle, high stagnation risk
4. **Content dependency** → Unstable traffic

## vs Amazon Comparison

| Item | Amazon | TikTok |
|------|--------|--------|
| Commission | 8-15% | 4-10% |
| Affiliate split | None | 10-30% |
| Payment cycle | 14 days | 7-15 days |
| Return rate | 5-15% | 10-30% |
| Traffic | Stable | Volatile |
| Viral cycle | Long | Short |

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**


