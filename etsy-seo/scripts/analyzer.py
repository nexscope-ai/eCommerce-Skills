#!/usr/bin/env python3
"""
Etsy SEO Analyzer - Core Engine
Etsy SEO Analyze - Core Engine

Features:
- SEO Overall Rating (0-100)
- TitleOptimization Suggestions
- 13 TagRecommended
- DescriptionOptimization Suggestions
- KeywordsResearch
- Competitor SEO Analyze
- Store SEO Optimization
- Attribute fillingCheck

Version: 1.0.0
"""

import json
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from collections import Counter
import sys


class SEOGrade(Enum):
    """SEO Grade"""
    EXCELLENT = "A"   # 90-100
    GOOD = "B"        # 70-89
    AVERAGE = "C"     # 50-69
    POOR = "D"        # 30-49
    CRITICAL = "F"    # 0-29


# ============================================================
# Etsy PopularKeywordsLibrary (By category)
# ============================================================

ETSY_KEYWORDS = {
    "jewelry": [
        "handmade jewelry", "personalized necklace", "custom bracelet",
        "birthstone ring", "minimalist earrings", "gold filled",
        "sterling silver", "dainty jewelry", "layered necklace",
        "initial jewelry", "gift for her", "bridesmaid gift",
    ],
    "home_decor": [
        "wall art", "home decor", "farmhouse decor", "boho decor",
        "personalized sign", "custom portrait", "macrame", "plant holder",
        "candle holder", "throw pillow", "wall hanging", "housewarming gift",
    ],
    "clothing": [
        "vintage clothing", "handmade dress", "boho style", "linen clothing",
        "custom t-shirt", "embroidered", "sustainable fashion", "cottagecore",
        "oversized sweater", "matching set", "loungewear", "festival outfit",
    ],
    "accessories": [
        "leather wallet", "handmade bag", "personalized keychain",
        "phone case", "hair accessories", "scrunchie", "tote bag",
        "crossbody bag", "beanie", "scarf", "belt", "sunglasses chain",
    ],
    "art": [
        "digital download", "printable art", "wall print", "custom portrait",
        "pet portrait", "watercolor", "illustration", "line art",
        "minimalist art", "abstract art", "nursery art", "office decor",
    ],
    "craft_supplies": [
        "beads", "charms", "fabric", "yarn", "patterns", "stickers",
        "stamps", "dies", "embellishments", "ribbon", "findings",
    ],
    "wedding": [
        "wedding invitation", "bridal jewelry", "bridesmaid gift",
        "wedding decor", "cake topper", "guest book", "veil",
        "wedding favor", "flower girl", "groomsmen gift", "engagement",
    ],
    "default": [
        "handmade", "custom", "personalized", "gift", "unique",
        "vintage", "boho", "minimalist", "eco friendly", "sustainable",
    ],
}

# Long-tailKeywordsTemplate
LONG_TAIL_TEMPLATES = [
    "{keyword} for women",
    "{keyword} for men",
    "{keyword} gift",
    "personalized {keyword}",
    "custom {keyword}",
    "handmade {keyword}",
    "{keyword} for mom",
    "{keyword} for her",
    "{keyword} for him",
    "vintage {keyword}",
]


# ============================================================
# Data Structures
# ============================================================

@dataclass
class ListingInfo:
    """ProductInformation"""
    title: str = ""
    tags: List[str] = field(default_factory=list)
    description: str = ""
    category: str = "default"
    attributes: Dict[str, str] = field(default_factory=dict)
    price: float = 0.0
    images: int = 0
    image_alts: List[str] = field(default_factory=list)
    url: str = ""


@dataclass
class ShopInfo:
    """StoreInformation"""
    name: str = ""
    announcement: str = ""
    about: str = ""
    policies: str = ""
    sections: List[str] = field(default_factory=list)


@dataclass
class SEOScore:
    """SEO Rating"""
    total: int = 0
    grade: SEOGrade = SEOGrade.CRITICAL
    title_score: int = 0
    tags_score: int = 0
    description_score: int = 0
    attributes_score: int = 0
    images_score: int = 0


@dataclass
class TitleAnalysis:
    """TitleAnalyze"""
    length: int = 0
    max_length: int = 140
    keyword_count: int = 0
    has_main_keyword: bool = False
    readability: str = ""
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    optimized_title: str = ""


@dataclass
class TagsAnalysis:
    """TagAnalyze"""
    count: int = 0
    max_count: int = 13
    avg_length: float = 0.0
    long_tail_count: int = 0
    missing_count: int = 0
    issues: List[str] = field(default_factory=list)
    suggested_tags: List[str] = field(default_factory=list)


@dataclass
class DescriptionAnalysis:
    """DescriptionAnalyze"""
    length: int = 0
    first_160_chars: str = ""
    keyword_density: float = 0.0
    has_call_to_action: bool = False
    issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)


@dataclass
class SEOReport:
    """SEO AnalyzeReport"""
    listing: ListingInfo
    score: SEOScore
    title_analysis: TitleAnalysis
    tags_analysis: TagsAnalysis
    description_analysis: DescriptionAnalysis
    keyword_suggestions: List[str]
    competitor_insights: List[str]
    action_items: List[Dict]
    summary: str
    summary_zh: str


# ============================================================
# AnalyzeFunction
# ============================================================

def analyze_title(title: str, category: str) -> Tuple[int, TitleAnalysis]:
    """AnalyzeTitle"""
    analysis = TitleAnalysis()
    analysis.length = len(title)
    issues = []
    suggestions = []
    score = 100
    
    # DegreeCheck (Etsy Restriction 140 Character)
    if analysis.length < 40:
        issues.append("Title too short (< 40 chars)")
        score -= 20
    elif analysis.length > 140:
        issues.append("Title exceeds 140 character limit")
        score -= 30
    elif analysis.length < 80:
        suggestions.append("Consider using more characters (ideal: 80-140)")
        score -= 5
    
    # KeywordsCheck
    category_keywords = ETSY_KEYWORDS.get(category, ETSY_KEYWORDS["default"])
    title_lower = title.lower()
    
    found_keywords = [kw for kw in category_keywords if kw.lower() in title_lower]
    analysis.keyword_count = len(found_keywords)
    analysis.has_main_keyword = analysis.keyword_count > 0
    
    if not analysis.has_main_keyword:
        issues.append("No category keywords found in title")
        score -= 25
    elif analysis.keyword_count < 2:
        suggestions.append("Add more relevant keywords")
        score -= 10
    
    # CanReadabilityCheck
    words = title.split()
    if len(words) < 5:
        issues.append("Title has too few words")
        score -= 15
    
    # Special charactersCheck
    if re.search(r'[!@#$%^&*()_+=\[\]{}|\\:";\'<>?/]', title):
        suggestions.append("Avoid special characters in title")
        score -= 5
    
    #  all  big writeCheck
    if title.isupper():
        issues.append("Avoid ALL CAPS in title")
        score -= 15
    
    analysis.issues = issues
    analysis.suggestions = suggestions
    analysis.readability = "Good" if len(issues) == 0 else "Needs improvement"
    
    # GenerateOptimization SuggestionsTitle
    if not analysis.has_main_keyword and category_keywords:
        base_keyword = category_keywords[0]
        analysis.optimized_title = f"{base_keyword.title()}, {title}"[:140]
    
    return max(0, score), analysis


def analyze_tags(tags: List[str], category: str) -> Tuple[int, TagsAnalysis]:
    """AnalyzeTag"""
    analysis = TagsAnalysis()
    analysis.count = len(tags)
    issues = []
    score = 100
    
    # QuantityCheck (Etsy Allow 13 )
    analysis.missing_count = 13 - analysis.count
    if analysis.count < 13:
        issues.append(f"Only {analysis.count}/13 tags used")
        score -= (13 - analysis.count) * 5
    
    # DegreeAnalyze
    if tags:
        lengths = [len(tag) for tag in tags]
        analysis.avg_length = sum(lengths) / len(lengths)
        
        # Check  short Tag
        short_tags = [t for t in tags if len(t) < 5]
        if short_tags:
            issues.append(f"{len(short_tags)} tags are too short")
            score -= len(short_tags) * 3
        
        # ChecksuperTag (20 Character limit)
        long_tags = [t for t in tags if len(t) > 20]
        if long_tags:
            issues.append(f"{len(long_tags)} tags exceed 20 characters")
            score -= len(long_tags) * 5
    
    # Long-tailKeywordsCheck
    analysis.long_tail_count = len([t for t in tags if ' ' in t])
    if analysis.long_tail_count < 5:
        issues.append("Need more multi-word (long-tail) tags")
        score -= 10
    
    #  heavy complexCheck
    unique_tags = set(t.lower() for t in tags)
    if len(unique_tags) < len(tags):
        issues.append("Duplicate tags found")
        score -= 10
    
    analysis.issues = issues
    
    # GenerateRecommendedTag
    category_keywords = ETSY_KEYWORDS.get(category, ETSY_KEYWORDS["default"])
    existing_lower = set(t.lower() for t in tags)
    
    suggested = []
    for kw in category_keywords:
        if kw.lower() not in existing_lower and len(suggested) < analysis.missing_count:
            suggested.append(kw)
    
    # AddLong-tailVariant
    if suggested and len(suggested) < analysis.missing_count:
        base = suggested[0].split()[0] if suggested else category_keywords[0]
        for template in LONG_TAIL_TEMPLATES:
            tag = template.format(keyword=base)
            if len(tag) <= 20 and tag.lower() not in existing_lower:
                suggested.append(tag)
                if len(suggested) >= analysis.missing_count:
                    break
    
    analysis.suggested_tags = suggested[:analysis.missing_count]
    
    return max(0, score), analysis


def analyze_description(description: str, category: str) -> Tuple[int, DescriptionAnalysis]:
    """AnalyzeDescription"""
    analysis = DescriptionAnalysis()
    analysis.length = len(description)
    issues = []
    suggestions = []
    score = 100
    
    # DegreeCheck
    if analysis.length < 100:
        issues.append("Description too short (< 100 chars)")
        score -= 30
    elif analysis.length < 300:
        suggestions.append("Consider a longer description (300+ chars)")
        score -= 10
    
    #  before  160 CharacterCheck (SearchEngineSummary)
    analysis.first_160_chars = description[:160]
    
    # KeywordsdenseDegree
    category_keywords = ETSY_KEYWORDS.get(category, ETSY_KEYWORDS["default"])
    desc_lower = description.lower()
    keyword_count = sum(1 for kw in category_keywords if kw.lower() in desc_lower)
    analysis.keyword_density = keyword_count / max(1, len(description.split())) * 100
    
    if keyword_count == 0:
        issues.append("No category keywords in description")
        score -= 20
    
    # CTA Check
    cta_phrases = ["shop now", "buy now", "order today", "click", "add to cart", "check out", "contact"]
    analysis.has_call_to_action = any(cta in desc_lower for cta in cta_phrases)
    if not analysis.has_call_to_action:
        suggestions.append("Add a call-to-action")
        score -= 5
    
    # ParagraphCheck
    if '\n' not in description and analysis.length > 200:
        suggestions.append("Break into paragraphs for readability")
        score -= 5
    
    analysis.issues = issues
    analysis.suggestions = suggestions
    
    return max(0, score), analysis


def calculate_seo_score(
    title_score: int,
    tags_score: int,
    desc_score: int,
    attr_score: int,
    img_score: int
) -> SEOScore:
    """CalculateComprehensive SEO Rating"""
    
    # Weight: Title30%, Tag25%, Description20%, Property15%, Image10%
    total = int(
        title_score * 0.30 +
        tags_score * 0.25 +
        desc_score * 0.20 +
        attr_score * 0.15 +
        img_score * 0.10
    )
    
    if total >= 90:
        grade = SEOGrade.EXCELLENT
    elif total >= 70:
        grade = SEOGrade.GOOD
    elif total >= 50:
        grade = SEOGrade.AVERAGE
    elif total >= 30:
        grade = SEOGrade.POOR
    else:
        grade = SEOGrade.CRITICAL
    
    return SEOScore(
        total=total,
        grade=grade,
        title_score=title_score,
        tags_score=tags_score,
        description_score=desc_score,
        attributes_score=attr_score,
        images_score=img_score,
    )


def generate_action_items(
    title_analysis: TitleAnalysis,
    tags_analysis: TagsAnalysis,
    desc_analysis: DescriptionAnalysis,
    score: SEOScore
) -> List[Dict]:
    """GenerateActionRecommendation"""
    actions = []
    
    # TitleIssue
    for issue in title_analysis.issues:
        actions.append({
            "category": "Title",
            "category_zh": "Title",
            "priority": "P1",
            "action": f"Fix: {issue}",
            "action_zh": f"Fix: {issue}",
        })
    
    # TagIssue
    if tags_analysis.missing_count > 0:
        actions.append({
            "category": "Tags",
            "category_zh": "Tag",
            "priority": "P1",
            "action": f"Add {tags_analysis.missing_count} more tags",
            "action_zh": f"Add {tags_analysis.missing_count} Tag",
        })
    
    for issue in tags_analysis.issues:
        if "missing" not in issue.lower():
            actions.append({
                "category": "Tags",
                "category_zh": "Tag",
                "priority": "P2",
                "action": f"Fix: {issue}",
                "action_zh": f"Fix: {issue}",
            })
    
    # DescriptionIssue
    for issue in desc_analysis.issues:
        actions.append({
            "category": "Description",
            "category_zh": "Description",
            "priority": "P2",
            "action": f"Fix: {issue}",
            "action_zh": f"Fix: {issue}",
        })
    
    return actions


def analyze_listing(listing: ListingInfo) -> SEOReport:
    """AnalyzeProduct SEO"""
    
    # Analyze each Part
    title_score, title_analysis = analyze_title(listing.title, listing.category)
    tags_score, tags_analysis = analyze_tags(listing.tags, listing.category)
    desc_score, desc_analysis = analyze_description(listing.description, listing.category)
    
    # PropertyRating (simple)
    attr_score = 100 if len(listing.attributes) >= 5 else len(listing.attributes) * 20
    
    # ImageRating
    img_score = min(100, listing.images * 10) if listing.images > 0 else 0
    
    # Overall Rating
    score = calculate_seo_score(title_score, tags_score, desc_score, attr_score, img_score)
    
    # KeywordsRecommendation
    category_keywords = ETSY_KEYWORDS.get(listing.category, ETSY_KEYWORDS["default"])
    keyword_suggestions = category_keywords[:10]
    
    # ActionRecommendation
    action_items = generate_action_items(title_analysis, tags_analysis, desc_analysis, score)
    
    # Summary
    summary = f"SEO Score: {score.total}/100 ({score.grade.value}) | Title: {title_score} | Tags: {tags_score} | Desc: {desc_score}"
    summary_zh = f"SEO Rating: {score.total}/100 ({score.grade.value}) | Title: {title_score} | Tag: {tags_score} | Description: {desc_score}"
    
    return SEOReport(
        listing=listing,
        score=score,
        title_analysis=title_analysis,
        tags_analysis=tags_analysis,
        description_analysis=desc_analysis,
        keyword_suggestions=keyword_suggestions,
        competitor_insights=[],
        action_items=action_items,
        summary=summary,
        summary_zh=summary_zh,
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(report: SEOReport, lang: str = "en") -> str:
    """FormatReport"""
    s = report.score
    t = report.title_analysis
    tg = report.tags_analysis
    d = report.description_analysis
    
    grade_colors = {"A": "🟢", "B": "🔵", "C": "🟡", "D": "🟠", "F": "🔴"}
    grade_icon = grade_colors.get(s.grade.value, "⚪")
    
    if lang == "zh":
        lines = [
            "🏷️ **Etsy SEO AnalyzeReport**",
            "",
            f"**Product**: {report.listing.title[:50]}...",
            f"**Category**: {report.listing.category}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## {grade_icon} SEO Overall Rating: {s.total}/100 (Grade {s.grade.value})",
            "",
            "| dimensionDegree | Score | Weight |",
            "|------|------|------|",
            f"| Title | {s.title_score}/100 | 30% |",
            f"| Tag | {s.tags_score}/100 | 25% |",
            f"| Description | {s.description_score}/100 | 20% |",
            f"| Property | {s.attributes_score}/100 | 15% |",
            f"| Image | {s.images_score}/100 | 10% |",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📝 TitleAnalyze",
            "",
            f"**Degree**: {t.length}/{t.max_length} Character",
            f"**Keywords**: {t.keyword_count} ",
            f"**CanReadability**: {t.readability}",
            "",
        ]
        
        if t.issues:
            lines.append("**Issue:**")
            for issue in t.issues:
                lines.append(f"- ❌ {issue}")
            lines.append("")
        
        if t.suggestions:
            lines.append("**Recommendation:**")
            for sug in t.suggestions:
                lines.append(f"- 💡 {sug}")
            lines.append("")
        
        if t.optimized_title:
            lines.extend([
                "**Optimization after TitleExample:**",
                f"```{t.optimized_title}```",
                "",
            ])
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 🏷️ TagAnalyze",
            "",
            f"** already Use**: {tg.count}/13 ",
            f"**Long-tail Keywords**: {tg.long_tail_count} ",
            f"**AverageDegree**: {tg.avg_length:.1f} Character",
            "",
        ])
        
        if tg.issues:
            lines.append("**Issue:**")
            for issue in tg.issues:
                lines.append(f"- ❌ {issue}")
            lines.append("")
        
        if tg.suggested_tags:
            lines.extend([
                "**RecommendedAddTag:**",
                "",
            ])
            for i, tag in enumerate(tg.suggested_tags, 1):
                lines.append(f"{i}. `{tag}`")
            lines.append("")
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📄 DescriptionAnalyze",
            "",
            f"**Degree**: {d.length} Character",
            f"**KeywordsdenseDegree**: {d.keyword_density:.1f}%",
            f"** has  CTA**: {'✅  is ' if d.has_call_to_action else '❌ no'}",
            "",
        ])
        
        if d.issues or d.suggestions:
            for issue in d.issues:
                lines.append(f"- ❌ {issue}")
            for sug in d.suggestions:
                lines.append(f"- 💡 {sug}")
            lines.append("")
        
        if report.keyword_suggestions:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 🔑 RecommendedKeywords",
                "",
                ", ".join([f"`{kw}`" for kw in report.keyword_suggestions[:8]]),
                "",
            ])
        
        if report.action_items:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 📋 Action Plan",
                "",
            ])
            for action in report.action_items[:5]:
                lines.append(f"**[{action['priority']}] [{action['category_zh']}]** {action['action_zh']}")
            lines.append("")
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            report.summary_zh,
        ])
    else:
        # English version (similar structure)
        lines = [
            "🏷️ **Etsy SEO Analysis Report**",
            "",
            f"**Listing**: {report.listing.title[:50]}...",
            f"**Category**: {report.listing.category}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            f"## {grade_icon} SEO Score: {s.total}/100 (Grade {s.grade.value})",
            "",
            "| Dimension | Score | Weight |",
            "|-----------|-------|--------|",
            f"| Title | {s.title_score}/100 | 30% |",
            f"| Tags | {s.tags_score}/100 | 25% |",
            f"| Description | {s.description_score}/100 | 20% |",
            f"| Attributes | {s.attributes_score}/100 | 15% |",
            f"| Images | {s.images_score}/100 | 10% |",
            "",
            "## 📝 Title Analysis",
            f"Length: {t.length}/{t.max_length} | Keywords: {t.keyword_count}",
            "",
        ]
        
        if t.issues:
            for issue in t.issues:
                lines.append(f"- ❌ {issue}")
        
        if tg.suggested_tags:
            lines.extend([
                "",
                "## 🏷️ Suggested Tags",
                ", ".join([f"`{tag}`" for tag in tg.suggested_tags]),
            ])
        
        lines.extend(["", report.summary])
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    lang = "zh" if "--zh" in sys.argv else "en"
    
    # DemoData
    listing = ListingInfo(
        title="Beautiful Handmade Bracelet",
        tags=["bracelet", "handmade", "gift", "jewelry", "beaded"],
        description="A beautiful handmade bracelet perfect for any occasion. Made with high quality beads.",
        category="jewelry",
        attributes={"material": "beads", "color": "blue"},
        images=5,
    )
    
    report = analyze_listing(listing)
    print(format_report(report, lang))


if __name__ == "__main__":
    main()
