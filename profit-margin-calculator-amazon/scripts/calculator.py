#!/usr/bin/env python3
"""
Amazon Profit Calculator - Core Engine
亚马逊利润计算器 - 核心计算引擎

功能:
- 成本明细计算
- 利润率计算 (毛利/净利)
- 盈亏平衡分析
- 定价建议
- 批量计算支持

版本: 1.0.0
"""

import json
import csv
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import sys


class ProfitStatus(Enum):
    HEALTHY = "healthy"      # >20% 净利率
    WARNING = "warning"      # 5-20% 净利率
    DANGER = "danger"        # <5% 净利率
    LOSS = "loss"           # 亏损


# ============================================================
# 亚马逊 Referral Fee 费率表 (按品类)
# ============================================================

REFERRAL_FEE_RATES = {
    # 品类: 费率
    "default": 0.15,
    "electronics": 0.08,
    "computers": 0.08,
    "camera": 0.08,
    "video_games": 0.15,
    "books": 0.15,
    "clothing": 0.17,
    "shoes": 0.15,
    "jewelry": 0.20,
    "watches": 0.15,
    "furniture": 0.15,
    "home": 0.15,
    "kitchen": 0.15,
    "beauty": 0.15,
    "health": 0.15,
    "grocery": 0.15,
    "pet": 0.15,
    "toys": 0.15,
    "baby": 0.15,
    "sports": 0.15,
    "outdoors": 0.15,
    "automotive": 0.12,
    "industrial": 0.12,
    "office": 0.15,
}

# FBA 配送费参考表 (简化版，基于尺寸分级)
FBA_FULFILLMENT_FEES = {
    "small_standard": 3.22,      # 小号标准 (<1lb)
    "large_standard_1lb": 4.75,  # 大号标准 (<1lb)
    "large_standard_2lb": 5.40,  # 大号标准 (1-2lb)
    "large_standard_3lb": 6.10,  # 大号标准 (2-3lb)
    "small_oversize": 9.73,      # 小号超大
    "medium_oversize": 19.05,    # 中号超大
    "large_oversize": 89.98,     # 大号超大
}

# 利润率阈值
PROFIT_THRESHOLDS = {
    "healthy": 0.20,    # >20%
    "warning": 0.05,    # 5-20%
    "danger": 0.00,     # 0-5%
}


# ============================================================
# 数据结构
# ============================================================

@dataclass
class ProductInput:
    """单个产品输入数据"""
    sku: str = "SKU001"
    name: str = "Product"
    
    # 售价
    selling_price: float = 0.0
    
    # 成本项
    product_cost: float = 0.0           # 产品成本 (FOB)
    shipping_cost: float = 0.0          # 头程运费
    fba_fulfillment_fee: float = 0.0    # FBA 配送费
    fba_storage_fee: float = 0.0        # FBA 仓储费 (月均)
    
    # 可选成本
    ad_spend_ratio: float = 0.0         # 广告费占比 (0-1)
    return_rate: float = 0.0            # 退货率 (0-1)
    return_processing_fee: float = 0.0  # 退货处理费/件
    other_fees: float = 0.0             # 其他杂费
    
    # 平台相关
    category: str = "default"           # 品类 (用于计算 Referral Fee)
    referral_fee_rate: Optional[float] = None  # 自定义佣金费率
    
    # 批量计算用
    monthly_sales: int = 0              # 月销量 (用于计算固定成本分摊)
    fixed_costs: float = 0.0            # 固定成本 (用于盈亏平衡)


@dataclass
class CostBreakdown:
    """成本拆解"""
    selling_price: float
    product_cost: float
    shipping_cost: float
    fba_fulfillment_fee: float
    fba_storage_fee: float
    referral_fee: float
    ad_cost: float
    return_cost: float
    other_fees: float
    
    total_cost: float = 0.0
    gross_profit: float = 0.0
    net_profit: float = 0.0
    gross_margin: float = 0.0
    net_margin: float = 0.0
    
    def __post_init__(self):
        self.total_cost = (
            self.product_cost +
            self.shipping_cost +
            self.fba_fulfillment_fee +
            self.fba_storage_fee +
            self.referral_fee +
            self.ad_cost +
            self.return_cost +
            self.other_fees
        )
        self.gross_profit = self.selling_price - self.product_cost - self.shipping_cost - self.fba_fulfillment_fee - self.referral_fee
        self.net_profit = self.selling_price - self.total_cost
        self.gross_margin = self.gross_profit / self.selling_price if self.selling_price > 0 else 0
        self.net_margin = self.net_profit / self.selling_price if self.selling_price > 0 else 0


@dataclass
class BreakEvenAnalysis:
    """盈亏平衡分析"""
    min_price: float              # 最低售价 (保本)
    break_even_units: int         # 保本销量
    safety_margin: float          # 安全边际
    current_margin_above_min: float  # 当前售价高于保本价的比例


@dataclass
class PricingSuggestion:
    """定价建议"""
    target_margin: float          # 目标利润率
    suggested_price: float        # 建议售价
    profit_per_unit: float        # 单件利润


@dataclass
class AnalysisResult:
    """完整分析结果"""
    product: ProductInput
    cost_breakdown: CostBreakdown
    break_even: BreakEvenAnalysis
    pricing_suggestions: List[PricingSuggestion]
    status: ProfitStatus
    summary: str


# ============================================================
# 核心计算函数
# ============================================================

def get_referral_fee_rate(category: str, custom_rate: Optional[float] = None) -> float:
    """获取 Referral Fee 费率"""
    if custom_rate is not None:
        return custom_rate
    return REFERRAL_FEE_RATES.get(category.lower(), REFERRAL_FEE_RATES["default"])


def calculate_costs(product: ProductInput) -> CostBreakdown:
    """计算成本明细"""
    # Referral Fee
    referral_rate = get_referral_fee_rate(product.category, product.referral_fee_rate)
    referral_fee = product.selling_price * referral_rate
    
    # 广告费
    ad_cost = product.selling_price * product.ad_spend_ratio
    
    # 退货成本 = 退货率 × (退货处理费 + 产品成本损失比例)
    return_cost = product.return_rate * (product.return_processing_fee + product.product_cost * 0.5)
    
    return CostBreakdown(
        selling_price=product.selling_price,
        product_cost=product.product_cost,
        shipping_cost=product.shipping_cost,
        fba_fulfillment_fee=product.fba_fulfillment_fee,
        fba_storage_fee=product.fba_storage_fee,
        referral_fee=round(referral_fee, 2),
        ad_cost=round(ad_cost, 2),
        return_cost=round(return_cost, 2),
        other_fees=product.other_fees
    )


def calculate_break_even(product: ProductInput, costs: CostBreakdown) -> BreakEvenAnalysis:
    """计算盈亏平衡点"""
    # 可变成本 (每件)
    variable_cost = (
        product.product_cost +
        product.shipping_cost +
        product.fba_fulfillment_fee +
        product.fba_storage_fee +
        costs.referral_fee +
        costs.return_cost +
        product.other_fees
    )
    
    # 最低售价 (覆盖可变成本 + 广告费)
    # 设广告费占比不变，则: min_price - variable_cost - min_price * ad_ratio = 0
    # min_price * (1 - ad_ratio) = variable_cost
    if product.ad_spend_ratio < 1:
        min_price = variable_cost / (1 - product.ad_spend_ratio)
    else:
        min_price = variable_cost * 2  # 异常情况
    
    # 保本销量 (如果有固定成本)
    if product.fixed_costs > 0 and costs.net_profit > 0:
        break_even_units = int(product.fixed_costs / costs.net_profit) + 1
    else:
        break_even_units = 0
    
    # 安全边际
    safety_margin = (product.selling_price - min_price) / product.selling_price if product.selling_price > 0 else 0
    margin_above_min = (product.selling_price - min_price) / min_price if min_price > 0 else 0
    
    return BreakEvenAnalysis(
        min_price=round(min_price, 2),
        break_even_units=break_even_units,
        safety_margin=round(safety_margin, 4),
        current_margin_above_min=round(margin_above_min, 4)
    )


def calculate_pricing_suggestions(product: ProductInput, target_margins: List[float] = None) -> List[PricingSuggestion]:
    """计算定价建议"""
    if target_margins is None:
        target_margins = [0.15, 0.20, 0.25, 0.30]
    
    suggestions = []
    
    # 基础成本 (不含 Referral Fee 和广告费，因为它们是售价的百分比)
    base_cost = (
        product.product_cost +
        product.shipping_cost +
        product.fba_fulfillment_fee +
        product.fba_storage_fee +
        product.other_fees +
        product.return_rate * product.return_processing_fee
    )
    
    referral_rate = get_referral_fee_rate(product.category, product.referral_fee_rate)
    
    for target_margin in target_margins:
        # 目标: net_profit / selling_price = target_margin
        # net_profit = selling_price - base_cost - selling_price * referral_rate - selling_price * ad_ratio
        # selling_price * target_margin = selling_price - base_cost - selling_price * (referral_rate + ad_ratio)
        # selling_price * (target_margin + referral_rate + ad_ratio - 1) = -base_cost
        # selling_price = base_cost / (1 - target_margin - referral_rate - ad_ratio)
        
        denominator = 1 - target_margin - referral_rate - product.ad_spend_ratio
        if denominator > 0:
            suggested_price = base_cost / denominator
            profit_per_unit = suggested_price * target_margin
            
            suggestions.append(PricingSuggestion(
                target_margin=target_margin,
                suggested_price=round(suggested_price, 2),
                profit_per_unit=round(profit_per_unit, 2)
            ))
    
    return suggestions


def evaluate_profit_status(net_margin: float) -> ProfitStatus:
    """评估利润状态"""
    if net_margin < 0:
        return ProfitStatus.LOSS
    elif net_margin < PROFIT_THRESHOLDS["warning"]:
        return ProfitStatus.DANGER
    elif net_margin < PROFIT_THRESHOLDS["healthy"]:
        return ProfitStatus.WARNING
    else:
        return ProfitStatus.HEALTHY


def analyze_product(product: ProductInput, target_margins: List[float] = None) -> AnalysisResult:
    """分析单个产品"""
    costs = calculate_costs(product)
    break_even = calculate_break_even(product, costs)
    pricing = calculate_pricing_suggestions(product, target_margins)
    status = evaluate_profit_status(costs.net_margin)
    
    # 生成摘要
    status_text = {
        ProfitStatus.HEALTHY: "✅ 健康",
        ProfitStatus.WARNING: "⚠️ 警告",
        ProfitStatus.DANGER: "🔴 危险",
        ProfitStatus.LOSS: "💀 亏损",
    }
    summary = f"{status_text[status]} | 净利率 {costs.net_margin*100:.1f}% | 单件利润 ${costs.net_profit:.2f}"
    
    return AnalysisResult(
        product=product,
        cost_breakdown=costs,
        break_even=break_even,
        pricing_suggestions=pricing,
        status=status,
        summary=summary
    )


def analyze_batch(products: List[ProductInput], target_margins: List[float] = None) -> List[AnalysisResult]:
    """批量分析"""
    return [analyze_product(p, target_margins) for p in products]


# ============================================================
# 输出格式化
# ============================================================

def format_cost_breakdown(costs: CostBreakdown) -> str:
    """格式化成本明细"""
    def pct(val):
        return f"{val/costs.selling_price*100:.1f}%" if costs.selling_price > 0 else "0%"
    
    lines = [
        f"售价              ${costs.selling_price:.2f}   100%",
        "─" * 35,
        f"产品成本          -${costs.product_cost:.2f}    {pct(costs.product_cost)}",
        f"头程运费          -${costs.shipping_cost:.2f}    {pct(costs.shipping_cost)}",
        f"FBA 配送费        -${costs.fba_fulfillment_fee:.2f}    {pct(costs.fba_fulfillment_fee)}",
        f"FBA 仓储费        -${costs.fba_storage_fee:.2f}    {pct(costs.fba_storage_fee)}",
        f"Referral Fee      -${costs.referral_fee:.2f}    {pct(costs.referral_fee)}",
        f"广告费            -${costs.ad_cost:.2f}    {pct(costs.ad_cost)}",
        f"退货成本          -${costs.return_cost:.2f}    {pct(costs.return_cost)}",
        f"其他杂费          -${costs.other_fees:.2f}    {pct(costs.other_fees)}",
        "─" * 35,
        f"总成本            ${costs.total_cost:.2f}    {pct(costs.total_cost)}",
        f"净利润            ${costs.net_profit:.2f}    {costs.net_margin*100:.1f}%",
    ]
    return "\n".join(lines)


def format_break_even(be: BreakEvenAnalysis, current_price: float) -> str:
    """格式化盈亏平衡分析"""
    lines = [
        f"最低售价 (保本): ${be.min_price:.2f}",
        f"├── 低于此价格将亏损",
        f"",
        f"当前售价: ${current_price:.2f}",
        f"├── 高于保本价 {be.current_margin_above_min*100:.1f}%",
        f"",
        f"安全边际: {be.safety_margin*100:.1f}%",
        f"├── 价格下降空间",
    ]
    if be.break_even_units > 0:
        lines.extend([
            f"",
            f"保本销量: {be.break_even_units} 件",
            f"├── 覆盖固定成本所需销量",
        ])
    return "\n".join(lines)


def format_pricing_suggestions(suggestions: List[PricingSuggestion], current_price: float, current_margin: float) -> str:
    """格式化定价建议"""
    lines = [
        "| 目标利润率 | 建议售价 | 单件利润 |",
        "|-----------|---------|---------|",
    ]
    for s in suggestions:
        lines.append(f"| {s.target_margin*100:.0f}% | ${s.suggested_price:.2f} | ${s.profit_per_unit:.2f} |")
    
    lines.append(f"\n当前售价 ${current_price:.2f} → 净利率 {current_margin*100:.1f}%")
    return "\n".join(lines)


def format_full_report(result: AnalysisResult) -> str:
    """生成完整报告"""
    status_icons = {
        ProfitStatus.HEALTHY: "✅",
        ProfitStatus.WARNING: "⚠️",
        ProfitStatus.DANGER: "🔴",
        ProfitStatus.LOSS: "💀",
    }
    
    report = f"""
💰 **亚马逊利润分析报告**

**产品**: {result.product.name} ({result.product.sku})
**状态**: {status_icons[result.status]} {result.summary}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **成本明细**

```
{format_cost_breakdown(result.cost_breakdown)}
```

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 **盈亏平衡分析**

{format_break_even(result.break_even, result.product.selling_price)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 **定价建议**

{format_pricing_suggestions(result.pricing_suggestions, result.product.selling_price, result.cost_breakdown.net_margin)}

"""
    return report


def format_batch_summary(results: List[AnalysisResult]) -> str:
    """格式化批量分析汇总"""
    status_icons = {
        ProfitStatus.HEALTHY: "✅",
        ProfitStatus.WARNING: "⚠️",
        ProfitStatus.DANGER: "🔴",
        ProfitStatus.LOSS: "💀",
    }
    
    lines = [
        "📊 **批量分析汇总**",
        "",
        "| SKU | 售价 | 总成本 | 净利润 | 利润率 | 状态 |",
        "|-----|------|--------|--------|--------|------|",
    ]
    
    total_profit = 0
    for r in results:
        c = r.cost_breakdown
        icon = status_icons[r.status]
        lines.append(f"| {r.product.sku} | ${c.selling_price:.2f} | ${c.total_cost:.2f} | ${c.net_profit:.2f} | {c.net_margin*100:.1f}% | {icon} |")
        total_profit += c.net_profit
    
    lines.append("")
    lines.append(f"**总计**: {len(results)} 个 SKU | 平均单件利润 ${total_profit/len(results):.2f}")
    
    # 统计
    healthy = sum(1 for r in results if r.status == ProfitStatus.HEALTHY)
    warning = sum(1 for r in results if r.status == ProfitStatus.WARNING)
    danger = sum(1 for r in results if r.status == ProfitStatus.DANGER)
    loss = sum(1 for r in results if r.status == ProfitStatus.LOSS)
    
    lines.append(f"**状态分布**: ✅ {healthy} | ⚠️ {warning} | 🔴 {danger} | 💀 {loss}")
    
    return "\n".join(lines)


# ============================================================
# CSV 批量处理
# ============================================================

def parse_csv(csv_content: str) -> List[ProductInput]:
    """解析 CSV 内容"""
    products = []
    reader = csv.DictReader(csv_content.strip().split('\n'))
    
    for row in reader:
        product = ProductInput(
            sku=row.get('sku', 'SKU'),
            name=row.get('name', 'Product'),
            selling_price=float(row.get('selling_price', 0)),
            product_cost=float(row.get('product_cost', 0)),
            shipping_cost=float(row.get('shipping_cost', 0)),
            fba_fulfillment_fee=float(row.get('fba_fee', 0)),
            fba_storage_fee=float(row.get('storage_fee', 0)),
            ad_spend_ratio=float(row.get('ad_ratio', 0)),
            return_rate=float(row.get('return_rate', 0)),
            return_processing_fee=float(row.get('return_fee', 0)),
            other_fees=float(row.get('other_fees', 0)),
            category=row.get('category', 'default'),
        )
        products.append(product)
    
    return products


# ============================================================
# CLI 入口
# ============================================================

def main():
    """命令行入口"""
    # 默认测试数据
    test_product = ProductInput(
        sku="TEST001",
        name="Kitchen Gadget",
        selling_price=29.99,
        product_cost=6.00,
        shipping_cost=1.50,
        fba_fulfillment_fee=5.50,
        fba_storage_fee=0.30,
        ad_spend_ratio=0.10,
        return_rate=0.03,
        return_processing_fee=2.00,
        other_fees=0.50,
        category="kitchen",
    )
    
    # 如果有 JSON 输入
    if len(sys.argv) > 1:
        try:
            input_data = json.loads(sys.argv[1])
            if isinstance(input_data, list):
                # 批量模式
                products = [ProductInput(**p) for p in input_data]
                results = analyze_batch(products)
                print(format_batch_summary(results))
                return
            else:
                test_product = ProductInput(**input_data)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
    
    # 单品分析
    result = analyze_product(test_product)
    print(format_full_report(result))


if __name__ == "__main__":
    main()
