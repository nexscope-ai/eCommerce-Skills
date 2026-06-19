---
name: dropshipping-product-research
description: "Product research for dropshipping businesses. Identify profitable products with reliable suppliers, healthy margins, and manageable competition. Evaluates shipping times, return risk, and marketing viability."
metadata:
  nexscope:
    emoji: "📦"
    category: ecommerce
---

# Dropshipping Product Research 📦

Product research for dropshipping businesses. Identify profitable products with reliable suppliers, healthy margins, and manageable competition. Evaluates shipping times, return risk, and marketing viability.

**Supported platforms:** Amazon, Shopify, WooCommerce, Walmart, TikTok Shop, Etsy, eBay, BigCommerce.

Built by [Nexscope](https://www.nexscope.ai/?co-from=skill) — your AI assistant for smarter e-commerce decisions.

## Install

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill dropshipping-product-research -g
```

## Usage

```
Help me find dropshipping products in the pet accessories niche. Budget is $2000 to start. I want to sell via Shopify with Meta ads.
```

## Capabilities

- Product viability scoring for dropshipping (margin, weight, fragility, return risk)
- Supplier reliability assessment framework
- Shipping time and cost analysis by origin/destination
- Marketing angle identification (social media, paid ads, SEO)
- Competition analysis specific to dropshipping niches
- Trend validation and longevity assessment

## How This Skill Works

**Step 1:** Collect information from the user's message — product, platform, current situation, and goals.

**Step 2:** Ask one follow-up with all remaining questions using multiple-choice format. Allow shorthand answers (e.g., "1b 2c 3a").

**Step 3:** Research and analyze using the frameworks and methodology below.

**Step 4:** Deliver structured, actionable output with specific recommendations, not vague advice.


## Risk Gates Before Recommendation

Use these gates before calling a dropshipping product viable. A product can have strong demand and still be a bad recommendation if one gate fails.

| Gate | Pass Signal | Hold / Reject Signal |
| --- | --- | --- |
| Shipping promise | Delivery time and tracking match the channel's customer expectation | Long or unclear delivery time would create chargebacks or poor reviews |
| Margin after ads | Gross margin survives product cost, shipping, platform fees, payment fees, refunds, and CAC | Profit depends on unrealistically cheap traffic or zero returns |
| Return and damage risk | Product is low-fragility, easy to explain, and has manageable sizing/fit issues | High breakage, subjective quality, sizing disputes, or expensive returns |
| Supplier evidence | Supplier has clear history, inventory, fulfillment process, and response quality | Supplier cannot confirm stock, processing time, packaging, or refund process |
| Policy and compliance | Product avoids restricted claims, safety risk, IP risk, and platform policy issues | Health, safety, branded, counterfeit, battery, or regulated claims are unresolved |

Decision rules:

- Use **Proceed** only when all gates pass or have clear mitigation.
- Use **Test First** when the product depends on one uncertain assumption that can be validated with a small ad or sample-order test.
- Use **Reject** when shipping promise, policy risk, supplier reliability, or realistic margin fails.
- Always include the single next validation action instead of only a score.

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
