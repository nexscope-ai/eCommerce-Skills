# 📊 E-Commerce Skills by Nexscope

Free AI agent skills for e-commerce businesses — cross-platform tools for marketing, profit analysis, brand protection, supply chain & more.

Works with **OpenClaw**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and any agent that supports the [Skills format](https://skills.sh).

> **🔍 Need Amazon-only tools?** Check out [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills) for FBA calculators, listing optimization, PPC campaigns, and keyword research.

## Available Skills

### 📢 Marketing & Content

| Skill | Description | Status |
|-------|-------------|--------|
| [ecommerce-content-marketing](./ecommerce-content-marketing/) | Content marketing strategy planner — customer reviews, trends, competitor analysis, content calendars. | ✅ Available |
| [ecommerce-email-marketing-builder](./ecommerce-email-marketing-builder/) | Email marketing campaign builder — flows, sequences, templates, automation strategies. | ✅ Available |
| [ecommerce-ppc-strategy-planner](./ecommerce-ppc-strategy-planner/) | Cross-platform PPC strategy — Google, Meta, TikTok ads. ROAS targets, budget allocation. | ✅ Available |
| [ecommerce-marketing-strategy-builder](./ecommerce-marketing-strategy-builder/) | Full-stack omnichannel marketing — paid ads, SEO, email/SMS, content, social, influencers. | ✅ Available |
| [product-description-generator](./product-description-generator/) | Product descriptions for any platform — Amazon, eBay, Walmart, Shopify, Etsy, TikTok Shop. | ✅ Available |

### 🛡️ Brand Protection

| Skill | Platforms | Status |
|-------|-----------|--------|
| [brand-protection](./brand-protection/) | Amazon, eBay, Shopify, TikTok, Walmart | ✅ Available |

Detect hijackers, counterfeits, unauthorized sellers, MAP violations. Includes complaint templates for Brand Registry, VeRO, DMCA.

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection/brand-protection-amazon -g
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection/brand-protection-ebay -g
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection/brand-protection-shopify -g
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection/brand-protection-tiktok -g
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection/brand-protection-walmart -g
```

### 💰 Profit Margin Calculator

| Skill | Platforms | Status |
|-------|-----------|--------|
| [profit-margin-calculator](./profit-margin-calculator/) | Amazon, Shopify, TikTok, Walmart | ✅ Available |

Calculate cost breakdowns, profit margins, break-even points, and pricing recommendations. Platform-specific fee structures included.

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator/profit-margin-calculator-amazon -g
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator/profit-margin-calculator-shopify -g
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator/profit-margin-calculator-tiktok -g
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator/profit-margin-calculator-walmart -g
```

### 📦 Supply Chain Optimization

| Skill | Platforms | Status |
|-------|-----------|--------|
| [supply-chain-optimization](./supply-chain-optimization/) | Amazon, Shopify, TikTok, Walmart | ✅ Available |

Diagnose bottlenecks in cash flow, inventory, fulfillment costs. Platform-specific optimization strategies.

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization/supply-chain-optimization-amazon -g
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization/supply-chain-optimization-shopify -g
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization/supply-chain-optimization-tiktok -g
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization/supply-chain-optimization-walmart -g
```

### 🔍 Review Checker

| Skill | Platforms | Status |
|-------|-----------|--------|
| [review-checker](./review-checker/) | Amazon, eBay, Walmart | ✅ Available |

Review authenticity analyzer — detect fake reviews, suspicious patterns, rating manipulation, time clustering.

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill review-checker/amazon-review-checker -g
npx skills add nexscope-ai/eCommerce-Skills --skill review-checker/ebay-review-checker -g
npx skills add nexscope-ai/eCommerce-Skills --skill review-checker/walmart-review-checker -g
```

### 🎯 Product Differentiation

| Skill | Platforms | Status |
|-------|-----------|--------|
| [product-differentiation](./product-differentiation/) | Amazon, eBay, Shopify, TikTok | ✅ Available |

Analyze competitor weaknesses, extract pain points from negative reviews, identify unique selling points, generate differentiation strategies.

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation/product-differentiation-amazon -g
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation/product-differentiation-ebay -g
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation/product-differentiation-shopify -g
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation/product-differentiation-tiktok -g
```

## Quick Install

### Install all skills

```bash
npx skills add nexscope-ai/eCommerce-Skills -g
```

### Install by category

```bash
# All brand protection skills
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection -g

# All profit calculators
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator -g

# All supply chain skills
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization -g

# All review checkers
npx skills add nexscope-ai/eCommerce-Skills --skill review-checker -g

# All product differentiation
npx skills add nexscope-ai/eCommerce-Skills --skill product-differentiation -g
```

### Install individual skills

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-content-marketing -g
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-email-marketing-builder -g
npx skills add nexscope-ai/eCommerce-Skills --skill product-description-generator -g
```

## Usage

Once installed, just ask your AI agent naturally. The agent will automatically pick the right skill.

### 📣 ecommerce-content-marketing
```
Build a content marketing strategy for my portable blender brand. Platforms: TikTok, Instagram.
```

### 🛡️ brand-protection
```
I found a hijacker on my Amazon listing. Help me file a Brand Registry complaint.
```

### 💰 profit-margin-calculator
```
Calculate my Shopify margins: Product cost $12, shipping $4, price $39.99, CAC $15
```

### 📦 supply-chain-optimization
```
My TikTok Shop return rate is 18%. Affiliate commissions eating my margins. How to optimize?
```

### 🔍 review-checker
```
Analyze reviews for this Amazon product — are they authentic or manipulated?
```

### 🎯 product-differentiation
```
Analyze my competitors' negative reviews and help me differentiate my product.
```

## Summary

| Category | Skills | Platforms |
|----------|:------:|-----------|
| 📢 Marketing & Content | 5 | Cross-platform |
| 🛡️ Brand Protection | 5 | Amazon, eBay, Shopify, TikTok, Walmart |
| 💰 Profit Calculator | 4 | Amazon, Shopify, TikTok, Walmart |
| 📦 Supply Chain | 4 | Amazon, Shopify, TikTok, Walmart |
| 🔍 Review Checker | 3 | Amazon, eBay, Walmart |
| 🎯 Product Differentiation | 4 | Amazon, eBay, Shopify, TikTok |
| **Total** | **25** | |

## Why Free?

These skills use publicly available data and proven frameworks — no API key, no paid subscription, no setup friction. Install and go.

Want more? **[Nexscope](https://www.nexscope.ai/)** — Your AI Assistant for smarter E-commerce decisions.

## Related

Looking for Amazon-only tools? Check out **[Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)** — FBA calculator, keyword research, listing optimization, PPC campaigns, sales estimation.

## License

MIT

---

Built by **[Nexscope](https://www.nexscope.ai/)** — research, validate, and act on e-commerce opportunities with AI.
