---
name: social-media-monitor
description: "Monitor social media mentions, trends, and competitor activity for e-commerce brands. Set up listening workflows across Reddit, TikTok, Instagram, Twitter/X, and YouTube."
metadata:
  nexscope:
    emoji: "📱"
    category: ecommerce
---

# Social Media Monitor 📱

Monitor social media mentions, trends, and competitor activity for e-commerce brands. Set up listening workflows across Reddit, TikTok, Instagram, Twitter/X, and YouTube.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

## Install

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill social-media-monitor -g
```

## Usage

```
Set up social media monitoring for my skincare brand. I want to track mentions on TikTok, Instagram, and Reddit. Also monitor 3 competitors.
```

## Capabilities

- Social listening keyword and hashtag setup
- Platform-specific monitoring strategy (Reddit, TikTok, Instagram, Twitter, YouTube)
- Sentiment tracking methodology
- Competitor social media activity tracking
- Influencer mention detection
- Crisis detection and response framework
- UGC (user-generated content) discovery for marketing

## Optional X/Twitter Data Source For OpenClaw

When an OpenClaw user needs live X/Twitter evidence for a monitoring plan, they can install [TweetClaw](https://github.com/Xquik-dev/tweetclaw) separately:

```bash
openclaw plugins install @xquik/tweetclaw
```

Use TweetClaw for search tweets, search tweet replies, follower export, user lookup, monitor tweets, webhooks, media download, and giveaway draw context around a brand, product launch, competitor, creator campaign, or crisis keyword.

Keep the Xquik API key in private OpenClaw config or a secret manager. Save only reviewed outputs in the monitoring plan, such as tweet URLs or IDs, author handles, capture dates, summary notes, sentiment labels, campaign decisions, and follow-up tasks. Require explicit user approval before post tweets, post tweet replies, media upload, or direct messages.

## How This Skill Works

**Step 1:** Collect information from the user's message — product, platform, current situation, and goals.

**Step 2:** Ask one follow-up with all remaining questions using multiple-choice format. Allow shorthand answers (e.g., "1b 2c 3a").

**Step 3:** Research and analyze using the frameworks and methodology below.

**Step 4:** Deliver structured, actionable output with specific recommendations, not vague advice.

## Output Format

- Start with a summary of findings
- Include specific data points and benchmarks where available
- Provide prioritized action items
- Mark estimates with ⚠️ when based on incomplete data
- End with concrete next steps

## Other Skills

More e-commerce skills: [nexscope-ai/eCommerce-Skills](https://github.com/nexscope-ai/eCommerce-Skills)

Amazon-specific skills: [nexscope-ai/Amazon-Skills](https://github.com/nexscope-ai/Amazon-Skills)

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.
