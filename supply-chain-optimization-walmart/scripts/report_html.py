#!/usr/bin/env python3
"""
Supply Chain Analyzer - HTML Report Generator
Supply ChainAnalyze - WebchartTableReportGenerate
"""

import json
from datetime import datetime
from calculator import SupplyChainInput, analyze, HealthStatus


def generate_html_report(data: SupplyChainInput, output_path: str = "report.html") -> str:
    """
    GenerateWebchartTableReport
    """
    result = analyze(data)
    
    # Prepare imageTableData
    metrics_data = [
        {"name": m.name, "value": m.value, "benchmark": m.benchmark, "status": m.status.value}
        for m in result.metrics
    ]
    
    cost_data = result.cost_breakdown
    
    bottlenecks_html = ""
    severity_colors = {"High": "#ef4444", " in ": "#f59e0b", " low ": "#22c55e"}
    for i, b in enumerate(result.bottlenecks, 1):
        color = severity_colors.get(b.severity, "#6b7280")
        bottlenecks_html += f"""
        <div class="bottleneck-card">
            <div class="bottleneck-header">
                <span class="priority">#{i}</span>
                <span class="severity" style="background: {color}">{b.severity}</span>
                <span class="title">{b.title}</span>
            </div>
            <div class="bottleneck-body">
                <p><strong>Issue:</strong> {b.problem}</p>
                <p><strong>Impact:</strong> {b.impact}</p>
                <p><strong>Recommendation:</strong> {b.suggestion}</p>
            </div>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supply ChainAnalyzeReport</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: #fff;
            min-height: 100vh;
            padding: 40px 20px;
        }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .header h1 {{
            font-size: 32px;
            margin-bottom: 8px;
        }}
        .header p {{
            color: rgba(255,255,255,0.6);
        }}
        .summary-banner {{
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.2) 0%, rgba(139, 92, 246, 0.2) 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 16px;
            padding: 24px 32px;
            margin-bottom: 40px;
            text-align: center;
        }}
        .summary-banner h2 {{
            font-size: 20px;
            margin-bottom: 8px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 24px;
            margin-bottom: 40px;
        }}
        .card {{
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 16px;
            padding: 24px;
        }}
        .card h3 {{
            font-size: 18px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .metrics-table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .metrics-table th, .metrics-table td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        .metrics-table th {{
            color: rgba(255,255,255,0.6);
            font-weight: 500;
        }}
        .status {{
            display: inline-flex;
            align-items: center;
            gap: 4px;
        }}
        .status.healthy {{ color: #22c55e; }}
        .status.warning {{ color: #f59e0b; }}
        .status.danger {{ color: #ef4444; }}
        .chart-container {{
            position: relative;
            height: 300px;
        }}
        .bottleneck-card {{
            background: rgba(0,0,0,0.2);
            border-radius: 12px;
            padding: 16px;
            margin-bottom: 16px;
        }}
        .bottleneck-header {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }}
        .priority {{
            background: rgba(99, 102, 241, 0.3);
            padding: 4px 10px;
            border-radius: 6px;
            font-weight: 600;
        }}
        .severity {{
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
        }}
        .title {{
            font-weight: 600;
            font-size: 16px;
        }}
        .bottleneck-body p {{
            color: rgba(255,255,255,0.7);
            font-size: 14px;
            margin-bottom: 8px;
        }}
        .footer {{
            text-align: center;
            color: rgba(255,255,255,0.4);
            font-size: 12px;
            margin-top: 40px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📦 Supply ChainBottleneckAnalyzeReport</h1>
            <p>GenerateTime: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
        </div>
        
        <div class="summary-banner">
            <h2>{result.summary}</h2>
            <p>Based onProvided by youData，WeFound  {len(result.bottlenecks)} NeedAttentionIssue</p>
        </div>
        
        <div class="grid">
            <div class="card">
                <h3>📊 Key Metrics</h3>
                <table class="metrics-table">
                    <thead>
                        <tr>
                            <th>Metrics</th>
                            <th>Value</th>
                            <th>Benchmark</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {"".join(f'''
                        <tr>
                            <td>{m.name}</td>
                            <td>{m.value}{m.unit}</td>
                            <td>{m.benchmark}{m.unit}</td>
                            <td><span class="status {m.status.value}">
                                {"✅" if m.status == HealthStatus.HEALTHY else "⚠️" if m.status == HealthStatus.WARNING else "🔴"}
                            </span></td>
                        </tr>
                        ''' for m in result.metrics)}
                    </tbody>
                </table>
            </div>
            
            <div class="card">
                <h3>💰 CostStructure</h3>
                <div class="chart-container">
                    <canvas id="costChart"></canvas>
                </div>
            </div>
        </div>
        
        <div class="card">
            <h3>🎯 Top 3 Bottleneck Diagnosis</h3>
            {bottlenecks_html if bottlenecks_html else "<p>✅ No obvious bottleneck found，Supply ChainOverallHealthy</p>"}
        </div>
        
        <div class="footer">
            <p>Powered by Supply Chain Analyzer Skill | NexScope</p>
        </div>
    </div>
    
    <script>
        // CostStructure pie chart
        const costCtx = document.getElementById('costChart').getContext('2d');
        new Chart(costCtx, {{
            type: 'doughnut',
            data: {{
                labels: ['ProductCost', 'InboundLogistics', 'FBAFulfillment', 'Storagefee', 'Advertisingfee', 'Other', 'Net Profit'],
                datasets: [{{
                    data: [
                        {cost_data['product_cost_ratio']},
                        {cost_data['shipping_ratio']},
                        {cost_data['fba_ratio']},
                        {cost_data['storage_ratio']},
                        {cost_data['ad_ratio']},
                        5,
                        {cost_data['net_margin']}
                    ],
                    backgroundColor: [
                        '#ef4444',
                        '#f59e0b',
                        '#3b82f6',
                        '#8b5cf6',
                        '#ec4899',
                        '#6b7280',
                        '#22c55e'
                    ],
                    borderWidth: 0
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        position: 'right',
                        labels: {{
                            color: '#fff',
                            padding: 12
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
"""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return output_path


if __name__ == "__main__":
    # TestData
    test_data = SupplyChainInput(
        product_cost=8.00,
        supplier_payment_days=0,
        production_days=25,
        shipping_cost_per_unit=0.75,
        shipping_days=35,
        selling_price=25.00,
        fba_fee=5.00,
        storage_fee=0.50,
        ad_spend_ratio=0.10,
        inventory_days=60,
        has_long_term_storage=True,
        platform="amazon"
    )
    
    output = generate_html_report(test_data, "supply_chain_report.html")
    print(f"✅ Report already Generate: {output}")
