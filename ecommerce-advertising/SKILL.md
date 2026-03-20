---
name: ecommerce-advertising
description: "Full-funnel e-commerce advertising planner for cross-channel campaigns. Covers keyword research, competitor ad analysis, audience insights, campaign architecture, budget allocation across channels (Amazon PPC, Google Ads, Meta Ads, TikTok Ads, Pinterest Ads), ad copy generation, and creative direction. Helps you build a complete multi-channel ad strategy from scratch. Works for Amazon, Shopify, Walmart, eBay, and multi-channel sellers. No API key required."
metadata:
  nexscope:
    emoji: "📢"
    category: ecommerce
---

# E-Commerce Advertising 📢

Build your full-funnel advertising strategy across all major channels: Amazon PPC, Google Ads, Meta Ads, TikTok Ads, and Pinterest Ads.

**Supported platforms:** Amazon, Shopify, Walmart, eBay, TikTok Shop, WooCommerce, Standalone DTC

Built by [Nexscope](https://www.nexscope.ai/) — your AI assistant for smarter e-commerce decisions.

## Install

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-advertising -g
```

## Capabilities

- **Keyword research**: Core keywords, long-tail opportunities, competition density, suggested bid ranges
- **Competitor ad analysis**: Which channels competitors use, what angles they run, what's working
- **Audience insights**: Target persona extraction from reviews and market data
- **Campaign architecture**: Campaign structure, ad group organization, targeting strategies
- **Cross-channel budget allocation**: How much to spend on each channel based on stage and goals
- **Ad copy generation**: Headlines, descriptions, CTAs optimized per platform
- **KPI targets**: ACoS, ROAS, CTR, CVR benchmarks for your category

## Usage Examples

```
I'm launching a silicone kitchen utensil set on Amazon US, also have a Shopify store. Price $29.99, cost $8. Monthly ad budget $3,000. Help me plan my advertising strategy.
```

```
Selling premium dog treats on Shopify. $45 AOV, 55% margin. Want to start with $2,000/month ads. Which platforms should I prioritize?
```

```
I have a TikTok Shop selling phone accessories. Budget $1,500/month. What's my ad strategy?
```

---

## How This Skill Works

### Step 1: Collect Information

Parse from the user's prompt:
- Product / category
- Target market (US, UK, DE, JP, CA, etc.)
- Sales platform(s)
- Monthly ad budget
- Profit margin
- Business stage (launch / growth / scale)
- Competitor ASINs or brand names (optional)

### Step 2: One Follow-Up Question Set

```
Great — kitchen utensils at $29.99 with $3,000/month budget. To build your strategy:

1. Your product cost per unit: $_____

2. Primary goal?
   a) Launch — build awareness, get initial sales
   b) Growth — scale proven winners
   c) Profitability — optimize for max ROAS
   d) Seasonal push — short-term spike

3. How do customers find products like yours?
   a) They search for it (e.g., "silicone spatula")
   b) They discover it visually
   c) They need to see it in action (demo)
   d) Not sure

4. Brand positioning?
   a) Premium  b) Mid-market  c) Budget  d) Other: ___

5. Competitors to analyze? (ASIN or brand, optional)

Reply like: 1. $8  2b  3a  4b  5. B09XYZ123
```

### Step 3: Execute Analysis

Generate the full output using the frameworks below.

---

## Keyword Research

Use `web_search` to gather keyword data.

**Step 1: Search for seed keywords**
```
web_search: "[product] keywords"
web_search: "[product] amazon autocomplete"
```

**Step 2: Research long-tail opportunities**
```
web_search: "[product] for [use case]"
web_search: "best [product] for [specific need]"
```

**Step 3: Analyze competition**
```
web_search: "[keyword] amazon sponsored"
```

| Competition | Indicators | Strategy |
|:-----------:|------------|----------|
| **Low** | <10K results, few ads | Bid aggressively |
| **Medium** | 10K-50K results | Balanced bid |
| **High** | 50K+ results | Long-tail focus |

**Bid Ranges by Platform:**
| Platform | Low | Med | High |
|----------|:---:|:---:|:----:|
| Amazon PPC | $0.30-0.60 | $0.60-1.20 | $1.20-2.50 |
| Google Shopping | $0.20-0.50 | $0.50-1.00 | $1.00-2.00 |
| Google Search | $0.50-1.00 | $1.00-2.00 | $2.00-4.00 |

---

## Competitor Ad Analysis

Use `web_search` and `web_fetch` to gather competitor intelligence.

**Step 1: Identify competitors**
```
web_search: "[product] best sellers amazon"
web_search: "[product category] top brands"
```

**Step 2: Analyze channel presence**
```
web_search: "[brand name] amazon sponsored"
web_fetch: https://www.facebook.com/ads/library/?q=[brand]
web_search: "[brand name] tiktok ads"
```

**Step 3: Extract ad angles**
```
web_search: "[competitor brand] marketing"
web_fetch: [competitor website]
```

**Step 4: Identify gaps**
- Angles competitors aren't using
- Platforms where they're weak
- Keywords they're missing

---

## Audience Insights

Use `web_search` and `web_fetch` to build personas.

**Step 1: Mine reviews**
```
web_fetch: https://www.amazon.com/dp/[ASIN]
web_search: "[product] reviews reddit"
web_search: "[product] complaints"
```

**Step 2: Build personas**
- Demographics (age, gender from review hints)
- Motivations (why they buy)
- Pain points (what they hate)
- Language (exact phrases for ad copy)

**Step 3: Extract ad copy angles**
- From positive reviews → benefits to highlight
- From negative competitor reviews → problems to solve

---

## Channel Selection

| Product Type | Primary Channel | Secondary |
|--------------|----------------|-----------|
| Search-driven | Amazon PPC / Google Shopping | Meta retargeting |
| Visual / lifestyle | Meta Ads | Pinterest, Google |
| Demo-driven | TikTok Ads | Meta, YouTube |
| Impulse (<$30) | TikTok, Meta | Amazon PPC |
| High-ticket (>$100) | Google Search | Meta retargeting |

### Platform Benchmarks (2025-2026)

| Platform | Avg ROAS | Top Quartile | Avg CPC |
|----------|:--------:|:------------:|:-------:|
| Amazon PPC | 3.5x | 5x+ | $0.80-1.50 |
| Google Shopping | 4.5x | 6x+ | $0.50-1.20 |
| Meta Ads | 2.2x | 4-5x | $0.70-1.50 |
| TikTok Ads | 1.4x | 2.5x+ | $0.50-1.00 |

*Sources: Triple Whale 2025, Lebesgue 2026*

### Budget Thresholds

| Budget | Strategy |
|:------:|----------|
| < $1,000 | ONE channel only |
| $1,000-3,000 | Primary (70%) + retargeting (30%) |
| $3,000-10,000 | 2-3 channels |
| $10,000+ | Full cross-channel |

---

## Budget Allocation (70-20-10)

| Allocation | Purpose |
|:----------:|---------|
| **70%** | Proven channels (highest ROAS) |
| **20%** | Promising channels (scaling) |
| **10%** | Testing / experimental |

---

## Campaign Architecture

### Amazon PPC
```
├── Exact Match - Core Keywords (40%)
├── Phrase Match - Discovery (25%)
├── Auto - Harvesting (20%)
└── Product Targeting (15%)
```

### Google Ads
```
├── Shopping - High Priority
├── Search - Brand
├── Search - Non-Brand
└── Performance Max
```

### Meta Ads
```
├── Prospecting - Interest Based
├── Prospecting - Lookalike
└── Retargeting (visitors, cart, purchasers)
```

### TikTok Ads
```
├── Broad Targeting
├── Spark Ads (boost organic)
└── Lookalike
```

---

## Ad Copy Templates

### Google Ads
```
Headline 1 (30 chars): [Keyword] - [Price/Offer]
Headline 2 (30 chars): [Key Benefit]
Headline 3 (30 chars): [Social Proof]
Description (90 chars): [What it is] + [Feature] + [CTA]
```

### Meta Ads
```
Primary (125 chars): [Hook] + [Benefit] + [Emoji]
Headline (40 chars): [Offer]
CTA: Shop Now
```

### TikTok
```
Caption (100 chars): [Hook] #hashtags
Hook formulas:
- "POV: [relatable situation]"
- "Stop buying [inferior product]"
- "This [product] changed my [routine]"
```

---

## KPI Targets

| Metric | Launch | Growth | Mature |
|--------|:------:|:------:|:------:|
| Amazon ACoS | 35-50% | 25-35% | 15-25% |
| Google ROAS | 2-3x | 3-4x | 4-6x |
| Meta ROAS | 1.5-2x | 2-3x | 3-4x |
| TikTok ROAS | 1-1.5x | 1.5-2x | 2-3x |

### Calculate Targets
```
Break-even ROAS = 1 / Profit Margin
Target ROAS = Break-even × 1.5
Max CPA = AOV × Profit Margin
```

---

## Output Format

```
# 📢 E-Commerce Advertising Strategy

**Product:** [name]
**Market:** [market]
**Budget:** $[budget]/month
**Stage:** [Launch / Growth / Scale]

## 1. Keyword Research
[Keyword tables]

## 2. Competitor Analysis
[Channel presence, angles, gaps]

## 3. Target Audience
[Personas, pain points, targeting]

## 4. Channel Strategy
[Recommended channels + budget split]

## 5. Campaign Architecture
[Platform structures]

## 6. Ad Copy
[Headlines, descriptions, hooks]

## 7. KPI Targets
[Metrics to hit]

## ⚠️ Notes
- Search volumes are estimates
- Use platform tools for precise data
```

---

## Limitations

This skill provides strategic analysis based on web research and industry benchmarks. For real-time keyword data, actual search volumes, live competitor tracking, and integrated campaign management, check out **[Nexscope](https://www.nexscope.ai/)** — Your AI Assistant for smarter E-commerce decisions.

---

## Related Skills

**For deeper PPC strategy:**
```bash
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-ppc-strategy-planner -g
```
Detailed ROAS calculations, budget allocation, and ad copy generation.

**For Amazon-specific advertising:**
```bash
npx skills add nexscope-ai/Amazon-Skills --skill amazon-ppc-campaign -g
```
Amazon Sponsored Products, Sponsored Brands, and Sponsored Display.

**All e-commerce skills:**
- [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills) — Cross-platform tools for marketing, pricing, brand protection, supply chain
- [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills) — Amazon-specific tools: FBA, PPC, listing optimization, keyword research

---

Built by [Nexscope](https://www.nexscope.ai/) — your AI assistant for smarter e-commerce decisions.
