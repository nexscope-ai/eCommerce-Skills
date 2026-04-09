---
name: warehouse-optimization
description: "E-commerce warehouse and inventory optimization advisor. Analyzes inventory health, calculates safety stock and reorder points, performs ABC analysis, evaluates fulfillment costs, and provides actionable recommendations for improving efficiency. Supports all major fulfillment models: Self-fulfillment, Amazon FBA/FBM, Walmart WFS, 3PL, Shopify Fulfillment, TikTok Shop, Dropshipping, and Hybrid setups. No API key required. Use when: (1) reducing stockouts or overstock, (2) calculating safety stock levels, (3) optimizing warehouse costs, (4) improving Amazon IPI score, (5) analyzing inventory KPIs."
metadata: {"nexscope":{"emoji":"🏭","category":"ecommerce"}}
---

# Warehouse & Inventory Optimization 🏭

Diagnose and optimize your warehouse operations: analyze inventory health, calculate safety stock, reduce costs, and improve efficiency. No API key required.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill warehouse-optimization -g
```

## Supported Fulfillment Models

| Model | Platform | Optimization Focus |
|-------|----------|-------------------|
| **Self-Fulfillment** | Any | Warehouse layout, staffing, pick/pack efficiency, storage costs |
| **Amazon FBA** | Amazon | IPI score, storage fees, aged inventory, restock limits |
| **Amazon FBM** | Amazon | Shipping speed, Prime eligibility, cost vs FBA |
| **Walmart WFS** | Walmart | Fulfillment fees, storage limits, Pro Seller status |
| **3PL** | Multi-channel | Provider costs, SLAs, contract optimization, hidden fees |
| **Shopify Fulfillment Network** | Shopify | Distributed inventory, delivery speed, cost analysis |
| **TikTok Shop Fulfillment** | TikTok | TikTok-specific requirements, shipping SLAs |
| **Dropshipping** | Any | Supplier reliability, lead times, stockout prevention |
| **Hybrid** | Multi-channel | Inventory allocation, channel balancing, split strategy |

## Usage Examples

```
Audit my warehouse operations. I'm self-fulfilling from a 2,000 sq ft warehouse.
500 SKUs, 3,000 orders/month. Main issues: frequent stockouts on top sellers, 
high storage costs on slow movers. Help me optimize.
```

```
I use FBA for my Amazon store. IPI score dropped to 350. I have excess inventory 
warnings on 40 SKUs. How do I fix this before I get storage limits?
```

```
Running FBM for my oversized products and FBA for standard. 200 orders/day total.
Which SKUs should I move to FBA vs keep FBM? Help me optimize the split.
```

```
Using ShipBob as my 3PL. Monthly bill is $8,500 for 2,000 orders. Is this competitive?
What should I negotiate or consider switching?
```

---

## First Interaction

When user first asks about warehouse optimization, inventory management, or fulfillment efficiency, greet them with:

```
🏭 Warehouse Optimization ready!

I'll help you diagnose issues and optimize your inventory operations.

**Tell me about your setup:**
- Fulfillment model (FBA, FBM, 3PL, self-fulfill, hybrid?)
- Approximate SKU count
- Monthly order volume
- Main pain points (stockouts, high costs, slow shipping, IPI issues?)

Or just describe your situation and I'll guide you from there.
```

---

## Handling Incomplete Input

```
To optimize your warehouse operations, I need:

**Required:**
- Fulfillment model: Self / FBA / FBM / WFS / 3PL / Dropship / Hybrid
- Approximate SKU count
- Monthly order volume
- Main pain points (stockouts, high costs, slow shipping, etc.)

**Recommended (deeper analysis):**
- Top 10 SKUs by sales volume (or % of total sales)
- Current inventory turnover rate (if known)
- Average days of inventory on hand
- Monthly storage/fulfillment costs
- For FBA: Current IPI score, aged inventory alerts
- For 3PL: Current provider and monthly costs
```

---

## Audit Workflow

### Step 1: Collect Current State Data

| Data Point | Why It Matters |
|------------|----------------|
| Fulfillment model | Determines optimization approach |
| SKU count | Complexity indicator |
| Monthly orders | Scale of operations |
| Top SKUs (% of sales) | For ABC analysis |
| Current turnover rate | Inventory health indicator |
| Days of inventory | Over/understock signal |
| Stockout frequency | Lost sales indicator |
| Storage costs | Cost optimization potential |
| Pick/pack accuracy | Quality indicator |

### Step 2: Calculate Key Metrics

**Inventory Turnover Rate:**
```
Inventory Turnover = Cost of Goods Sold (COGS) / Average Inventory Value
```
- **Benchmark:** 4-6x/year for most e-commerce (higher = better)
- **Low turnover (<4):** Excess inventory, capital tied up
- **High turnover (>8):** Risk of stockouts, tight supply chain

**Days of Inventory (DOI):**
```
DOI = (Average Inventory / COGS) × 365
```
- **Target:** 30-60 days for most products
- **Too high (>90 days):** Overstock, storage cost drain
- **Too low (<14 days):** Stockout risk

**Stockout Rate:**
```
Stockout Rate = (Days Out of Stock / Total Days) × 100
```
- **Target:** <2%
- **Impact:** Each 1% stockout ≈ 1% lost revenue

**Perfect Order Rate:**
```
Perfect Order Rate = (Orders Shipped Complete, On-Time, Undamaged / Total Orders) × 100
```
- **Target:** >95%

### Step 3: Perform ABC Analysis

Classify SKUs by revenue contribution:

| Class | % of SKUs | % of Revenue | Inventory Strategy |
|-------|-----------|--------------|-------------------|
| **A** | ~20% | ~80% | High priority, never stockout, frequent replenishment |
| **B** | ~30% | ~15% | Moderate priority, standard replenishment |
| **C** | ~50% | ~5% | Low priority, review for discontinuation |

**Recommendations by class:**
- **A items:** Safety stock = 2-4 weeks, reorder frequently, prime warehouse locations
- **B items:** Safety stock = 2-3 weeks, standard locations
- **C items:** Minimal safety stock, consider dropship or discontinue slow movers

### Step 4: Calculate Safety Stock & Reorder Points

**Safety Stock Formula:**
```
Safety Stock = Z × σd × √L

Where:
- Z = Service level factor (1.65 for 95%, 2.33 for 99%)
- σd = Standard deviation of daily demand
- L = Lead time in days
```

**Simplified Safety Stock (if limited data):**
```
Safety Stock = (Max Daily Sales - Avg Daily Sales) × Lead Time
```

**Reorder Point Formula:**
```
Reorder Point = (Avg Daily Sales × Lead Time) + Safety Stock
```

**Example calculation:**
```
Product: Widget A
- Average daily sales: 10 units
- Max daily sales: 18 units
- Lead time: 14 days

Safety Stock = (18 - 10) × 14 = 112 units
Reorder Point = (10 × 14) + 112 = 252 units

→ Reorder when inventory hits 252 units
→ Keep 112 units as buffer
```

### Step 5: Analyze Costs

**Fulfillment Cost Benchmarks:**

| Cost Component | Self-Fulfill | 3PL | FBA |
|----------------|--------------|-----|-----|
| Storage | $0.30-0.50/cu ft | $0.45-0.75/cu ft | $0.87-2.40/cu ft |
| Pick & Pack | Labor-based | $1.50-3.00/order | Included in fee |
| Shipping | Carrier rates | Discounted rates | Prime rates |
| Returns | Labor + space | $3-8/return | Free for buyers |

**Cost Per Order (CPO):**
```
CPO = (Storage + Labor + Packaging + Shipping) / Total Orders
```

**Inventory Carrying Cost:**
```
Carrying Cost = Average Inventory Value × Carrying Rate (typically 20-30%/year)

Includes: Storage, insurance, obsolescence, opportunity cost
```

### Step 6: Platform-Specific Analysis

**Amazon FBA:**
- **IPI Score factors:** Excess inventory %, sell-through rate, stranded inventory, in-stock rate
- **Storage fee triggers:** Aged inventory (181+ days), low IPI (<400)
- **Restock limits:** Based on IPI and sales velocity

**Amazon FBM:**
- **Prime eligibility:** Seller Fulfilled Prime requirements
- **Shipping performance:** On-time delivery, valid tracking rate
- **Cost comparison:** When FBM beats FBA (oversized, slow movers)

**Walmart WFS:**
- **Pro Seller badge:** Fulfillment performance requirements
- **Storage fees:** Generally lower than FBA
- **Limitations:** Product restrictions, geographic coverage

**3PL Providers:**
- **Contract terms:** Minimum commitments, peak surcharges
- **Hidden costs:** Receiving fees, special handling, return processing
- **Performance SLAs:** Shipping accuracy, turnaround time

### Step 7: Generate Recommendations

Prioritize by impact and effort:

```
## Recommendations

### 🔴 Critical (Do Now)
| Issue | Impact | Action | Expected Result |
|-------|--------|--------|-----------------|

### 🟡 Important (This Month)
| Issue | Impact | Action | Expected Result |
|-------|--------|--------|-----------------|

### 🟢 Optimization (This Quarter)
| Issue | Impact | Action | Expected Result |
|-------|--------|--------|-----------------|
```

---

## FBA-Specific Optimization

### IPI Score Improvement

| Factor | Target | Actions |
|--------|--------|---------|
| **Excess inventory** | <5% | Create removal orders, run promotions, liquidate |
| **Sell-through rate** | >4.5 | Improve listing, PPC, reduce price |
| **Stranded inventory** | 0% | Fix listing errors, match ASINs |
| **In-stock rate** | >90% | Increase replenishment frequency |

**Aged Inventory Prevention:**
- Monitor inventory age weekly
- Take action before 181 days (aged fee trigger)
- Options: Removal order, outlet deals, liquidation, donate

**Storage Fee Calendar:**
- **Jan-Sep:** Standard rates
- **Oct-Dec:** Peak rates (3x higher)
- **Aged inventory surcharge:** 181+ days

### FBA Restock Calculation

```
Target FBA Inventory = (Avg Daily Units × Days of Cover) + Safety Buffer

Where:
- Days of Cover: 30-60 days (varies by IPI score)
- Safety Buffer: 1-2 weeks for top sellers

Example:
- Selling 10 units/day
- Target 45 days cover
- Safety: 10 days

Target = (10 × 45) + (10 × 10) = 550 units
```

---

## 3PL Cost Optimization

### Evaluate Your 3PL Costs

| Cost Type | What to Check |
|-----------|---------------|
| **Storage** | Per pallet vs per cu ft, minimum charges |
| **Pick & Pack** | Per order vs per item, kit fees |
| **Receiving** | Per unit, per carton, or per shipment |
| **Special handling** | Fragile, hazmat, temperature-controlled |
| **Peak surcharges** | Q4 rate increases |
| **Minimum commitments** | Monthly minimums, long-term contracts |

### 3PL Benchmark Costs (2025)

| Service | Low | Average | High |
|---------|-----|---------|------|
| Storage (per pallet/mo) | $8 | $15 | $25 |
| Pick & Pack (per order) | $2.50 | $4.00 | $6.00 |
| Additional item | $0.30 | $0.75 | $1.50 |
| Receiving (per unit) | $0.20 | $0.40 | $0.75 |

### When to Switch 3PLs

- Cost per order >20% above benchmark
- SLA failures >5% of orders
- Poor communication / slow issue resolution
- No volume-based discounts after 6+ months
- Geographic mismatch (shipping zones too far)

---

## Output Format

```
# 🏭 Warehouse Optimization Report

**Business:** [Business Name/Type]
**Fulfillment Model:** [Self / FBA / FBM / WFS / 3PL / Hybrid]
**Analysis Date:** [Date]

---

## 1. Current State Summary

| Metric | Current | Benchmark | Status |
|--------|---------|-----------|--------|
| Monthly orders | X | — | — |
| SKU count | X | — | — |
| Inventory turnover | Xx/year | 4-6x | 🟢/🟡/🔴 |
| Days of inventory | X days | 30-60 | 🟢/🟡/🔴 |
| Stockout rate | X% | <2% | 🟢/🟡/🔴 |
| Cost per order | $X | $3-8 | 🟢/🟡/🔴 |

---

## 2. ABC Analysis

[SKU classification table]

---

## 3. Inventory Optimization

### Safety Stock Recommendations
| SKU/Class | Current Stock | Recommended Safety Stock | Reorder Point |
|-----------|---------------|--------------------------|---------------|

### Overstock Alert
[SKUs with excess inventory]

### Stockout Risk
[SKUs at risk of stockout]

---

## 4. Cost Analysis

[Cost breakdown and optimization opportunities]

---

## 5. Recommendations

### 🔴 Critical
[High-impact, do now]

### 🟡 Important  
[Medium-impact, this month]

### 🟢 Optimization
[Lower priority improvements]

---

## 6. Expected Results

| Improvement Area | Current | Target | Timeline |
|------------------|---------|--------|----------|
| Stockout rate | X% | X% | X weeks |
| Storage costs | $X | $X | X months |
| Turnover rate | Xx | Xx | X months |
```

---

## Calculations Reference

### Core Formulas

| Metric | Formula |
|--------|---------|
| **Inventory Turnover** | COGS / Average Inventory |
| **Days of Inventory** | (Avg Inventory / COGS) × 365 |
| **Safety Stock** | Z × σd × √Lead Time |
| **Reorder Point** | (Avg Daily Sales × Lead Time) + Safety Stock |
| **Carrying Cost** | Avg Inventory × 25% (typical rate) |
| **Cost Per Order** | Total Fulfillment Costs / Total Orders |

### Service Level Factors (Z)

| Service Level | Z Factor |
|---------------|----------|
| 90% | 1.28 |
| 95% | 1.65 |
| 97.5% | 1.96 |
| 99% | 2.33 |

---

## Limitations

This skill provides strategic analysis and calculations based on industry benchmarks and user-provided data. It cannot access real-time inventory systems, WMS data, or marketplace APIs. For integrated inventory management, check out **[Nexscope](https://www.nexscope.ai/?co-from=skill)** — Your AI Assistant for smarter E-commerce decisions.

---

## Related Skills

- **[Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)** — Keyword research, listing optimization, PPC campaigns, sales estimation
- **[eCommerce Skills](https://github.com/nexscope-ai/eCommerce-Skills)** — Cross-platform tools for all e-commerce businesses

---

**Built by [Nexscope](https://www.nexscope.ai/?co-from=skill)** — research, validate, and act on e-commerce opportunities with AI.
