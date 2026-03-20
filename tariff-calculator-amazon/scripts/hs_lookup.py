#!/usr/bin/env python3
"""
HS Code Lookup & Matcher
HScodeQuery and smart can Match

Features:
- ProductDescription → HScodeRecommendation
- HScode → ProductCategoryother
- Section 301 ListQuery
- Common HScodeDataLibrary

Version: 1.0.0
"""

import re
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class HSCodeInfo:
    """HScodeInformation"""
    code: str
    description: str
    description_zh: str
    chapter: str
    section_301: bool
    section_301_rate: float
    notes: str = ""


# ============================================================
# HScodeDataLibrary (Common e-commerceProduct)
# ============================================================

HS_DATABASE = {
    # ElectronicProduct (Chapter 85)
    "8517120000": HSCodeInfo(
        code="8517120000",
        description="Smartphones",
        description_zh="Smartphone",
        chapter="85",
        section_301=True,
        section_301_rate=0.0,  # example outside 
        notes="Usually exempt from Section 301"
    ),
    "8518300000": HSCodeInfo(
        code="8518300000",
        description="Headphones and earphones",
        description_zh="Headphones",
        chapter="85",
        section_301=True,
        section_301_rate=0.075,
    ),
    "8471300000": HSCodeInfo(
        code="8471300000",
        description="Laptops and notebooks",
        description_zh="Laptop computer",
        chapter="84",
        section_301=True,
        section_301_rate=0.0,  # example outside 
        notes="Currently exempt from Section 301"
    ),
    "8504400000": HSCodeInfo(
        code="8504400000",
        description="Power adapters and chargers",
        description_zh="Power adapter/Charging",
        chapter="85",
        section_301=True,
        section_301_rate=0.25,
    ),
    "8528590000": HSCodeInfo(
        code="8528590000",
        description="Monitors",
        description_zh="Display",
        chapter="85",
        section_301=True,
        section_301_rate=0.25,
    ),
    
    # Home goods (Chapter 94)
    "9403200000": HSCodeInfo(
        code="9403200000",
        description="Metal furniture",
        description_zh="Metal furniture",
        chapter="94",
        section_301=True,
        section_301_rate=0.25,
    ),
    "9403600000": HSCodeInfo(
        code="9403600000",
        description="Wooden furniture",
        description_zh="Wooden furniture",
        chapter="94",
        section_301=True,
        section_301_rate=0.25,
    ),
    "9405100000": HSCodeInfo(
        code="9405100000",
        description="Chandeliers and ceiling lights",
        description_zh="Chandelier/Ceiling light",
        chapter="94",
        section_301=True,
        section_301_rate=0.25,
    ),
    "9405400000": HSCodeInfo(
        code="9405400000",
        description="LED lights and strips",
        description_zh="LEDlight/Light strip",
        chapter="94",
        section_301=True,
        section_301_rate=0.25,
    ),
    
    # Apparel (Chapter 61/62)
    "6109100000": HSCodeInfo(
        code="6109100000",
        description="Cotton T-shirts",
        description_zh="CottonTshirt",
        chapter="61",
        section_301=True,
        section_301_rate=0.075,
    ),
    "6110200000": HSCodeInfo(
        code="6110200000",
        description="Cotton sweaters",
        description_zh="Cotton sweater",
        chapter="61",
        section_301=True,
        section_301_rate=0.075,
    ),
    "6203420000": HSCodeInfo(
        code="6203420000",
        description="Men's cotton trousers",
        description_zh="Men cotton pants",
        chapter="62",
        section_301=True,
        section_301_rate=0.075,
    ),
    "6204620000": HSCodeInfo(
        code="6204620000",
        description="Women's cotton trousers",
        description_zh="Women cotton pants",
        chapter="62",
        section_301=True,
        section_301_rate=0.075,
    ),
    
    # shoeCategory (Chapter 64)
    "6402990000": HSCodeInfo(
        code="6402990000",
        description="Rubber/plastic footwear",
        description_zh="Rubber/Plastic shoes",
        chapter="64",
        section_301=True,
        section_301_rate=0.075,
    ),
    "6403990000": HSCodeInfo(
        code="6403990000",
        description="Leather footwear",
        description_zh="Leather shoes",
        chapter="64",
        section_301=True,
        section_301_rate=0.075,
    ),
    "6404190000": HSCodeInfo(
        code="6404190000",
        description="Textile footwear",
        description_zh="Textile shoes",
        chapter="64",
        section_301=True,
        section_301_rate=0.075,
    ),
    
    # boxPackage (Chapter 42)
    "4202210000": HSCodeInfo(
        code="4202210000",
        description="Leather handbags",
        description_zh="Leather handbag",
        chapter="42",
        section_301=True,
        section_301_rate=0.075,
    ),
    "4202920000": HSCodeInfo(
        code="4202920000",
        description="Backpacks and bags (textile)",
        description_zh="backPackage/bag (Textile)",
        chapter="42",
        section_301=True,
        section_301_rate=0.075,
    ),
    
    # Toy (Chapter 95)
    "9503000000": HSCodeInfo(
        code="9503000000",
        description="Toys and games",
        description_zh="ToyAndGame",
        chapter="95",
        section_301=True,
        section_301_rate=0.25,
    ),
    
    # Plastic products (Chapter 39)
    "3924100000": HSCodeInfo(
        code="3924100000",
        description="Plastic tableware and kitchenware",
        description_zh="Plastic tableware/Kitchenware",
        chapter="39",
        section_301=True,
        section_301_rate=0.25,
    ),
    "3926909000": HSCodeInfo(
        code="3926909000",
        description="Other plastic articles",
        description_zh="OtherPlastic products",
        chapter="39",
        section_301=True,
        section_301_rate=0.25,
    ),
    
    # Beauty care (Chapter 33)
    "3304990000": HSCodeInfo(
        code="3304990000",
        description="Beauty and makeup products",
        description_zh="BeautyProduct",
        chapter="33",
        section_301=False,
        section_301_rate=0.0,
    ),
    
    # Pet supplies
    "6307900000": HSCodeInfo(
        code="6307900000",
        description="Pet beds and textile products",
        description_zh="Pet bed/Textile products",
        chapter="63",
        section_301=True,
        section_301_rate=0.075,
    ),
}

# Keywords → HScodeMapping
KEYWORD_MAPPING = {
    # Electronic
    "earphone": "8518300000",
    "earbud": "8518300000",
    "headphone": "8518300000",
    "earbuds": "8518300000",
    "Headphones": "8518300000",
    "charger": "8504400000",
    "adapter": "8504400000",
    "Charging": "8504400000",
    "monitor": "8528590000",
    "Display": "8528590000",
    "laptop": "8471300000",
    "notebook": "8471300000",
    "Computer": "8471300000",
    "phone": "8517120000",
    "smartphone": "8517120000",
    "Phone": "8517120000",
    
    # Home
    "furniture": "9403600000",
    "Furniture": "9403600000",
    "desk": "9403200000",
    "table": "9403200000",
    "chair": "9401610000",
    "light": "9405400000",
    "lamp": "9405100000",
    "light": "9405400000",
    "led": "9405400000",
    
    # Apparel
    "t-shirt": "6109100000",
    "tshirt": "6109100000",
    "shirt": "6109100000",
    "sweater": "6110200000",
    "Sweater": "6110200000",
    "pants": "6203420000",
    "trousers": "6203420000",
    "Pants": "6203420000",
    
    # shoe
    "shoe": "6402990000",
    "footwear": "6402990000",
    "sneaker": "6404190000",
    "boot": "6403990000",
    "shoe": "6402990000",
    
    # boxPackage
    "bag": "4202920000",
    "backpack": "4202920000",
    "handbag": "4202210000",
    "Package": "4202920000",
    
    # Toy
    "toy": "9503000000",
    "game": "9503000000",
    "Toy": "9503000000",
    
    # Plastic
    "plastic": "3926909000",
    "Plastic": "3926909000",
    
    # Pet
    "pet": "6307900000",
    "Pet": "6307900000",
}


def search_hs_code(query: str) -> List[Tuple[str, HSCodeInfo, float]]:
    """Search HScode
    
    Return: [(hs_code, info, confidence), ...]
    """
    results = []
    query_lower = query.lower()
    
    # 1. Direct HScodeQuery
    if query.isdigit() and len(query) >= 4:
        for code, info in HS_DATABASE.items():
            if code.startswith(query):
                results.append((code, info, 1.0))
        if results:
            return sorted(results, key=lambda x: -x[2])
    
    # 2. KeywordsMatch
    for keyword, hs_code in KEYWORD_MAPPING.items():
        if keyword in query_lower:
            if hs_code in HS_DATABASE:
                info = HS_DATABASE[hs_code]
                confidence = 0.8 if len(keyword) > 3 else 0.6
                results.append((hs_code, info, confidence))
    
    # 3. DescriptionMatch
    for code, info in HS_DATABASE.items():
        desc_match = False
        if query_lower in info.description.lower():
            desc_match = True
            confidence = 0.7
        elif query_lower in info.description_zh:
            desc_match = True
            confidence = 0.7
        
        if desc_match and (code, info, confidence) not in results:
            results.append((code, info, confidence))
    
    # remove heavy andSort
    seen = set()
    unique_results = []
    for code, info, conf in sorted(results, key=lambda x: -x[2]):
        if code not in seen:
            seen.add(code)
            unique_results.append((code, info, conf))
    
    return unique_results[:5]


def get_hs_info(hs_code: str) -> HSCodeInfo:
    """Get HScodeDetails"""
    # PreciseMatch
    if hs_code in HS_DATABASE:
        return HS_DATABASE[hs_code]
    
    #  before suffixMatch
    for code, info in HS_DATABASE.items():
        if code.startswith(hs_code) or hs_code.startswith(code[:4]):
            return info
    
    # Return default
    chapter = hs_code[:2] if len(hs_code) >= 2 else "00"
    return HSCodeInfo(
        code=hs_code,
        description=f"HS Chapter {chapter} product",
        description_zh=f"HS number {chapter} chapterProduct",
        chapter=chapter,
        section_301=False,
        section_301_rate=0.0,
        notes="Custom HS code - verify with customs authority"
    )


def format_search_results(results: List[Tuple[str, HSCodeInfo, float]], lang: str = "en") -> str:
    """FormatSearchResult"""
    if not results:
        if lang == "zh":
            return "❌ Not foundMatch HScode，Please manuallyInputOr consult customs。"
        return "❌ No matching HS codes found. Please enter manually or consult customs."
    
    lines = []
    if lang == "zh":
        lines.append("🔍 **HScodeSearchResult**\n")
        for i, (code, info, conf) in enumerate(results, 1):
            conf_icon = "🟢" if conf >= 0.8 else "🟡" if conf >= 0.6 else "🔴"
            s301 = f"⚠️ 301Tariff {info.section_301_rate*100:.1f}%" if info.section_301 and info.section_301_rate > 0 else ""
            lines.append(f"**{i}. {code}** {conf_icon}")
            lines.append(f"   {info.description_zh}")
            if s301:
                lines.append(f"   {s301}")
            lines.append("")
    else:
        lines.append("🔍 **HS Code Search Results**\n")
        for i, (code, info, conf) in enumerate(results, 1):
            conf_icon = "🟢" if conf >= 0.8 else "🟡" if conf >= 0.6 else "🔴"
            s301 = f"⚠️ Section 301: {info.section_301_rate*100:.1f}%" if info.section_301 and info.section_301_rate > 0 else ""
            lines.append(f"**{i}. {code}** {conf_icon}")
            lines.append(f"   {info.description}")
            if s301:
                lines.append(f"   {s301}")
            lines.append("")
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    import sys
    
    lang = "zh" if "--zh" in sys.argv else "en"
    query = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "earbuds"
    
    results = search_hs_code(query)
    print(format_search_results(results, lang))


if __name__ == "__main__":
    main()
