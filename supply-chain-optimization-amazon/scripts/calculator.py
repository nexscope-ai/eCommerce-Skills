#!/usr/bin/env python3
"""
Supply Chain Analyzer - Core Calculator
Supply Chain Analyzer - Core Calculator

Purpose: Calculate key metrics and diagnose bottlenecks
Version: 1.0.0
"""

import json
from dataclasses import dataclass
from typing import Optional, List, Dict
from enum import Enum


class HealthStatus(Enum):
    HEALTHY = "healthy"
    WARNING = "warning"
    DANGER = "danger"


# ============================================================
# Benchmark Configuration (customizable)
# ============================================================

BENCHMARKS = {
    "amazon": {
        "gross_margin": {
            "healthy": 0.40,    # >40% Healthy
            "warning": 0.30,    # 30-40% Warning
            "danger": 0.20      # <20% Danger
        },
        "shipping_ratio": {
            "healthy": 0.05,    # <5% Healthy
            "warning": 0.10,    # 5-10% Warning
            "danger": 0.15      # >15% Danger
        },
        "inventory_days": {
            "healthy": 45,      # <45days Healthy
            "warning": 60,      # 45-60days Warning
            "danger": 90        # >90days Danger
        },
        "cash_cycle": {
            "healthy": 90,      # <90days Healthy
            "warning": 120,     # 90-120days Warning
            "danger": 150       # >150days Danger
        },
        "net_margin": {
            "healthy": 0.20,    # >20% Healthy
            "warning": 0.10,    # 10-20% Warning
            "danger": 0.05      # <5% Danger
        }
    },
    "walmart": {
        "gross_margin": {
            "healthy": 0.35,    # Walmart Commission more  low 
            "warning": 0.25,
            "danger": 0.15
        },
        "shipping_ratio": {
            "healthy": 0.06,    # WFS ShippingSlightly higher
            "warning": 0.10,
            "danger": 0.15
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 100,     # Payment CycleSlightly longer
            "warning": 130,
            "danger": 160
        },
        "net_margin": {
            "healthy": 0.18,
            "warning": 0.10,
            "danger": 0.05
        }
    },
    "tiktok": {
        "gross_margin": {
            "healthy": 0.45,    # NeedCoverInfluencerCommission
            "warning": 0.35,
            "danger": 0.25
        },
        "shipping_ratio": {
            "healthy": 0.05,
            "warning": 0.08,
            "danger": 0.12
        },
        "inventory_days": {
            "healthy": 30,      # TikTok Best sellerweeksPeriod short 
            "warning": 45,
            "danger": 60
        },
        "cash_cycle": {
            "healthy": 60,      # Fast payment
            "warning": 90,
            "danger": 120
        },
        "net_margin": {
            "healthy": 0.15,    # InfluencerShare after 
            "warning": 0.08,
            "danger": 0.03
        }
    },
    "shopify": {
        "gross_margin": {
            "healthy": 0.60,    # DTC Requires high gross marginAdvertising
            "warning": 0.50,
            "danger": 0.40
        },
        "shipping_ratio": {
            "healthy": 0.08,    # 3PL Fee
            "warning": 0.12,
            "danger": 0.18
        },
        "inventory_days": {
            "healthy": 45,
            "warning": 60,
            "danger": 90
        },
        "cash_cycle": {
            "healthy": 45,      # Fast payment (2-3days)
            "warning": 70,
            "danger": 100
        },
        "net_margin": {
            "healthy": 0.20,
            "warning": 0.12,
            "danger": 0.05
        }
    }
}


# ============================================================
# Data Structures
# ============================================================

@dataclass
class SupplyChainInput:
    """Supply ChainInput Data"""
    # Procurementend
    product_cost: float          # ProductCost (FOB)
    supplier_payment_days: int   # SupplierPayment terms (days)
    production_days: int         # ProductionweeksPeriod (days)
    
    # Logisticsend
    shipping_cost_per_unit: float  # Single pieceInboundCost
    shipping_days: int             # TransportTimeeffect (days)
    
    # Saleend
    selling_price: float         # Selling Price
    fba_fee: float              # FBA Fulfillment
    storage_fee: float          # monthsaverageStoragefee ( each piece)
    ad_spend_ratio: float       # AdvertisingfeeProportion (0-1)
    
    # Inventoryend
    inventory_days: int         # CurrentInventorydays
    has_long_term_storage: bool #  is no has PeriodStoragefee
    
    # Optional:  from  API Get
    daily_sales: Optional[float] = None      # DayAverage sales
    current_inventory: Optional[int] = None  # CurrentInventoryquantity
    
    # Platform
    platform: str = "amazon"


@dataclass
class MetricResult:
    """singleItemMetricsResult"""
    name: str
    value: float
    unit: str
    status: HealthStatus
    benchmark: float
    description: str


@dataclass 
class BottleneckItem:
    """BottleneckItem"""
    priority: int           # excellent first Level 1-3
    severity: str          # High/ in / low 
    title: str
    problem: str
    impact: str
    suggestion: str


@dataclass
class AnalysisResult:
    """AnalyzeResult"""
    metrics: List[MetricResult]
    cost_breakdown: Dict[str, float]
    bottlenecks: List[BottleneckItem]
    summary: str


# ============================================================
# CoreCalculateFunction
# ============================================================

def evaluate_status(value: float, thresholds: dict, higher_is_better: bool = True) -> HealthStatus:
    """
    EvaluateMetricsHealthyStatus
    
    Args:
        value: MetricsValue
        thresholds: ThresholdDictionary {"healthy": x, "warning": y, "danger": z}
        higher_is_better: True=ValueexceedHighexceed good , False=Valueexceed low exceed good 
    """
    if higher_is_better:
        if value >= thresholds["healthy"]:
            return HealthStatus.HEALTHY
        elif value >= thresholds["warning"]:
            return HealthStatus.WARNING
        else:
            return HealthStatus.DANGER
    else:
        if value <= thresholds["healthy"]:
            return HealthStatus.HEALTHY
        elif value <= thresholds["warning"]:
            return HealthStatus.WARNING
        else:
            return HealthStatus.DANGER


def calculate_metrics(data: SupplyChainInput) -> List[MetricResult]:
    """
    Calculateplace has Key Metrics
    """
    benchmarks = BENCHMARKS.get(data.platform, BENCHMARKS["amazon"])
    metrics = []
    
    # 1. Gross Margin
    gross_profit = data.selling_price - data.product_cost - data.shipping_cost_per_unit - data.fba_fee
    gross_margin = gross_profit / data.selling_price
    metrics.append(MetricResult(
        name="Gross Margin",
        value=round(gross_margin * 100, 1),
        unit="%",
        status=evaluate_status(gross_margin, benchmarks["gross_margin"], higher_is_better=True),
        benchmark=benchmarks["gross_margin"]["healthy"] * 100,
        description=f"(Selling Price - ProductCost - Inbound - FBAfee) / Selling Price"
    ))
    
    # 2. InboundProportion
    shipping_ratio = data.shipping_cost_per_unit / data.selling_price
    metrics.append(MetricResult(
        name="InboundProportion",
        value=round(shipping_ratio * 100, 1),
        unit="%",
        status=evaluate_status(shipping_ratio, benchmarks["shipping_ratio"], higher_is_better=False),
        benchmark=benchmarks["shipping_ratio"]["healthy"] * 100,
        description="InboundCost / Selling Price"
    ))
    
    # 3. Net Margin
    ad_cost = data.selling_price * data.ad_spend_ratio
    other_cost = data.selling_price * 0.05  # Other FeesEstimate 5%
    net_profit = gross_profit - data.storage_fee - ad_cost - other_cost
    net_margin = net_profit / data.selling_price
    metrics.append(MetricResult(
        name="Net Margin",
        value=round(net_margin * 100, 1),
        unit="%",
        status=evaluate_status(net_margin, benchmarks["net_margin"], higher_is_better=True),
        benchmark=benchmarks["net_margin"]["healthy"] * 100,
        description="Deduct allCost after Profit Margin"
    ))
    
    # 4. Inventory Days
    metrics.append(MetricResult(
        name="Inventoryweeksconvert",
        value=data.inventory_days,
        unit="days",
        status=evaluate_status(data.inventory_days, benchmarks["inventory_days"], higher_is_better=False),
        benchmark=benchmarks["inventory_days"]["healthy"],
        description="CurrentInventoryCanselldays"
    ))
    
    # 5. CashweeksconvertweeksPeriod
    cash_cycle = (
        data.production_days + 
        data.shipping_days + 
        data.inventory_days + 
        14  # AmazonPayment Cycle
        - data.supplier_payment_days
    )
    metrics.append(MetricResult(
        name="Cash Cycle",
        value=cash_cycle,
        unit="days",
        status=evaluate_status(cash_cycle, benchmarks["cash_cycle"], higher_is_better=False),
        benchmark=benchmarks["cash_cycle"]["healthy"],
        description=" from PaymentComplete payment cycleweeksPeriod"
    ))
    
    return metrics


def calculate_cost_breakdown(data: SupplyChainInput) -> Dict[str, float]:
    """
    CalculateCostStructure breakdown
    """
    ad_cost = data.selling_price * data.ad_spend_ratio
    other_cost = data.selling_price * 0.05
    
    net_profit = (
        data.selling_price 
        - data.product_cost 
        - data.shipping_cost_per_unit 
        - data.fba_fee 
        - data.storage_fee 
        - ad_cost 
        - other_cost
    )
    
    return {
        "selling_price": data.selling_price,
        "product_cost": data.product_cost,
        "shipping_cost": data.shipping_cost_per_unit,
        "fba_fee": data.fba_fee,
        "storage_fee": data.storage_fee,
        "ad_cost": round(ad_cost, 2),
        "other_cost": round(other_cost, 2),
        "net_profit": round(net_profit, 2),
        # Proportion
        "product_cost_ratio": round(data.product_cost / data.selling_price * 100, 1),
        "shipping_ratio": round(data.shipping_cost_per_unit / data.selling_price * 100, 1),
        "fba_ratio": round(data.fba_fee / data.selling_price * 100, 1),
        "storage_ratio": round(data.storage_fee / data.selling_price * 100, 1),
        "ad_ratio": round(ad_cost / data.selling_price * 100, 1),
        "net_margin": round(net_profit / data.selling_price * 100, 1)
    }


def diagnose_bottlenecks(data: SupplyChainInput, metrics: List[MetricResult]) -> List[BottleneckItem]:
    """
    DiagnoseBottleneckandSort
    """
    bottlenecks = []
    benchmarks = BENCHMARKS.get(data.platform, BENCHMARKS["amazon"])
    
    # Check each Metrics
    for metric in metrics:
        if metric.status == HealthStatus.DANGER:
            severity = "High"
            priority = 1
        elif metric.status == HealthStatus.WARNING:
            severity = " in "
            priority = 2
        else:
            continue  # HealthyNot addBottleneck
            
        # Based onMetricsCategoryTypeGenerateRecommendation
        if metric.name == "Inventoryweeksconvert":
            bottlenecks.append(BottleneckItem(
                priority=priority,
                severity=severity,
                title="Inventoryweeksconvert slow ",
                problem=f"Current {metric.value} days vs Recommendation <{benchmarks['inventory_days']['healthy']} days",
                impact="CapitalOccupyIncrease，MayGeneratePeriodStoragefee",
                suggestion="1. Clear slow-movingSKU 2. Set safetyInventoryFormula 3.  small BatchHigh frequencyRestock"
            ))
        elif metric.name == "Cash Cycle":
            bottlenecks.append(BottleneckItem(
                priority=priority,
                severity=severity,
                title="Cash Cycle ",
                problem=f"Current {metric.value} days vs Recommendation <{benchmarks['cash_cycle']['healthy']} days",
                impact="CapitalUtilizeeffectRate low ，ImpactExpansionCapability",
                suggestion="1. StriveSupplierPayment terms 2. shrink short Inventorydays 3. ConsiderSupply ChainFinance"
            ))
        elif metric.name == "InboundProportion":
            bottlenecks.append(BottleneckItem(
                priority=priority,
                severity=severity,
                title="LogisticsCost High",
                problem=f"Current {metric.value}% vs Recommendation <{benchmarks['shipping_ratio']['healthy']*100}%",
                impact="ErodeProfitempty",
                suggestion="1. Sea freightReplaceAir freight 2. LCL/Full containerOptimization 3. Compare multiple freight forwarders"
            ))
        elif metric.name == "Gross Margin":
            bottlenecks.append(BottleneckItem(
                priority=priority,
                severity=severity,
                title="Gross Marginbias low ",
                problem=f"Current {metric.value}% vs Recommendation >{benchmarks['gross_margin']['healthy']*100}%",
                impact="Risk resistanceCapabilityWeak，difficult to SupportAdvertisingInput",
                suggestion="1. Raise price or Optimizationlistingconvert 2. reduce low ProcurementCost 3. OptimizationProductCombo"
            ))
        elif metric.name == "Net Margin":
            bottlenecks.append(BottleneckItem(
                priority=priority,
                severity=severity,
                title="Net Margin  low ",
                problem=f"Current {metric.value}% vs Recommendation >{benchmarks['net_margin']['healthy']*100}%",
                impact="ProfitCapabilityWeak，BusinessCannotSustain",
                suggestion="1. OptimizationAdvertisingACOS 2. ControlStoragefee 3. Increase average order value"
            ))
    
    # CheckPeriodStoragefee
    if data.has_long_term_storage:
        bottlenecks.append(BottleneckItem(
            priority=2,
            severity=" in ",
            title="ExistPeriodStoragefee",
            problem="PartInventorysuper 365days",
            impact="amount outside CostExpenditure，CapitalWaste",
            suggestion="1. ExportLibraryageReport 2. On-site promotion clearanceInventory 3. Remove or destroy"
        ))
    
    #  by excellent first LevelSort
    bottlenecks.sort(key=lambda x: x.priority)
    
    return bottlenecks[:3]  #  only Return Top 3


def analyze(data: SupplyChainInput) -> AnalysisResult:
    """
    ExecuteCompleteAnalyze
    """
    metrics = calculate_metrics(data)
    cost_breakdown = calculate_cost_breakdown(data)
    bottlenecks = diagnose_bottlenecks(data, metrics)
    
    # GenerateSummary
    danger_count = sum(1 for m in metrics if m.status == HealthStatus.DANGER)
    warning_count = sum(1 for m in metrics if m.status == HealthStatus.WARNING)
    
    if danger_count > 0:
        summary = f"Found {danger_count} CriticalIssueNeedImmediatelyProcess"
    elif warning_count > 0:
        summary = f"Found {warning_count} potential in IssueRecommendationOptimization"
    else:
        summary = "Supply ChainOverallHealthy，CanAttentionSustainOptimization"
    
    return AnalysisResult(
        metrics=metrics,
        cost_breakdown=cost_breakdown,
        bottlenecks=bottlenecks,
        summary=summary
    )


# ============================================================
# OutputFormat
# ============================================================

def format_metrics_table(metrics: List[MetricResult]) -> str:
    """FormatMetricsTable"""
    status_icons = {
        HealthStatus.HEALTHY: "✅",
        HealthStatus.WARNING: "⚠️",
        HealthStatus.DANGER: "🔴"
    }
    
    lines = ["| Metrics | Value | Benchmark | Status |", "|------|------|------|------|"]
    for m in metrics:
        icon = status_icons[m.status]
        lines.append(f"| {m.name} | {m.value}{m.unit} | {m.benchmark}{m.unit} | {icon} |")
    
    return "\n".join(lines)


def format_cost_breakdown(breakdown: Dict[str, float]) -> str:
    """FormatCostBreakdown"""
    lines = [
        f"Selling Price            ${breakdown['selling_price']:.2f}   100%",
        "─────────────────────────────",
        f"ProductCost        -${breakdown['product_cost']:.2f}    {breakdown['product_cost_ratio']}%",
        f"InboundLogistics        -${breakdown['shipping_cost']:.2f}     {breakdown['shipping_ratio']}%",
        f"FBA Fulfillment      -${breakdown['fba_fee']:.2f}    {breakdown['fba_ratio']}%",
        f"FBA Storagefee      -${breakdown['storage_fee']:.2f}     {breakdown['storage_ratio']}%",
        f"Advertisingfee          -${breakdown['ad_cost']:.2f}    {breakdown['ad_ratio']}%",
        f"OtherFee        -${breakdown['other_cost']:.2f}     5.0%",
        "─────────────────────────────",
        f"Net Profit          ${breakdown['net_profit']:.2f}     {breakdown['net_margin']}%"
    ]
    return "\n".join(lines)


def format_bottlenecks(bottlenecks: List[BottleneckItem]) -> str:
    """FormatBottleneckcolumnTable"""
    if not bottlenecks:
        return "✅ No obvious bottleneck found"
    
    lines = []
    priority_icons = {1: "🥇", 2: "🥈", 3: "🥉"}
    
    for i, b in enumerate(bottlenecks, 1):
        icon = priority_icons.get(i, "•")
        lines.append(f"\n{icon} **【{b.severity}】{b.title}**")
        lines.append(f"   Issue: {b.problem}")
        lines.append(f"   Impact: {b.impact}")
        lines.append(f"   Recommendation: {b.suggestion}")
    
    return "\n".join(lines)


def format_full_report(result: AnalysisResult) -> str:
    """GenerateCompleteReport"""
    report = f"""
🔍 **Supply ChainBottleneck DiagnosisReport**

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Key Metrics**

{format_metrics_table(result.metrics)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 **CostStructure breakdown** ( each piece)

```
{format_cost_breakdown(result.cost_breakdown)}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 **Top 3 Bottleneck Diagnosis**

{format_bottlenecks(result.bottlenecks)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 **Summary**: {result.summary}
"""
    return report


# ============================================================
# CLI Entry Point
# ============================================================

def main():
    """CLI Entry Point - use at Test"""
    import sys
    
    # ExampleData
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
    
    # If JSON input provided
    if len(sys.argv) > 1:
        try:
            input_json = json.loads(sys.argv[1])
            test_data = SupplyChainInput(**input_json)
        except Exception as e:
            print(f"Error parsing input: {e}")
            sys.exit(1)
    
    # ExecuteAnalyze
    result = analyze(test_data)
    
    # OutputReport
    print(format_full_report(result))
    
    # Output JSON (For program call)
    # print(json.dumps({
    #     "metrics": [{"name": m.name, "value": m.value, "status": m.status.value} for m in result.metrics],
    #     "bottlenecks": [{"title": b.title, "severity": b.severity} for b in result.bottlenecks],
    #     "summary": result.summary
    # }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
