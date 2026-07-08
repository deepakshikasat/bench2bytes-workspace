import sys
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))
from src.features import compute_tox_features

df = pd.read_csv(root / "data/compound_tox.csv")
features = df.apply(compute_tox_features, axis=1, result_type="expand")
out = pd.concat([df[["compound_id", "compound_class"]], features], axis=1)
out.to_csv(root / "outputs/tox_features.csv", index=False)
print(out.head())
