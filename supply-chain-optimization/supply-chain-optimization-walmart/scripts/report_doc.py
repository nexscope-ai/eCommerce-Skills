#!/usr/bin/env python3
"""
Supply Chain Analyzer - Document Report Generator
Supply ChainAnalyze - Report documentGenerate（Suitable for sharing/Demo）
"""

from datetime import datetime
from calculator import SupplyChainInput, analyze, HealthStatus


def generate_doc_report(data: SupplyChainInput, output_path: str = "report.md") -> str:
    """
    GenerateReport document（Markdown Format，SuitableExport PDF/PPT）
    """
    result = analyze(data)
    
    # StatusIcon
    status_icons = {
        HealthStatus.HEALTHY: "🟢",
        HealthStatus.WARNING: "🟡",
        HealthStatus.DANGER: "🔴"
    }
    
    # MetricsTable
    metrics_table = "| Metrics | CurrentValue | HealthyBenchmark | Status |\n|:---:|:---:|:---:|:---:|\n"
    for m in result.metrics:
        icon = status_icons[m.status]
        metrics_table += f"| {m.name} | **{m.value}{m.unit}** | {m.benchmark}{m.unit} | {icon} |\n"
    
    # CostStructure
    cost = result.cost_breakdown
    cost_bars = ""
    cost_items = [
        ("ProductCost", cost['product_cost_ratio'], "🔴"),
        ("FBAFulfillment", cost['fba_ratio'], "🔵"),
        ("Advertisingfee", cost['ad_ratio'], "🟣"),
        ("InboundLogistics", cost['shipping_ratio'], "🟠"),
        ("Storagefee", cost['storage_ratio'], "🟤"),
        ("Other", 5, "⚪"),
        ("Net Profit", cost['net_margin'], "🟢"),
    ]
    for name, ratio, emoji in cost_items:
        bar = "█" * int(ratio / 2) if ratio > 0 else ""
        cost_bars += f"| {emoji} {name} | {bar} | {ratio}% |\n"
    
    # BottleneckPart
    bottlenecks_section = ""
    if result.bottlenecks:
        for i, b in enumerate(result.bottlenecks, 1):
            emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉"
            bottlenecks_section += f"""
### {emoji} Bottleneck {i}: {b.title}

**CriticalprocessDegree**: {b.severity}

**IssueDescription**  
{b.problem}

**BusinessImpact**  
{b.impact}

**Optimization Suggestions**  
{b.suggestion}

---
"""
    else:
        bottlenecks_section = "\n✅ **No obvious bottleneck found，Supply ChainOverallHealthy**\n"
    
    # ExecuteList
    action_items = """
### 📋 ExecuteList

**basicweeks**
- [ ] Export FBA LibraryageReport，Mark exceeds 60 days SKU
- [ ] Calculate each  SKU safe all Inventoryquantity
- [ ] OrganizeSupplierContact info，Prepare negotiation

** below weeks**
- [ ] Clear slow-movingInventory（On-site promotion/Off-site clearance）
- [ ] ContactSuppliertalkPayment terms
- [ ] AdjustRestockfrequencyRate

**basicmonths**
- [ ] InventorydaysTarget：Drop to 45 days to  inside 
- [ ] Evaluate small BatchHigh frequencyRestockModeFeasibility
- [ ] Review execution results
"""
    
    # Assemble document
    doc = f"""---
title: Supply ChainBottleneckAnalyzeReport
date: {datetime.now().strftime("%Y-%m-%d")}
author: Supply Chain Analyzer
---

# 📦 Supply ChainBottleneckAnalyzeReport

> **GenerateTime**: {datetime.now().strftime("%Yyears%mmonths%dDay %H:%M")}  
> **AnalyzePlatform**: Amazon ({data.platform.upper()})

---

## 📌 CoreConclusion

<div style="background: #f0f9ff; padding: 20px; border-radius: 8px; border-left: 4px solid #3b82f6;">

**{result.summary}**

Based onProvided by youData，Found **{len([m for m in result.metrics if m.status != HealthStatus.HEALTHY])}** MetricsNeedAttention。

</div>

---

## 📊 Key MetricsOverview

{metrics_table}

---

## 💰 CostStructureAnalyze

** each pieceProductCostBreakdown** (Selling Price ${cost['selling_price']:.2f})

| Itemitem | Proportion | Ratio |
|:---|:---|---:|
{cost_bars}

**Net Profit: ${cost['net_profit']:.2f}/piece ({cost['net_margin']}%)**

---

## 🎯 Bottleneck Diagnosis & Optimization Suggestions

{bottlenecks_section}

---

## 🚀 Action Plan

{action_items}

---

## 📈 prePeriodEffect

| OptimizationItem | Current | Target | prePeriodRevenue |
|:---|:---:|:---:|:---|
| Inventoryweeksconvert | {data.inventory_days}days | 45days | ReleaseInventoryCapital，ReduceStoragefee |
| PeriodStoragefee |  has  | no | Save $500+/months |
| SupplierPayment terms | {data.supplier_payment_days}days | 30days | Improve cash flow |

---

## 📎 Appendix

### DataSource

- ProductCost: ${data.product_cost}/piece (UserInput)
- InboundCost: ${data.shipping_cost_per_unit}/piece (UserInput)
- FBA Fee: ${data.fba_fee}/piece (UserInput)
- Selling Price: ${data.selling_price}/piece (UserInput)
- Inventorydays: {data.inventory_days}days (UserInput)

### BenchmarkValueDescription

basicReportUseHealthyBenchmarkValueBased onAmazonSellerIndustryData，Can be adjusted according to actual situation。

---

<div style="text-align: center; color: #6b7280; font-size: 12px; margin-top: 40px;">

**Powered by Supply Chain Analyzer Skill | NexScope**

</div>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(doc)
    
    return output_path


if __name__ == "__main__":
    # TestData
    test_data = SupplyChainInput(
        product_cost=8.00,
        supplier_payment_days=0,
        production_days=25,
        shipping_cost_per_unit=0.75,
        shipping_days=35,
        selling_price=25.00,
        fba_fee=5.00,
        storage_fee=0.50,
        ad_spend_ratio=0.10,
        inventory_days=60,
        has_long_term_storage=True,
        platform="amazon"
    )
    
    output = generate_doc_report(test_data, "supply_chain_report.md")
    print(f"✅ Report documentGenerate: {output}")
