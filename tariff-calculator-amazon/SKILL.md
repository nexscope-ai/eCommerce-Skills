---
name: tariff-calculator-amazon
version: 1.0.0
author: Nexscope AI
description: "Universal tariff calculator for Amazon sellers. Calculate import duties, landed costs, and VAT/GST for any trade route. Supports CN→US, CN→EU, US→EU, EU→US, US→CN and custom origin/destination pairs. Includes Section 301 tariffs, trade agreement rates (USMCA, EVFTA), and HS code lookup. No API key required."
metadata: {"nexscope":{"emoji":"💰","category":"ecommerce"}}
---

# Tariff Calculator — Amazon 💰

Universal tariff and landed cost calculator for international Amazon sellers.

## Installation

```bash
npx skills add nexscope-ai/eCommerce-Skills --skill tariff-calculator-amazon -g
```

## Features

- **Universal Trade Routes** — Any origin to any destination
- **Tariff Rate Lookup** — HS code → duty rate
- **Section 301 Tariffs** — US additional duties on China imports
- **VAT/GST Calculation** — EU, UK, CA, AU, CN rates
- **Landed Cost** — Complete cost breakdown
- **HS Code Matcher** — Product description → HS code suggestions
- **Trade Agreements** — USMCA, EVFTA, RCEP preferential rates

## Supported Trade Routes

| Route | Key Tariffs | VAT/GST |
|-------|-------------|---------|
| 🇨🇳 → 🇺🇸 China → USA | Section 301 (7.5-25%) | N/A |
| 🇨🇳 → 🇪🇺 China → EU | Standard duties | 19-22% |
| 🇨🇳 → 🇬🇧 China → UK | Standard duties | 20% |
| 🇺🇸 → 🇪🇺 USA → EU | Standard duties | 19-22% |
| 🇪🇺 → 🇺🇸 EU → USA | Standard duties | N/A |
| 🇺🇸 → 🇨🇳 USA → China | Retaliatory tariffs | 13% VAT |
| 🇨🇳 → 🇨🇦 China → Canada | Standard duties | 5% GST |
| 🇨🇳 → 🇦🇺 China → Australia | Standard duties | 10% GST |
| **Custom** | User-defined | User-defined |

## Section 301 Tariffs (China → USA)

| HS Chapter | Products | Additional Rate |
|------------|----------|-----------------|
| 84xx | Computers, machinery | 25% |
| 85xx | Electronics (some) | 0-25% |
| 94xx | Furniture, lighting | 25% |
| 95xx | Toys | 25% |
| 61/62 | Apparel | 7.5% |
| 64xx | Footwear | 7.5% |
| 42xx | Bags, accessories | 7.5% |

## Landed Cost Formula

```
Landed Cost = 
    FOB Value
  + International Freight
  + Insurance
  + Import Duty
  + VAT/GST (if applicable)
  + Customs Clearance
  + Port Fees
  + Inland Freight
```

## Usage

### Basic Calculation

```bash
python3 scripts/calculator.py
```

### With Parameters

```bash
python3 scripts/calculator.py '{
  "hs_code": "8518300000",
  "origin_country": "CN",
  "destination_country": "US",
  "fob_value": 5000.00,
  "quantity": 500,
  "freight_cost": 200.00
}'
```

### HS Code Lookup

```bash
python3 scripts/hs_lookup.py "wireless earbuds"
python3 scripts/hs_lookup.py "bluetooth speaker"
```

### Custom Trade Route

```bash
python3 scripts/calculator.py '{
  "hs_code": "9503009000",
  "origin_country": "VN",
  "destination_country": "DE",
  "fob_value": 10000.00,
  "quantity": 1000,
  "freight_cost": 500.00,
  "custom_duty_rate": 0.047,
  "custom_vat_rate": 0.19
}'
```

## Output Example

```
💰 Tariff & Landed Cost Report

Product: Wireless Bluetooth Earbuds
HS Code: 8518300000
Route: China 🇨🇳 → USA 🇺🇸

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📦 Cost Breakdown

FOB Value               $  5,000.00
International Freight   $    200.00
Insurance               $     15.00
CIF Value               $  5,215.00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏛️ Duties & Taxes

Base Duty (0.0%)        $      0.00
Section 301 (0.0%)      $      0.00
Total Duty              $      0.00
Customs Clearance       $    150.00
Port Fees               $     50.00

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💵 Landed Cost Summary

Total Landed Cost       $  5,515.00
Per Unit Cost           $     11.03
```

## Trade Agreement Support

| Agreement | Countries | Benefit |
|-----------|-----------|---------|
| USMCA | US, Mexico, Canada | Reduced/zero duties |
| EVFTA | EU, Vietnam | Reduced duties |
| RCEP | Asia-Pacific | Reduced duties |
| UK-Japan | UK, Japan | Reduced duties |

## Custom Configuration

Create a custom config for your routes:

```json
{
  "default_origin": "CN",
  "default_destination": "US",
  "include_insurance": true,
  "insurance_rate": 0.003,
  "customs_fee": 150,
  "port_fee": 50
}
```

---

**Part of [Nexscope AI](https://www.nexscope.ai/) — AI tools for e-commerce sellers.**
