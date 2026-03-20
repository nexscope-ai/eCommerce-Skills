#!/usr/bin/env python3
"""
Tariff Calculator - Core Engine
TariffCalculate - Core Engine

Features:
- TariffTax RateQuery (HScode → Tax Rate)
- TariffCalculate (goodsValue × Tax Rate)
- VAT/GST Calculate
-  to shoreCost (Landed Cost) CompleteCalculate
- Section 301 TariffQuery
- Trade agreement benefits
-  many CurrencySupport

Version: 1.0.0
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime
import sys


class Country(Enum):
    """Country/Region"""
    CN = "CN"  #  in country
    US = "US"  # USA
    EU = "EU"  # EU
    UK = "UK"  # UK
    CA = "CA"  # Canada big 
    AU = "AU"  # Australia
    VN = "VN"  # Vietnam
    MX = "MX"  # Mexico
    IN = "IN"  # printDegree
    JP = "JP"  # Daybasic
    KR = "KR"  # Korea


# ============================================================
# Tax RateData (2024)
# ============================================================

# BasicTariffTax Rate (MFN  most MFN)
BASE_TARIFF_RATES = {
    # HS Chapter  before 2position → BasicTax Rate
    "39": {"US": 0.065, "EU": 0.065, "UK": 0.065, "CA": 0.06, "AU": 0.05},  # Plastic
    "42": {"US": 0.08, "EU": 0.04, "UK": 0.04, "CA": 0.08, "AU": 0.05},   # Leather products
    "61": {"US": 0.12, "EU": 0.12, "UK": 0.12, "CA": 0.18, "AU": 0.10},   # Knitted apparel
    "62": {"US": 0.12, "EU": 0.12, "UK": 0.12, "CA": 0.18, "AU": 0.10},   # Non-knitted apparel
    "64": {"US": 0.10, "EU": 0.08, "UK": 0.08, "CA": 0.18, "AU": 0.05},   # shoeCategory
    "84": {"US": 0.0, "EU": 0.02, "UK": 0.02, "CA": 0.0, "AU": 0.0},      # Mechanical equipment
    "85": {"US": 0.0, "EU": 0.02, "UK": 0.02, "CA": 0.0, "AU": 0.0},      # Electronicelectric
    "94": {"US": 0.0, "EU": 0.0, "UK": 0.0, "CA": 0.08, "AU": 0.05},      # Furniture
    "95": {"US": 0.0, "EU": 0.045, "UK": 0.045, "CA": 0.0, "AU": 0.05},   # Toy
    "default": {"US": 0.05, "EU": 0.05, "UK": 0.05, "CA": 0.05, "AU": 0.05},
}

# Section 301 Tariff ( in country → USA)
SECTION_301_RATES = {
    # HS 4Digit code → AdditionalTax Rate
    "8471": 0.25,  # Computer
    "8473": 0.25,  # Computer accessories
    "8504": 0.25,  # Transformer/Power
    "8517": 0.25,  # Communication equipment
    "8528": 0.25,  # Display
    "9403": 0.25,  # Furniture
    "9405": 0.25,  # Lighting
    "9503": 0.25,  # Toy
    "6110": 0.075, # Knit shirt
    "6203": 0.075, # Men wear
    "6204": 0.075, # Women wear
    "6402": 0.075, # shoeCategory
    "3926": 0.25,  # Plastic products
    "4202": 0.075, # boxPackage
}

# VAT/GST Tax Rate
VAT_RATES = {
    "US": 0.0,      # US has no federal VAT ( each state has  Sales Tax)
    "EU": 0.20,     # EUAverage (Germany19%, France20%, meaning big profit22%)
    "UK": 0.20,     # UK VAT 20%
    "CA": 0.05,     # Canada big  GST 5% (+ PST varies)
    "AU": 0.10,     # Australia GST 10%
}

# EU each country VAT
EU_VAT_RATES = {
    "DE": 0.19,  # Germany
    "FR": 0.20,  # France
    "IT": 0.22,  # meaning big profit
    "ES": 0.21,  # Spain
    "NL": 0.21,  # Netherlands
    "PL": 0.23,  # Poland
}

# Trade agreement benefits
TRADE_AGREEMENTS = {
    ("MX", "US"): {"name": "USMCA", "reduction": 1.0},  # 100% Exemption
    ("CA", "US"): {"name": "USMCA", "reduction": 1.0},
    ("VN", "EU"): {"name": "EVFTA", "reduction": 0.5},  # 50% Exemption
    ("AU", "US"): {"name": "AUSFTA", "reduction": 1.0},
    ("KR", "US"): {"name": "KORUS", "reduction": 1.0},
}

# CurrencyExchange rate ( for  USD)
EXCHANGE_RATES = {
    "USD": 1.0,
    "EUR": 1.08,
    "GBP": 1.26,
    "CAD": 0.74,
    "AUD": 0.65,
    "CNY": 0.14,
    "JPY": 0.0067,
}


# ============================================================
# Data Structures
# ============================================================

@dataclass
class ProductInfo:
    """ProductInformation"""
    description: str = ""
    hs_code: str = ""           # 6-10position HScode
    origin_country: str = "CN"  # Country of origin
    fob_value: float = 0.0      # FOB Price (USD)
    quantity: int = 1
    unit_weight_kg: float = 0.0
    currency: str = "USD"


@dataclass
class ShippingInfo:
    """TransportInformation"""
    destination_country: str = "US"
    destination_eu_country: str = ""  # EU specificCountry
    shipping_method: str = "sea"      # sea/air/express
    freight_cost: float = 0.0         # Shipping (USD)
    insurance_rate: float = 0.003     # InsuranceRate (0.3%)


@dataclass
class CostBreakdown:
    """Cost Breakdown"""
    # Basic
    fob_value: float = 0.0
    freight: float = 0.0
    insurance: float = 0.0
    cif_value: float = 0.0
    
    # Taxes and fees
    base_tariff_rate: float = 0.0
    base_tariff: float = 0.0
    section_301_rate: float = 0.0
    section_301_tariff: float = 0.0
    total_tariff_rate: float = 0.0
    total_tariff: float = 0.0
    vat_rate: float = 0.0
    vat: float = 0.0
    
    # Miscellaneous fees
    customs_clearance: float = 0.0
    port_fees: float = 0.0
    inland_freight: float = 0.0
    other_fees: float = 0.0
    
    # Summary
    total_taxes_fees: float = 0.0
    landed_cost: float = 0.0
    landed_cost_per_unit: float = 0.0
    
    # Trade agreement
    trade_agreement: str = ""
    tariff_reduction: float = 0.0


@dataclass
class TariffResult:
    """CalculateResult"""
    product: ProductInfo
    shipping: ShippingInfo
    breakdown: CostBreakdown
    hs_code_info: Dict
    warnings: List[str]
    summary: str
    summary_zh: str


# ============================================================
# CoreCalculateFunction
# ============================================================

def get_hs_chapter(hs_code: str) -> str:
    """Get HS Chapter ( before 2position)"""
    return hs_code[:2] if len(hs_code) >= 2 else "00"


def get_hs_heading(hs_code: str) -> str:
    """Get HS Tax ID ( before 4position)"""
    return hs_code[:4] if len(hs_code) >= 4 else "0000"


def get_base_tariff_rate(hs_code: str, destination: str) -> float:
    """GetBasicTariffTax Rate"""
    chapter = get_hs_chapter(hs_code)
    rates = BASE_TARIFF_RATES.get(chapter, BASE_TARIFF_RATES["default"])
    return rates.get(destination, 0.05)


def get_section_301_rate(hs_code: str, origin: str, destination: str) -> float:
    """Get Section 301 AdditionalTariff"""
    if origin != "CN" or destination != "US":
        return 0.0
    
    heading = get_hs_heading(hs_code)
    return SECTION_301_RATES.get(heading, 0.0)


def get_trade_agreement(origin: str, destination: str) -> Optional[Dict]:
    """Get trade agreement benefits"""
    return TRADE_AGREEMENTS.get((origin, destination))


def get_vat_rate(destination: str, eu_country: str = "") -> float:
    """GetVAT/GST Tax Rate"""
    if destination == "EU" and eu_country:
        return EU_VAT_RATES.get(eu_country, VAT_RATES["EU"])
    return VAT_RATES.get(destination, 0.0)


def estimate_freight(weight_kg: float, method: str, destination: str) -> float:
    """EstimateShipping"""
    # Simple estimate
    rates = {
        "sea": {"US": 0.8, "EU": 1.0, "UK": 1.1, "CA": 0.7, "AU": 1.2},     # $/kg
        "air": {"US": 5.0, "EU": 5.5, "UK": 5.5, "CA": 4.5, "AU": 6.0},     # $/kg
        "express": {"US": 8.0, "EU": 9.0, "UK": 9.0, "CA": 7.5, "AU": 10.0}, # $/kg
    }
    rate = rates.get(method, rates["sea"]).get(destination, 1.0)
    return weight_kg * rate


def calculate_landed_cost(
    product: ProductInfo,
    shipping: ShippingInfo,
    customs_clearance: float = 150.0,
    port_fees: float = 50.0,
    inland_freight: float = 100.0,
    other_fees: float = 0.0
) -> TariffResult:
    """Calculate to shoreCost"""
    
    warnings = []
    hs_info = {
        "code": product.hs_code,
        "chapter": get_hs_chapter(product.hs_code),
        "heading": get_hs_heading(product.hs_code),
    }
    
    # 1. FOB
    fob = product.fob_value
    
    # 2. Shipping
    freight = shipping.freight_cost
    if freight == 0 and product.unit_weight_kg > 0:
        total_weight = product.unit_weight_kg * product.quantity
        freight = estimate_freight(total_weight, shipping.shipping_method, shipping.destination_country)
        warnings.append(f"Freight estimated: ${freight:.2f} based on {total_weight}kg")
    
    # 3. Insurance
    insurance = fob * shipping.insurance_rate
    
    # 4. CIF
    cif = fob + freight + insurance
    
    # 5. BasicTariff
    base_rate = get_base_tariff_rate(product.hs_code, shipping.destination_country)
    
    # 6. Section 301 ( in country→USA)
    s301_rate = get_section_301_rate(product.hs_code, product.origin_country, shipping.destination_country)
    if s301_rate > 0:
        warnings.append(f"⚠️ Section 301 tariff applies: {s301_rate*100:.1f}%")
    
    # 7. Trade agreement benefits
    agreement = get_trade_agreement(product.origin_country, shipping.destination_country)
    tariff_reduction = 0.0
    agreement_name = ""
    if agreement:
        agreement_name = agreement["name"]
        tariff_reduction = base_rate * agreement["reduction"]
        base_rate = base_rate * (1 - agreement["reduction"])
        warnings.append(f"✅ Trade agreement {agreement_name} applies: {agreement['reduction']*100:.0f}% tariff reduction")
    
    # 8. totalTariff
    total_tariff_rate = base_rate + s301_rate
    total_tariff = cif * total_tariff_rate
    
    # 9. VAT/GST
    vat_rate = get_vat_rate(shipping.destination_country, shipping.destination_eu_country)
    vat_base = cif + total_tariff  # VAT UsuallyBased on CIF + Tariff
    vat = vat_base * vat_rate
    
    # 10. totalTaxes and fees
    total_taxes = total_tariff + vat + customs_clearance + port_fees
    
    # 11.  to shoreCost
    landed_cost = cif + total_taxes + inland_freight + other_fees
    landed_cost_per_unit = landed_cost / product.quantity if product.quantity > 0 else landed_cost
    
    breakdown = CostBreakdown(
        fob_value=round(fob, 2),
        freight=round(freight, 2),
        insurance=round(insurance, 2),
        cif_value=round(cif, 2),
        base_tariff_rate=round(base_rate, 4),
        base_tariff=round(cif * base_rate, 2),
        section_301_rate=round(s301_rate, 4),
        section_301_tariff=round(cif * s301_rate, 2),
        total_tariff_rate=round(total_tariff_rate, 4),
        total_tariff=round(total_tariff, 2),
        vat_rate=round(vat_rate, 4),
        vat=round(vat, 2),
        customs_clearance=round(customs_clearance, 2),
        port_fees=round(port_fees, 2),
        inland_freight=round(inland_freight, 2),
        other_fees=round(other_fees, 2),
        total_taxes_fees=round(total_taxes, 2),
        landed_cost=round(landed_cost, 2),
        landed_cost_per_unit=round(landed_cost_per_unit, 2),
        trade_agreement=agreement_name,
        tariff_reduction=round(tariff_reduction, 4),
    )
    
    # Summary
    summary = f"Landed Cost: ${landed_cost:.2f} | Tariff: {total_tariff_rate*100:.1f}% (${total_tariff:.2f}) | VAT: {vat_rate*100:.0f}%"
    summary_zh = f" to shoreCost: ${landed_cost:.2f} | Tariff: {total_tariff_rate*100:.1f}% (${total_tariff:.2f}) | VAT: {vat_rate*100:.0f}%"
    
    return TariffResult(
        product=product,
        shipping=shipping,
        breakdown=breakdown,
        hs_code_info=hs_info,
        warnings=warnings,
        summary=summary,
        summary_zh=summary_zh,
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(result: TariffResult, lang: str = "en") -> str:
    """FormatReport"""
    p = result.product
    s = result.shipping
    b = result.breakdown
    
    origin_names = {"CN": "China 🇨🇳", "VN": "Vietnam 🇻🇳", "MX": "Mexico 🇲🇽", "IN": "India 🇮🇳"}
    dest_names = {"US": "USA 🇺🇸", "EU": "EU 🇪🇺", "UK": "UK 🇬🇧", "CA": "Canada 🇨🇦", "AU": "Australia 🇦🇺"}
    
    origin_display = origin_names.get(p.origin_country, p.origin_country)
    dest_display = dest_names.get(s.destination_country, s.destination_country)
    
    if lang == "zh":
        lines = [
            "💰 **Tariff and  to shoreCostCalculateReport**",
            "",
            f"**Product**: {p.description or 'N/A'}",
            f"**HScode**: {p.hs_code}",
            f"**Route**: {origin_display} → {dest_display}",
            f"**Quantity**: {p.quantity} piece",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📦 Cost Breakdown",
            "",
            "```",
            f"FOB goodsValue                ${b.fob_value:>10,.2f}",
            f"InternationalShipping                ${b.freight:>10,.2f}",
            f"Insurance fee (0.3%)           ${b.insurance:>10,.2f}",
            f"────────────────────────────────────",
            f"CIF  to CIF price              ${b.cif_value:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 🏛️ Taxes and feesBreakdown",
            "",
            "```",
            f"BasicTariff ({b.base_tariff_rate*100:>5.1f}%)       ${b.base_tariff:>10,.2f}",
        ]
        
        if b.section_301_rate > 0:
            lines.append(f"Section 301 ({b.section_301_rate*100:>4.1f}%)     ${b.section_301_tariff:>10,.2f}")
        
        lines.extend([
            f"────────────────────────────────────",
            f"totalTariff ({b.total_tariff_rate*100:>5.1f}%)         ${b.total_tariff:>10,.2f}",
        ])
        
        if b.vat_rate > 0:
            lines.append(f"VAT/GST ({b.vat_rate*100:>4.0f}%)       ${b.vat:>10,.2f}")
        
        lines.extend([
            f"Customs clearancefee                  ${b.customs_clearance:>10,.2f}",
            f"Portfee                  ${b.port_fees:>10,.2f}",
            f"────────────────────────────────────",
            f"Taxes and feesTotal                ${b.total_taxes_fees:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 🚚 OtherFee",
            "",
            "```",
            f" inside landShipping                ${b.inland_freight:>10,.2f}",
            f"Other Fees                ${b.other_fees:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 💵  to shoreCostSummary",
            "",
            "```",
            f"CIF  to CIF price              ${b.cif_value:>10,.2f}",
            f"Taxes and feesTotal                ${b.total_taxes_fees:>10,.2f}",
            f"OtherFee                ${b.inland_freight + b.other_fees:>10,.2f}",
            f"════════════════════════════════════",
            f"total to shoreCost              ${b.landed_cost:>10,.2f}",
            f"Single pieceCost                ${b.landed_cost_per_unit:>10,.2f}",
            "```",
        ])
        
        if result.warnings:
            lines.extend([
                "",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## ⚠️ NoticeItem",
                "",
            ])
            for w in result.warnings:
                lines.append(f"• {w}")
        
        lines.extend([
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            result.summary_zh,
        ])
    else:
        lines = [
            "💰 **Tariff & Landed Cost Report**",
            "",
            f"**Product**: {p.description or 'N/A'}",
            f"**HS Code**: {p.hs_code}",
            f"**Route**: {origin_display} → {dest_display}",
            f"**Quantity**: {p.quantity} units",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📦 Cost Breakdown",
            "",
            "```",
            f"FOB Value               ${b.fob_value:>10,.2f}",
            f"International Freight   ${b.freight:>10,.2f}",
            f"Insurance (0.3%)        ${b.insurance:>10,.2f}",
            f"────────────────────────────────────",
            f"CIF Value               ${b.cif_value:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 🏛️ Duties & Taxes",
            "",
            "```",
            f"Base Tariff ({b.base_tariff_rate*100:>5.1f}%)      ${b.base_tariff:>10,.2f}",
        ]
        
        if b.section_301_rate > 0:
            lines.append(f"Section 301 ({b.section_301_rate*100:>4.1f}%)     ${b.section_301_tariff:>10,.2f}")
        
        lines.extend([
            f"────────────────────────────────────",
            f"Total Tariff ({b.total_tariff_rate*100:>4.1f}%)     ${b.total_tariff:>10,.2f}",
        ])
        
        if b.vat_rate > 0:
            lines.append(f"VAT/GST ({b.vat_rate*100:>4.0f}%)           ${b.vat:>10,.2f}")
        
        lines.extend([
            f"Customs Clearance       ${b.customs_clearance:>10,.2f}",
            f"Port Fees               ${b.port_fees:>10,.2f}",
            f"────────────────────────────────────",
            f"Total Taxes & Fees      ${b.total_taxes_fees:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 🚚 Other Costs",
            "",
            "```",
            f"Inland Freight          ${b.inland_freight:>10,.2f}",
            f"Other Fees              ${b.other_fees:>10,.2f}",
            "```",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 💵 Landed Cost Summary",
            "",
            "```",
            f"CIF Value               ${b.cif_value:>10,.2f}",
            f"Total Taxes & Fees      ${b.total_taxes_fees:>10,.2f}",
            f"Other Costs             ${b.inland_freight + b.other_fees:>10,.2f}",
            f"════════════════════════════════════",
            f"Total Landed Cost       ${b.landed_cost:>10,.2f}",
            f"Cost Per Unit           ${b.landed_cost_per_unit:>10,.2f}",
            "```",
        ])
        
        if result.warnings:
            lines.extend([
                "",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## ⚠️ Notices",
                "",
            ])
            for w in result.warnings:
                lines.append(f"• {w}")
        
        lines.extend([
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            result.summary,
        ])
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    lang = "zh" if "--zh" in sys.argv else "en"
    
    # DemoData
    product = ProductInfo(
        description="Wireless Bluetooth Earbuds",
        hs_code="8518300000",
        origin_country="CN",
        fob_value=5000.00,
        quantity=500,
        unit_weight_kg=0.1,
    )
    
    shipping = ShippingInfo(
        destination_country="US",
        shipping_method="sea",
        freight_cost=200.00,
        insurance_rate=0.003,
    )
    
    # Calculate
    result = calculate_landed_cost(product, shipping)
    
    # Output
    print(format_report(result, lang))


if __name__ == "__main__":
    main()
