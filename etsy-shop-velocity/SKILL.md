---
name: etsy-shop-velocity
version: 1.0.0
author: Publicrecords Data
description: "Is this Etsy shop growing, and how fast? Daily sales counters with history, 30-day deltas, a fitted sales rate and breakout flags for any Etsy shop, from a hosted daily panel — no proxy, no scraping on your side. Uses an Apify Actor through MCP; needs an Apify token (free tier works)."
metadata: {"nexscope":{"emoji":"📈","category":"ecommerce"}}
---

# Etsy Shop Velocity 📈

The question every seller tool guesses at and this one measures: how many sales did a shop make this week, and is that accelerating?

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill etsy-shop-velocity -g
```

This skill calls the **Etsy Shop Sales Tracker** Actor (`publicrecords/etsy-shop-velocity`) through the Apify MCP server:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=publicrecords/etsy-shop-velocity",
      "headers": { "Authorization": "Bearer <APIFY_TOKEN>" }
    }
  }
}
```

The Actor reads from a daily panel of shops that is captured once a day and served from a snapshot; your query never touches Etsy. Shops not yet in the panel are omitted from the dataset (no charge) and are queued for the next day's snapshot.

## What a record contains

| field | meaning |
|---|---|
| `shop`, `shop_url` | shop name and URL |
| `sales_count`, `reviews_count`, `admirers`, `listings_active` | lifetime counters as of the snapshot date |
| `delta_7d`, `delta_28d` | sales-counter deltas from the daily panel readings |
| `sales_per_day` | fitted daily sales rate; `units_day` / `units_lo` / `units_hi` when modelled |
| `breakout`, `breakout_p` | true when the recent rate is well above the shop's own baseline |
| `first_seen`, `last_changed`, `history_days` | how much history stands behind the numbers |
| `sales_precision` | how exact the day's counter reading is (`exact` / `rounded`) |
| `snapshot_date`, `snapshot_stale` | panel vintage |

## Usage

- "Is *KJPottery* growing? Compare its 30-day sales to its baseline."
- "Of these ten shops from my keyword scan, which three are accelerating?"
- "Flag any shop in my watch list with a breakout this week."

Tool call the agent makes:

```json
{ "shops": ["KJPottery", "OrelCeramics"] }
```

## How it pairs with other skills

- **etsy-live-search** — find the shops that own page 1 for a keyword, then ask which of them are growing.
- **etsy-seller-guide** / **ecommerce-growth-strategy** — ground "what is working in this niche" in shops that are measurably selling more.

## Limits

- Numbers are shop-level counters Etsy publishes; listing-level sales are estimates and are labelled as such.
- A shop added today has one reading; rates need several days of history and say so.
