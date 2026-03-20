#!/usr/bin/env python3
"""
Amazon Review Checker - Core Analyzer
AmazonReviewAuthenticityDetection - CoreAnalyzeEngine

Features:
- ProgressiveAnalyze ( has  many  few Data，Give conclusion)
-  many dimensionDegreeDetection (Time/Content/Rating/Account/VP)
- Friendly guidance (HintCanDeepenDirection)

Version: 1.0.0
"""

import json
import re
import math
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from datetime import datetime, timedelta
from collections import Counter
from enum import Enum
import sys


class RiskLevel(Enum):
    LOW = "low"           # 0-30
    MEDIUM = "medium"     # 31-60
    HIGH = "high"         # 61-80
    CRITICAL = "critical" # 81-100


class AnalysisLevel(Enum):
    L1_BASIC = "L1"      # onlyContent
    L2_TIMED = "L2"      # + Time
    L3_SCORED = "L3"     # + Rating
    L4_FULL = "L4"       #  all Field


# ============================================================
# Data Structures
# ============================================================

@dataclass
class Review:
    """Single itemReview"""
    content: str
    rating: Optional[int] = None          # 1-5 star
    date: Optional[str] = None            # DayPeriod
    reviewer_name: Optional[str] = None   # Reviewperson
    verified_purchase: Optional[bool] = None  # VP
    helpful_votes: Optional[int] = None   #  has Help
    reviewer_reviews_count: Optional[int] = None  # ReviewTotalReview Count
    
    @property
    def has_rating(self) -> bool:
        return self.rating is not None
    
    @property
    def has_date(self) -> bool:
        return self.date is not None
    
    @property
    def has_vp(self) -> bool:
        return self.verified_purchase is not None


@dataclass
class DimensionResult:
    """Single dimensionDegreeDetectionResult"""
    name: str
    name_zh: str
    score: float          # 0-100, exceedHighexceedSuspicious
    status: str           # ✅ ⚠️ 🔴
    detail: str
    detail_zh: str
    weight: float = 0.0


@dataclass
class SuspiciousReview:
    """SuspiciousReview"""
    content: str
    risk_score: float
    reasons: List[str]
    reasons_zh: List[str]


@dataclass
class AnalysisResult:
    """AnalyzeResult"""
    asin: str
    total_reviews: int
    analysis_level: AnalysisLevel
    authenticity_score: int       # 0-100, exceedHighexceedReal
    risk_level: RiskLevel
    dimensions: List[DimensionResult]
    suspicious_reviews: List[SuspiciousReview]
    available_fields: List[str]
    missing_fields: List[str]
    deepening_hints: List[str]
    deepening_hints_zh: List[str]
    summary: str
    summary_zh: str


# ============================================================
# DetectionAlgorithm
# ============================================================

def detect_content_similarity(reviews: List[Review]) -> DimensionResult:
    """DetectionSimilar contentDegree"""
    if len(reviews) < 2:
        return DimensionResult(
            name="Content Similarity",
            name_zh="Similar contentDegree",
            score=0,
            status="✅",
            detail="Not enough reviews to compare",
            detail_zh="Review CountInsufficient，CannotComparison",
            weight=0.20
        )
    
    # Simple similarityDegreeDetection：CheckRepeated phrases
    contents = [r.content.lower() for r in reviews]
    
    # Extract3-gram
    def get_ngrams(text, n=3):
        words = re.findall(r'\w+', text)
        return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    
    all_ngrams = []
    for content in contents:
        all_ngrams.extend(get_ngrams(content))
    
    # Statistics heavy complex
    ngram_counts = Counter(all_ngrams)
    repeated = sum(1 for count in ngram_counts.values() if count > 1)
    total = len(ngram_counts) if ngram_counts else 1
    
    similarity_ratio = repeated / total if total > 0 else 0
    score = min(100, similarity_ratio * 500)  # put big 
    
    # CheckHighDegreeSimilarReview for 
    similar_pairs = 0
    for i, c1 in enumerate(contents):
        for c2 in contents[i+1:]:
            if len(c1) > 20 and len(c2) > 20:
                # Simple Jaccard SimilarDegree
                set1, set2 = set(c1.split()), set(c2.split())
                if set1 and set2:
                    jaccard = len(set1 & set2) / len(set1 | set2)
                    if jaccard > 0.5:
                        similar_pairs += 1
    
    if similar_pairs > 0:
        score = max(score, 50 + similar_pairs * 10)
    
    score = min(100, score)
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    return DimensionResult(
        name="Content Similarity",
        name_zh="Similar contentDegree",
        score=round(score, 1),
        status=status,
        detail=f"Found {similar_pairs} similar review pairs",
        detail_zh=f"Found {similar_pairs} groupHighDegreeSimilarReview",
        weight=0.20
    )


def detect_time_clustering(reviews: List[Review]) -> Optional[DimensionResult]:
    """DetectionTimeAggregate"""
    dated_reviews = [r for r in reviews if r.has_date]
    
    if len(dated_reviews) < 5:
        return None  # DataInsufficient
    
    # ParseDayPeriod
    dates = []
    for r in dated_reviews:
        try:
            # TryMultipleFormat
            for fmt in ['%Y-%m-%d', '%B %d, %Y', '%d %B %Y', '%m/%d/%Y']:
                try:
                    dates.append(datetime.strptime(r.date, fmt))
                    break
                except:
                    continue
        except:
            pass
    
    if len(dates) < 5:
        return None
    
    dates.sort()
    
    # CalculateAdjacentReviewTimeseparate
    intervals = [(dates[i+1] - dates[i]).days for i in range(len(dates)-1)]
    
    if not intervals:
        return None
    
    # DetectionAggregate： short Time inside Large amountReview
    short_intervals = sum(1 for i in intervals if i <= 1)  # 1days inside 
    clustering_ratio = short_intervals / len(intervals)
    
    # Detection 48h Outbreak
    burst_count = 0
    window_size = 2  # 2daysWindow
    for i in range(len(dates) - 1):
        count_in_window = sum(1 for d in dates if 0 <= (d - dates[i]).days <= window_size)
        burst_count = max(burst_count, count_in_window)
    
    score = 0
    if clustering_ratio > 0.5:
        score += 40
    if clustering_ratio > 0.7:
        score += 20
    if burst_count > len(dates) * 0.3:
        score += 30
    
    score = min(100, score)
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    return DimensionResult(
        name="Time Clustering",
        name_zh="TimeAggregate",
        score=round(score, 1),
        status=status,
        detail=f"Max {burst_count} reviews in 48h window, {clustering_ratio*100:.0f}% within 1 day",
        detail_zh=f"48h inside  most  many  {burst_count} itemReview，{clustering_ratio*100:.0f}%  in 1days inside ",
        weight=0.25
    )


def detect_rating_distribution(reviews: List[Review]) -> Optional[DimensionResult]:
    """DetectionRating Distribution"""
    rated_reviews = [r for r in reviews if r.has_rating]
    
    if len(rated_reviews) < 5:
        return None
    
    ratings = [r.rating for r in rated_reviews]
    rating_counts = Counter(ratings)
    total = len(ratings)
    
    # CalculateDistribution
    five_star_ratio = rating_counts.get(5, 0) / total
    one_star_ratio = rating_counts.get(1, 0) / total
    extreme_ratio = five_star_ratio + one_star_ratio
    
    # Natural distribution usually is：5star ~50-60%, 4star ~20%, 3star ~10%, 2star ~5%, 1star ~10%
    # Abnormal case： all 5star、Polarized
    
    score = 0
    anomaly_detail = []
    
    if five_star_ratio > 0.85:
        score += 50
        anomaly_detail.append(f"{five_star_ratio*100:.0f}% 5-star (abnormal)")
    elif five_star_ratio > 0.75:
        score += 30
        anomaly_detail.append(f"{five_star_ratio*100:.0f}% 5-star (suspicious)")
    
    # Polarized
    if extreme_ratio > 0.9 and one_star_ratio > 0.1:
        score += 30
        anomaly_detail.append("Polarized distribution")
    
    # MissingMiddleRating
    mid_ratings = sum(rating_counts.get(r, 0) for r in [2, 3, 4])
    if mid_ratings / total < 0.1 and total > 10:
        score += 20
        anomaly_detail.append("Missing mid-range ratings")
    
    score = min(100, score)
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    dist_str = ", ".join([f"{r}★:{rating_counts.get(r,0)}" for r in [5,4,3,2,1]])
    
    return DimensionResult(
        name="Rating Distribution",
        name_zh="Rating Distribution",
        score=round(score, 1),
        status=status,
        detail=f"Distribution: {dist_str}. {'; '.join(anomaly_detail) if anomaly_detail else 'Normal'}",
        detail_zh=f"Distribution: {dist_str}。{'; '.join(anomaly_detail) if anomaly_detail else 'Normal'}",
        weight=0.20
    )


def detect_vp_ratio(reviews: List[Review]) -> Optional[DimensionResult]:
    """Detection Verified Purchase Ratio"""
    vp_reviews = [r for r in reviews if r.has_vp]
    
    if len(vp_reviews) < 5:
        return None
    
    vp_count = sum(1 for r in vp_reviews if r.verified_purchase)
    vp_ratio = vp_count / len(vp_reviews)
    
    # Normal VP Ratio should  should  in  60-80%
    score = 0
    if vp_ratio < 0.4:
        score = 70
    elif vp_ratio < 0.5:
        score = 50
    elif vp_ratio < 0.6:
        score = 30
    else:
        score = 10
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    return DimensionResult(
        name="Verified Purchase Ratio",
        name_zh="VPRatio",
        score=round(score, 1),
        status=status,
        detail=f"{vp_ratio*100:.0f}% verified purchase ({vp_count}/{len(vp_reviews)})",
        detail_zh=f"{vp_ratio*100:.0f}%  already VerifyPurchase ({vp_count}/{len(vp_reviews)})",
        weight=0.15
    )


def detect_review_length(reviews: List[Review]) -> DimensionResult:
    """DetectionReviewDegreeDistribution"""
    lengths = [len(r.content) for r in reviews]
    
    if not lengths:
        return DimensionResult(
            name="Review Length",
            name_zh="ReviewDegree",
            score=0,
            status="✅",
            detail="No reviews",
            detail_zh="noReview",
            weight=0.05
        )
    
    avg_length = sum(lengths) / len(lengths)
    short_count = sum(1 for l in lengths if l < 50)
    short_ratio = short_count / len(lengths)
    
    # DetectionTemplate（DegreeHighDegreeConsistent）
    if len(lengths) > 5:
        length_std = (sum((l - avg_length) ** 2 for l in lengths) / len(lengths)) ** 0.5
        cv = length_std / avg_length if avg_length > 0 else 0  # Variation coefficient
    else:
        cv = 1
    
    score = 0
    if short_ratio > 0.7:
        score += 40
    if cv < 0.3 and len(lengths) > 10:  # DegreeToo consistent
        score += 40
    
    score = min(100, score)
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    return DimensionResult(
        name="Review Length",
        name_zh="ReviewDegree",
        score=round(score, 1),
        status=status,
        detail=f"Avg length: {avg_length:.0f} chars, {short_ratio*100:.0f}% short (<50)",
        detail_zh=f"AverageDegree: {avg_length:.0f} Character, {short_ratio*100:.0f}%   short  (<50)",
        weight=0.05
    )


def detect_keywords(reviews: List[Review]) -> DimensionResult:
    """DetectionFake ordersKeywords"""
    # Common fake ordersReviewKeywords
    suspicious_keywords = [
        'received free', 'free product', 'in exchange', 'honest review',
        'discount code', 'promotional', 'gifted', 'complimentary',
        'five stars', '5 stars', 'best ever', 'amazing product',
        'highly recommend', 'must buy', 'perfect product',
        #  in text
        'Positive ReviewCashback', 'Five starPositive Review', 'Free trial', 'Gift'
    ]
    
    keyword_hits = 0
    for review in reviews:
        content_lower = review.content.lower()
        for keyword in suspicious_keywords:
            if keyword.lower() in content_lower:
                keyword_hits += 1
                break
    
    hit_ratio = keyword_hits / len(reviews) if reviews else 0
    score = min(100, hit_ratio * 200)
    
    if score < 30:
        status = "✅"
    elif score < 60:
        status = "⚠️"
    else:
        status = "🔴"
    
    return DimensionResult(
        name="Suspicious Keywords",
        name_zh="SuspiciousKeywords",
        score=round(score, 1),
        status=status,
        detail=f"{keyword_hits} reviews contain suspicious keywords",
        detail_zh=f"{keyword_hits} itemReviewPackagecontainSuspiciousKeywords",
        weight=0.05
    )


def identify_suspicious_reviews(reviews: List[Review], dimensions: List[DimensionResult]) -> List[SuspiciousReview]:
    """IdentifyHigh RiskReview"""
    suspicious = []
    
    for review in reviews:
        risk_score = 0
        reasons = []
        reasons_zh = []
        
        #  short Review
        if len(review.content) < 30:
            risk_score += 20
            reasons.append("Very short review")
            reasons_zh.append("Review  short ")
        
        # non VP
        if review.has_vp and not review.verified_purchase:
            risk_score += 25
            reasons.append("Not verified purchase")
            reasons_zh.append("nonVerifyPurchase")
        
        # ExtremeRating + TemplateContent
        if review.has_rating and review.rating == 5:
            generic_phrases = ['great', 'amazing', 'perfect', 'love it', 'best', 'excellent']
            if any(p in review.content.lower() for p in generic_phrases) and len(review.content) < 100:
                risk_score += 30
                reasons.append("Generic 5-star template")
                reasons_zh.append("Template5starPositive Review")
        
        # SuspiciousKeywords
        suspicious_keywords = ['received free', 'in exchange', 'honest review', 'discount']
        if any(k in review.content.lower() for k in suspicious_keywords):
            risk_score += 35
            reasons.append("Contains incentivized review keywords")
            reasons_zh.append("Contains incentiveReviewKeywords")
        
        if risk_score >= 40:
            suspicious.append(SuspiciousReview(
                content=review.content[:100] + "..." if len(review.content) > 100 else review.content,
                risk_score=min(100, risk_score),
                reasons=reasons,
                reasons_zh=reasons_zh
            ))
    
    #  by RiskScoreSort
    suspicious.sort(key=lambda x: x.risk_score, reverse=True)
    return suspicious[:10]  # Top 10


def determine_analysis_level(reviews: List[Review]) -> Tuple[AnalysisLevel, List[str], List[str]]:
    """ConfirmAnalyzelayerLevelAndMissing field"""
    available = ["content"]
    missing = []
    
    has_rating = any(r.has_rating for r in reviews)
    has_date = any(r.has_date for r in reviews)
    has_vp = any(r.has_vp for r in reviews)
    has_reviewer = any(r.reviewer_name for r in reviews)
    
    if has_rating:
        available.append("rating")
    else:
        missing.append("rating")
    
    if has_date:
        available.append("date")
    else:
        missing.append("date")
    
    if has_vp:
        available.append("verified_purchase")
    else:
        missing.append("verified_purchase")
    
    if has_reviewer:
        available.append("reviewer_info")
    else:
        missing.append("reviewer_info")
    
    # Determine levelLevel
    if has_rating and has_date and has_vp:
        level = AnalysisLevel.L4_FULL
    elif has_rating and has_date:
        level = AnalysisLevel.L3_SCORED
    elif has_date:
        level = AnalysisLevel.L2_TIMED
    else:
        level = AnalysisLevel.L1_BASIC
    
    return level, available, missing


def generate_deepening_hints(missing: List[str]) -> Tuple[List[str], List[str]]:
    """GenerateDeepenHint"""
    hints_en = []
    hints_zh = []
    
    hint_map = {
        "rating": (
            "Add star ratings → Unlock 'Rating Distribution Analysis'",
            "Add starLevelRating → Unlock「Rating DistributionAnalyze」"
        ),
        "date": (
            "Add review dates → Unlock 'Time Clustering Detection'",
            "SupplementReviewDayPeriod → Unlock「TimeAggregateDetection」"
        ),
        "verified_purchase": (
            "Add VP status → Unlock 'Verified Purchase Analysis'",
            "SupplementVPStatus → Unlock「PurchaseVerifyAnalyze」"
        ),
        "reviewer_info": (
            "Add reviewer info → Unlock 'Account Profile Analysis'",
            "SupplementReviewpersonInformation → Unlock「Account profileAnalyze」"
        ),
    }
    
    for field in missing:
        if field in hint_map:
            hints_en.append(hint_map[field][0])
            hints_zh.append(hint_map[field][1])
    
    return hints_en, hints_zh


def analyze_reviews(reviews: List[Review], asin: str = "UNKNOWN") -> AnalysisResult:
    """MainAnalyzeFunction"""
    if not reviews:
        return AnalysisResult(
            asin=asin,
            total_reviews=0,
            analysis_level=AnalysisLevel.L1_BASIC,
            authenticity_score=50,
            risk_level=RiskLevel.MEDIUM,
            dimensions=[],
            suspicious_reviews=[],
            available_fields=[],
            missing_fields=["content"],
            deepening_hints=["Please provide review data"],
            deepening_hints_zh=["Please provideReview Countdata"],
            summary="No reviews to analyze",
            summary_zh="noReview Countdata"
        )
    
    # ConfirmAnalyzelayerLevel
    level, available, missing = determine_analysis_level(reviews)
    hints_en, hints_zh = generate_deepening_hints(missing)
    
    # ExecuteDetection
    dimensions = []
    
    # L1: BasicDetection (AlwaysExecute)
    dimensions.append(detect_content_similarity(reviews))
    dimensions.append(detect_review_length(reviews))
    dimensions.append(detect_keywords(reviews))
    
    # L2+: TimeDetection
    time_result = detect_time_clustering(reviews)
    if time_result:
        dimensions.append(time_result)
    
    # L3+: RatingDetection
    rating_result = detect_rating_distribution(reviews)
    if rating_result:
        dimensions.append(rating_result)
    
    # L4: VPDetection
    vp_result = detect_vp_ratio(reviews)
    if vp_result:
        dimensions.append(vp_result)
    
    # CalculateComprehensiveScore (WeightedAverageSuspiciousDegree，ThenConvert toAuthenticityScore)
    total_weight = sum(d.weight for d in dimensions)
    if total_weight > 0:
        suspicion_score = sum(d.score * d.weight for d in dimensions) / total_weight
    else:
        suspicion_score = 50
    
    authenticity_score = max(0, min(100, 100 - suspicion_score))
    
    # ConfirmRiskGrade
    if authenticity_score >= 70:
        risk_level = RiskLevel.LOW
    elif authenticity_score >= 50:
        risk_level = RiskLevel.MEDIUM
    elif authenticity_score >= 30:
        risk_level = RiskLevel.HIGH
    else:
        risk_level = RiskLevel.CRITICAL
    
    # IdentifySuspiciousReview
    suspicious = identify_suspicious_reviews(reviews, dimensions)
    
    # GenerateSummary
    risk_text = {
        RiskLevel.LOW: ("Low risk - Reviews appear authentic", "Low Risk - ReviewLooks likeReal"),
        RiskLevel.MEDIUM: ("Medium risk - Some concerns detected", " in  etcRisk - FoundSomeConcern"),
        RiskLevel.HIGH: ("High risk - Multiple red flags", "High Risk -  many DangerSignal"),
        RiskLevel.CRITICAL: ("Critical risk - Likely fake reviews", "CriticalRisk - MayExistLarge amountFakeReview"),
    }
    
    summary_en = f"{risk_text[risk_level][0]}. Analyzed {len(reviews)} reviews at {level.value} level."
    summary_zh = f"{risk_text[risk_level][1]}。Analyze  {len(reviews)} itemReview，AnalyzelayerLevel {level.value}。"
    
    return AnalysisResult(
        asin=asin,
        total_reviews=len(reviews),
        analysis_level=level,
        authenticity_score=round(authenticity_score),
        risk_level=risk_level,
        dimensions=dimensions,
        suspicious_reviews=suspicious,
        available_fields=available,
        missing_fields=missing,
        deepening_hints=hints_en,
        deepening_hints_zh=hints_zh,
        summary=summary_en,
        summary_zh=summary_zh
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(result: AnalysisResult, lang: str = "en") -> str:
    """FormatReport"""
    risk_icons = {
        RiskLevel.LOW: "✅",
        RiskLevel.MEDIUM: "⚠️",
        RiskLevel.HIGH: "🔴",
        RiskLevel.CRITICAL: "💀",
    }
    
    if lang == "zh":
        lines = [
            f"📊 **ReviewAuthenticityAnalyzeReport**",
            f"",
            f"**ASIN**: {result.asin}",
            f"**Review Count**: {result.total_reviews}",
            f"**AnalyzelayerLevel**: {result.analysis_level.value}",
            f"",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"",
            f"## AuthenticityRating: {result.authenticity_score}/100 {risk_icons[result.risk_level]}",
            f"",
            f"{result.summary_zh}",
            f"",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"",
            f"## DetectiondimensionDegree",
            f"",
        ]
        
        for d in result.dimensions:
            lines.append(f"{d.status} **{d.name_zh}**: {d.score:.0f}/100")
            lines.append(f"   {d.detail_zh}")
            lines.append("")
        
        if result.suspicious_reviews:
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append("")
            lines.append(f"## High RiskReview (Top {len(result.suspicious_reviews)})")
            lines.append("")
            for i, sr in enumerate(result.suspicious_reviews[:5], 1):
                lines.append(f"**{i}. Risk {sr.risk_score:.0f}%**")
                lines.append(f'   "{sr.content}"')
                lines.append(f"   Reason: {', '.join(sr.reasons_zh)}")
                lines.append("")
        
        if result.deepening_hints_zh:
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append("")
            lines.append("🔍 **Want more accurateAnalyze？Supplement with following info:**")
            lines.append("")
            for hint in result.deepening_hints_zh:
                lines.append(f"• {hint}")
    else:
        lines = [
            f"📊 **Review Authenticity Report**",
            f"",
            f"**ASIN**: {result.asin}",
            f"**Reviews**: {result.total_reviews}",
            f"**Analysis Level**: {result.analysis_level.value}",
            f"",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"",
            f"## Authenticity Score: {result.authenticity_score}/100 {risk_icons[result.risk_level]}",
            f"",
            f"{result.summary}",
            f"",
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            f"",
            f"## Detection Dimensions",
            f"",
        ]
        
        for d in result.dimensions:
            lines.append(f"{d.status} **{d.name}**: {d.score:.0f}/100")
            lines.append(f"   {d.detail}")
            lines.append("")
        
        if result.suspicious_reviews:
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append("")
            lines.append(f"## Suspicious Reviews (Top {len(result.suspicious_reviews)})")
            lines.append("")
            for i, sr in enumerate(result.suspicious_reviews[:5], 1):
                lines.append(f"**{i}. Risk {sr.risk_score:.0f}%**")
                lines.append(f'   "{sr.content}"')
                lines.append(f"   Reasons: {', '.join(sr.reasons)}")
                lines.append("")
        
        if result.deepening_hints:
            lines.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            lines.append("")
            lines.append("🔍 **Want more accurate analysis? Add the following:**")
            lines.append("")
            for hint in result.deepening_hints:
                lines.append(f"• {hint}")
    
    return "\n".join(lines)


# ============================================================
# Parse
# ============================================================

def parse_simple_reviews(text: str) -> List[Review]:
    """ParseSimpleTextFormatReview"""
    reviews = []
    
    # TrySplit by paragraph
    paragraphs = re.split(r'\n\n+', text.strip())
    
    for para in paragraphs:
        para = para.strip()
        if len(para) > 10:
            review = Review(content=para)
            
            # TryExtract starLevel
            star_match = re.search(r'(\d)\s*(?:star|★|⭐)', para, re.I)
            if star_match:
                review.rating = int(star_match.group(1))
            
            # TryExtractDayPeriod
            date_match = re.search(r'(\d{4}-\d{2}-\d{2}|\w+\s+\d{1,2},?\s+\d{4})', para)
            if date_match:
                review.date = date_match.group(1)
            
            # TryExtract VP
            if 'verified purchase' in para.lower() or 'VP' in para:
                review.verified_purchase = True
            elif 'not verified' in para.lower():
                review.verified_purchase = False
            
            reviews.append(review)
    
    return reviews


# ============================================================
# CLI Entry Point
# ============================================================

def main():
    """CLI Entry Point"""
    # TestData
    test_reviews = [
        Review(content="Great product! Works perfectly. Highly recommend to everyone.", rating=5, verified_purchase=True, date="2024-01-15"),
        Review(content="Amazing! Best purchase ever. Love it!", rating=5, verified_purchase=False, date="2024-01-15"),
        Review(content="Great product! Works perfectly. Must buy!", rating=5, verified_purchase=False, date="2024-01-16"),
        Review(content="Received free product in exchange for honest review. It's good.", rating=5, verified_purchase=False, date="2024-01-16"),
        Review(content="Excellent quality, fast shipping. Very satisfied with purchase.", rating=5, verified_purchase=True, date="2024-01-20"),
        Review(content="Not as described. Cheap quality.", rating=1, verified_purchase=True, date="2024-02-01"),
        Review(content="Perfect!", rating=5, verified_purchase=False, date="2024-01-16"),
        Review(content="Good value for money. Does what it says.", rating=4, verified_purchase=True, date="2024-02-15"),
        Review(content="Five stars! Amazing product!", rating=5, verified_purchase=False, date="2024-01-17"),
        Review(content="Decent product for the price.", rating=3, verified_purchase=True, date="2024-03-01"),
    ]
    
    # If command lineInput
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--demo":
            pass  # UseTestData
        elif arg.startswith('['):
            # JSON group
            try:
                data = json.loads(arg)
                test_reviews = [Review(**r) for r in data]
            except:
                pass
        else:
            # pureText
            test_reviews = parse_simple_reviews(arg)
    
    result = analyze_reviews(test_reviews, asin="B08XXXXX")
    
    # Default ChineseOutput
    lang = "zh" if "--zh" in sys.argv else "en"
    print(format_report(result, lang))


if __name__ == "__main__":
    main()
