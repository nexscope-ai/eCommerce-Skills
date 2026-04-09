---
name: profit-margin-calculator-amazon
description: "Amazon profit margin calculator for sellers. Calculate cost breakdowns, profit margins, break-even points, and get pricing recommendations. Supports single product analysis and batch calculations. Input product cost, shipping, FBA fees, and get instant profitability analysis. No API key required. Use when: (1) evaluating new product profitability before sourcing, (2) diagnosing existing product margins, (3) adjusting pricing strategy, (4) analyzing multiple SKUs at once."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Profit Margin Calculator — Amazon 💰

Calculate product profitability for Amazon FBA sellers — cost breakdowns, profit margins, break-even analysis, and pricing recommendations. No API key required.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator-amazon -g
```

## Use Cases

| Scenario | What You'll Get |
|----------|-----------------|
| **New product evaluation** | Profitability forecast before sourcing |
| **Existing product diagnosis** | Margin analysis with cost breakdown |
| **Pricing adjustment** | Recommended prices for target margins |
| **Batch SKU analysis** | Multi-product comparison table |

## Usage Examples

### Single Product Analysis

```
Calculate profit for my Amazon product:
- Selling price: $29.99
- Product cost: $6
- Shipping to FBA: $1.50
- FBA fulfillment fee: $5.50
- FBA storage: $0.30/month
- Ad spend: 10% of sales
- Category: Kitchen
```

### Quick Analysis

```
Is this product profitable?
Price $19.99, cost $5, FBA fee $4.50, shipping $1
```

### Batch Analysis

```
Analyze these SKUs:
A001, Yoga Mat, $29.99, cost $6, shipping $1.5, FBA $5.5
A002, Resistance Bands, $19.99, cost $3, shipping $0.8, FBA $4
A003, Foam Roller, $24.99, cost $8, shipping $2, FBA $6
```

---

## Input Parameters

### Required

| Parameter | Description | Example |
|-----------|-------------|---------|
| `selling_price` | Amazon listing price | $29.99 |
| `product_cost` | FOB/sourcing cost per unit | $6.00 |
| `fba_fee` | FBA fulfillment fee | $5.50 |

### Recommended

| Parameter | Description | Default |
|-----------|-------------|---------|
| `shipping_cost` | Inbound shipping per unit | $0 |
| `storage_fee` | Monthly FBA storage per unit | $0.30 |
| `ad_ratio` | PPC spend as % of sales | 10% |
| `category` | Product category for referral fee | default (15%) |

### Optional

| Parameter | Description | Default |
|-----------|-------------|---------|
| `return_rate` | Expected return rate | 3% |
| `other_fees` | Packaging, labels, etc. | $0 |

---

## Cost Components

| Cost Item | Description | Calculation |
|-----------|-------------|-------------|
| **Product Cost** | FOB purchase price | User input |
| **Inbound Shipping** | Sea/air freight to FBA | User input |
| **FBA Fulfillment** | Amazon pick, pack, ship | User input |
| **FBA Storage** | Monthly warehouse fee | User input |
| **Referral Fee** | Amazon commission (8-20%) | Auto × category rate |
| **Advertising** | PPC spend | Price × ad ratio |
| **Returns** | Return processing loss | Return rate × handling |
| **Other Fees** | Packaging, labels, prep | User input |

---

## Referral Fee Rates by Category

| Category | Rate |
|----------|------|
| Electronics / Computers | 8% |
| Camera / Photo | 8% |
| Automotive / Industrial | 12% |
| **Most Categories (default)** | **15%** |
| Clothing / Apparel | 17% |
| Jewelry | 20% |

---

## Output Format

### Cost Breakdown

```
Selling Price         $29.99   100.0%
───────────────────────────────────────
Product Cost          -$6.00    20.0%
Inbound Shipping      -$1.50     5.0%
FBA Fulfillment       -$5.50    18.3%
FBA Storage           -$0.30     1.0%
Referral Fee (15%)    -$4.50    15.0%
Advertising (10%)     -$3.00    10.0%
Returns (3%)          -$0.15     0.5%
Other Fees            -$0.50     1.7%
───────────────────────────────────────
Total Cost            $21.45    71.5%
Net Profit            $8.54     28.5%
```

### Break-Even Analysis

```
Break-even Price:     $20.50
Current Margin:       +46.3% above break-even
Safety Margin:        31.6%
```

### Pricing Recommendations

```
| Target Margin | Recommended Price | Profit/Unit |
|---------------|-------------------|-------------|
| 15%           | $23.10            | $3.47       |
| 20%           | $25.20            | $5.04       |
| 25%           | $27.72            | $6.93       |
| 30%           | $30.80            | $9.24       |
```

---

## Profitability Status

| Net Margin | Status | Recommendation |
|------------|--------|----------------|
| >20% | ✅ **Healthy** | Maintain current strategy |
| 5-20% | ⚠️ **Warning** | Optimize costs or raise price |
| 0-5% | 🔴 **Danger** | Needs adjustment |
| <0% | 💀 **Loss** | Stop or restructure |

---

## Batch Input Format

### CSV

```csv
sku,name,selling_price,product_cost,shipping_cost,fba_fee,storage_fee,ad_ratio,category
A001,Yoga Mat,29.99,6,1.5,5.5,0.3,0.1,sports
A002,Resistance Bands,19.99,3,0.8,4,0.2,0.12,sports
A003,Foam Roller,24.99,8,2,6,0.3,0.1,sports
```

### Natural Language

```
Batch calculate:
SKU A001: Yoga Mat, $29.99, cost $6, shipping $1.5, FBA $5.5
SKU A002: Bands, $19.99, cost $3, shipping $0.8, FBA $4
```

---

## Script Usage

```bash
# Default demo
python3 scripts/calculator.py

# Custom input
python3 scripts/calculator.py '{"selling_price": 29.99, "product_cost": 6, "fba_fee": 5.5}'

# Batch analysis
python3 scripts/calculator.py '[{"sku": "A001", ...}, {"sku": "A002", ...}]'
```

---

## Handling Incomplete Input

If user doesn't provide enough info, ask:

```
To calculate your profit margin, I need:

**Required:**
- Selling price
- Product cost (FOB)
- FBA fulfillment fee

**Recommended (more accurate):**
- Inbound shipping cost per unit
- FBA storage fee per unit/month
- Ad spend ratio (% of sales)
- Product category (for referral fee)

Example:
"Price $25, cost $5, FBA $4.50, shipping $1, ads 10%, category: kitchen"
```

---

## Integration with Other Skills

Looking for more e-commerce tools? Check out our other skill collections:

- **[Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)** — Specialized tools for Amazon sellers: keyword research, listing optimization, PPC campaigns
- **[eCommerce Skills](https://github.com/nexscope-ai/eCommerce-Skills)** — Cross-platform tools for all e-commerce businesses

---

## Limitations

This skill calculates margins based on user-provided costs. For real-time FBA fee lookups, exact category rates, and advanced analytics, check out **[Nexscope](https://nexscope.ai)**.

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

