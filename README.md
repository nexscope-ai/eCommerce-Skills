# 📊 E-Commerce Skills by Nexscope

Free AI agent skills for e-commerce businesses — cross-platform tools for product research, PPC strategy, listing optimization, supply chain & more.

Works with **OpenClaw**, **Claude Code**, **Cursor**, **Windsurf**, **Codex**, and any agent that supports the [Skills format](https://skills.sh).

> **🔍 Need Amazon-specific tools?** Check out [Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills) for FBA, Amazon PPC, listing optimization, and keyword research.

## Available Skills

| Skill | Description | Status |
|-------|-------------|--------|
| [product-description-generator](./product-description-generator/) | Generate platform-optimized product copy (title, bullets, description, tags) using competitor research + keyword scoring + FABE copywriting. Two modes: (A) Create from scratch with optional competitor analysis, (B) Optimize existing listing with keyword gap analysis. Supports Amazon, eBay, Walmart, Shopify, Etsy, TikTok Shop, Lazada, Shopee. No API key needed. | ✅ Available |
| [ecommerce-ppc-strategy-planner](./ecommerce-ppc-strategy-planner/) | Cross-platform PPC strategy planner — analyzes your product and margins, recommends the right ad platforms (Google Ads, Meta Ads, TikTok Ads), calculates ROAS targets, allocates budget, and generates campaign briefs with ad copy + creative asset prompts. Two modes: Build from scratch or Optimize existing campaigns. No API key needed. | ✅ Available |

## Quick Install

```bash
# Install all skills
npx skills add nexscope-ai/eCommerce-Skills -g
```

```bash
# Install a specific skill
npx skills add nexscope-ai/eCommerce-Skills --skill product-description-generator -g
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-ppc-strategy-planner -g
```

## Usage

Once installed, just ask your AI agent naturally. The agent will automatically pick the right skill.

### 📝 product-description-generator

```
Create a listing for my yoga mat on eBay UK.
Competitors: https://www.ebay.co.uk/itm/123456789
My product: 6mm TPE, non-slip, carrying strap included. Brand: ZenMat. Tone: Friendly.
```

```
Optimize this Shopify listing: https://mystore.com/products/portable-blender
Find keyword gaps and rewrite.
```

```
Platform: Etsy. Product: hand-poured soy candle, lavender scent, 8oz glass jar.
Target audience: gift buyers. Brand: WickCraft. Tone: Luxury.
```

### 📢 ecommerce-ppc-strategy-planner

```
I sell handmade candles on Shopify. Price $34, cost $8. Monthly ad budget $2,000. Help me plan which platforms to advertise on.
```

```
Running Google Shopping (ROAS 3.2x, $3,000/mo) and Facebook ($1,800/mo, ROAS 1.4x). Margin is 45%. Should I shift budget?
```

```
I'm launching a fitness resistance band set, $29.99, 60% margin. $5,000/month budget. Where should I advertise?
```

## Skill Categories

*Skills are being built and published progressively. Star this repo to get notified!*

| # | Category | Skills | Status |
|:-:|----------|:------:|:------:|
| 🔍 | **Product Research** | 8 | 🔜 Coming soon |
| 🕵️ | **Competitor Analysis** | 6 | 🔜 Coming soon |
| 📝 | **Listing Optimization** | 8 | ✅ 1 available |
| 💰 | **Pricing & Profitability** | 6 | 🔜 Coming soon |
| 📢 | **Advertising** | 7 | ✅ 1 available |
| 🔔 | **Monitoring & Alerts** | 5 | 🔜 Coming soon |
| 🛒 | **E-Commerce Marketing** | 7 | 🔜 Coming soon |
| 🚀 | **Growth & Expansion** | 7 | 🔜 Coming soon |
| 🏭 | **Supply Chain & Logistics** | 6 | 🔜 Coming soon |
| 📊 | **Operations & Analytics** | 7 | 🔜 Coming soon |

**Current: 2 skills available · 65 more planned**

## Why Free?

These skills use publicly available data and proven frameworks — no API key, no paid subscription, no setup friction. Install and go.

Want more? **[Nexscope](https://www.nexscope.ai/)** — your AI assistant for smarter e-commerce decisions. Research products, validate demand, spot trends, and get clear next steps in one conversation.

## License

MIT

---

Built by **[Nexscope](https://www.nexscope.ai/)** — research, validate, and act on e-commerce opportunities with AI.
