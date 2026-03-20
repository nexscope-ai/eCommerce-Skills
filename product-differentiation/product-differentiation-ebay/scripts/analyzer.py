#!/usr/bin/env python3
"""
Product Differentiation Analyzer - Core Engine
ProductDifferenceAnalyze - Core Engine

Features:
- CompetitorFeatureComparisonMatrix
- CompetitorNegative ReviewPain pointMining
- Positive ReviewSelling point extraction
- Difference angleDegreeIdentify
- MarketPositioningStrategy
- PricingStrategyRecommendation
- MarketingSelling pointRecommendation
- ProductImproveRecommendation

SupportProgressiveAnalyze:
L1: BasicComparison (ProductInformation)
L2: Pain pointAnalyze (+ CompetitorNegative Review)
L3: Selling point extraction (+ SelfPositive Review)
L4: CompleteStrategy (+ MarketData)

Version: 1.0.0
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime
import sys
import re
from collections import Counter


class AnalysisLevel(Enum):
    """AnalyzelayerLevel"""
    L1 = "L1"  # BasicComparison
    L2 = "L2"  # Pain pointAnalyze
    L3 = "L3"  # Selling point extraction
    L4 = "L4"  # CompleteStrategy


class DiffAngle(Enum):
    """Difference angleDegree"""
    FUNCTION = "function"       # FeatureDifference
    QUALITY = "quality"         # QualityDifference
    DESIGN = "design"           # Design difference
    PRICE = "price"             # PriceDifference
    SERVICE = "service"         # Service difference
    AUDIENCE = "audience"       # Audience difference
    SCENARIO = "scenario"       # Scenario difference
    BRAND = "brand"             # BrandDifference


# ============================================================
# Pain pointKeywordsLibrary
# ============================================================

PAIN_POINT_KEYWORDS = {
    "quality": {
        "en": ["cheap", "broke", "broken", "flimsy", "poor quality", "fell apart", "defective", "doesn't last", "stopped working"],
        "zh": ["Poor quality", " bad  ", "Fragile", "Poor workmanship", "Not durable", "StopWork"],
    },
    "function": {
        "en": ["doesn't work", "not working", "malfunction", "missing feature", "can't", "won't", "failed", "useless"],
        "zh": ["notWork", "Fault", "FeatureMissing", "Cannot", "Failed", "Useless"],
    },
    "design": {
        "en": ["ugly", "looks cheap", "bulky", "heavy", "uncomfortable", "awkward", "hard to use", "confusing"],
        "zh": ["ugly", "Looks cheap", "clumsy heavy ", " heavy ", "Uncomfortable", "Hard to use", "Complex"],
    },
    "size": {
        "en": ["too small", "too big", "wrong size", "doesn't fit", "smaller than expected", "bigger than"],
        "zh": [" too  small ", " too  big ", "Sizenot for ", "Not suitable"],
    },
    "shipping": {
        "en": ["late", "damaged", "wrong item", "missing parts", "packaging"],
        "zh": ["late to ", "loss bad ", "Sent wrong", "Missing parts", "Packaging"],
    },
    "value": {
        "en": ["overpriced", "not worth", "waste of money", "rip off", "too expensive"],
        "zh": [" too expensive", "notValue", "Waste money", "trap"],
    },
}

SELLING_POINT_KEYWORDS = {
    "quality": {
        "en": ["solid", "sturdy", "durable", "well made", "high quality", "premium", "excellent", "perfect"],
        "zh": ["Sturdy", "Durable", "Workmanship good ", "HighQuality", "Quality", "Perfect"],
    },
    "function": {
        "en": ["works great", "works perfectly", "easy to use", "convenient", "efficient", "powerful", "fast"],
        "zh": [" good use", "Convenient", "Higheffect", "strong big ", " fast "],
    },
    "design": {
        "en": ["beautiful", "sleek", "stylish", "modern", "compact", "lightweight", "elegant"],
        "zh": ["Beautiful", "Timeyet", "Modern", " small clever", " light easy", "Elegant"],
    },
    "value": {
        "en": ["great value", "worth it", "good price", "affordable", "best purchase", "recommend"],
        "zh": ["Value ", "Value for money", "Recommended", "Worth it"],
    },
    "service": {
        "en": ["great service", "fast shipping", "well packaged", "responsive seller"],
        "zh": ["Service good ", "Shipping fast ", "Packaging good ", "SellerResponse fast "],
    },
}


# ============================================================
# Data Structures
# ============================================================

@dataclass
class ProductInfo:
    """ProductInformation"""
    name: str = ""
    asin: str = ""
    price: float = 0.0
    rating: float = 0.0
    review_count: int = 0
    features: List[str] = field(default_factory=list)
    bullet_points: List[str] = field(default_factory=list)
    category: str = ""
    brand: str = ""
    is_mine: bool = False


@dataclass
class ReviewData:
    """Review Countdata"""
    positive: List[str] = field(default_factory=list)  # Positive Review
    negative: List[str] = field(default_factory=list)  # Negative Review
    neutral: List[str] = field(default_factory=list)   # Neutral review


@dataclass
class PainPoint:
    """Pain point"""
    category: str
    description: str
    description_zh: str
    frequency: int
    severity: str  # high/medium/low
    example_reviews: List[str] = field(default_factory=list)


@dataclass
class SellingPoint:
    """Selling point"""
    category: str
    description: str
    description_zh: str
    frequency: int
    strength: str  # strong/medium/weak
    example_reviews: List[str] = field(default_factory=list)


@dataclass
class DiffOpportunity:
    """Differentiation Opportunities"""
    angle: DiffAngle
    opportunity: str
    opportunity_zh: str
    priority: str  # high/medium/low
    action: str
    action_zh: str
    potential_impact: str


@dataclass
class PositioningStrategy:
    """PositioningStrategy"""
    position_type: str  # premium/value/niche/innovation
    target_audience: str
    target_audience_zh: str
    price_strategy: str
    price_strategy_zh: str
    key_message: str
    key_message_zh: str
    marketing_angles: List[str] = field(default_factory=list)


@dataclass
class AnalysisResult:
    """AnalyzeResult"""
    level: AnalysisLevel
    my_product: ProductInfo
    competitors: List[ProductInfo]
    comparison_matrix: Dict
    pain_points: List[PainPoint]
    selling_points: List[SellingPoint]
    diff_opportunities: List[DiffOpportunity]
    positioning: Optional[PositioningStrategy]
    action_items: List[Dict]
    next_level_hint: str
    next_level_hint_zh: str
    summary: str
    summary_zh: str


# ============================================================
# AnalyzeFunction
# ============================================================

def extract_pain_points(reviews: List[str], lang: str = "en") -> List[PainPoint]:
    """ from Negative Review in ExtractPain point"""
    pain_points = []
    category_counts = Counter()
    category_examples = {}
    
    for review in reviews:
        review_lower = review.lower()
        for category, keywords in PAIN_POINT_KEYWORDS.items():
            for keyword in keywords.get(lang, []) + keywords.get("en", []):
                if keyword.lower() in review_lower:
                    category_counts[category] += 1
                    if category not in category_examples:
                        category_examples[category] = []
                    if len(category_examples[category]) < 3:
                        category_examples[category].append(review[:100])
                    break
    
    category_names = {
        "quality": ("Quality Issues", "QualityIssue"),
        "function": ("Functionality Problems", "FeatureIssue"),
        "design": ("Design Flaws", "Design defect"),
        "size": ("Size/Fit Issues", "SizeIssue"),
        "shipping": ("Shipping/Packaging", "LogisticsPackaging"),
        "value": ("Value Concerns", "Value for money"),
    }
    
    for category, count in category_counts.most_common():
        if count >= 1:
            severity = "high" if count >= 5 else "medium" if count >= 2 else "low"
            names = category_names.get(category, (category.title(), category))
            pain_points.append(PainPoint(
                category=category,
                description=names[0],
                description_zh=names[1],
                frequency=count,
                severity=severity,
                example_reviews=category_examples.get(category, []),
            ))
    
    return pain_points


def extract_selling_points(reviews: List[str], lang: str = "en") -> List[SellingPoint]:
    """ from Positive ReviewExtract selling points from"""
    selling_points = []
    category_counts = Counter()
    category_examples = {}
    
    for review in reviews:
        review_lower = review.lower()
        for category, keywords in SELLING_POINT_KEYWORDS.items():
            for keyword in keywords.get(lang, []) + keywords.get("en", []):
                if keyword.lower() in review_lower:
                    category_counts[category] += 1
                    if category not in category_examples:
                        category_examples[category] = []
                    if len(category_examples[category]) < 3:
                        category_examples[category].append(review[:100])
                    break
    
    category_names = {
        "quality": ("Build Quality", "WorkmanshipQuality"),
        "function": ("Functionality", "Featurenature"),
        "design": ("Design & Aesthetics", "Beautiful design"),
        "value": ("Value for Money", "Value for money"),
        "service": ("Service & Shipping", "ServiceLogistics"),
    }
    
    for category, count in category_counts.most_common():
        if count >= 1:
            strength = "strong" if count >= 5 else "medium" if count >= 2 else "weak"
            names = category_names.get(category, (category.title(), category))
            selling_points.append(SellingPoint(
                category=category,
                description=names[0],
                description_zh=names[1],
                frequency=count,
                strength=strength,
                example_reviews=category_examples.get(category, []),
            ))
    
    return selling_points


def build_comparison_matrix(my_product: ProductInfo, competitors: List[ProductInfo]) -> Dict:
    """BuildComparisonMatrix"""
    matrix = {
        "products": [my_product.name] + [c.name for c in competitors],
        "prices": [my_product.price] + [c.price for c in competitors],
        "ratings": [my_product.rating] + [c.rating for c in competitors],
        "review_counts": [my_product.review_count] + [c.review_count for c in competitors],
    }
    
    # PricePositioning
    all_prices = [p for p in matrix["prices"] if p > 0]
    if all_prices:
        avg_price = sum(all_prices) / len(all_prices)
        matrix["price_position"] = "above_avg" if my_product.price > avg_price else "below_avg"
        matrix["avg_price"] = avg_price
    
    # RatingPositioning
    all_ratings = [r for r in matrix["ratings"] if r > 0]
    if all_ratings:
        avg_rating = sum(all_ratings) / len(all_ratings)
        matrix["rating_position"] = "above_avg" if my_product.rating > avg_rating else "below_avg"
        matrix["avg_rating"] = avg_rating
    
    return matrix


def identify_opportunities(
    my_product: ProductInfo,
    competitors: List[ProductInfo],
    pain_points: List[PainPoint],
    selling_points: List[SellingPoint],
    matrix: Dict
) -> List[DiffOpportunity]:
    """IdentifyDifferentiation Opportunities"""
    opportunities = []
    
    # 1. Based onCompetitorPain pointOpportunity
    for pain in pain_points:
        if pain.severity == "high":
            opp = DiffOpportunity(
                angle=DiffAngle.FUNCTION if pain.category == "function" else DiffAngle.QUALITY,
                opportunity=f"Address competitor weakness: {pain.description}",
                opportunity_zh=f"SolveCompetitorWeakness: {pain.description_zh}",
                priority="high",
                action=f"Improve {pain.category} and highlight in marketing",
                action_zh=f"Improve{pain.description_zh}and in Marketing in Highlight",
                potential_impact="High - directly addresses customer pain",
            )
            opportunities.append(opp)
    
    # 2. Based onPriceOpportunity
    if matrix.get("price_position") == "below_avg":
        opportunities.append(DiffOpportunity(
            angle=DiffAngle.PRICE,
            opportunity="Value positioning - lower price than competitors",
            opportunity_zh="Value for moneyPositioning - Price low  at Competitor",
            priority="medium",
            action="Emphasize value proposition in marketing",
            action_zh=" in Marketing in EmphasizeValue for money",
            potential_impact="Medium - price-sensitive customers",
        ))
    elif matrix.get("price_position") == "above_avg":
        opportunities.append(DiffOpportunity(
            angle=DiffAngle.PRICE,
            opportunity="Premium positioning - justify higher price",
            opportunity_zh="PremiumPositioning - ProofHigherPriceReasonable",
            priority="high",
            action="Highlight premium features and quality",
            action_zh="HighlightPremiumFeatureAndQuality",
            potential_impact="High - must justify price premium",
        ))
    
    # 3. Based onRatingOpportunity
    if matrix.get("rating_position") == "above_avg":
        opportunities.append(DiffOpportunity(
            angle=DiffAngle.QUALITY,
            opportunity="Quality leader - leverage higher rating",
            opportunity_zh="Qualitylead first  - UtilizeHigherRating",
            priority="high",
            action="Display rating prominently, collect more reviews",
            action_zh="HighlightDisplayRating，Collect more  many Review",
            potential_impact="High - social proof advantage",
        ))
    
    # 4. SegmentMarketOpportunity
    opportunities.append(DiffOpportunity(
        angle=DiffAngle.AUDIENCE,
        opportunity="Niche targeting - focus on specific user segment",
        opportunity_zh="SegmentPositioning - Focus on specificUserGroup",
        priority="medium",
        action="Identify underserved segment and tailor product/marketing",
        action_zh="IdentifyUnmetSegmentMarket，CustomProduct/Marketing",
        potential_impact="Medium - reduced competition in niche",
    ))
    
    return opportunities


def generate_positioning(
    my_product: ProductInfo,
    matrix: Dict,
    opportunities: List[DiffOpportunity]
) -> PositioningStrategy:
    """GeneratePositioningStrategy"""
    
    # ConfirmPositioningCategoryType
    price_pos = matrix.get("price_position", "below_avg")
    rating_pos = matrix.get("rating_position", "below_avg")
    
    if price_pos == "above_avg" and rating_pos == "above_avg":
        position_type = "premium"
        target = "Quality-conscious buyers willing to pay more"
        target_zh = "Willing for QualityPayPremiumUser"
        price_strategy = "Maintain premium pricing, bundle with extras"
        price_strategy_zh = "MaintainPremiumPricing，Bundle increaseValueService"
        key_message = "The premium choice for discerning customers"
        key_message_zh = "PremiumUserSmart choice"
    elif price_pos == "below_avg":
        position_type = "value"
        target = "Price-sensitive buyers seeking good deals"
        target_zh = "FindHighValue for moneyPriceSensitiveUser"
        price_strategy = "Competitive pricing, volume-focused"
        price_strategy_zh = "CompetitivePricing，Pursue sales volume"
        key_message = "Same quality, better price"
        key_message_zh = "same etcQuality， more excellentPrice"
    else:
        position_type = "balanced"
        target = "Mainstream buyers seeking reliable products"
        target_zh = "FindCanrelyProductMainflowUser"
        price_strategy = "Market-aligned pricing"
        price_strategy_zh = "MarketPricing"
        key_message = "The trusted choice"
        key_message_zh = "ValueTrustedChoice"
    
    marketing_angles = [
        f"[{opp.angle.value.upper()}] {opp.opportunity}" 
        for opp in opportunities[:3] if opp.priority == "high"
    ]
    
    return PositioningStrategy(
        position_type=position_type,
        target_audience=target,
        target_audience_zh=target_zh,
        price_strategy=price_strategy,
        price_strategy_zh=price_strategy_zh,
        key_message=key_message,
        key_message_zh=key_message_zh,
        marketing_angles=marketing_angles,
    )


def generate_action_items(
    opportunities: List[DiffOpportunity],
    pain_points: List[PainPoint],
    positioning: PositioningStrategy
) -> List[Dict]:
    """GenerateActionRecommendation"""
    actions = []
    
    # ProductImprove
    for pain in pain_points[:2]:
        if pain.severity in ["high", "medium"]:
            actions.append({
                "category": "Product",
                "category_zh": "Product",
                "action": f"Address {pain.description}",
                "action_zh": f"Solve{pain.description_zh}",
                "priority": "P1" if pain.severity == "high" else "P2",
                "timeline": "1-3 months",
            })
    
    # MarketingImprove
    for opp in opportunities[:2]:
        if opp.priority == "high":
            actions.append({
                "category": "Marketing",
                "category_zh": "Marketing",
                "action": opp.action,
                "action_zh": opp.action_zh,
                "priority": "P1",
                "timeline": "Immediate",
            })
    
    # PositioningRelated
    actions.append({
        "category": "Positioning",
        "category_zh": "Positioning",
        "action": f"Adopt {positioning.position_type} positioning strategy",
        "action_zh": f"Adopt{positioning.position_type}PositioningStrategy",
        "priority": "P1",
        "timeline": "Ongoing",
    })
    
    return actions


def determine_level(
    my_product: ProductInfo,
    competitors: List[ProductInfo],
    competitor_reviews: ReviewData,
    my_reviews: ReviewData
) -> AnalysisLevel:
    """ConfirmAnalyzelayerLevel"""
    has_products = my_product.name and len(competitors) > 0
    has_competitor_reviews = len(competitor_reviews.negative) > 0
    has_my_reviews = len(my_reviews.positive) > 0
    has_market_data = my_product.price > 0 and my_product.rating > 0
    
    if has_products and has_competitor_reviews and has_my_reviews and has_market_data:
        return AnalysisLevel.L4
    elif has_products and has_competitor_reviews and has_my_reviews:
        return AnalysisLevel.L3
    elif has_products and has_competitor_reviews:
        return AnalysisLevel.L2
    else:
        return AnalysisLevel.L1


def analyze(
    my_product: ProductInfo,
    competitors: List[ProductInfo],
    competitor_reviews: ReviewData = None,
    my_reviews: ReviewData = None,
) -> AnalysisResult:
    """MainAnalyzeFunction"""
    
    if competitor_reviews is None:
        competitor_reviews = ReviewData()
    if my_reviews is None:
        my_reviews = ReviewData()
    
    # ConfirmAnalyzelayerLevel
    level = determine_level(my_product, competitors, competitor_reviews, my_reviews)
    
    # BuildComparisonMatrix
    matrix = build_comparison_matrix(my_product, competitors)
    
    # ExtractPain point (L2+)
    pain_points = []
    if level.value >= AnalysisLevel.L2.value:
        pain_points = extract_pain_points(competitor_reviews.negative)
    
    # Extract selling points (L3+)
    selling_points = []
    if level.value >= AnalysisLevel.L3.value:
        selling_points = extract_selling_points(my_reviews.positive)
    
    # IdentifyDifferentiation Opportunities
    opportunities = identify_opportunities(my_product, competitors, pain_points, selling_points, matrix)
    
    # GeneratePositioningStrategy (L4)
    positioning = None
    if level == AnalysisLevel.L4:
        positioning = generate_positioning(my_product, matrix, opportunities)
    
    # GenerateActionRecommendation
    action_items = generate_action_items(opportunities, pain_points, positioning or PositioningStrategy(
        position_type="balanced", target_audience="", target_audience_zh="",
        price_strategy="", price_strategy_zh="", key_message="", key_message_zh=""
    ))
    
    #  below oneLevelHint
    hints = {
        AnalysisLevel.L1: ("Add competitor negative reviews for pain point analysis", "AddCompetitorNegative Review to ProceedPain pointAnalyze"),
        AnalysisLevel.L2: ("Add your product's positive reviews for selling point extraction", "AddyouProductPositive ReviewTo extract selling points"),
        AnalysisLevel.L3: ("Add price and rating data for complete positioning strategy", "AddPriceAndRatingDataTo obtainCompletePositioningStrategy"),
        AnalysisLevel.L4: ("Full analysis complete!", "CompleteAnalyze already Complete！"),
    }
    next_hint, next_hint_zh = hints[level]
    
    # Summary
    summary = f"Level {level.value} Analysis | {len(opportunities)} opportunities | {len(pain_points)} pain points identified"
    summary_zh = f"{level.value} LevelAnalyze | {len(opportunities)} Differentiation Opportunities | {len(pain_points)} Pain pointIdentify"
    
    return AnalysisResult(
        level=level,
        my_product=my_product,
        competitors=competitors,
        comparison_matrix=matrix,
        pain_points=pain_points,
        selling_points=selling_points,
        diff_opportunities=opportunities,
        positioning=positioning,
        action_items=action_items,
        next_level_hint=next_hint,
        next_level_hint_zh=next_hint_zh,
        summary=summary,
        summary_zh=summary_zh,
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(result: AnalysisResult, lang: str = "en") -> str:
    """FormatReport"""
    
    if lang == "zh":
        lines = [
            "🎯 **ProductDifferenceAnalyzeReport**",
            "",
            f"**AnalyzelayerLevel**: {result.level.value}",
            f"**IProduct**: {result.my_product.name}",
            f"**CompetitorQuantity**: {len(result.competitors)}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📊 CompetitorComparisonMatrix",
            "",
        ]
        
        # ComparisonTable
        lines.append("| Product | Price | Rating | Review Count |")
        lines.append("|------|------|------|--------|")
        lines.append(f"| **{result.my_product.name}** (I) | ${result.my_product.price:.2f} | {result.my_product.rating} | {result.my_product.review_count} |")
        for c in result.competitors:
            lines.append(f"| {c.name} | ${c.price:.2f} | {c.rating} | {c.review_count} |")
        
        if result.pain_points:
            lines.extend([
                "",
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 😤 CompetitorPain point (Differentiation Opportunities)",
                "",
            ])
            for i, pain in enumerate(result.pain_points, 1):
                severity_icon = "🔴" if pain.severity == "high" else "🟡" if pain.severity == "medium" else "🟢"
                lines.append(f"**{i}. {pain.description_zh}** {severity_icon}")
                lines.append(f"   Occurrence frequency: {pain.frequency} | CriticalprocessDegree: {pain.severity}")
                if pain.example_reviews:
                    lines.append(f"   Example: \"{pain.example_reviews[0][:50]}...\"")
                lines.append("")
        
        if result.selling_points:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## ✨ My selling point",
                "",
            ])
            for i, sp in enumerate(result.selling_points, 1):
                strength_icon = "💪" if sp.strength == "strong" else "👍" if sp.strength == "medium" else "👌"
                lines.append(f"**{i}. {sp.description_zh}** {strength_icon}")
                lines.append(f"   Occurrence frequency: {sp.frequency}")
                lines.append("")
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 💡 Differentiation Opportunities",
            "",
        ])
        for i, opp in enumerate(result.diff_opportunities[:5], 1):
            priority_icon = "🔴" if opp.priority == "high" else "🟡"
            lines.append(f"**{i}. [{opp.angle.value.upper()}] {opp.opportunity_zh}** {priority_icon}")
            lines.append(f"   Action: {opp.action_zh}")
            lines.append("")
        
        if result.positioning:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 🎯 PositioningStrategy",
                "",
                f"**PositioningCategoryType**: {result.positioning.position_type.upper()}",
                f"**Target audience**: {result.positioning.target_audience_zh}",
                f"**PriceStrategy**: {result.positioning.price_strategy_zh}",
                f"**CoreInformation**: {result.positioning.key_message_zh}",
                "",
            ])
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📋 Action Plan",
            "",
        ])
        for action in result.action_items[:5]:
            lines.append(f"**[{action['priority']}] [{action['category_zh']}]** {action['action_zh']}")
            lines.append(f"   Timeline: {action['timeline']}")
            lines.append("")
        
        if result.level != AnalysisLevel.L4:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                f"🔍 **Want to go deeperAnalyze？** {result.next_level_hint_zh}",
            ])
        
        lines.extend([
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            result.summary_zh,
        ])
    else:
        # English version (similar structure)
        lines = [
            "🎯 **Product Differentiation Analysis Report**",
            "",
            f"**Analysis Level**: {result.level.value}",
            f"**My Product**: {result.my_product.name}",
            f"**Competitors**: {len(result.competitors)}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📊 Comparison Matrix",
            "",
            "| Product | Price | Rating | Reviews |",
            "|---------|-------|--------|---------|",
            f"| **{result.my_product.name}** (Mine) | ${result.my_product.price:.2f} | {result.my_product.rating} | {result.my_product.review_count} |",
        ]
        for c in result.competitors:
            lines.append(f"| {c.name} | ${c.price:.2f} | {c.rating} | {c.review_count} |")
        
        if result.pain_points:
            lines.extend(["", "## 😤 Competitor Pain Points", ""])
            for i, pain in enumerate(result.pain_points, 1):
                lines.append(f"**{i}. {pain.description}** (Frequency: {pain.frequency})")
        
        if result.diff_opportunities:
            lines.extend(["", "## 💡 Differentiation Opportunities", ""])
            for i, opp in enumerate(result.diff_opportunities[:5], 1):
                lines.append(f"**{i}. [{opp.angle.value}]** {opp.opportunity}")
                lines.append(f"   Action: {opp.action}")
        
        if result.level != AnalysisLevel.L4:
            lines.extend(["", f"🔍 **Want deeper analysis?** {result.next_level_hint}"])
        
        lines.extend(["", result.summary])
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    lang = "zh" if "--zh" in sys.argv else "en"
    
    # DemoData
    my_product = ProductInfo(
        name="My Wireless Earbuds Pro",
        asin="B08MYASIN1",
        price=49.99,
        rating=4.3,
        review_count=150,
        features=["ANC", "30h battery", "Waterproof"],
        is_mine=True,
    )
    
    competitors = [
        ProductInfo(name="Competitor A Earbuds", asin="B08COMP1", price=59.99, rating=4.1, review_count=500),
        ProductInfo(name="Competitor B Earbuds", asin="B08COMP2", price=39.99, rating=4.5, review_count=1200),
        ProductInfo(name="Competitor C Earbuds", asin="B08COMP3", price=45.99, rating=3.9, review_count=300),
    ]
    
    competitor_reviews = ReviewData(
        negative=[
            "The quality is poor, broke after 2 weeks",
            "Sound quality is bad, very cheap feeling",
            "Doesn't fit well, keeps falling out",
            "Battery life is terrible, only lasts 2 hours",
            "Charging case stopped working after a month",
            "Too expensive for this quality",
            "Bluetooth keeps disconnecting",
        ]
    )
    
    my_reviews = ReviewData(
        positive=[
            "Great sound quality, very clear!",
            "Battery lasts forever, love it",
            "Perfect fit, stays in my ears during workout",
            "Excellent value for money, recommend!",
            "Fast shipping, well packaged",
        ]
    )
    
    result = analyze(my_product, competitors, competitor_reviews, my_reviews)
    print(format_report(result, lang))


if __name__ == "__main__":
    main()
