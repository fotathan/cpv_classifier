"""
Smoke test: verify the classification pipeline (cosine similarity, per-code
aggregation, div4 rollup, threshold filtering) on a tiny synthetic embedding
matrix. We mock the embeddings so this can run without the real 420 MB model.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
from app import score_codes, aggregate_to_div4

LANG_COLUMNS = [
    "BG", "CS", "DA", "DE", "EL", "EN", "ES", "ET", "FI", "FR",
    "GA", "HR", "HU", "IT", "LT", "LV", "MT", "NL", "PL", "PT",
    "RO", "SK", "SL", "SV",
]


def fake_embed(text: str, dim: int = 16, seed_offset: int = 0) -> np.ndarray:
    """Hash text to a deterministic L2-normalised vector."""
    rng = np.random.default_rng(abs(hash(text)) % (2**32) + seed_offset)
    v = rng.standard_normal(dim).astype(np.float32)
    return v / np.linalg.norm(v)


def main() -> None:
    df = pd.read_csv("data/cpv_full.csv", encoding="utf-8-sig", dtype=str).fillna("")
    df["code_clean"] = df["CODE"].str.split("-").str[0]
    df["div4"] = df["code_clean"].str[:4] + "0000"

    # Take a small slice to keep the test fast
    sample = df.head(200).copy()

    codes: list[str] = []
    langs: list[str] = []
    vecs: list[np.ndarray] = []
    for _, row in sample.iterrows():
        for lang in LANG_COLUMNS:
            desc = row[lang].strip()
            if not desc:
                continue
            codes.append(row["code_clean"])
            langs.append(lang)
            vecs.append(fake_embed(desc))

    matrix = np.vstack(vecs).astype(np.float32)
    print(f"Built mock matrix: {matrix.shape}, {len(set(codes))} unique codes")

    # Pretend the query is the EN description of a known row -> sim should be 1.0
    target_idx = 5
    target_code = sample.iloc[target_idx]["code_clean"]
    target_div = sample.iloc[target_idx]["div4"]
    query_text = sample.iloc[target_idx]["EN"]
    qv = fake_embed(query_text)

    print(f"\nQuery (EN of row {target_idx}): {query_text!r}")
    print(f"Expected best code: {target_code} (div4: {target_div})")

    # Test 1: per-code scoring + aggregation
    scored = score_codes(qv, matrix, codes, langs, aggregator="max")
    top = scored.sort_values("sim", ascending=False).head(5)
    print("\nTop 5 per-code matches (mock):")
    print(top.to_string(index=False))
    assert top.iloc[0]["code"] == target_code, "Best per-code match should be the exact target"
    assert abs(top.iloc[0]["sim"] - 1.0) < 1e-5, "Self-match similarity should be ~1.0"
    print("✓ Per-code scoring picks the exact target with similarity ≈ 1.0")

    # Test 2: div4 rollup
    rolled = aggregate_to_div4(scored, sample)
    print("\nTop 5 div4 rollups:")
    print(rolled.head(5).to_string(index=False))
    assert rolled.iloc[0]["div4"] == target_div, "Best div4 should contain the target code"
    print("✓ Div4 rollup correctly bubbles up the strongest descendant")

    # Test 3: deterministic — same input twice gives identical results
    rolled2 = aggregate_to_div4(score_codes(qv, matrix, codes, langs, aggregator="max"), sample)
    pd.testing.assert_frame_equal(rolled.reset_index(drop=True), rolled2.reset_index(drop=True))
    print("✓ Pipeline is deterministic")

    # Test 4: threshold filtering yields a subset of the CSV's div4 codes
    above = rolled[rolled["score"] >= 0.5]
    valid_div4s = set(df["div4"].unique())
    assert set(above["div4"]).issubset(valid_div4s), "All output div4 codes must exist in the catalogue"
    print(f"✓ All {len(above)} returned div4 codes are real CPV divisions (no hallucination)")

    print("\n✅ All smoke tests passed.")


if __name__ == "__main__":
    main()
