#!/usr/bin/env python3
"""
Brand Protection Detector - Core Engine
Brand ProtectionDetector - Core Engine

Features:
- Hijacker Detection (Hijacker Detection)
- PriceAbnormalMonitoring (Price Alert)
- CounterfeitIdentify (Counterfeit Detection)
- ImageStolenDetection (Image Theft)
- RiskEvaluate (Risk Assessment)
- Rights protectionRecommendation (Action Recommendations)

Version: 1.0.0
"""

import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum
from datetime import datetime
import sys
import re


class RiskLevel(Enum):
    """RiskGrade"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ViolationType(Enum):
    """InfringementCategoryType"""
    HIJACKER = "hijacker"           # Hijacking
    COUNTERFEIT = "counterfeit"     # Counterfeit
    PRICE_VIOLATION = "price"       # PriceViolation
    IMAGE_THEFT = "image_theft"     # ImageStolen
    TRADEMARK = "trademark"         # TrademarkInfringement
    LISTING_ABUSE = "listing_abuse" # Listing Abuse


# ============================================================
# Data Structures
# ============================================================

@dataclass
class BrandInfo:
    """BrandInformation"""
    brand_name: str
    trademark_number: Optional[str] = None
    brand_registry: bool = False
    authorized_sellers: List[str] = field(default_factory=list)
    protected_asins: List[str] = field(default_factory=list)
    min_price: Optional[float] = None  # MAP  most  low price
    logo_url: Optional[str] = None


@dataclass
class SellerInfo:
    """SellerInformation"""
    seller_id: str
    seller_name: str
    price: float
    is_fba: bool = False
    rating: Optional[float] = None
    review_count: Optional[int] = None
    is_authorized: bool = False
    storefront_url: Optional[str] = None


@dataclass
class ListingInfo:
    """Listing Information"""
    asin: str
    title: str
    brand_in_title: bool = False
    price: float = 0.0
    image_urls: List[str] = field(default_factory=list)
    seller_count: int = 1
    sellers: List[SellerInfo] = field(default_factory=list)
    buy_box_seller: Optional[str] = None
    category: Optional[str] = None


@dataclass
class Violation:
    """InfringementRecord"""
    violation_type: ViolationType
    risk_level: RiskLevel
    seller: Optional[SellerInfo] = None
    listing: Optional[ListingInfo] = None
    evidence: List[str] = field(default_factory=list)
    description: str = ""
    description_zh: str = ""
    recommended_action: str = ""
    recommended_action_zh: str = ""


@dataclass
class DetectionResult:
    """DetectionResult"""
    brand: BrandInfo
    scan_time: str
    total_asins_scanned: int
    violations: List[Violation]
    risk_score: int  # 0-100
    risk_level: RiskLevel
    summary: str
    summary_zh: str
    action_plan: List[Dict[str, str]]


# ============================================================
# DetectionLogic
# ============================================================

def detect_hijackers(brand: BrandInfo, listing: ListingInfo) -> List[Violation]:
    """DetectionHijacking"""
    violations = []
    
    for seller in listing.sellers:
        # skip AuthorizedSeller
        if seller.seller_id in brand.authorized_sellers:
            continue
        if seller.is_authorized:
            continue
        
        # FoundnotAuthorizedSeller
        risk = RiskLevel.HIGH if listing.buy_box_seller == seller.seller_id else RiskLevel.MEDIUM
        
        violations.append(Violation(
            violation_type=ViolationType.HIJACKER,
            risk_level=risk,
            seller=seller,
            listing=listing,
            evidence=[
                f"Unauthorized seller on ASIN: {listing.asin}",
                f"Seller: {seller.seller_name} ({seller.seller_id})",
                f"Price: ${seller.price}",
            ],
            description=f"Unauthorized seller '{seller.seller_name}' found on your listing",
            description_zh=f"FoundnotAuthorizedSeller '{seller.seller_name}'  in you Listing  above Sale",
            recommended_action="File Brand Registry complaint or send cease & desist",
            recommended_action_zh="Pass Brand Registry Complaint or cease and desist letter",
        ))
    
    return violations


def detect_price_violations(brand: BrandInfo, listing: ListingInfo) -> List[Violation]:
    """DetectionPriceViolation"""
    violations = []
    
    if brand.min_price is None:
        return violations
    
    for seller in listing.sellers:
        if seller.price < brand.min_price:
            discount = (brand.min_price - seller.price) / brand.min_price * 100
            
            risk = RiskLevel.CRITICAL if discount > 30 else RiskLevel.HIGH if discount > 15 else RiskLevel.MEDIUM
            
            violations.append(Violation(
                violation_type=ViolationType.PRICE_VIOLATION,
                risk_level=risk,
                seller=seller,
                listing=listing,
                evidence=[
                    f"Price ${seller.price} below MAP ${brand.min_price}",
                    f"Discount: {discount:.1f}% below minimum",
                ],
                description=f"Seller '{seller.seller_name}' selling {discount:.1f}% below MAP",
                description_zh=f"Seller '{seller.seller_name}' Selling Price low  at  MAP {discount:.1f}%",
                recommended_action="Send MAP violation notice, consider distribution review",
                recommended_action_zh="Send MAP Violation notice，ConsiderReviewDistributionChannel",
            ))
    
    return violations


def detect_counterfeit_signals(listing: ListingInfo, reviews: List[Dict] = None) -> List[Violation]:
    """DetectionCounterfeit Signals"""
    violations = []
    
    # SuspiciousKeywords
    counterfeit_keywords = [
        "fake", "counterfeit", "not genuine", "knockoff", "replica",
        "poor quality", "not authentic", "cheap copy", "different from picture",
        "Counterfeit", "fake", "Imitation", "Knockoff", "Poor quality", "AndImageDifferent",
    ]
    
    if reviews:
        suspicious_reviews = []
        for review in reviews:
            content = review.get("content", "").lower()
            for keyword in counterfeit_keywords:
                if keyword.lower() in content:
                    suspicious_reviews.append(review)
                    break
        
        if len(suspicious_reviews) >= 3:
            violations.append(Violation(
                violation_type=ViolationType.COUNTERFEIT,
                risk_level=RiskLevel.CRITICAL,
                listing=listing,
                evidence=[
                    f"Found {len(suspicious_reviews)} reviews mentioning counterfeit/fake",
                    "Sample keywords: " + ", ".join(counterfeit_keywords[:5]),
                ],
                description=f"Multiple reviews indicate potential counterfeit products",
                description_zh=f" many itemReviewmention and Counterfeit/Imitation，ExistCounterfeitRisk",
                recommended_action="Initiate Test Buy to collect physical evidence",
                recommended_action_zh="Proceed Test Buy Test purchase to collect physical evidence",
            ))
    
    return violations


def detect_trademark_abuse(brand: BrandInfo, listing: ListingInfo) -> List[Violation]:
    """DetectionTrademarkAbuse"""
    violations = []
    
    # CheckWhether title abuses brand name
    title_lower = listing.title.lower()
    brand_lower = brand.brand_name.lower()
    
    # SuspiciousMode：Brandname + "compatible", "for", "replacement"
    abuse_patterns = [
        f"for {brand_lower}",
        f"compatible with {brand_lower}",
        f"{brand_lower} compatible",
        f"fits {brand_lower}",
        f"replacement for {brand_lower}",
    ]
    
    for pattern in abuse_patterns:
        if pattern in title_lower:
            violations.append(Violation(
                violation_type=ViolationType.TRADEMARK,
                risk_level=RiskLevel.MEDIUM,
                listing=listing,
                evidence=[
                    f"Title contains: '{pattern}'",
                    f"Full title: {listing.title}",
                ],
                description=f"Potential trademark abuse in listing title",
                description_zh=f"Listing Title may contain trademark abuse",
                recommended_action="File trademark complaint if unauthorized use",
                recommended_action_zh=" such as notAuthorizedUse，SubmitTrademarkInfringementComplaint",
            ))
            break
    
    return violations


def calculate_risk_score(violations: List[Violation]) -> tuple:
    """CalculateRiskRating"""
    if not violations:
        return 0, RiskLevel.LOW
    
    # Weight
    weights = {
        RiskLevel.LOW: 5,
        RiskLevel.MEDIUM: 15,
        RiskLevel.HIGH: 30,
        RiskLevel.CRITICAL: 50,
    }
    
    total_score = sum(weights[v.risk_level] for v in violations)
    score = min(100, total_score)
    
    if score >= 70:
        level = RiskLevel.CRITICAL
    elif score >= 40:
        level = RiskLevel.HIGH
    elif score >= 20:
        level = RiskLevel.MEDIUM
    else:
        level = RiskLevel.LOW
    
    return score, level


def generate_action_plan(violations: List[Violation], brand: BrandInfo) -> List[Dict[str, str]]:
    """GenerateRights action plan"""
    actions = []
    
    #  by CategoryTypeGroup
    hijackers = [v for v in violations if v.violation_type == ViolationType.HIJACKER]
    counterfeits = [v for v in violations if v.violation_type == ViolationType.COUNTERFEIT]
    price_violations = [v for v in violations if v.violation_type == ViolationType.PRICE_VIOLATION]
    
    # HijackingProcess
    if hijackers:
        if brand.brand_registry:
            actions.append({
                "priority": "1",
                "action": "Report via Brand Registry",
                "action_zh": "Pass Brand Registry Complaint",
                "detail": f"Report {len(hijackers)} unauthorized seller(s) via Amazon Brand Registry portal",
                "detail_zh": f"Pass Amazon Brand Registry PortalComplaint {len(hijackers)} notAuthorizedSeller",
                "timeline": "24-48 hours",
            })
        else:
            actions.append({
                "priority": "1",
                "action": "Send Cease & Desist",
                "action_zh": "SendStopInfringementLetter",
                "detail": "Contact sellers directly with legal notice",
                "detail_zh": "Direct contactSellerSend legal letter",
                "timeline": "3-5 business days",
            })
    
    # CounterfeitProcess
    if counterfeits:
        actions.append({
            "priority": "1",
            "action": "Initiate Test Buy",
            "action_zh": "Proceed Test Buy",
            "detail": "Purchase product from suspected seller to collect physical evidence",
            "detail_zh": " from SuspiciousSeller at PurchaseProductCollectPhysicalEvidence",
            "timeline": "7-14 days",
        })
        actions.append({
            "priority": "2",
            "action": "File Counterfeit Report",
            "action_zh": "SubmitCounterfeitComplaint",
            "detail": "Submit counterfeit complaint with evidence to Amazon",
            "detail_zh": " to  Amazon Submit counterfeit complaint and evidence",
            "timeline": "After test buy",
        })
    
    # PriceViolationProcess
    if price_violations:
        actions.append({
            "priority": "2",
            "action": "Send MAP Violation Notice",
            "action_zh": "Send MAP Violation notice",
            "detail": f"Notify {len(price_violations)} seller(s) of MAP policy violation",
            "detail_zh": f"Notification {len(price_violations)} Seller MAP Policy violation",
            "timeline": "48-72 hours",
        })
    
    # GeneralRecommendation
    if not brand.brand_registry and violations:
        actions.append({
            "priority": "3",
            "action": "Enroll in Brand Registry",
            "action_zh": "Register Brand Registry",
            "detail": "Get enhanced brand protection tools from Amazon",
            "detail_zh": "Get Amazon EnhanceBrand ProtectionTool",
            "timeline": "2-4 weeks (requires trademark)",
        })
    
    return actions


# ============================================================
# MainDetectionFunction
# ============================================================

def detect(
    brand: BrandInfo,
    listings: List[ListingInfo],
    reviews: Dict[str, List[Dict]] = None
) -> DetectionResult:
    """MainDetectionFunction"""
    
    all_violations = []
    
    for listing in listings:
        # Hijacker Detection
        all_violations.extend(detect_hijackers(brand, listing))
        
        # PriceViolationDetection
        all_violations.extend(detect_price_violations(brand, listing))
        
        # TrademarkAbuseDetection
        all_violations.extend(detect_trademark_abuse(brand, listing))
        
        # Counterfeit SignalsDetection
        if reviews and listing.asin in reviews:
            all_violations.extend(detect_counterfeit_signals(listing, reviews[listing.asin]))
    
    # CalculateRiskRating
    risk_score, risk_level = calculate_risk_score(all_violations)
    
    # GenerateAction Plan
    action_plan = generate_action_plan(all_violations, brand)
    
    # GenerateSummary
    hijacker_count = len([v for v in all_violations if v.violation_type == ViolationType.HIJACKER])
    counterfeit_count = len([v for v in all_violations if v.violation_type == ViolationType.COUNTERFEIT])
    
    if risk_level == RiskLevel.CRITICAL:
        status = "🚨 CRITICAL"
        status_zh = "🚨 CriticalRisk"
    elif risk_level == RiskLevel.HIGH:
        status = "🔴 HIGH RISK"
        status_zh = "🔴 High Risk"
    elif risk_level == RiskLevel.MEDIUM:
        status = "⚠️ MEDIUM RISK"
        status_zh = "⚠️  in  etcRisk"
    else:
        status = "✅ LOW RISK"
        status_zh = "✅ Low Risk"
    
    summary = f"{status} | {len(all_violations)} violation(s) found | {hijacker_count} hijacker(s), {counterfeit_count} counterfeit signal(s)"
    summary_zh = f"{status_zh} | Found {len(all_violations)} Infringement | {hijacker_count} Hijacking, {counterfeit_count} Counterfeit Signals"
    
    return DetectionResult(
        brand=brand,
        scan_time=datetime.now().isoformat(),
        total_asins_scanned=len(listings),
        violations=all_violations,
        risk_score=risk_score,
        risk_level=risk_level,
        summary=summary,
        summary_zh=summary_zh,
        action_plan=action_plan,
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(result: DetectionResult, lang: str = "en") -> str:
    """FormatReport"""
    b = result.brand
    
    if lang == "zh":
        lines = [
            "🛡️ **Brand ProtectionDetectionReport**",
            "",
            f"**Brand**: {b.brand_name}",
            f"**Brand Registry**: {'✅  already Register' if b.brand_registry else '❌ notRegister'}",
            f"**ScanTime**: {result.scan_time[:19]}",
            f"**Scan ASIN **: {result.total_asins_scanned}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## 🎯 RiskRating: {result.risk_score}/100",
            "",
            result.summary_zh,
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## ⚠️ InfringementDetails",
            "",
        ]
        
        if not result.violations:
            lines.append("✅ No infringement found")
        else:
            for i, v in enumerate(result.violations[:10], 1):
                risk_icon = {"critical": "🚨", "high": "🔴", "medium": "⚠️", "low": "✅"}[v.risk_level.value]
                lines.append(f"**{i}. [{v.violation_type.value.upper()}] {risk_icon}**")
                lines.append(f"   {v.description_zh}")
                if v.seller:
                    lines.append(f"   Seller: {v.seller.seller_name} | Price: ${v.seller.price}")
                lines.append(f"   Recommendation: {v.recommended_action_zh}")
                lines.append("")
        
        if result.action_plan:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 📋 Rights action plan",
                "",
            ])
            for action in result.action_plan:
                lines.append(f"**[P{action['priority']}] {action['action_zh']}**")
                lines.append(f"   {action['detail_zh']}")
                lines.append(f"   ExpectedTime: {action['timeline']}")
                lines.append("")
    else:
        lines = [
            "🛡️ **Brand Protection Detection Report**",
            "",
            f"**Brand**: {b.brand_name}",
            f"**Brand Registry**: {'✅ Enrolled' if b.brand_registry else '❌ Not Enrolled'}",
            f"**Scan Time**: {result.scan_time[:19]}",
            f"**ASINs Scanned**: {result.total_asins_scanned}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## 🎯 Risk Score: {result.risk_score}/100",
            "",
            result.summary,
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## ⚠️ Violations Found",
            "",
        ]
        
        if not result.violations:
            lines.append("✅ No violations detected")
        else:
            for i, v in enumerate(result.violations[:10], 1):
                risk_icon = {"critical": "🚨", "high": "🔴", "medium": "⚠️", "low": "✅"}[v.risk_level.value]
                lines.append(f"**{i}. [{v.violation_type.value.upper()}] {risk_icon}**")
                lines.append(f"   {v.description}")
                if v.seller:
                    lines.append(f"   Seller: {v.seller.seller_name} | Price: ${v.seller.price}")
                lines.append(f"   Action: {v.recommended_action}")
                lines.append("")
        
        if result.action_plan:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 📋 Action Plan",
                "",
            ])
            for action in result.action_plan:
                lines.append(f"**[P{action['priority']}] {action['action']}**")
                lines.append(f"   {action['detail']}")
                lines.append(f"   Timeline: {action['timeline']}")
                lines.append("")
    
    return "\n".join(lines)


# ============================================================
# DemoData
# ============================================================

def get_demo_data():
    """GetDemoData"""
    brand = BrandInfo(
        brand_name="TechGadget",
        trademark_number="US12345678",
        brand_registry=True,
        authorized_sellers=["A1B2C3D4E5F6G7"],
        protected_asins=["B08XXXXXX1", "B08XXXXXX2"],
        min_price=29.99,
    )
    
    listings = [
        ListingInfo(
            asin="B08XXXXXX1",
            title="TechGadget Premium Wireless Charger",
            brand_in_title=True,
            price=29.99,
            seller_count=3,
            buy_box_seller="A1B2C3D4E5F6G7",
            sellers=[
                SellerInfo(
                    seller_id="A1B2C3D4E5F6G7",
                    seller_name="TechGadget Official",
                    price=29.99,
                    is_fba=True,
                    rating=4.8,
                    is_authorized=True,
                ),
                SellerInfo(
                    seller_id="X9Y8Z7W6V5U4T3",
                    seller_name="CheapDeals123",
                    price=18.99,
                    is_fba=False,
                    rating=3.2,
                    is_authorized=False,
                ),
                SellerInfo(
                    seller_id="M1N2O3P4Q5R6S7",
                    seller_name="BestPriceStore",
                    price=24.99,
                    is_fba=True,
                    rating=4.1,
                    is_authorized=False,
                ),
            ],
        ),
        ListingInfo(
            asin="B09YYYYYY1",
            title="Compatible with TechGadget Wireless Charger Case",
            brand_in_title=True,
            price=9.99,
            seller_count=1,
            sellers=[
                SellerInfo(
                    seller_id="K1L2M3N4O5P6Q7",
                    seller_name="AccessoryWorld",
                    price=9.99,
                    is_fba=True,
                    rating=4.0,
                    is_authorized=False,
                ),
            ],
        ),
    ]
    
    reviews = {
        "B08XXXXXX1": [
            {"content": "Great product, works perfectly!", "rating": 5},
            {"content": "Received a fake product, not genuine TechGadget", "rating": 1},
            {"content": "This is counterfeit, poor quality", "rating": 1},
            {"content": "Not authentic, different from picture", "rating": 2},
            {"content": "Amazing charger, fast shipping", "rating": 5},
        ],
    }
    
    return brand, listings, reviews


# ============================================================
# CLI
# ============================================================

def main():
    lang = "zh" if "--zh" in sys.argv else "en"
    
    # DemoMode
    brand, listings, reviews = get_demo_data()
    
    # ExecuteDetection
    result = detect(brand, listings, reviews)
    
    # OutputReport
    print(format_report(result, lang))


if __name__ == "__main__":
    main()
