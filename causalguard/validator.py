import pandas as pd
from typing import Literal
from .detectors import (
    detect_temporal_leakage,
    detect_label_noise,
    detect_dag_violations
)

class CausalGuard:
    def __init__(self, preset: Literal["fraud", "marketing", "general"] = "fraud"):
        self.preset = preset
        self.issues = []

    def scan(self, data: pd.DataFrame, target: str = None):
        self.issues = []
        self.issues += detect_temporal_leakage(data)
        self.issues += detect_label_noise(data, target)
        self.issues += detect_dag_violations(data, preset=self.preset)
        return self

    def show(self):
        from .reporter import generate_report
        generate_report(self.issues, preset=self.preset)