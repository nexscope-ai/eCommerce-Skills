---
name: product-description-generator
description: "E-commerce product description generator for any platform. Generates optimized titles, bullet points, descriptions, and backend keywords using competitor research + keyword scoring + FABE copywriting. Four modes: (A) Competitor Analysis — reverse-engineer competitor listings, (B) From Scratch — generate from product specs, (C) Rewrite — optimize existing listing with gap analysis, (D) From Image — analyze product photo and generate copy. Supports Amazon, eBay, Walmart, Shopify, Etsy, TikTok Shop, Lazada, Shopee. No API key required. Use when: (1) writing a new product listing, (2) analyzing what makes competitors rank, (3) improving an underperforming listing, (4) generating copy from a product image."
metadata: {"nexscope":{"emoji":"📝","category":"ecommerce"}}
---

# Product Description Generator 📝

Generate platform-optimized product copy — titles, bullet points, descriptions, and backend keywords — for any major e-commerce platform. No API key required.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill product-description-generator -g
```

## Four Modes

| Mode | Starting Point | Best For |
|------|----------------|----------|
| **A — Competitor Analysis** | Have competitor URLs to study | Reverse-engineering what's working |
| **B — From Scratch** | Have product specs, no competitors | New product launches |
| **C — Rewrite** | Have existing listing to improve | Underperforming listings |
| **D — From Image** | Have product photo only | Quick draft from visual |

## Supported Platforms

| Platform | Output Components |
|----------|-------------------|
| **Amazon** | Title (≤200) + 5 Bullets (≤500 each) + Description (≤2000) + Backend (≤250 bytes) |
| **eBay** | Title (≤80) + HTML Description |
| **Walmart** | Title (≤75) + Short Desc (≤150) + 10 Features + Long Desc |
| **Shopify/DTC** | SEO Title (≤60) + Meta Desc (≤160) + Product Description |
| **Etsy** | Title (≤140) + Description + 13 Tags (≤20 each) |
| **TikTok Shop** | Title (≤255) + Description (≤1000) |
| **Lazada/Shopee** | Title (≤120) + 5 Highlights + Description |

Default: **Amazon** if not specified.

## Usage Examples

### Mode A — Competitor Analysis
```
Analyze these competitors and create a listing for my yoga mat:
- https://www.amazon.com/dp/B07K47PQZV
- https://www.amazon.com/dp/B01NCBX6LZ
My product: 6mm TPE, non-slip, comes with carrying strap. Brand: ZenMat.
```

### Mode B — From Scratch
```
Platform: Amazon US. Product: portable blender.
Specs: 380ml, USB-C rechargeable, BPA-free Tritan, 6 blades.
Target audience: gym-goers, office workers.
Tone: Friendly.
```

### Mode C — Rewrite
```
Optimize this underperforming listing:
[paste current title and bullets]
Find keyword gaps and rewrite. Platform: Amazon US.
```

### Mode D — From Image
```
Platform: Etsy. Here's my product image: [image]
It's a hand-poured soy candle. Brand: WickCraft.
Generate a full listing.
```

---

## Mode A Workflow — Competitor Analysis

### Step 1: Fetch Competitor Listings

For each competitor URL provided:

```
Use web_fetch to retrieve the product page.
Extract:
- Title (full product title)
- Bullets / Features (all feature points)
- Description / A+ Content (if visible)
- Price and review count (for context)
- Brand name (⚠️ flag for exclusion)
```

If `web_fetch` fails, fallback:
```
Use web_search: "[product name]" site:amazon.com
Extract data from search snippets and cached results.
```

Compile into **Competitor Table**:
| # | Title | Key Features | Brand | Price | Reviews |
|---|-------|--------------|-------|-------|---------|

### Step 2: Extract Keywords from Competitors

Parse all competitor content and extract keywords in these categories:

- **Product-type terms**: What it IS (yoga mat, exercise mat, fitness mat)
- **Feature terms**: What it DOES (non-slip, eco-friendly, extra thick)
- **Use-case terms**: WHERE/WHEN used (home gym, yoga studio, pilates)
- **Audience terms**: WHO buys (beginners, athletes, seniors)
- **Attribute terms**: Specs (6mm, TPE material, 72 inches)

⚠️ **Critical**: Remove all competitor brand names — never include them in output.

### Step 3: Expand Keywords

Discover additional keywords competitors missed:

```
web_search: "[product type]" best seller features what buyers want
web_search: "[product type]" review complaints common issues
```

Platform autocomplete (search the product type and note suggestions):
```
web_search: site:[platform].com "[product type]"
```

### Step 4: Score and Prioritize Keywords

Score each keyword (1-9 points):

| Dimension | Scoring |
|-----------|---------|
| **Frequency** | In 3+ competitor titles = 3 pts / In 1-2 = 2 pts / Bullets only = 1 pt |
| **Relevance** | Core descriptor = 3 pts / Feature = 2 pts / Peripheral = 1 pt |
| **Opportunity** | Few competitors use = 3 pts / Most use = 2 pts / All use = 1 pt |

Assign to tiers:
```
🔴 Primary (7-9 pts)   → Title
🟡 Secondary (4-6 pts) → Bullets
🟢 Tertiary (2-3 pts)  → Description
⚪ Backend (1 pt)       → Tags/Search Terms
```

Proceed to **Generate Copy**.

---

## Mode B Workflow — From Scratch

### Step 1: Collect Product Info

| Field | Required | Example |
|-------|----------|---------|
| `product_name` | ✅ | Portable blender |
| `platform` | ✅ | Amazon US |
| `brand` | ✅ | BlendJet |
| `key_features` | ✅ | USB-C, 6 blades, BPA-free |
| `specs` | ✅ | 380ml, 175W motor |
| `target_audience` | 👍 | Gym-goers, travelers |
| `use_cases` | 👍 | Smoothies, protein shakes |
| `tone` | Optional | Professional / Friendly / Luxury / Urgent |

### Step 2: Discover Keywords

Since no competitors provided, discover keywords:

```
web_search: "[product name]" best seller [platform] features
web_search: "[product name]" review what customers love
web_search: "[product name]" vs alternatives comparison
```

Extract keywords from top 5 results.

### Step 3: Score Keywords

Follow same scoring as Mode A Step 4.

Proceed to **Generate Copy**.

---

## Mode C Workflow — Rewrite Existing

### Step 1: Analyze Current Listing

User provides current title, bullets, description.

Parse and extract:
- All keywords currently in the listing
- Structure and format
- Obvious gaps (missing features, weak benefits)

### Step 2: Gap Analysis

Compare current keywords vs. ideal keywords:

```
web_search: "[product type]" top keywords [platform]
```

If competitor URLs provided, run Mode A Steps 1-2.

Create gap report:

```
## Keyword Gap Analysis

### ✅ Keywords You Have
| Keyword | Title | Bullets | Description |
|---------|-------|---------|-------------|
| yoga mat | ✅ | ✅ | ✅ |

### ❌ Keywords You're Missing
| Keyword | Priority | Found In Competitors | Recommendation |
|---------|----------|---------------------|----------------|
| non-slip | High | 3/3 titles | Add to title |
| eco-friendly | Medium | 2/3 bullets | Add to bullet 2 |

Coverage: 12/20 keywords (60%) → Target: 90%+
```

### Step 3: Rewrite

Generate new copy incorporating missing keywords.

Show **Before → After** for each component.

Proceed to **Generate Copy**.

---

## Mode D Workflow — From Image

### Step 1: Analyze Image

Examine the product image carefully:

```
Image Analysis:
- Product type: [identified]
- Visible materials: [list]
- Key visual features: [list]
- Colors/variants: [list]
- Apparent use cases: [list]
- Package contents visible: [list]
```

### Step 2: Confirm with User

Ask for details not visible in image:
- Brand name
- Hidden specs (weight, capacity, certifications)
- Target audience
- Price point / positioning

### Step 3: Discover Keywords

Follow Mode B Step 2 using image analysis as product info.

Proceed to **Generate Copy**.

---

## Generate Copy

Final step for all modes after keyword priority table is built.

### Writing Framework: FABE

Apply to every bullet:

```
F — Feature:   What the product HAS or DOES
A — Advantage: Why this is BETTER than alternatives
B — Benefit:   What this MEANS for the customer
E — Evidence:  Spec, number, or proof that backs the claim
```

**Lead with the Benefit** — customers buy outcomes, not features.

Example:
```
❌ "Made with BPA-free Tritan plastic"
✅ "SAFE FOR YOUR FAMILY — BPA-free Tritan plastic means no harmful chemicals leaching into your smoothies, even after 1000+ uses"
```

### Platform-Specific Writing Rules

#### Amazon
- **Title**: Brand + Primary Keyword + Attribute + Attribute + Secondary Keyword
- **Bullets**: [CAPS HEADER] — Benefit-led sentence with 1-2 keywords
- **Description**: Hook → Features → Use cases → What's in box → CTA
- **Backend**: Space-separated, no duplicates, ≤250 bytes
- ⚠️ Cosmo Algorithm: Use situational language (when/where/why), cover multiple use cases

#### eBay (Cassini)
- **Title**: Front-load exact-match keywords, 80 chars max
- **Description**: Repeat top 3 keywords naturally, include specs table

#### Shopify (Google SEO)
- **SEO Title**: Primary keyword + brand, written for Google
- **Meta**: Keyword + benefit + CTA, drives CTR from search

#### Etsy (Tag Matching)
- **Title**: Long-tail phrase first, match tags exactly
- **Tags**: 13 tags, match phrases in title, include occasions

#### TikTok Shop (Social Commerce)
- **Title**: Lead with problem/desire, hook-driven
- **Description**: Conversational, emoji-friendly, problem→solution

### Tone Guide

| Tone | Style |
|------|-------|
| **Professional** | Authoritative, spec-focused |
| **Friendly** | Conversational, benefit-focused |
| **Urgent** | Scarcity-driven, action words |
| **Luxury** | Premium, sensory language |

Default: **Professional**

---

## Output Format

```
# ✅ Your Listing — Ready to Copy

Platform: [Platform] | Marketplace: [XX] | Tone: [Tone]

## Title
[title]

## Bullets / Features
1. [HEADER] — [text]
2. [HEADER] — [text]
3. [HEADER] — [text]
4. [HEADER] — [text]
5. [HEADER] — [text]

## Description
[description]

## Backend Keywords / Tags
[keywords per platform format]

---

# 📊 Diagnostic Report

**Mode:** [A/B/C/D] | **Keywords scored:** [N] | **Competitors analyzed:** [N]

## Keyword Priority Table
| # | Keyword | Score | Tier | Placed In |
|---|---------|-------|------|-----------|
| 1 | ... | 8 | 🔴 | Title |

## Coverage Map
| Keyword | Title | Bullets | Desc | Backend | Status |
|---------|-------|---------|------|---------|--------|
| [kw] | ✅ | ✅ | ❌ | — | 🟢 |

Coverage: X/Y (Z%)
🟢 90%+ Excellent · 🟡 70-89% Good · 🔴 <70% Needs work

## ⚠️ Excluded Brands
[competitor brands removed from output]
```

---

## Handling Incomplete Input

If user doesn't specify enough info, ask upfront:

```
I need a few more details to generate your listing:

**Required:**
- Platform: Amazon / eBay / Walmart / Shopify / Etsy / TikTok Shop / Lazada / Shopee
- Product name and key features
- Brand name

**Helpful (better output):**
- Target audience
- 1-3 competitor URLs to analyze
- Tone preference

Which mode?
A — I have competitor URLs to analyze
B — Starting from scratch with product specs
C — I have an existing listing to improve
D — I have a product image
```

---

## Limitations

This skill uses publicly available data via web search and page fetching. It cannot access:
- Exact search volume data
- Backend keywords of existing listings
- Platform-specific ranking metrics

For deeper keyword data, chain with **[amazon-keyword-research](https://github.com/nexscope-ai/Amazon-Skills)** first.

---

**Part of [Nexscope AI](https://github.com/nexscope-ai) — AI tools for e-commerce sellers.**
