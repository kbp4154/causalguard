# CausalGuard 🛡️

**The data quality guardian for causal inference & fraud detection**  
*Catch flipped labels, temporal leaks, and causal biases before they destroy your model — in 5 lines of code.*

[![PyPI version](https://badge.fury.io/py/causalguard.svg)](https://badge.fury.io/py/causalguard) [![Downloads](https://static.pepy.tech/badge/causalguard/month)](https://pepy.tech/project/causalguard) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Stars](https://img.shields.io/github/stars/kbp4154/causalguard?style=social)](https://github.com/kbp4154/causalguard)

https://github.com/user-attachments/assets/4e5e3c13-8e0f-4e9e-9c3e-2f3a4b6d7e8f

### The bugs that quietly kill 40–60% of fraud & marketing models:

- `first_purchase_ts` < `signup_ts` in 38% of rows  
- Flipped fraud labels from bad annotation  
- Treatment applied before user even existed  
- Collider bias opening backdoor paths  
- Silent distribution shift in causal features  

**I’ve personally lost months and millions because of these. Never again.**

### One-liner that saves you:

```python
from causalguard import CausalGuard

report = CausalGuard(preset="fraud").scan(df)
report.show()  # → instant beautiful HTML report with fixes
