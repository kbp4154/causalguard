from typing import List, Dict
import pandas as pd

COMMON_LEAKS = [
    ("first_purchase_ts", "signup_ts"),
    ("transaction_time", "account_created_at"),
    ("order_date", "user_registration_date"),
    ("click_ts", "impression_ts"),
]

def detect_temporal_leakage(df: pd.DataFrame) -> List[Dict]:
    issues = []
    for future, past in COMMON_LEAKS:
        if future in df.columns and past in df.columns:
            rate = (df[future] < df[past]).mean()
            if rate > 0.005:
                issues.append({
                    "type": "temporal_leakage",
                    "severity": "CRITICAL",
                    "message": f"{future} occurs before {past} in {rate:.1%} of rows",
                    "suggestion": f"Ensure {future} is derived only from data before {past}"
                })
    return issues