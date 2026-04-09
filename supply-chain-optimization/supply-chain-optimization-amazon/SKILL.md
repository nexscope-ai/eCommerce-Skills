---
name: supply-chain-optimization-amazon-lite
version: 1.0.0
description: Supply Chain Optimization (Lite) - Diagnose bottlenecks and provide cost reduction strategies through conversation
platform: amazon
lang: en
---

# Supply Chain Optimization (Lite)

Supply chain bottleneck analysis tool - Conversation-based version

No API integration required. Collect data through guided conversation, automatically diagnose bottlenecks and output cost reduction strategies.

## Use Cases

- Amazon seller supply chain health check
- Bottleneck identification and cost optimization
- Supply chain decision support

## Workflow

### Step 1: Trigger Skill

User says:
```
Analyze my supply chain
Supply chain diagnosis
I want to optimize supply chain costs
```

### Step 2: Business Profile Collection

Guide user to describe in natural language:

```
👋 Starting Supply Chain Analysis

Please describe your situation in a sentence or two, like:
"I sell kitchen products, 15 SKUs, $50K monthly sales, sourcing from Yiwu, sea freight to FBA, shipping costs seem high"

Or just tell me what problem you want to solve.
```

**Identify and confirm:**
- Category
- SKU count
- Monthly revenue scale
- Sourcing location
- Logistics model
- Main pain points

### Step 3: Supply Chain Data Collection

Guide user to provide key data:

```
📊 I need some data to locate bottlenecks (rough numbers are fine)

**Sourcing**
• Product cost (FOB): $___/unit
• Supplier payment terms: ___ days
• Lead time: ___ days

**Logistics**
• Shipping cost per unit: $___
• Transit time: ___ days

**Sales**
• Average selling price: $___
• FBA fulfillment fee: $___/unit
• Monthly storage fee: $___/unit
• Ad spend ratio: ___%

**Inventory**
• Current inventory days: ___ days
• Long-term storage fees: Yes/No

Just reply in natural language.
```

### Step 4: Bottleneck Diagnosis

Run calculation script:

```bash
python3 scripts/calculator.py '{"product_cost": 8, "supplier_payment_days": 0, ...}'
```

Output diagnosis report:
- Key metrics table (with health status)
- Cost structure breakdown
- Top 3 bottlenecks

### Step 5: Cost Reduction Strategies

For each bottleneck provide:
- Problem description
- Impact analysis
- Specific recommendations
- Action checklist

### Step 6: Output Format Selection

```
📤 Analysis complete! Choose output format:

1️⃣ **Text** - View in current conversation (already shown)
2️⃣ **Web Chart** - Generate visual report webpage
3️⃣ **Report Doc** - Document format for sharing/presentation

Reply with number or say "generate web report"
```

---

## Benchmark Configuration

The following benchmarks can be customized based on your business:

| Metric | Healthy | Warning | Danger |
|--------|---------|---------|--------|
| Gross Margin | >40% | 30-40% | <30% |
| Shipping Ratio | <5% | 5-10% | >10% |
| Net Margin | >20% | 10-20% | <10% |
| Inventory Turnover | <45 days | 45-60 days | >60 days |
| Cash Cycle | <90 days | 90-120 days | >120 days |

To adjust, modify `BENCHMARKS` in `scripts/calculator.py`.

---

## File Structure

```
amazon-lite/
├── SKILL.md          # Index (this file)
├── SKILL.en.md       # English version
├── SKILL.zh-CN.md    # Chinese version
├── _meta.json
└── scripts/
    └── calculator.py
```

---

_Version 1.0.0 | Platform: Amazon | Lang: English_

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**

