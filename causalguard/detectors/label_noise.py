from typing import List, Dict
import pandas as pd

def detect_label_noise(df: pd.DataFrame, target: str = None) -> List[Dict]:
    issues = []
    if target and target in df.columns:
        label_rate = df[target].mean()
        if label_rate < 0.001 or label_rate > 0.3:
            issues.append({
                "type": "suspicious_label_distribution",
                "severity": "HIGH",
                "message": f"Label '{target}' has extreme rate: {label_rate:.4f}",
                "suggestion": "Check for label leakage or annotation errors"
            })
    return issues