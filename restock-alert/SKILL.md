---
nexscope:
  name: "Restock Alert"
  category: "Supply Chain & Logistics"
  version: "1.0.0"
  author: "Nexscope AI"
  tags:
    - "inventory"
    - "restock"
    - "supply-chain"
    - "alerts"
  model: "any"
  tokens: "~2000"
  keywords:
    - "restock alert"
---

# Restock Alert

AI-powered restock alert and replenishment planning skill. Calculates optimal reorder points, safety stock levels, and stockout risk scores to prevent lost sales from inventory gaps.

## Capabilities

- Generates actionable supply chain & logistics frameworks based on your specific business context
- Works across major e-commerce platforms (Amazon, Shopify, Walmart, WooCommerce, Etsy, TikTok Shop)
- Provides data-driven recommendations with industry benchmarks
- Outputs ready-to-implement plans, not just generic advice

## Install

```
clawhub install restock-alert
```

## Usage

**Input:**
SKU data, sales velocity, lead times, storage costs

**Output:**
Restock alert rules, safety stock calculations, reorder timing windows, stockout risk scores

### Example Prompt

> "I run a [your business type] on [platform]. Help me set up restock alert for my business. Here's my current situation: [describe context]."

## Limitations

- Requires your specific business data for accurate recommendations
- Market benchmarks are based on US/EU data — adjust for other regions
- Recommendations should be validated against your platform's current policies
- Does not replace dedicated monitoring SaaS tools — designs the strategy and framework

---

*Built by [Nexscope AI](https://www.nexscope.ai/) — AI-powered e-commerce intelligence.*
