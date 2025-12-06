from jinja2 import Template
import webbrowser
import os

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>CausalGuard Report</title>
    <meta charset="utf-8">
    <style>
        body { font-family: system-ui, sans-serif; margin: 40px; background: #0d1117; color: #c9d1d9; }
        .critical { background: #490202; border-left: 6px solid #f85149; }
        .high     { background: #5a1e02; border-left: 6px solid #f0883e; }
        .medium   { background: #663d00; border-left: 6px solid #d29922; }
        .issue { padding: 16px; margin: 12px 0; border-radius: 8px; }
        h1 { color: #58a6ff; }
        .header { text-align: center; margin-bottom: 40px; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Shield CausalGuard Report</h1>
        <p><strong>{{ issues|length }}</strong> potential issues found</p>
    </div>
    {% for issue in issues %}
    <div class="issue {{ issue.severity.lower() }}">
        <h3>[{{ issue.severity }}] {{ issue.type.replace('_', ' ') | title }}</h3>
        <p>{{ issue.message }}</p>
        {% if issue.suggestion %}<p><strong>Suggestion:</strong> {{ issue.suggestion }}</p>{% endif %}
    </div>
    {% endfor %}
    {% if not issues %}
    <div class="issue medium"><h3>No critical issues detected!</h3><p>Your data looks clean for causal modeling.</p></div>
    {% endif %}
</body>
</html>
"""

def generate_report(issues, preset="fraud"):
    template = Template(HTML_TEMPLATE)
    html = template.render(issues=issues, preset=preset)
    path = "causalguard_report.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open(f"file://{os.path.abspath(path)}")