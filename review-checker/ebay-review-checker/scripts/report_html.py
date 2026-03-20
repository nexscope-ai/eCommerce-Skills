#!/usr/bin/env python3
"""
Review Analysis HTML Report Generator
ReviewAnalyze HTML ReportGenerate

Features:
- CanViewTable (Chart.js)
- Responsive layout
-  deep colorMaintopic
- InteractiveDataDisplay

Version: 1.0.0
"""

import json
from typing import List, Dict, Any
from datetime import datetime


def generate_html_report(
    asin: str,
    authenticity_score: int,
    risk_level: str,
    dimensions: List[Dict[str, Any]],
    suspicious_reviews: List[Dict[str, Any]],
    total_reviews: int,
    analysis_level: str,
    summary: str,
    output_path: str = "review_analysis_report.html"
) -> str:
    """Generate HTML Report"""
    
    # RiskGradeColor
    risk_colors = {
        "low": "#10b981",      # Green
        "medium": "#f59e0b",   # Yellow
        "high": "#ef4444",     # Red
        "critical": "#7c2d12", #  deep red
    }
    
    risk_color = risk_colors.get(risk_level.lower(), "#6b7280")
    
    # dimensionDegreeData (use at chartTable)
    dimension_labels = json.dumps([d.get('name', d.get('name_zh', '')) for d in dimensions])
    dimension_scores = json.dumps([d.get('score', 0) for d in dimensions])
    
    # SuspiciousReview JSON
    suspicious_json = json.dumps(suspicious_reviews[:10], ensure_ascii=False, default=str)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Review Analysis Report - {asin}</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #e4e4e7;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        
        .header {{
            text-align: center;
            padding: 40px 20px;
            background: rgba(255,255,255,0.05);
            border-radius: 16px;
            margin-bottom: 30px;
        }}
        
        .header h1 {{
            font-size: 2rem;
            background: linear-gradient(90deg, #a78bfa, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        
        .header .asin {{
            color: #a1a1aa;
            font-size: 1.1rem;
        }}
        
        .score-card {{
            background: rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 40px;
            text-align: center;
            margin-bottom: 30px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .score-number {{
            font-size: 5rem;
            font-weight: bold;
            color: {risk_color};
            line-height: 1;
        }}
        
        .score-label {{
            font-size: 1.2rem;
            color: #a1a1aa;
            margin-top: 10px;
        }}
        
        .risk-badge {{
            display: inline-block;
            padding: 8px 20px;
            border-radius: 20px;
            background: {risk_color};
            color: white;
            font-weight: 600;
            margin-top: 15px;
            text-transform: uppercase;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: rgba(255,255,255,0.08);
            border-radius: 12px;
            padding: 24px;
            border: 1px solid rgba(255,255,255,0.1);
        }}
        
        .card h3 {{
            font-size: 1.1rem;
            margin-bottom: 20px;
            color: #a78bfa;
        }}
        
        .stat {{
            display: flex;
            justify-content: space-between;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .stat:last-child {{
            border-bottom: none;
        }}
        
        .stat-label {{
            color: #a1a1aa;
        }}
        
        .stat-value {{
            font-weight: 600;
        }}
        
        .chart-container {{
            position: relative;
            height: 300px;
            width: 100%;
        }}
        
        .dimension-item {{
            display: flex;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        
        .dimension-icon {{
            width: 30px;
            font-size: 1.2rem;
        }}
        
        .dimension-name {{
            flex: 1;
        }}
        
        .dimension-score {{
            font-weight: 600;
            width: 80px;
            text-align: right;
        }}
        
        .suspicious-item {{
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.3);
            border-radius: 8px;
            padding: 16px;
            margin-bottom: 12px;
        }}
        
        .suspicious-header {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 8px;
        }}
        
        .suspicious-risk {{
            color: #ef4444;
            font-weight: 600;
        }}
        
        .suspicious-content {{
            color: #d4d4d8;
            font-style: italic;
            margin-bottom: 8px;
        }}
        
        .suspicious-reasons {{
            color: #a1a1aa;
            font-size: 0.9rem;
        }}
        
        .summary {{
            background: rgba(167, 139, 250, 0.1);
            border: 1px solid rgba(167, 139, 250, 0.3);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            color: #71717a;
            font-size: 0.9rem;
        }}
        
        @media (max-width: 768px) {{
            .score-number {{
                font-size: 3rem;
            }}
            .grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Review Authenticity Analysis</h1>
            <div class="asin">ASIN: {asin}</div>
        </div>
        
        <div class="score-card">
            <div class="score-number">{authenticity_score}</div>
            <div class="score-label">Authenticity Score (0-100)</div>
            <div class="risk-badge">{risk_level.upper()} RISK</div>
        </div>
        
        <div class="summary">
            <strong>Summary:</strong> {summary}
        </div>
        
        <div class="grid">
            <div class="card">
                <h3>📈 Overview</h3>
                <div class="stat">
                    <span class="stat-label">Total Reviews</span>
                    <span class="stat-value">{total_reviews}</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Analysis Level</span>
                    <span class="stat-value">{analysis_level}</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Suspicious Reviews</span>
                    <span class="stat-value">{len(suspicious_reviews)}</span>
                </div>
                <div class="stat">
                    <span class="stat-label">Generated</span>
                    <span class="stat-value">{datetime.now().strftime('%Y-%m-%d %H:%M')}</span>
                </div>
            </div>
            
            <div class="card">
                <h3>🎯 Detection Dimensions</h3>
                <div class="chart-container">
                    <canvas id="dimensionChart"></canvas>
                </div>
            </div>
        </div>
        
        <div class="card" style="margin-bottom: 30px;">
            <h3>🔍 Dimension Details</h3>
            {"".join([f'''
            <div class="dimension-item">
                <div class="dimension-icon">{d.get('status', '❓')}</div>
                <div class="dimension-name">{d.get('name', d.get('name_zh', ''))}</div>
                <div class="dimension-score" style="color: {'#10b981' if d.get('score', 0) < 30 else '#f59e0b' if d.get('score', 0) < 60 else '#ef4444'}">{d.get('score', 0):.0f}/100</div>
            </div>
            <div style="color: #a1a1aa; font-size: 0.9rem; padding-left: 30px; padding-bottom: 12px;">{d.get('detail', d.get('detail_zh', ''))}</div>
            ''' for d in dimensions])}
        </div>
        
        <div class="card">
            <h3>⚠️ Suspicious Reviews (Top {min(len(suspicious_reviews), 5)})</h3>
            <div id="suspiciousReviews"></div>
        </div>
        
        <div class="footer">
            <p>Generated by Amazon Review Checker | Nexscope AI</p>
            <p>This analysis is for reference only. Results may not be 100% accurate.</p>
        </div>
    </div>
    
    <script>
        // dimensionDegreeRadar chart
        const ctx = document.getElementById('dimensionChart').getContext('2d');
        new Chart(ctx, {{
            type: 'radar',
            data: {{
                labels: {dimension_labels},
                datasets: [{{
                    label: 'Suspicion Score',
                    data: {dimension_scores},
                    backgroundColor: 'rgba(167, 139, 250, 0.2)',
                    borderColor: 'rgba(167, 139, 250, 1)',
                    borderWidth: 2,
                    pointBackgroundColor: 'rgba(167, 139, 250, 1)',
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                scales: {{
                    r: {{
                        beginAtZero: true,
                        max: 100,
                        ticks: {{
                            color: '#a1a1aa',
                            backdropColor: 'transparent'
                        }},
                        grid: {{
                            color: 'rgba(255,255,255,0.1)'
                        }},
                        pointLabels: {{
                            color: '#e4e4e7',
                            font: {{ size: 11 }}
                        }}
                    }}
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }}
                }}
            }}
        }});
        
        // SuspiciousReview
        const suspicious = {suspicious_json};
        const container = document.getElementById('suspiciousReviews');
        
        if (suspicious.length === 0) {{
            container.innerHTML = '<p style="color: #10b981;">No highly suspicious reviews detected.</p>';
        }} else {{
            suspicious.slice(0, 5).forEach((review, index) => {{
                container.innerHTML += `
                    <div class="suspicious-item">
                        <div class="suspicious-header">
                            <span>#${{index + 1}}</span>
                            <span class="suspicious-risk">Risk: ${{review.risk_score?.toFixed(0) || 'N/A'}}%</span>
                        </div>
                        <div class="suspicious-content">"${{review.content}}"</div>
                        <div class="suspicious-reasons">Reasons: ${{(review.reasons || review.reasons_zh || []).join(', ')}}</div>
                    </div>
                `;
            }});
        }}
    </script>
</body>
</html>
"""
    
    # SaveFile
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ HTML report saved to: {output_path}")
    return output_path


# CLI
if __name__ == "__main__":
    # TestData
    generate_html_report(
        asin="B08XXXXX",
        authenticity_score=66,
        risk_level="medium",
        dimensions=[
            {"name": "Content Similarity", "name_zh": "Similar contentDegree", "score": 24, "status": "✅", "detail": "Found 0 similar review pairs"},
            {"name": "Time Clustering", "name_zh": "TimeAggregate", "score": 70, "status": "🔴", "detail": "6 reviews in 48h window"},
            {"name": "Rating Distribution", "name_zh": "Rating Distribution", "score": 0, "status": "✅", "detail": "Normal distribution"},
            {"name": "VP Ratio", "name_zh": "VPRatio", "score": 30, "status": "⚠️", "detail": "50% verified purchase"},
            {"name": "Review Length", "name_zh": "ReviewDegree", "score": 0, "status": "✅", "detail": "Normal length distribution"},
            {"name": "Suspicious Keywords", "name_zh": "SuspiciousKeywords", "score": 80, "status": "🔴", "detail": "4 reviews contain suspicious keywords"},
        ],
        suspicious_reviews=[
            {"content": "Perfect!", "risk_score": 75, "reasons": ["Very short", "Not VP", "Generic template"]},
            {"content": "Five stars! Amazing product!", "risk_score": 75, "reasons": ["Very short", "Not VP", "Generic template"]},
            {"content": "Received free product in exchange for honest review...", "risk_score": 60, "reasons": ["Not VP", "Incentivized review"]},
        ],
        total_reviews=10,
        analysis_level="L4",
        summary="Medium risk - Some concerns detected. Analyzed 10 reviews at L4 level.",
        output_path="review_analysis_report.html"
    )
