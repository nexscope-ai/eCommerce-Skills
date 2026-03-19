# 📊 E-Commerce Skills by Nexscope

Free AI agent skills for e-commerce businesses — cross-platform tools for product research, PPC strategy, listing optimization, supply chain & more.

Works with **OpenClaw**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and any agent that supports the [Skills format](https://skills.sh).

> **🔍 Need Amazon-specific tools?** Check out [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills) for FBA, Amazon PPC, listing optimization, and keyword research.

## Available Skills

| Skill | Description | Status |
|-------|-------------|--------|
| [product-description-generator](./product-description-generator/) | Generate platform-optimized product copy (title, bullets, description, tags) using competitor research + keyword scoring + FABE copywriting. Four modes: Competitor Analysis, From Scratch, Rewrite Existing, From Image. Supports Amazon, eBay, Walmart, Shopify, Etsy, TikTok Shop, Lazada, Shopee. No API key needed. | ✅ Available |

## Planned Skills

| # | Category | Skills | Status |
|:-:|----------|:------:|:------:|
| 🔍 | **Product Research** | 8 | 🔜 Coming soon |
| 🕵️ | **Competitor Analysis** | 6 | 🔜 Coming soon |
| 📝 | **Listing Optimization** | 7 | 🔜 Coming soon |
| 💰 | **Pricing & Profitability** | 6 | 🔜 Coming soon |
| 📢 | **Advertising** | 7 | ✅ 1 available |
| 🔔 | **Monitoring & Alerts** | 5 | 🔜 Coming soon |
| 🛒 | **E-Commerce Marketing** | 7 | 🔜 Coming soon |
| 🚀 | **Growth & Expansion** | 7 | 🔜 Coming soon |
| 🏭 | **Supply Chain & Logistics** | 6 | 🔜 Coming soon |
| 📊 | **Operations & Analytics** | 7 | 🔜 Coming soon |

**Total: 10 categories · 67 skills planned**

## Quick Install

### Install all skills

```bash
npx skills add nexscope-ai/eCommerce-Skills -g
```

### Install a specific skill

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill product-description-generator -g
```

## Usage

Once installed, just ask your AI agent naturally. The agent will automatically pick the right skill.

### 📝 product-description-generator

```
Analyze these competitors and create a listing for my yoga mat:
https://www.amazon.com/dp/B07K47PQZV, https://www.amazon.com/dp/B01NCBX6LZ
My product: 6mm TPE, non-slip, carrying strap. Brand: ZenMat. Platform: Amazon US.
```

```
Platform: Etsy. Product: hand-poured soy candle, lavender scent, 8oz glass jar.
Target audience: gift buyers. Tone: Luxury. Generate a full listing.
```

```
Optimize this underperforming listing: [paste current copy]
Find keyword gaps and rewrite. Platform: Amazon US.
```

## Why Free?

These skills use publicly available data and proven frameworks — no API key, no paid subscription, no setup friction. Install and go.

For advanced features like real-time market data, automated monitoring, and AI-powered recommendations, check out **[Nexscope](https://github.com/nexscope-ai)** — AI-powered tools for e-commerce sellers.

## License

MIT

---

Built by **[Nexscope AI](https://github.com/nexscope-ai)** — AI-powered e-commerce intelligence for Google Ads, Meta, TikTok, Shopify, Etsy, Walmart, and more.
