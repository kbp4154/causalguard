from jinja2 import Template
import webbrowser, os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CausalGuard Report</title>
    <style>
        body { font-family: system-ui; margin: 40px; background: #0d1117; color: #c9d1d9; }
        .critical { background: #490202; color: #ffa8a8; }
        .high { background: #5a1e02; color: #ffd8b1; }
        .medium { background: #663d00; color: #ffe8b8; }
        .issue { padding: 16px; margin: 12px 0; border-radius: 8px; border-left: 6px solid #f85149; }
        h1 { color: #58a6ff; }
    </style>
</head>
<body>
    <h1>🛡️ CausalGuard Report — {{ issues|length }} issues found</h1>
    {% for issue in issues %}
    <div class="issue {{ issue.severity.lower() }}">
        <h3>[{{ issue.severity }}] {{ issue.type }}</h3>
        <p>{{ issue.message }}</p>
        {% if issue.suggestion %}<p><strong>Suggestion:</strong> {{ issue.suggestion }}</p>{% endif %}
    </div>
    {% endfor %}
</body>
</html>
"""

def generate_html_report(issues, preset="fraud"):
    template = Template(HTML_TEMPLATE)
    html = template.render(issues=issues, preset=preset)
    
    with open("causalguard_report.html", "w") as f:
        f.write(html)
    
    webbrowser.open("causalguard_report.html")
