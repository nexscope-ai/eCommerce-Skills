---
name: supply-chain-optimization-shopify
version: 1.0.0
description: "Supply Chain Bottleneck Analyzer for Shopify/DTC stores. Diagnose cash flow, inventory, shipping costs, and customer acquisition efficiency. Includes CAC/LTV analysis, 3PL cost optimization, and ad spend benchmarks. No API key required for basic analysis."
metadata: {"nexscope":{"emoji":"📦","category":"ecommerce"}}
---

# Supply Chain Optimization — Shopify/DTC 📦

Supply chain bottleneck analyzer for Shopify and Direct-to-Consumer stores. Diagnose cash flow, inventory, shipping, and customer acquisition costs.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization-shopify -g
```

## Platform Characteristics

| Feature | Shopify/DTC | vs Amazon |
|---------|-------------|-----------|
| Fulfillment | Self-select (ShipBob/self) | FBA |
| Platform fee | None | 8-15% |
| Payment fee | 2.9% + $0.30 | Included in fee |
| Payment cycle | 2-3 days | 14 days |
| Traffic cost | High (self-built) | Low (platform) |
| Data ownership | Full | Limited |

## Cost Structure (Shopify/DTC)

```
Selling Price $XX
├── Product Cost
├── Inbound Shipping (to warehouse)
├── 3PL Storage Fee (e.g., ShipBob)
├── 3PL Fulfillment Fee
├── Payment Processing (2.9% + $0.30)
├── Shopify Subscription (allocated)
├── Advertising (Meta/Google/TikTok) ← Key Cost
└── Net Profit
```

## Benchmark Configuration

```python
BENCHMARKS = {
    "shopify": {
        "gross_margin": {
            "healthy": 0.60,    # DTC needs high margin for ads
            "warning": 0.50,
            "danger": 0.40
        },
        "shipping_ratio": {
            "healthy": 0.08,    # 3PL fees
            "warning": 0.12,
            "danger": 0.18
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 45,      # Fast payment
            "warning": 70,
            "danger": 100
        },
        "net_margin": {
            "healthy": 0.20,
            "warning": 0.12,
            "danger": 0.05
        },
        # DTC-specific metrics
        "cac": {               # Customer Acquisition Cost
            "healthy": 0.25,   # CAC < 25% of price
            "warning": 0.35,
            "danger": 0.50
        },
        "ltv_cac_ratio": {     # LTV/CAC
            "healthy": 3.0,    # LTV > 3x CAC
            "warning": 2.0,
            "danger": 1.0
        },
        "ad_spend_ratio": {    # Ad spend ratio
            "healthy": 0.25,
            "warning": 0.35,
            "danger": 0.45
        }
    }
}
```

## DTC-Specific Costs

### Advertising Costs (Critical!)

```
Meta Ads (Facebook/Instagram): CPM $10-30
Google Ads: CPC $1-5
TikTok Ads: CPM $5-15
Influencer Marketing: Variable

DTC ad spend typically 20-40% of revenue
```

### 3PL Logistics Costs

```
Common 3PL Options:
├── ShipBob
├── Deliverr
├── ShipMonk
└── Red Stag

Fee Structure:
├── Receiving: $2-5/case
├── Storage: $0.5-1/cubic ft/month
├── Pick & Pack: $2-4/order
└── Shipping: By weight/zone
```

### Payment Processing Fees

```
Shopify Payments: 2.9% + $0.30
PayPal: 2.9% + $0.30
Stripe: 2.9% + $0.30

High AOV: Ratio acceptable
Low AOV: Erodes profit
```

## Input Data

```
**Sales (Shopify-specific)**
• Average Selling Price: $___
• Average Order Value (AOV): $___
• Payment Fee: 2.9% + $0.30

**Logistics (3PL)**
• 3PL Fulfillment Fee: $___/order
• 3PL Storage Fee: $___/unit/month
• Receiving Fee: $___/case

**Marketing (Critical!)**
• Ad Spend Ratio: ___%
• Customer Acquisition Cost (CAC): $___
• Customer Lifetime Value (LTV): $___
• Repeat Purchase Rate: ___%
```

## API Integration

### Shopify Admin API

```bash
export SHOPIFY_STORE_URL="xxx.myshopify.com"
export SHOPIFY_ACCESS_TOKEN="xxx"
```

### Available Data

| Data | API |
|------|-----|
| Orders | Orders API |
| Products | Products API |
| Inventory | Inventory API |
| Customers | Customers API |

### 3PL API (e.g., ShipBob)

```bash
export SHIPBOB_API_TOKEN="xxx"
```

## Bottleneck Diagnosis Focus

DTC-specific bottlenecks:

1. **High CAC** → Low ad efficiency, acquisition cost eating profit
2. **LTV/CAC < 3** → Customer value insufficient to support CAC
3. **High 3PL costs** → Poor logistics choice
4. **Low repeat rate** → Reliant on new customers, high cost
5. **Low gross margin** → Cannot support ad spend

## DTC Health Formula

```
Net Profit = Price - Product Cost - Shipping - Payment Fee - Ad Spend - Ops Cost

DTC Golden Ratios:
├── Gross Margin > 60%
├── Ad Spend < 30%
├── Shipping < 15%
├── Net Margin > 15%
└── LTV/CAC > 3
```

## vs Amazon Comparison

| Item | Amazon | Shopify/DTC |
|------|--------|-------------|
| Platform fee | 8-15% | 0% |
| Payment fee | Included | 2.9% + $0.30 |
| Payment cycle | 14 days | 2-3 days |
| Ad spend | 10-20% | 20-40% |
| Traffic | Platform | Self-built |
| Margin need | 40%+ | 60%+ |
| Data | Limited | Full ownership |

---

**Part of [Nexscope AI](https://www.nexscope.ai/) — AI tools for e-commerce sellers.**


