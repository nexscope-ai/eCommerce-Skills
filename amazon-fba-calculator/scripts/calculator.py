#!/usr/bin/env python3
"""
Amazon FBA Calculator - Core Engine
Amazon FBA FeeCalculate - Core Engine

Features:
- SizedivideLevelJudgment (Size Tier)
- FBA Fulfillment Fee Precise calculation
- Monthly Storage Fee
- Referral Fee
- Long-term Storage Fee
- Profit Analysis
- FeeOptimization Suggestions

Based on 2024 years Amazon FBA Rate

Version: 1.0.0
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime
import sys


class SizeTier(Enum):
    """FBA SizedivideLevel"""
    SMALL_STANDARD = "Small Standard"
    LARGE_STANDARD = "Large Standard"
    SMALL_OVERSIZE = "Small Oversize"
    MEDIUM_OVERSIZE = "Medium Oversize"
    LARGE_OVERSIZE = "Large Oversize"
    SPECIAL_OVERSIZE = "Special Oversize"


class StorageSeason(Enum):
    """StorageSeason"""
    STANDARD = "standard"      # Jan-Sep
    PEAK = "peak"              # Oct-Dec


# ============================================================
# 2024 FBA RateTable
# ============================================================

# FBA Fulfillment Fee (Fulfillmentfee) - 2024
FBA_FULFILLMENT_FEES = {
    SizeTier.SMALL_STANDARD: {
        #  heavy quantity (oz): Fee
        "base": 3.22,
        "per_oz_above_4": 0.08,
        "max_weight_oz": 16,
    },
    SizeTier.LARGE_STANDARD: {
        # By weight tier
        "tiers": [
            (4, 3.86),      # 0-4 oz
            (8, 4.08),      # 4+ to 8 oz
            (12, 4.24),     # 8+ to 12 oz
            (16, 4.75),     # 12+ to 16 oz (1 lb)
            (32, 5.40),     # 1+ to 2 lb
            (48, 6.10),     # 2+ to 3 lb
            (320, 6.10),    # 3+ to 20 lb (base + per lb)
        ],
        "per_lb_above_3": 0.38,
    },
    SizeTier.SMALL_OVERSIZE: {
        "base": 9.73,
        "per_lb_above_1": 0.42,
    },
    SizeTier.MEDIUM_OVERSIZE: {
        "base": 19.05,
        "per_lb_above_1": 0.42,
    },
    SizeTier.LARGE_OVERSIZE: {
        "base": 89.98,
        "per_lb_above_90": 0.83,
    },
    SizeTier.SPECIAL_OVERSIZE: {
        "base": 158.49,
        "per_lb_above_90": 0.83,
    },
}

# Monthly Storage Fee (monthsStoragefee) - 2024
STORAGE_FEE_PER_CUBIC_FOOT = {
    SizeTier.SMALL_STANDARD: {"standard": 0.78, "peak": 2.40},
    SizeTier.LARGE_STANDARD: {"standard": 0.78, "peak": 2.40},
    SizeTier.SMALL_OVERSIZE: {"standard": 0.56, "peak": 1.40},
    SizeTier.MEDIUM_OVERSIZE: {"standard": 0.56, "peak": 1.40},
    SizeTier.LARGE_OVERSIZE: {"standard": 0.56, "peak": 1.40},
    SizeTier.SPECIAL_OVERSIZE: {"standard": 0.56, "peak": 1.40},
}

# Long-term Storage Fee (PeriodStoragefee) - 2024
LONG_TERM_STORAGE_FEE = {
    "271_365_days": 1.50,    # Per cubic foot
    "over_365_days": 6.90,   # Per cubic foot
}

# Referral Fee (CommissionRate)
REFERRAL_FEE_RATES = {
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
    "automotive": 0.12,
}

# Removal/Disposal Fee
REMOVAL_FEE = {
    SizeTier.SMALL_STANDARD: 0.97,
    SizeTier.LARGE_STANDARD: 0.97,
    SizeTier.SMALL_OVERSIZE: 4.15,
    SizeTier.MEDIUM_OVERSIZE: 4.15,
    SizeTier.LARGE_OVERSIZE: 6.87,
    SizeTier.SPECIAL_OVERSIZE: 6.87,
}


# ============================================================
# Data Structures
# ============================================================

@dataclass
class ProductDimensions:
    """ProductSize"""
    length: float  # inches
    width: float   # inches
    height: float  # inches
    weight: float  # lbs
    
    @property
    def dimensional_weight(self) -> float:
        """Volume heavy  (DIM weight)"""
        return (self.length * self.width * self.height) / 139
    
    @property
    def billable_weight(self) -> float:
        """Billable weight (Take the greater of actual and dimensional weight)"""
        return max(self.weight, self.dimensional_weight)
    
    @property
    def cubic_feet(self) -> float:
        """Cubic feet"""
        return (self.length * self.width * self.height) / 1728
    
    @property
    def girth(self) -> float:
        """range (2*(width+height))"""
        return 2 * (self.width + self.height)
    
    @property
    def length_plus_girth(self) -> float:
        """Degree + range"""
        return self.length + self.girth


@dataclass
class ProductInput:
    """ProductInput"""
    # BasicInformation
    sku: str = "SKU001"
    name: str = "Product"
    
    # Size (inches)
    length: float = 0.0
    width: float = 0.0
    height: float = 0.0
    
    #  heavy quantity (lbs)
    weight: float = 0.0
    
    # Price
    selling_price: float = 0.0
    product_cost: float = 0.0
    
    # Logistics
    inbound_shipping_cost: float = 0.0  # InboundCost/piece
    
    # Other
    category: str = "default"
    monthly_units_sold: int = 100
    inventory_days: int = 30
    inventory_age_days: int = 0  # Libraryage (use at PeriodStoragefee)
    
    @property
    def dimensions(self) -> ProductDimensions:
        return ProductDimensions(
            length=self.length,
            width=self.width,
            height=self.height,
            weight=self.weight
        )


@dataclass
class FeeBreakdown:
    """FeeBreakdown"""
    # FBA Fee
    fba_fulfillment_fee: float = 0.0
    monthly_storage_fee: float = 0.0
    long_term_storage_fee: float = 0.0
    referral_fee: float = 0.0
    
    # OtherFee
    inbound_shipping: float = 0.0
    removal_fee: float = 0.0
    
    # Summary
    total_amazon_fees: float = 0.0
    total_all_fees: float = 0.0
    
    # Profit
    gross_profit: float = 0.0
    net_profit: float = 0.0
    gross_margin: float = 0.0
    net_margin: float = 0.0
    roi: float = 0.0


@dataclass
class SizeTierInfo:
    """SizedivideLevelInformation"""
    tier: SizeTier
    reason: str
    billable_weight: float
    dimensional_weight: float
    actual_weight: float


@dataclass
class OptimizationTip:
    """Optimization Suggestions"""
    category: str
    tip: str
    tip_zh: str
    potential_savings: float


@dataclass
class CalculationResult:
    """CalculateResult"""
    product: ProductInput
    size_tier: SizeTierInfo
    fees: FeeBreakdown
    optimization_tips: List[OptimizationTip]
    summary: str
    summary_zh: str


# ============================================================
# CoreCalculateFunction
# ============================================================

def determine_size_tier(dims: ProductDimensions) -> SizeTierInfo:
    """JudgmentSizedivideLevel"""
    L, W, H = sorted([dims.length, dims.width, dims.height], reverse=True)
    weight_oz = dims.weight * 16
    
    # Small Standard: ≤15oz, ≤15"×12"×0.75"
    if weight_oz <= 16 and L <= 15 and W <= 12 and H <= 0.75:
        tier = SizeTier.SMALL_STANDARD
        reason = f"Weight ≤1lb, dims ≤15×12×0.75"
    
    # Large Standard: ≤20lb, ≤18"×14"×8"
    elif dims.weight <= 20 and L <= 18 and W <= 14 and H <= 8:
        tier = SizeTier.LARGE_STANDARD
        reason = f"Weight ≤20lb, dims ≤18×14×8"
    
    # Small Oversize: ≤70lb, ≤60"×30" (longest side ≤60, median ≤30)
    elif dims.weight <= 70 and L <= 60 and W <= 30:
        tier = SizeTier.SMALL_OVERSIZE
        reason = f"Weight ≤70lb, longest ≤60, median ≤30"
    
    # Medium Oversize: ≤150lb, length+girth ≤108"
    elif dims.weight <= 150 and dims.length_plus_girth <= 108:
        tier = SizeTier.MEDIUM_OVERSIZE
        reason = f"Weight ≤150lb, L+girth ≤108"
    
    # Large Oversize: ≤150lb, length+girth ≤165"
    elif dims.weight <= 150 and dims.length_plus_girth <= 165:
        tier = SizeTier.LARGE_OVERSIZE
        reason = f"Weight ≤150lb, L+girth ≤165"
    
    # Special Oversize
    else:
        tier = SizeTier.SPECIAL_OVERSIZE
        reason = f"Exceeds Large Oversize limits"
    
    return SizeTierInfo(
        tier=tier,
        reason=reason,
        billable_weight=dims.billable_weight,
        dimensional_weight=dims.dimensional_weight,
        actual_weight=dims.weight
    )


def calculate_fba_fulfillment_fee(size_tier: SizeTier, weight_lbs: float) -> float:
    """Calculate FBA Fulfillment"""
    weight_oz = weight_lbs * 16
    
    if size_tier == SizeTier.SMALL_STANDARD:
        fee_info = FBA_FULFILLMENT_FEES[size_tier]
        if weight_oz <= 4:
            return fee_info["base"]
        else:
            extra_oz = min(weight_oz - 4, 12)  # max 16oz total
            return fee_info["base"] + extra_oz * fee_info["per_oz_above_4"]
    
    elif size_tier == SizeTier.LARGE_STANDARD:
        fee_info = FBA_FULFILLMENT_FEES[size_tier]
        for max_oz, fee in fee_info["tiers"]:
            if weight_oz <= max_oz:
                return fee
        # Above 3 lb
        extra_lbs = weight_lbs - 3
        base = 6.10
        return base + extra_lbs * fee_info["per_lb_above_3"]
    
    elif size_tier == SizeTier.SMALL_OVERSIZE:
        fee_info = FBA_FULFILLMENT_FEES[size_tier]
        if weight_lbs <= 1:
            return fee_info["base"]
        return fee_info["base"] + (weight_lbs - 1) * fee_info["per_lb_above_1"]
    
    elif size_tier == SizeTier.MEDIUM_OVERSIZE:
        fee_info = FBA_FULFILLMENT_FEES[size_tier]
        if weight_lbs <= 1:
            return fee_info["base"]
        return fee_info["base"] + (weight_lbs - 1) * fee_info["per_lb_above_1"]
    
    elif size_tier == SizeTier.LARGE_OVERSIZE:
        fee_info = FBA_FULFILLMENT_FEES[size_tier]
        if weight_lbs <= 90:
            return fee_info["base"]
        return fee_info["base"] + (weight_lbs - 90) * fee_info["per_lb_above_90"]
    
    else:  # Special Oversize
        fee_info = FBA_FULFILLMENT_FEES[SizeTier.SPECIAL_OVERSIZE]
        if weight_lbs <= 90:
            return fee_info["base"]
        return fee_info["base"] + (weight_lbs - 90) * fee_info["per_lb_above_90"]


def calculate_storage_fee(size_tier: SizeTier, cubic_feet: float, month: int = None) -> float:
    """CalculatemonthsStoragefee"""
    if month is None:
        month = datetime.now().month
    
    season = "peak" if month >= 10 else "standard"
    rate = STORAGE_FEE_PER_CUBIC_FOOT[size_tier][season]
    
    return cubic_feet * rate


def calculate_long_term_storage_fee(cubic_feet: float, age_days: int) -> float:
    """CalculatePeriodStoragefee"""
    if age_days > 365:
        return cubic_feet * LONG_TERM_STORAGE_FEE["over_365_days"]
    elif age_days > 270:
        return cubic_feet * LONG_TERM_STORAGE_FEE["271_365_days"]
    return 0.0


def calculate_referral_fee(selling_price: float, category: str) -> float:
    """CalculateCommission"""
    rate = REFERRAL_FEE_RATES.get(category.lower(), REFERRAL_FEE_RATES["default"])
    return selling_price * rate


def calculate_all_fees(product: ProductInput) -> Tuple[FeeBreakdown, SizeTierInfo]:
    """Calculateplace has Fee"""
    dims = product.dimensions
    size_info = determine_size_tier(dims)
    
    # FBA Fulfillment
    fba_fee = calculate_fba_fulfillment_fee(size_info.tier, size_info.billable_weight)
    
    # monthsStoragefee ( by InventorydaysAllocate)
    storage_monthly = calculate_storage_fee(size_info.tier, dims.cubic_feet)
    storage_per_unit = storage_monthly * (product.inventory_days / 30)
    
    # PeriodStoragefee
    ltsf = calculate_long_term_storage_fee(dims.cubic_feet, product.inventory_age_days)
    
    # Commission
    referral = calculate_referral_fee(product.selling_price, product.category)
    
    # Removal fee
    removal = REMOVAL_FEE.get(size_info.tier, 0)
    
    # Summary
    total_amazon = fba_fee + storage_per_unit + ltsf + referral
    total_all = total_amazon + product.inbound_shipping_cost
    
    # ProfitCalculate
    gross_profit = product.selling_price - product.product_cost - referral - fba_fee
    net_profit = product.selling_price - product.product_cost - total_all
    
    gross_margin = gross_profit / product.selling_price if product.selling_price > 0 else 0
    net_margin = net_profit / product.selling_price if product.selling_price > 0 else 0
    
    # ROI
    total_investment = product.product_cost + product.inbound_shipping_cost
    roi = net_profit / total_investment if total_investment > 0 else 0
    
    fees = FeeBreakdown(
        fba_fulfillment_fee=round(fba_fee, 2),
        monthly_storage_fee=round(storage_per_unit, 2),
        long_term_storage_fee=round(ltsf, 2),
        referral_fee=round(referral, 2),
        inbound_shipping=round(product.inbound_shipping_cost, 2),
        removal_fee=round(removal, 2),
        total_amazon_fees=round(total_amazon, 2),
        total_all_fees=round(total_all, 2),
        gross_profit=round(gross_profit, 2),
        net_profit=round(net_profit, 2),
        gross_margin=round(gross_margin, 4),
        net_margin=round(net_margin, 4),
        roi=round(roi, 4),
    )
    
    return fees, size_info


def generate_optimization_tips(product: ProductInput, fees: FeeBreakdown, size_info: SizeTierInfo) -> List[OptimizationTip]:
    """GenerateOptimization Suggestions"""
    tips = []
    
    # SizeOptimization
    if size_info.tier == SizeTier.LARGE_STANDARD:
        if product.length > 15 or product.width > 12:
            tips.append(OptimizationTip(
                category="Size",
                tip="Consider smaller packaging to qualify for Small Standard tier",
                tip_zh="Consider reducing package size to reach small standardLevelother",
                potential_savings=fees.fba_fulfillment_fee - 3.22
            ))
    
    #  heavy quantityOptimization
    if size_info.dimensional_weight > size_info.actual_weight * 1.5:
        tips.append(OptimizationTip(
            category="Weight",
            tip="Product is being charged by dimensional weight. Reduce package size.",
            tip_zh="ProductCharge by dimensional weight。ReducePackagingSizeCan reduceFee。",
            potential_savings=0
        ))
    
    # Inventoryweeksconvert
    if product.inventory_days > 45:
        tips.append(OptimizationTip(
            category="Inventory",
            tip=f"Inventory days ({product.inventory_days}) is high. Faster turnover reduces storage fees.",
            tip_zh=f"Inventorydays ({product.inventory_days}) biasHigh。add fast weeksconvertCanReduceStoragefee。",
            potential_savings=fees.monthly_storage_fee * 0.3
        ))
    
    # PeriodStorage
    if product.inventory_age_days > 180:
        tips.append(OptimizationTip(
            category="Long-term Storage",
            tip="Watch out for long-term storage fees after 271 days",
            tip_zh="Note 271 daysWill generate afterPeriodStoragefee",
            potential_savings=0
        ))
    
    # Profit Margin
    if fees.net_margin < 0.15:
        tips.append(OptimizationTip(
            category="Pricing",
            tip="Net margin below 15%. Consider raising price or reducing costs.",
            tip_zh="Net Margin low  at  15%。Consider raising price or reducingCost。",
            potential_savings=0
        ))
    
    return tips


def calculate(product: ProductInput) -> CalculationResult:
    """MainCalculateFunction"""
    fees, size_info = calculate_all_fees(product)
    tips = generate_optimization_tips(product, fees, size_info)
    
    # GenerateSummary
    if fees.net_margin >= 0.20:
        status = "✅ Healthy"
        status_zh = "✅ Healthy"
    elif fees.net_margin >= 0.10:
        status = "⚠️ Marginal"
        status_zh = "⚠️  side edge"
    elif fees.net_margin >= 0:
        status = "🔴 Low"
        status_zh = "🔴  low "
    else:
        status = "💀 Loss"
        status_zh = "💀 Loss"
    
    summary = f"{status} | Net margin: {fees.net_margin*100:.1f}% | FBA fee: ${fees.fba_fulfillment_fee}"
    summary_zh = f"{status_zh} | Net Margin: {fees.net_margin*100:.1f}% | FBAfee: ${fees.fba_fulfillment_fee}"
    
    return CalculationResult(
        product=product,
        size_tier=size_info,
        fees=fees,
        optimization_tips=tips,
        summary=summary,
        summary_zh=summary_zh
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(result: CalculationResult, lang: str = "en") -> str:
    """FormatReport"""
    p = result.product
    f = result.fees
    s = result.size_tier
    
    if lang == "zh":
        lines = [
            "💰 **FBA FeeCalculateReport**",
            "",
            f"**Product**: {p.name} ({p.sku})",
            f"**Size**: {p.length}\" × {p.width}\" × {p.height}\"",
            f"** heavy quantity**: {p.weight} lbs ({p.weight*16:.0f} oz)",
            f"**Selling Price**: ${p.selling_price:.2f}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## 📏 SizedivideLevel: {s.tier.value}",
            f"   {s.reason}",
            f"   Billable weight: {s.billable_weight:.2f} lbs",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 💵 FeeBreakdown",
            "",
            f"```",
            f"Selling Price                    ${p.selling_price:.2f}",
            f"────────────────────────────────",
            f"ProductCost                -${p.product_cost:.2f}",
            f"FBA Fulfillment              -${f.fba_fulfillment_fee:.2f}",
            f"monthsStoragefee (Allocate)         -${f.monthly_storage_fee:.2f}",
            f"PlatformCommission                -${f.referral_fee:.2f}",
            f"InboundShipping                -${f.inbound_shipping:.2f}",
        ]
        
        if f.long_term_storage_fee > 0:
            lines.append(f"PeriodStoragefee              -${f.long_term_storage_fee:.2f}")
        
        lines.extend([
            f"────────────────────────────────",
            f"Amazon FeeTotal         ${f.total_amazon_fees:.2f}",
            f"totalFee                  ${f.total_all_fees:.2f}",
            f"────────────────────────────────",
            f"Gross Profit                  ${f.gross_profit:.2f} ({f.gross_margin*100:.1f}%)",
            f"Net Profit                  ${f.net_profit:.2f} ({f.net_margin*100:.1f}%)",
            f"ROI                     {f.roi*100:.1f}%",
            f"```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            result.summary_zh,
        ])
        
        if result.optimization_tips:
            lines.extend([
                "",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 💡 Optimization Suggestions",
                "",
            ])
            for i, tip in enumerate(result.optimization_tips, 1):
                lines.append(f"**{i}. [{tip.category}]** {tip.tip_zh}")
                if tip.potential_savings > 0:
                    lines.append(f"   potential in Save: ${tip.potential_savings:.2f}")
                lines.append("")
    else:
        lines = [
            "💰 **FBA Fee Calculation Report**",
            "",
            f"**Product**: {p.name} ({p.sku})",
            f"**Dimensions**: {p.length}\" × {p.width}\" × {p.height}\"",
            f"**Weight**: {p.weight} lbs ({p.weight*16:.0f} oz)",
            f"**Selling Price**: ${p.selling_price:.2f}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## 📏 Size Tier: {s.tier.value}",
            f"   {s.reason}",
            f"   Billable Weight: {s.billable_weight:.2f} lbs",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 💵 Fee Breakdown",
            "",
            f"```",
            f"Selling Price           ${p.selling_price:.2f}",
            f"────────────────────────────────",
            f"Product Cost            -${p.product_cost:.2f}",
            f"FBA Fulfillment Fee     -${f.fba_fulfillment_fee:.2f}",
            f"Monthly Storage (pro-rated) -${f.monthly_storage_fee:.2f}",
            f"Referral Fee            -${f.referral_fee:.2f}",
            f"Inbound Shipping        -${f.inbound_shipping:.2f}",
        ]
        
        if f.long_term_storage_fee > 0:
            lines.append(f"Long-term Storage       -${f.long_term_storage_fee:.2f}")
        
        lines.extend([
            f"────────────────────────────────",
            f"Total Amazon Fees       ${f.total_amazon_fees:.2f}",
            f"Total All Fees          ${f.total_all_fees:.2f}",
            f"────────────────────────────────",
            f"Gross Profit            ${f.gross_profit:.2f} ({f.gross_margin*100:.1f}%)",
            f"Net Profit              ${f.net_profit:.2f} ({f.net_margin*100:.1f}%)",
            f"ROI                     {f.roi*100:.1f}%",
            f"```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            result.summary,
        ])
        
        if result.optimization_tips:
            lines.extend([
                "",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 💡 Optimization Tips",
                "",
            ])
            for i, tip in enumerate(result.optimization_tips, 1):
                lines.append(f"**{i}. [{tip.category}]** {tip.tip}")
                if tip.potential_savings > 0:
                    lines.append(f"   Potential Savings: ${tip.potential_savings:.2f}")
                lines.append("")
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    # TestData
    test_product = ProductInput(
        sku="TEST001",
        name="Kitchen Gadget",
        length=10.0,
        width=6.0,
        height=3.0,
        weight=1.2,
        selling_price=29.99,
        product_cost=8.00,
        inbound_shipping_cost=1.50,
        category="kitchen",
        monthly_units_sold=100,
        inventory_days=45,
        inventory_age_days=60,
    )
    
    # ParseCommand line parameter
    if len(sys.argv) > 1:
        try:
            data = json.loads(sys.argv[1])
            test_product = ProductInput(**data)
        except:
            pass
    
    result = calculate(test_product)
    
    lang = "zh" if "--zh" in sys.argv else "en"
    print(format_report(result, lang))


if __name__ == "__main__":
    main()
