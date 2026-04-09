---
name: ecommerce-content-marketing
description: "E-commerce content marketing strategy planner. Generates content calendars, topic ideas, and platform-specific strategies by analyzing customer reviews, trends, competitor content, and SEO opportunities. Two modes: (A) Build — create a full content strategy from scratch, (B) Audit — analyze existing content and find gaps. Supports TikTok, Instagram, YouTube, Pinterest, blog/SEO, and Amazon A+. No API key required. Use when: (1) planning content for a new product launch, (2) building a content calendar, (3) finding viral content ideas, (4) analyzing competitor content strategies, (5) extracting customer pain points for content topics."
metadata: {"nexscope":{"emoji":"📣","category":"ecommerce"}}
---

# E-Commerce Content Marketing Planner 📣

Plan your content marketing strategy: discover what topics resonate with your audience, analyze competitor content, find trending formats, and generate a ready-to-execute content calendar. No API key required.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill ecommerce-content-marketing -g
```

## Two Modes

| Mode | When to Use | Input |
|------|-------------|-------|
| **A — Build** | Creating content strategy from scratch | Product info + target platforms + optional competitor URLs |
| **B — Audit** | Analyzing existing content performance | Your content URLs/handles + competitor URLs |

## Supported Platforms

| Platform | Content Types |
|----------|---------------|
| **TikTok** | Short-form video, TikTok Shop, trends, duets, sounds |
| **Instagram** | Reels, Stories, carousels, static posts, Lives |
| **YouTube** | Shorts, long-form tutorials, product reviews, vlogs |
| **X (Twitter)** | Threads, short videos, product announcements, engagement posts |
| **Pinterest** | Pins, Idea Pins, product pins, boards |
| **Blog/SEO** | Articles, guides, listicles, comparison posts |
| **Amazon A+** | Brand story, enhanced product descriptions, comparison charts |

## Usage Examples

### Mode A — Build Strategy
```
Build a content marketing strategy for my portable blender brand.
Target market: US. Platforms: TikTok, Instagram, Blog.
Content goal: Brand awareness + product education.
Target audience: Health-conscious millennials, gym-goers.
Content period: 4 weeks.
```

```
Create a content calendar for my handmade candle shop on Etsy.
Platforms: Pinterest, Instagram, TikTok.
Competitor: https://www.instagram.com/brooklyncandlestudio/
Goal: Drive traffic to my Etsy store.
```

### Mode B — Audit
```
Audit my content strategy. Here's my TikTok: @mybrandhandle
Compare against competitors: @competitor1, @competitor2
Find gaps and opportunities.
```

---

## First Interaction

When user first asks about content marketing, mentions this skill, or gives a vague content-related request, greet them with:

```
✅ Content Marketing Planner ready!

I can help you with two modes:

**A — Build**: Create a full content strategy from scratch
   → Best for: New product launches, brand building, entering new platforms

**B — Audit**: Analyze your existing content and find gaps
   → Best for: Improving performance, competitive analysis, strategy refresh

Which mode do you need? Or just describe what you're working on and I'll guide you.
```

---

## Handling Incomplete Input

If user doesn't provide enough info, ask upfront:

**For Mode A — Build:**
```
To build your content strategy, I need:

**Required:**
- Product / Category (what are you selling?)
- Target Market: US / UK / DE / FR / AU / CA / JP / Global / Multi-region (specify)
- Target Platforms: TikTok / Instagram / YouTube / X (Twitter) / Pinterest / Blog / Amazon A+

**Recommended (better results):**
- Content Goal: Brand awareness / Product education / Drive conversions / All three
- Target Audience: Demographics, interests, pain points
- Competitor brand names or social handles to analyze (e.g., @brandname)
- Content Period: 4 weeks / 8 weeks / 3 months
```

**For Mode B — Audit:**
```
To audit your content, I need:

**Required:**
- Your brand's social handles (e.g., TikTok: @yourbrand, Instagram: @yourbrand)
- OR your website/blog URL
- Platforms you're currently active on

**Recommended (better results):**
- Competitor brand names or handles to compare against
- Your current posting frequency
- What's working / not working (your observations)
- Goals for improvement
```

Which mode?
- **A — Build**: Creating a new content strategy from scratch
- **B — Audit**: Analyzing existing content and finding gaps

---

## Mode A Workflow — Build Content Strategy

### Step 1: Collect Strategy Inputs

| Field | Required | Example |
|-------|----------|---------|
| `product_category` | ✅ | Portable blender, handmade candles |
| `target_market` | ✅ | US, UK, DE, FR, AU, CA, JP, Global, Multi-region |
| `platforms` | ✅ | TikTok, Instagram, YouTube, X, Pinterest, Blog, Amazon A+ |
| `content_goal` | 👍 | Awareness / Education / Conversion / All |
| `target_audience` | 👍 | Health-conscious millennials, 25-35, female |
| `competitor_urls` | 👍 | Brand URLs, social handles, or product pages |
| `content_period` | Optional | 4 weeks (default) / 8 weeks / 3 months |

### Step 2: Customer Insight Mining

Extract buyer language, pain points, and use cases from customer reviews across multiple sources.

**Review Sources to Search (in order of priority):**

| Source | How to Access | Best For |
|--------|---------------|----------|
| **Amazon Reviews** | `web_search: site:amazon.com "[product]" reviews` | Product-specific pain points |
| **Reddit** | `web_search: site:reddit.com "[product]" review OR feedback` | Honest opinions, complaints |
| **Trustpilot** | `web_search: site:trustpilot.com "[brand/product]"` | Brand reputation |
| **YouTube Comments** | `web_search: "[product]" review youtube comments` | Visual product concerns |
| **TikTok Comments** | `web_search: "[product]" tiktok comments reactions` | Gen Z language, viral concerns |
| **Google Reviews** | `web_search: "[brand]" google reviews` | Local/service feedback |
| **Niche Forums** | `web_search: "[product]" forum discussion` | Deep enthusiast insights |

**If product URL or ASIN provided:**
```
Use web_fetch on product page to extract visible reviews.
Also search: site:amazon.com "[product name]" reviews
Focus on: 3-star reviews (balanced), 5-star (what they love), 1-star (pain points).
```

**If only product category (no URL):**
```
web_search: "[product category]" customer reviews pain points
web_search: site:reddit.com "[product category]" what do you hate about
web_search: site:amazon.com "[product category]" review verified purchase
web_search: "[product category]" TikTok comments "love this" OR "hate this"
```

**Extract and categorize:**
- **Pain points**: Problems customers mention (e.g., "battery dies too fast")
- **Use cases**: How customers actually use the product (e.g., "I use it at the gym")
- **Emotional triggers**: Language that shows excitement or frustration
- **Feature highlights**: What customers praise most
- **Objections**: Hesitations before buying

Compile into **Customer Voice Bank**:
```
## Customer Voice Bank

### Pain Points (Content Opportunities)
| Pain Point | Frequency | Content Angle |
|------------|-----------|---------------|
| "Hard to clean" | High | "How to clean your blender in 30 seconds" |
| "Battery anxiety" | Medium | "Real battery test: X hours of use" |

### Use Cases (Lifestyle Content)
| Use Case | Frequency | Content Angle |
|----------|-----------|---------------|
| Post-gym smoothies | High | "Gym bag essentials" content series |
| Office lunch | Medium | "Desk lunch upgrade" trend hook |

### Emotional Language (Copy Bank)
- "Game changer for my mornings"
- "Finally a blender that actually works"
- "My kids love it"
```

### Step 3: Trend & Topic Research

Discover trending topics and seasonal content opportunities.

**Google Trends analysis:**
```
web_search: "[product category]" Google Trends seasonal demand
web_search: "[product category]" trending topics 2024 2025
```

**Platform-specific trends:**
```
web_search: "[product category]" TikTok viral trends
web_search: "[product category]" Instagram Reels trending
web_search: "[product category]" Pinterest trending ideas
```

**Seasonal & event mapping:**
```
web_search: "[product category]" seasonal marketing calendar events
```

Compile into **Trend Opportunities**:
```
## Trend Opportunities

### Currently Trending
| Trend | Platform | Relevance | Content Idea |
|-------|----------|-----------|--------------|
| "That girl" morning routine | TikTok | High | Product in aesthetic routine |
| ASMR unboxing | TikTok/YouTube | Medium | Satisfying product sounds |

### Upcoming Seasonal Opportunities
| Event/Season | Timing | Content Angle |
|--------------|--------|---------------|
| New Year fitness | Jan 1-15 | "New year, new routine" |
| Summer travel | May-Aug | "Travel-friendly products" |
| Black Friday | Nov | Gift guide, deals content |
```

### Step 4: Competitor Content Analysis

If competitor brand name or handle provided, analyze their content strategy across ALL platforms.

**Step 4.1: Discover Competitor Presence**

Given a competitor name (e.g., "BlendJet"), search for their presence on each platform:

```
web_search: "[competitor name]" TikTok official account
web_search: "[competitor name]" Instagram official
web_search: "[competitor name]" YouTube channel
web_search: "[competitor name]" Twitter OR X official
web_search: "[competitor name]" Pinterest
web_search: "[competitor name]" blog content marketing
```

Compile their social handles:
| Platform | Handle | Followers (if visible) |
|----------|--------|------------------------|
| TikTok | @[handle] | [count] |
| Instagram | @[handle] | [count] |
| YouTube | [channel] | [count] |
| X | @[handle] | [count] |
| Pinterest | [profile] | [count] |
| Blog | [URL] | — |

**Step 4.2: Analyze Content on Each Platform**

For each platform where competitor is active:

```
web_search: site:tiktok.com "@[competitor handle]" viral OR trending
web_search: "[competitor name]" Instagram content strategy what they post
web_search: "[competitor name]" YouTube most popular videos
web_search: "[competitor name]" marketing strategy case study
```

If possible, `web_fetch` their profile pages or recent posts.

**Step 4.3: Extract Strategy Insights**

For each competitor, analyze:
- **Content pillars**: What themes do they cover repeatedly?
- **Posting frequency**: How often do they post per platform?
- **Top performing content**: What formats/topics get most engagement?
- **Content formats**: Video %, carousel %, static %, UGC %?
- **Tone & style**: Professional, funny, educational, relatable?
- **Hashtag strategy**: What hashtags do they consistently use?
- **Influencer/UGC strategy**: Do they repost customer content?
- **Gaps**: What are they NOT covering that you could own?

Compile into **Competitor Analysis**:
```
## Competitor Content Analysis

### [Competitor Name]
| Aspect | Finding |
|--------|---------|
| Main platforms | TikTok, Instagram |
| Posting frequency | 1x/day TikTok, 3x/week IG |
| Top content types | How-to videos, UGC reposts |
| Tone | Casual, relatable, humor |
| Content pillars | Recipes, lifestyle, behind-scenes |

### Content Gaps (Your Opportunities)
- Competitor doesn't cover: [topic]
- Underserved format: [format]
- Missing audience segment: [segment]
```

### Step 5: SEO Content Keyword Research

Find keywords with content potential (informational intent).

```
web_search: "[product category]" content SEO keywords blog topics
web_search: "[product category]" questions people ask FAQ
web_search: "[product category]" how to guide tutorial
web_search: site:answerthepublic.com OR site:alsoasked.com "[product category]"
```

**Categorize by content type:**
- **How-to keywords**: "how to clean portable blender", "how to make smoothies"
- **Comparison keywords**: "blender vs juicer", "best portable blender for gym"
- **Problem keywords**: "blender not working", "smoothie too thick"
- **Listicle keywords**: "best smoothie recipes", "portable blender accessories"

Compile into **SEO Content Opportunities**:
```
## SEO Content Keywords

| Keyword | Search Intent | Content Type | Difficulty |
|---------|---------------|--------------|------------|
| how to clean portable blender | Informational | How-to video + blog | Low |
| best protein smoothie recipes | Informational | Listicle + video | Medium |
| portable blender vs regular | Comparison | Comparison blog | Medium |
```

### Step 6: Generate Content Pillars

Based on all research, define 3-5 content pillars:

```
## Content Pillars

| Pillar | Description | % of Content | Platforms |
|--------|-------------|--------------|-----------|
| **Education** | How-tos, tutorials, tips | 40% | All |
| **Lifestyle** | Product in real life, aesthetics | 25% | TikTok, IG, Pinterest |
| **Social Proof** | Reviews, UGC, testimonials | 20% | All |
| **Behind the Scenes** | Brand story, process, team | 10% | IG, YouTube |
| **Trending/Reactive** | Trend participation, memes | 5% | TikTok, IG |
```

### Step 7: Generate Content Calendar

Create a week-by-week content calendar based on the strategy period.

**Calendar format:**
```
## Content Calendar — Week [X]

### Monday
| Platform | Content Type | Topic | Pillar | Caption Hook |
|----------|--------------|-------|--------|--------------|
| TikTok | How-to (30s) | "3 smoothie mistakes you're making" | Education | "Stop doing this..." |
| Instagram | Carousel | Same topic, slide format | Education | "Save this for later ☝️" |

### Wednesday
| Platform | Content Type | Topic | Pillar | Caption Hook |
|----------|--------------|-------|--------|--------------|
| TikTok | Trend | [Current trend] + product | Trending | [Trend audio] |
| Pinterest | Pin | Recipe infographic | Education | "Easy protein smoothie" |

### Friday
| Platform | Content Type | Topic | Pillar | Caption Hook |
|----------|--------------|-------|--------|--------------|
| Instagram | Reel | Customer transformation/UGC | Social Proof | "When @customer said..." |
| Blog | Article | "Best smoothie recipes for weight loss" | SEO | [Meta description] |
```

**Include for each week:**
- Posting schedule per platform
- Content type and format
- Topic aligned to content pillar
- Caption hook or headline
- Relevant hashtags or sounds (for social)

---

## Mode B Workflow — Audit Existing Content

### Step 1: Collect Current Content

**Required information from user:**

| Info Needed | Example | Why |
|-------------|---------|-----|
| Social handles | TikTok: @mybrand, IG: @mybrand | To analyze your content |
| Platforms active on | TikTok, Instagram, Blog | To know where to look |
| Website/blog URL | mybrand.com/blog | To analyze SEO content |
| Competitor handles | @competitor1, @competitor2 | For benchmarking |
| Current posting frequency | "3x/week on IG, daily on TikTok" | To assess consistency |
| Known issues | "Low engagement", "Not growing" | To focus analysis |

If user only provides brand name, search for their presence:
```
web_search: "[brand name]" TikTok Instagram YouTube official
```

**Fetch content data for each platform:**
```
web_search: site:tiktok.com "@[user handle]" 
web_search: site:instagram.com "[user handle]"
web_search: "[brand name]" content recent posts
web_fetch: [provided URLs if accessible]
```

### Step 2: Analyze Current Performance

Evaluate:
- **Content mix**: What % is education, lifestyle, promo, etc.?
- **Posting frequency**: How consistent?
- **Platform fit**: Right content for right platform?
- **Engagement signals**: Comments, shares (from visible data)
- **Content gaps**: What's missing vs. competitors?

### Step 3: Generate Gap Analysis

```
## Content Audit Results

### Current State
| Metric | Your Brand | Competitor Avg |
|--------|------------|----------------|
| Posting frequency | 2x/week | 5x/week |
| Video content % | 20% | 60% |
| UGC/Social proof | 5% | 25% |

### Gaps & Opportunities
| Gap | Impact | Recommendation |
|-----|--------|----------------|
| Low video content | High | Increase to 50% video |
| No how-to content | High | Add 2 tutorials/week |
| Missing TikTok | High | Launch TikTok with 3x/week |

### Action Plan
1. [Immediate action]
2. [Short-term action]
3. [Long-term action]
```

### Step 4: Generate Recommendations

Output improved content calendar (same format as Mode A Step 7).

---

## Platform-Specific Guidelines

### TikTok
- **Optimal length**: 15-60 seconds for engagement, up to 3 min for tutorials
- **Posting frequency**: 1-3x daily for growth, 5x/week minimum
- **Best formats**: Trends + product, how-tos, before/after, POV, storytime
- **Hook**: First 1-2 seconds must grab attention
- **Sound**: Use trending audio when relevant
- **Hashtags**: 3-5 relevant hashtags, mix broad + niche

### Instagram
- **Reels**: 15-30 seconds, vertical, trending audio
- **Carousels**: 5-10 slides, educational or storytelling, strong cover
- **Stories**: Daily, behind-scenes, polls, Q&A, links
- **Posting frequency**: 4-7x/week (mix Reels + carousel + static)
- **Hashtags**: 5-15 relevant hashtags

### YouTube
- **Shorts**: <60 seconds, hook in first 2 seconds, vertical
- **Long-form**: 8-15 minutes for tutorials, strong intro + timestamps
- **Posting frequency**: 1-2x/week long-form, 3-5x/week Shorts
- **SEO**: Keyword in title, description, tags, thumbnail text

### X (Twitter)
- **Thread length**: 3-10 tweets for educational content, storytelling
- **Video**: <2:20 for native video, vertical or square
- **Posting frequency**: 3-5x/day for growth, minimum 1x/day
- **Best formats**: Hot takes, threads, product announcements, engagement questions, memes
- **Hook**: First line must be scroll-stopping
- **Engagement**: Reply to comments, quote tweet customers, join conversations
- **Hashtags**: 1-2 max, or none (hashtags less important on X)

### Pinterest
- **Pin format**: 2:3 vertical, text overlay, bright colors
- **Idea Pins**: Multi-page tutorials, step-by-step
- **Posting frequency**: 5-15 pins/day, consistency > volume
- **Keywords**: In pin title, description, board names

### Blog/SEO
- **Article length**: 1,500-2,500 words for ranking
- **Structure**: H2/H3 headers, short paragraphs, images
- **Posting frequency**: 2-4 articles/month
- **SEO**: Keyword in title, first paragraph, headers, meta description

### Amazon A+
- **Brand Story**: Lifestyle imagery, brand values, founder story
- **Comparison charts**: vs. competitors (without naming them)
- **Enhanced images**: Infographics, feature callouts, lifestyle shots
- **Focus**: Benefits over features, address common objections

---

## Output Format

```
# 📣 Content Marketing Strategy

**Product:** [Product/Category]
**Target Market:** [Market]
**Platforms:** [Platforms]
**Content Period:** [Duration]
**Content Goal:** [Goal]

---

## 1. Target Audience Profile

**Demographics:**
- Age: [range]
- Gender: [split]
- Location: [markets]

**Psychographics:**
- Interests: [list]
- Values: [list]
- Content consumption habits: [platforms, times, formats]

---

## 2. Customer Voice Bank

[Pain points, use cases, emotional language extracted from reviews]

---

## 3. Trend & Topic Opportunities

[Currently trending, upcoming seasonal, platform-specific trends]

---

## 4. Competitor Content Analysis

[Competitor strategies, content gaps, your opportunities]

---

## 5. SEO Content Keywords

[Keywords with content potential, categorized by content type]

---

## 6. Content Pillars

[3-5 pillars with % allocation and platform mapping]

---

## 7. Content Calendar

[Week-by-week calendar with specific content pieces]

---

## 8. Visual Style Guide

**Aesthetic:** [e.g., clean minimalist, bold colorful, cozy lifestyle]
**Colors:** [primary, secondary, accent]
**Typography:** [font style recommendations]
**Photo style:** [product shots, lifestyle, UGC]
**Video style:** [talking head, b-roll, text overlay]

---

## 9. Next Steps Checklist

- [ ] Set up content creation workflow
- [ ] Create template library for each content type
- [ ] Schedule first week of content
- [ ] Set up analytics tracking
- [ ] Plan first 30-day review
```

---

## Limitations

This skill uses publicly available data via web search and page fetching. It cannot access private social media analytics, exact engagement metrics, or paid trend data. For deeper analytics, check out **[Nexscope](https://www.nexscope.ai/?co-from=skill)** — Your AI Assistant for smarter E-commerce decisions.

---

## Integration with Other Skills

Looking for more e-commerce tools? Check out our other skill collections:

- **[Amazon Skills](https://github.com/nexscope-ai/Amazon-Skills)** — Specialized tools for Amazon sellers: keyword research, listing optimization, PPC campaigns, sales estimation
- **[eCommerce Skills](https://github.com/nexscope-ai/eCommerce-Skills)** — Cross-platform tools for all e-commerce businesses

---

**Built by [Nexscope](https://www.nexscope.ai/?co-from=skill)** — research, validate, and act on e-commerce opportunities with AI.
