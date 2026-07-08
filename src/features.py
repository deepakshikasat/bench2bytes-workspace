from __future__ import annotations
import pandas as pd

REQUIRED = ["alt_fold_change", "ast_fold_change", "ggt_fold_change"]

def compute_tox_features(row: pd.Series) -> dict:
    """Return toxicity summary features for one compound row.

    Example:
        >>> compute_tox_features(pd.Series({"alt_fold_change": 4, "ast_fold_change": 3.5, "ggt_fold_change": 1.2}))["tox_severity"]
        'moderate'
    """
    missing = [c for c in REQUIRED if c not in row]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    values = [float(row[c]) for c in REQUIRED]
    max_fc = max(values)
    return {
        "max_fold_change": max_fc,
        "n_elevated_markers": sum(v > 3 for v in values),
        "tox_severity": "none" if max_fc < 2 else "mild" if max_fc < 3 else "moderate" if max_fc <= 5 else "severe",
        "is_high_risk": float(row["alt_fold_change"]) > 3 and float(row["ast_fold_change"]) > 3,
    }
