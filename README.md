# 📊 E-Commerce Skills by Nexscope

Free AI agent skills for e-commerce businesses — cross-platform tools for pricing, PPC strategy, supply chain, brand protection & more.

Works with **OpenClaw**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and any agent that supports the [Skills format](https://skills.sh).

> **🔍 Need Amazon-specific tools?** Check out [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills) for FBA, Amazon PPC, listing optimization, and keyword research.

## Available Skills

### 💰 Pricing & Financial Planning

| Skill | Description | Status |
|-------|-------------|--------|
| [profit-margin-calculator](./profit-margin-calculator/) | Calculate profit margins with all costs included — COGS, shipping, platform fees, returns, and advertising. Supports any e-commerce platform. Break-even analysis and pricing recommendations included. No API key needed. | ✅ Available |
| tariff-calculator | Calculate import duties, customs fees, and total landed costs for cross-border e-commerce | 🔜 Coming soon |
| ecommerce-pricing-strategy | Data-driven pricing recommendations based on competitor analysis and margin targets | 🔜 Coming soon |

### 📢 Marketing & Advertising

| Skill | Description | Status |
|-------|-------------|--------|
| ecommerce-ppc | Cross-platform PPC strategy planner — recommends platforms (Google, Meta, TikTok), allocates budget, calculates ROAS targets, generates ad copy and creative briefs. No API key needed. | 🔜 Coming soon |
| ecommerce-marketing-strategy | Omnichannel marketing blueprints for e-commerce growth | 🔜 Coming soon |

### 🏭 Operations & Logistics

| Skill | Description | Status |
|-------|-------------|--------|
| [supply-chain-optimization](./supply-chain-optimization/) | End-to-end supply chain analysis — supplier evaluation, lead time optimization, inventory planning, and cost reduction strategies. Works for any product type and fulfillment model. No API key needed. | ✅ Available |
| 3pl-fulfillment | Compare third-party logistics providers by cost, speed, and coverage | 🔜 Coming soon |

### 🛡️ Brand Protection & Monitoring

| Skill | Description | Status |
|-------|-------------|--------|
| [brand-protection](./brand-protection/) | Monitor and protect your intellectual property — trademark monitoring, counterfeit detection strategies, enforcement action plans, and platform-specific brand registry guidance. No API key needed. | ✅ Available |
| brand-monitoring | Track brand mentions, sentiment, and reputation across the web | 🔜 Coming soon |

## Quick Install

### Install all skills

```bash
npx skills add nexscope-ai/eCommerce-Skills
```

### Install a specific skill

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill profit-margin-calculator
```

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill supply-chain-optimization
```

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-protection
```

### Install globally (recommended)

```bash
npx skills add nexscope-ai/eCommerce-Skills -g
```

## Usage

Once installed, just ask your AI agent naturally. The agent will automatically pick the right skill.

### 💰 profit-margin-calculator
```
Calculate margins for my product: sells for $29.99, costs $6 to manufacture, $3.50 shipping, selling on Shopify with 2.9% + $0.30 transaction fee.
```
```
Compare profit margins: sell on Amazon FBA ($34.99, fees ~35%) vs my own Shopify store ($34.99, fees ~5%).
```

### 🏭 supply-chain-optimization
```
I source products from 3 suppliers in China with 45-day lead times. Help me optimize my supply chain and reduce stockout risk.
```
```
Analyze my supply chain: MOQ 500 units, $8/unit, 60-day production, 30-day shipping. Monthly sales ~200 units.
```

### 🛡️ brand-protection
```
I'm launching a new brand for pet accessories. Help me create a brand protection strategy.
```
```
I found counterfeit versions of my product on 3 marketplaces. What's my enforcement action plan?
```

## Skill Categories

| Category | Available | Planned | Focus |
|----------|:---------:|:-------:|-------|
| **Pricing & Finance** | 1 | 2 | Margin calculation, tariffs, pricing strategy |
| **Marketing & Ads** | 0 | 2 | PPC strategy, omnichannel marketing |
| **Operations** | 1 | 1 | Supply chain, fulfillment |
| **Brand Protection** | 1 | 1 | IP protection, monitoring |

**Current: 3 skills available · 6 more planned**

## Why Free?

These skills use publicly available data and proven frameworks — no API key, no paid subscription, no setup friction. Install and go.

For advanced features like real-time market data, automated monitoring, and AI-powered recommendations, check out **[Nexscope](https://github.com/nexscope-ai)** — AI-powered tools for e-commerce sellers.

## License

MIT

---

Built by **[Nexscope AI](https://github.com/nexscope-ai)** — AI-powered e-commerce intelligence for Google Ads, Meta, TikTok, Shopify, Etsy, Walmart, and more.
