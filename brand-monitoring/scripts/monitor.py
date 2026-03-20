#!/usr/bin/env python3
"""
Brand Monitoring - Core Engine
Brand Monitoring - Core Engine

Features:
- BrandMention Monitoring
- SentimentAnalyze (positive/negative/ in )
- TrendTrack
- Abnormal/Crisis Detection
- CompetitorVolumeComparison
- Keyword Extraction
- ReportGenerate

Datasource (Lite):
- Reddit (PublicSearch)
- Google ( new news/Blog)
- YouTube (Review)
- ManualInput

Version: 1.0.0
"""

import json
import re
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple
from enum import Enum
from datetime import datetime, timedelta
from collections import Counter
import sys


class Sentiment(Enum):
    """SentimentCategoryType"""
    POSITIVE = "positive"
    NEGATIVE = "negative"
    NEUTRAL = "neutral"


class Platform(Enum):
    """PlatformCategoryType"""
    REDDIT = "reddit"
    TWITTER = "twitter"
    YOUTUBE = "youtube"
    AMAZON = "amazon"
    GOOGLE = "google"
    TIKTOK = "tiktok"
    FACEBOOK = "facebook"
    FORUM = "forum"
    NEWS = "news"
    OTHER = "other"


class AlertLevel(Enum):
    """AlertLevelother"""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


# ============================================================
# SentimentKeywordsLibrary
# ============================================================

POSITIVE_KEYWORDS = {
    "en": [
        "love", "great", "amazing", "awesome", "excellent", "perfect", "best",
        "fantastic", "wonderful", "recommend", "happy", "satisfied", "quality",
        "worth", "impressed", "reliable", "favorite", "brilliant", "superb"
    ],
    "zh": [
        "Like", " very  good ", "great", "Excellent", "Perfect", " most  good ", "Recommended", "Satisfied", "Quality good ",
        "Value ", "Impressive", "Canrely", " most love", "Excellent"
    ]
}

NEGATIVE_KEYWORDS = {
    "en": [
        "hate", "terrible", "awful", "worst", "bad", "horrible", "disappointed",
        "waste", "scam", "fake", "poor", "broken", "useless", "regret", "avoid",
        "never", "refund", "complaint", "problem", "issue", "sucks"
    ],
    "zh": [
        "Hate", "Terrible", "difference", " most difference", " bad ", "Disappointed", "Waste", "Scammer", "Counterfeit",
        "Poor", " bad  ", "Useless", " after regret", "Avoid", "Refund", "Complaint", "Issue"
    ]
}

CRISIS_KEYWORDS = {
    "en": [
        "lawsuit", "recall", "investigation", "fraud", "scandal", "danger",
        "safety", "warning", "banned", "illegal", "death", "injury", "toxic"
    ],
    "zh": [
        "Lawsuit", "Recall", "Investigation", "Fraud", "Scandal", "Danger", "safe all ", "Warning",
        "Prohibited", "Illegal", "Death", "Harm", " has toxic"
    ]
}


# ============================================================
# Data Structures
# ============================================================

@dataclass
class Mention:
    """Brandmention and """
    content: str
    platform: Platform
    url: str = ""
    author: str = ""
    date: Optional[datetime] = None
    engagement: int = 0  # Interactivequantity (likes, comments, shares)
    sentiment: Sentiment = Sentiment.NEUTRAL
    sentiment_score: float = 0.0
    keywords: List[str] = field(default_factory=list)
    is_influential: bool = False


@dataclass
class BrandMetrics:
    """BrandMetrics"""
    total_mentions: int = 0
    positive_count: int = 0
    negative_count: int = 0
    neutral_count: int = 0
    avg_sentiment_score: float = 0.0
    total_engagement: int = 0
    top_keywords: List[Tuple[str, int]] = field(default_factory=list)
    platform_distribution: Dict[str, int] = field(default_factory=dict)
    daily_trend: Dict[str, int] = field(default_factory=dict)


@dataclass
class Alert:
    """Alert"""
    level: AlertLevel
    title: str
    title_zh: str
    description: str
    description_zh: str
    trigger: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class CompetitorComparison:
    """CompetitorComparison"""
    brand: str
    metrics: BrandMetrics
    share_of_voice: float = 0.0


@dataclass
class MonitoringReport:
    """MonitoringReport"""
    brand_name: str
    period_start: datetime
    period_end: datetime
    metrics: BrandMetrics
    mentions: List[Mention]
    alerts: List[Alert]
    competitors: List[CompetitorComparison]
    top_positive: List[Mention]
    top_negative: List[Mention]
    summary: str
    summary_zh: str


# ============================================================
# SentimentAnalyze
# ============================================================

def analyze_sentiment(text: str, lang: str = "en") -> Tuple[Sentiment, float]:
    """AnalyzeTextSentiment"""
    text_lower = text.lower()
    
    positive_score = 0
    negative_score = 0
    
    # KeywordsMatch
    for keyword in POSITIVE_KEYWORDS.get(lang, []) + POSITIVE_KEYWORDS.get("en", []):
        if keyword.lower() in text_lower:
            positive_score += 1
    
    for keyword in NEGATIVE_KEYWORDS.get(lang, []) + NEGATIVE_KEYWORDS.get("en", []):
        if keyword.lower() in text_lower:
            negative_score += 1
    
    # CalculateScore (-1  to  +1)
    total = positive_score + negative_score
    if total == 0:
        return Sentiment.NEUTRAL, 0.0
    
    score = (positive_score - negative_score) / max(total, 1)
    
    if score > 0.2:
        sentiment = Sentiment.POSITIVE
    elif score < -0.2:
        sentiment = Sentiment.NEGATIVE
    else:
        sentiment = Sentiment.NEUTRAL
    
    return sentiment, round(score, 2)


def extract_keywords(text: str, top_n: int = 5) -> List[str]:
    """ExtractKeywords"""
    # SimpleWord frequencyStatistics
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    
    # FilterStop words
    stopwords = {"this", "that", "with", "have", "from", "they", "been", "were", "will", "would", "could", "should", "about", "their", "there", "which", "when", "what", "your", "just", "some", "more", "very", "really"}
    words = [w for w in words if w not in stopwords]
    
    counter = Counter(words)
    return [word for word, count in counter.most_common(top_n)]


def detect_crisis(text: str) -> bool:
    """DetectionCrisisKeywords"""
    text_lower = text.lower()
    for keyword in CRISIS_KEYWORDS.get("en", []):
        if keyword in text_lower:
            return True
    return False


# ============================================================
# DataCollect (Lite - Simulate/Demo)
# ============================================================

def search_reddit(brand_name: str, limit: int = 20) -> List[Mention]:
    """Search Reddit (Lite: SimulateData)"""
    # In real implementation， this  in  will Use Reddit API  or Crawler
    # Lite versionUse pushshift.io  or CategorySeemingly free service
    print(f"[Reddit] Searching for: {brand_name}")
    return []


def search_google_news(brand_name: str, limit: int = 20) -> List[Mention]:
    """Search Google News (Lite: SimulateData)"""
    print(f"[Google News] Searching for: {brand_name}")
    return []


def get_demo_mentions(brand_name: str) -> List[Mention]:
    """GetDemoData"""
    now = datetime.now()
    
    return [
        Mention(
            content=f"Just got my {brand_name} product and I absolutely love it! Best purchase this year.",
            platform=Platform.REDDIT,
            url="https://reddit.com/r/product/xxx",
            author="happy_customer",
            date=now - timedelta(hours=2),
            engagement=150,
        ),
        Mention(
            content=f"Has anyone tried {brand_name}? Looking for honest reviews before buying.",
            platform=Platform.REDDIT,
            url="https://reddit.com/r/product/yyy",
            author="curious_buyer",
            date=now - timedelta(hours=5),
            engagement=45,
        ),
        Mention(
            content=f"Disappointed with {brand_name} quality. The product broke after 2 weeks. Waste of money!",
            platform=Platform.TWITTER,
            url="https://twitter.com/user/status/xxx",
            author="angry_buyer",
            date=now - timedelta(hours=8),
            engagement=320,
        ),
        Mention(
            content=f"Comparing {brand_name} vs competitors - honest review video coming soon!",
            platform=Platform.YOUTUBE,
            url="https://youtube.com/watch?v=xxx",
            author="tech_reviewer",
            date=now - timedelta(days=1),
            engagement=5000,
        ),
        Mention(
            content=f"{brand_name} announces new product line with improved features",
            platform=Platform.NEWS,
            url="https://news.example.com/article",
            author="TechNews",
            date=now - timedelta(days=1),
            engagement=200,
        ),
        Mention(
            content=f"I've been using {brand_name} for 6 months now. Highly recommend for anyone looking for quality.",
            platform=Platform.REDDIT,
            url="https://reddit.com/r/reviews/xxx",
            author="long_time_user",
            date=now - timedelta(days=2),
            engagement=89,
        ),
        Mention(
            content=f"Warning: {brand_name} customer service is terrible. Been waiting 3 weeks for refund!",
            platform=Platform.TWITTER,
            url="https://twitter.com/user/status/yyy",
            author="frustrated_customer",
            date=now - timedelta(days=2),
            engagement=180,
        ),
        Mention(
            content=f"Just saw {brand_name} at the store. The packaging looks premium!",
            platform=Platform.TIKTOK,
            url="https://tiktok.com/@user/video/xxx",
            author="shopping_vlog",
            date=now - timedelta(days=3),
            engagement=2500,
        ),
    ]


# ============================================================
# CoreAnalyze
# ============================================================

def analyze_mentions(mentions: List[Mention]) -> Tuple[List[Mention], BrandMetrics]:
    """Analyzemention and Data"""
    
    # SentimentAnalyze
    for mention in mentions:
        sentiment, score = analyze_sentiment(mention.content)
        mention.sentiment = sentiment
        mention.sentiment_score = score
        mention.keywords = extract_keywords(mention.content)
        mention.is_influential = mention.engagement > 1000
    
    # CalculateMetrics
    metrics = BrandMetrics()
    metrics.total_mentions = len(mentions)
    metrics.positive_count = len([m for m in mentions if m.sentiment == Sentiment.POSITIVE])
    metrics.negative_count = len([m for m in mentions if m.sentiment == Sentiment.NEGATIVE])
    metrics.neutral_count = len([m for m in mentions if m.sentiment == Sentiment.NEUTRAL])
    
    if mentions:
        metrics.avg_sentiment_score = round(sum(m.sentiment_score for m in mentions) / len(mentions), 2)
        metrics.total_engagement = sum(m.engagement for m in mentions)
    
    # PlatformDistribution
    for mention in mentions:
        platform = mention.platform.value
        metrics.platform_distribution[platform] = metrics.platform_distribution.get(platform, 0) + 1
    
    # KeywordsStatistics
    all_keywords = []
    for mention in mentions:
        all_keywords.extend(mention.keywords)
    metrics.top_keywords = Counter(all_keywords).most_common(10)
    
    return mentions, metrics


def generate_alerts(mentions: List[Mention], metrics: BrandMetrics) -> List[Alert]:
    """GenerateAlert"""
    alerts = []
    
    # NegativeSentimentProportionAlert
    if metrics.total_mentions > 0:
        negative_ratio = metrics.negative_count / metrics.total_mentions
        if negative_ratio > 0.4:
            alerts.append(Alert(
                level=AlertLevel.CRITICAL,
                title="High Negative Sentiment",
                title_zh="NegativeSentiment High",
                description=f"Negative mentions at {negative_ratio*100:.1f}% - above 40% threshold",
                description_zh=f"Negativemention and Proportion {negative_ratio*100:.1f}% - super  40% Threshold",
                trigger=f"negative_ratio > 0.4",
            ))
        elif negative_ratio > 0.3:
            alerts.append(Alert(
                level=AlertLevel.WARNING,
                title="Elevated Negative Sentiment",
                title_zh="NegativeEmotion riseHigh",
                description=f"Negative mentions at {negative_ratio*100:.1f}% - above 30% threshold",
                description_zh=f"Negativemention and Proportion {negative_ratio*100:.1f}% - super  30% Threshold",
                trigger=f"negative_ratio > 0.3",
            ))
    
    # HighImpactpowerNegativemention and 
    influential_negative = [m for m in mentions if m.is_influential and m.sentiment == Sentiment.NEGATIVE]
    if influential_negative:
        alerts.append(Alert(
            level=AlertLevel.CRITICAL,
            title="Influential Negative Mention",
            title_zh="HighImpactpowerNegativemention and ",
            description=f"Found {len(influential_negative)} negative mention(s) with high engagement",
            description_zh=f"Found {len(influential_negative)} itemHighInteractivequantityNegativemention and ",
            trigger="engagement > 1000 AND sentiment = negative",
        ))
    
    # CrisisKeywordsDetection
    crisis_mentions = [m for m in mentions if detect_crisis(m.content)]
    if crisis_mentions:
        alerts.append(Alert(
            level=AlertLevel.CRITICAL,
            title="Potential Crisis Detected",
            title_zh="potential in Crisis Detection",
            description=f"Found {len(crisis_mentions)} mention(s) with crisis keywords",
            description_zh=f"Found {len(crisis_mentions)} Contains crisisKeywordsmention and ",
            trigger="crisis_keywords detected",
        ))
    
    return alerts


def monitor_brand(
    brand_name: str,
    competitors: List[str] = None,
    mentions: List[Mention] = None,
) -> MonitoringReport:
    """Brand MonitoringMainFunction"""
    
    now = datetime.now()
    period_start = now - timedelta(days=7)
    
    # GetData
    if mentions is None:
        mentions = get_demo_mentions(brand_name)
    
    # Analyze
    mentions, metrics = analyze_mentions(mentions)
    
    # GenerateAlert
    alerts = generate_alerts(mentions, metrics)
    
    # CompetitorComparison
    competitor_data = []
    if competitors:
        total_mentions = metrics.total_mentions
        for comp in competitors:
            comp_mentions = get_demo_mentions(comp)[:3]  # Demo:  few quantityData
            _, comp_metrics = analyze_mentions(comp_mentions)
            sov = comp_metrics.total_mentions / (total_mentions + comp_metrics.total_mentions) if total_mentions > 0 else 0
            competitor_data.append(CompetitorComparison(
                brand=comp,
                metrics=comp_metrics,
                share_of_voice=round(sov, 2),
            ))
    
    # Top mention and 
    sorted_positive = sorted([m for m in mentions if m.sentiment == Sentiment.POSITIVE], key=lambda x: -x.engagement)
    sorted_negative = sorted([m for m in mentions if m.sentiment == Sentiment.NEGATIVE], key=lambda x: -x.engagement)
    
    # Summary
    pos_pct = metrics.positive_count / metrics.total_mentions * 100 if metrics.total_mentions > 0 else 0
    neg_pct = metrics.negative_count / metrics.total_mentions * 100 if metrics.total_mentions > 0 else 0
    
    summary = f"📊 {metrics.total_mentions} mentions | 😊 {pos_pct:.0f}% positive | 😠 {neg_pct:.0f}% negative | ⚠️ {len(alerts)} alerts"
    summary_zh = f"📊 {metrics.total_mentions} Item mention and  | 😊 {pos_pct:.0f}% Positive | 😠 {neg_pct:.0f}% Negative | ⚠️ {len(alerts)} itemAlert"
    
    return MonitoringReport(
        brand_name=brand_name,
        period_start=period_start,
        period_end=now,
        metrics=metrics,
        mentions=mentions,
        alerts=alerts,
        competitors=competitor_data,
        top_positive=sorted_positive[:3],
        top_negative=sorted_negative[:3],
        summary=summary,
        summary_zh=summary_zh,
    )


# ============================================================
# OutputFormat
# ============================================================

def format_report(report: MonitoringReport, lang: str = "en") -> str:
    """FormatReport"""
    m = report.metrics
    
    if lang == "zh":
        lines = [
            "📡 **Brand MonitoringReport**",
            "",
            f"**Brand**: {report.brand_name}",
            f"**MonitoringweeksPeriod**: {report.period_start.strftime('%Y-%m-%d')} ~ {report.period_end.strftime('%Y-%m-%d')}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📊 OverallMetrics",
            "",
            f"| Metrics | Value |",
            f"|------|------|",
            f"| Total mention and  | {m.total_mentions} |",
            f"| Positivemention and  | {m.positive_count} ({m.positive_count/m.total_mentions*100:.0f}%) |" if m.total_mentions > 0 else f"| Positivemention and  | 0 |",
            f"| Negativemention and  | {m.negative_count} ({m.negative_count/m.total_mentions*100:.0f}%) |" if m.total_mentions > 0 else f"| Negativemention and  | 0 |",
            f"| Neutralmention and  | {m.neutral_count} |",
            f"| AverageSentiment score | {m.avg_sentiment_score} |",
            f"| Total engagement | {m.total_engagement:,} |",
            "",
        ]
        
        # Alert
        if report.alerts:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## ⚠️ Alert",
                "",
            ])
            for alert in report.alerts:
                level_icon = "🚨" if alert.level == AlertLevel.CRITICAL else "⚠️" if alert.level == AlertLevel.WARNING else "ℹ️"
                lines.append(f"**{level_icon} {alert.title_zh}**")
                lines.append(f"   {alert.description_zh}")
                lines.append("")
        
        # PlatformDistribution
        if m.platform_distribution:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 📱 PlatformDistribution",
                "",
            ])
            for platform, count in sorted(m.platform_distribution.items(), key=lambda x: -x[1]):
                pct = count / m.total_mentions * 100 if m.total_mentions > 0 else 0
                lines.append(f"- **{platform}**: {count} ({pct:.0f}%)")
            lines.append("")
        
        # PopularKeywords
        if m.top_keywords:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 🔑 PopularKeywords",
                "",
                ", ".join([f"`{word}` ({count})" for word, count in m.top_keywords[:8]]),
                "",
            ])
        
        # Top Positivemention and 
        if report.top_positive:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 😊 PopularPositivemention and ",
                "",
            ])
            for i, mention in enumerate(report.top_positive[:3], 1):
                lines.append(f"**{i}. [{mention.platform.value}]** Interactive: {mention.engagement:,}")
                lines.append(f"   \"{mention.content[:80]}...\"")
                lines.append("")
        
        # Top Negativemention and 
        if report.top_negative:
            lines.extend([
                "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
                "",
                "## 😠  need AttentionNegativemention and ",
                "",
            ])
            for i, mention in enumerate(report.top_negative[:3], 1):
                lines.append(f"**{i}. [{mention.platform.value}]** Interactive: {mention.engagement:,}")
                lines.append(f"   \"{mention.content[:80]}...\"")
                lines.append("")
        
        lines.extend([
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            report.summary_zh,
        ])
    else:
        # English version
        lines = [
            "📡 **Brand Monitoring Report**",
            "",
            f"**Brand**: {report.brand_name}",
            f"**Period**: {report.period_start.strftime('%Y-%m-%d')} ~ {report.period_end.strftime('%Y-%m-%d')}",
            "",
            "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
            "",
            "## 📊 Overview Metrics",
            "",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Total Mentions | {m.total_mentions} |",
            f"| Positive | {m.positive_count} ({m.positive_count/m.total_mentions*100:.0f}%) |" if m.total_mentions > 0 else "| Positive | 0 |",
            f"| Negative | {m.negative_count} ({m.negative_count/m.total_mentions*100:.0f}%) |" if m.total_mentions > 0 else "| Negative | 0 |",
            f"| Neutral | {m.neutral_count} |",
            f"| Avg Sentiment | {m.avg_sentiment_score} |",
            f"| Total Engagement | {m.total_engagement:,} |",
            "",
        ]
        
        if report.alerts:
            lines.extend(["## ⚠️ Alerts", ""])
            for alert in report.alerts:
                level_icon = "🚨" if alert.level == AlertLevel.CRITICAL else "⚠️"
                lines.append(f"**{level_icon} {alert.title}**: {alert.description}")
            lines.append("")
        
        if m.platform_distribution:
            lines.extend(["## 📱 Platform Distribution", ""])
            for platform, count in sorted(m.platform_distribution.items(), key=lambda x: -x[1]):
                lines.append(f"- **{platform}**: {count}")
            lines.append("")
        
        lines.extend(["", report.summary])
    
    return "\n".join(lines)


# ============================================================
# CLI
# ============================================================

def main():
    lang = "zh" if "--zh" in sys.argv else "en"
    brand = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--") else "TechBrand"
    
    report = monitor_brand(brand, competitors=["CompetitorA", "CompetitorB"])
    print(format_report(report, lang))


if __name__ == "__main__":
    main()
