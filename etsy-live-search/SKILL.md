---
name: etsy-live-search
version: 1.0.0
author: Publicrecords Data
description: "Live Etsy search results for any keyword, market phrase or category: price, rating, review count, Bestseller / Star Seller / Etsy's Pick badges, ad-vs-organic flag, rank position and shop. Feeds etsy-seo and ecommerce-keyword-research with real listings instead of assumptions. Uses an Apify Actor through MCP; needs an Apify token (free tier works)."
metadata: {"nexscope":{"emoji":"🔎","category":"ecommerce"}}
---

# Etsy Live Search 🔎

Give the agent real Etsy search results to reason from: what is actually ranking for a keyword right now, at what price, with which badges, and how much of page 1 is paid.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill etsy-live-search -g
```

This skill calls the **Etsy Search Scraper** Actor (`publicrecords/etsy-search-scraper`) through the Apify MCP server. Add it to your agent's MCP config once:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=publicrecords/etsy-search-scraper",
      "headers": { "Authorization": "Bearer <APIFY_TOKEN>" }
    }
  }
}
```

An Apify account is free; the Actor bills $6 per 1,000 listing rows and nothing for a blocked page. It runs on your proxy (Apify residential by default).

## What a row contains

| field | meaning |
|---|---|
| `query`, `page`, `position` | the keyword and the exact rank Etsy showed the listing at |
| `listing_id`, `url`, `title` | the listing |
| `price`, `currency` | shown price |
| `rating_value`, `review_count`, `review_count_approx` | rating; `true` when Etsy rounded ("3.8k") |
| `bestseller`, `popular_now`, `star_seller`, `etsys_pick`, `free_shipping` | badges |
| `is_ad` | sponsored slot (from Etsy's own slot list) or `null` when unknown |
| `shop_name`, `shop_id`, `shop_url` | the seller |

## Usage

Ask the agent, for example:

- "Pull page 1–3 for *personalized dog collar* and tell me the price band, how many slots are ads, and which titles carry Bestseller."
- "Run my `etsy-seo` analysis against the live top 24 for *ceramic mug* instead of guessing the competition."
- "Which shops own the most page-1 slots for *linen apron*?"

Tool call the agent makes:

```json
{ "queries": ["personalized dog collar"], "maxPages": 3 }
```

Optional filters: `is_best_seller`, `is_star_seller`, `free_shipping`, `is_discounted`, `instant_download`, `ship_to` (e.g. `"US"`). `marketPhrases` and `categoryUrls` take Etsy's `/market/` phrases and category pages.

## How it pairs with other skills

- **etsy-seo** — score a title against the titles that actually rank, not a generic rubric.
- **ecommerce-keyword-research** — replace the "estimated competition" step with counted rows: bestsellers on page 1, ad density, median price.
- **etsy-shop-velocity** — once the shops are known, check whether they are growing.

## Limits

- Results are what Etsy shows a logged-out visitor from your proxy's region.
- Etsy caps a query at 20 pages.
- If Etsy challenges a page on your proxy, the run stops with `blocked_on_your_proxy` and that page is not charged.
