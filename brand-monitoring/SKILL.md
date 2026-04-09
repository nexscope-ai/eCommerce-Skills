---
name: brand-monitoring
version: 1.0.0
author: Nexscope AI
description: "Brand monitoring tool for tracking mentions across social media platforms. Monitor Reddit, Google News, YouTube, and DuckDuckGo for brand mentions. Includes sentiment analysis, trend tracking, crisis detection, and competitor comparison. No API key required for basic monitoring."
metadata: {"nexscope":{"emoji":"📡","category":"ecommerce"}}
---

# Brand Monitoring 📡

Track brand mentions across social media platforms and analyze sentiment.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill brand-monitoring -g
```

## Features

- **Mention Monitoring** — Track brand mentions across platforms
- **Sentiment Analysis** — Positive/negative/neutral classification
- **Trend Tracking** — Monitor mention volume changes
- **Crisis Detection** — Alerts for negative spikes or crisis keywords
- **Competitor Comparison** — Share of voice analysis
- **Keyword Extraction** — Identify trending topics
- **Report Generation** — Weekly/monthly reports

## Supported Platforms

| Platform | Method | Stability |
|----------|--------|-----------|
| Reddit | Public JSON API | ⚠️ Rate limited |
| Google News | RSS Feed | ✅ Stable |
| DuckDuckGo | Instant Answer API | ✅ Stable |
| YouTube | HTML/RSS | ⚠️ Unstable |

## Analysis Dimensions

| Dimension | Method | Output |
|-----------|--------|--------|
| Volume | Mention count | Trend graph |
| Sentiment | NLP analysis | Sentiment score |
| Sources | Platform breakdown | Source distribution |
| Keywords | Topic extraction | Word cloud |
| Competitors | Share of voice | Comparison chart |

## Usage

### Basic Monitoring

```bash
python3 scripts/monitor.py "YourBrand"
```

### With Competitors

```bash
python3 scripts/monitor.py '{
  "brand": "YourBrand",
  "competitors": ["CompA", "CompB"],
  "platforms": ["reddit", "google_news"]
}'
```

### Demo Mode

```bash
python3 scripts/monitor.py --demo
```

## Output Example

```
📡 Brand Monitoring Report

Brand: YourBrand
Period: Last 7 days
Platforms: Reddit, Google News, YouTube

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 MENTION OVERVIEW

Total Mentions: 127
├── Reddit: 82 (65%)
├── Google News: 35 (28%)
└── YouTube: 10 (8%)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

😊 SENTIMENT ANALYSIS

Positive: 45% ████████░░
Neutral:  38% ███████░░░
Negative: 17% ███░░░░░░░

Overall Score: 7.2/10 ✅

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 TREND (7 days)

Mon ████████ 25
Tue ██████ 18
Wed ███████ 21
Thu █████████ 28
Fri ████████ 22
Sat ███ 8
Sun ██ 5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔥 TRENDING KEYWORDS

1. quality (32x)
2. shipping (28x)
3. customer service (22x)
4. price (18x)
5. recommended (15x)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ ALERTS

🔴 Negative spike on Thursday (+40%)
   Related to: shipping delays
   Recommendation: Monitor and respond
```

## Crisis Detection

| Alert Level | Trigger | Action |
|-------------|---------|--------|
| 🟢 Normal | < 20% negative | Continue monitoring |
| 🟡 Warning | 20-40% negative | Investigate sources |
| 🔴 Crisis | > 40% negative | Immediate response needed |

## Monitoring Workflow

```
Set up brand keywords
      ↓
Monitor platforms
      ↓
Analyze sentiment
      ↓
Detect anomalies
      ↓
Generate alerts
      ↓
Weekly report
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/?co-from=skill) — AI tools for e-commerce sellers.**
