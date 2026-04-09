---
name: supply-chain-optimization-walmart
version: 1.0.0
description: "Supply Chain Bottleneck Analyzer for Walmart Marketplace sellers. Diagnose cash flow, inventory, WFS costs, and referral fees. Includes comparison with Amazon FBA, lower storage fee optimization, and Walmart Connect ad spend analysis. No API key required for basic analysis."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — Walmart 📦

Supply chain bottleneck analyzer for Walmart Marketplace sellers. Diagnose cash flow, inventory, WFS costs, and referral fees.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization-walmart -g
```

## Platform Characteristics

| Feature | Walmart | vs Amazon |
|---------|---------|-----------|
| Fulfillment | WFS (Walmart Fulfillment Services) | FBA |
| Commission | 6-15% (by category) | 8-15% |
| Payment cycle | 14-21 days | 14 days |
| Storage fees | Lower | Higher |
| Long-term storage | No extra fee | Yes |

## Cost Structure (Walmart)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping
├── WFS Fulfillment Fee (similar to FBA)
├── WFS Storage Fee (lower than FBA)
├── Referral Fee (6-15%)
├── Advertising (Walmart Connect)
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "walmart": {
        "gross_margin": {
            "healthy": 0.35,    # Walmart commission lower, benchmark can be lower
            "warning": 0.25,
            "danger": 0.15
        },
        "shipping_ratio": {
            "healthy": 0.06,    # WFS shipping slightly higher
            "warning": 0.10,
            "danger": 0.15
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 100,     # Payment cycle slightly longer
            "warning": 130,
            "danger": 160
        },
        "net_margin": {
            "healthy": 0.18,
            "warning": 0.10,
            "danger": 0.05
        }
    }
}
```

## API Integration

### Walmart Marketplace API

```bash
export WALMART_CLIENT_ID="xxx"
export WALMART_CLIENT_SECRET="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Orders API |
| Inventory | Inventory API |
| Fee Reports | Reports API |

## Usage Flow

Same 4-step process as Amazon version:

1. Business profile collection
2. Supply chain data collection
3. Bottleneck diagnosis
4. Cost reduction plan output

## Input Data

```
**Sales (Walmart-specific)**
• Average Selling Price: $___
• WFS Fulfillment Fee: $___/unit
• Referral Fee Rate: ___%
• Walmart Connect Ad Spend Ratio: ___%

**Inventory**
• Current Inventory Days: ___ days
• (Walmart has no long-term storage fees)
```

## vs Amazon Comparison

| Item | Amazon | Walmart |
|------|--------|---------|
| Fulfillment | FBA | WFS |
| Storage fees | High | Low |
| Long-term storage | Yes | No |
| Commission | 8-15% | 6-15% |
| Payment cycle | 14 days | 14-21 days |
| Traffic | High | Medium |

## Key Advantages

- **No long-term storage fees** — Better for slow-moving inventory
- **Lower referral fees** — 6-15% vs Amazon's 8-15%
- **Lower storage costs** — WFS storage cheaper than FBA
- **Growing marketplace** — Less competition than Amazon

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

