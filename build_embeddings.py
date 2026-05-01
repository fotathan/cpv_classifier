"""
Precompute multilingual embeddings for the entire CPV catalogue.

Run this once locally before deploying:

    python build_embeddings.py

It produces ``data/cpv_embeddings.npz`` containing one embedding per
(CPV code, language) pair, L2-normalised so cosine similarity reduces to
a dot product at query time.

We embed each language separately rather than concatenating all 24 into
one giant string per code. This gives much sharper matches: a Greek
tender hits the Greek description strongly, a Polish tender hits the
Polish description strongly, etc. With ~9,454 codes × 24 languages we
get ~227k vectors of 768 dims (~700 MB float32, ~350 MB float16). The
matrix multiply at query time is still well under 100 ms on CPU.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer

DATA_DIR = Path(__file__).parent / "data"
CSV_PATH = DATA_DIR / "cpv_full.csv"
OUT_PATH = DATA_DIR / "cpv_embeddings.npz"
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

LANG_COLUMNS = [
    "BG", "CS", "DA", "DE", "EL", "EN", "ES", "ET", "FI", "FR",
    "GA", "HR", "HU", "IT", "LT", "LV", "MT", "NL", "PL", "PT",
    "RO", "SK", "SL", "SV",
]


def main() -> None:
    df = pd.read_csv(CSV_PATH, encoding="utf-8-sig", dtype=str).fillna("")
    df["code_clean"] = df["CODE"].str.split("-").str[0]

    # Build flat list of (code, lang, text) triples, dropping empty descriptions
    codes: list[str] = []
    langs: list[str] = []
    texts: list[str] = []
    for _, row in df.iterrows():
        for lang in LANG_COLUMNS:
            desc = row[lang].strip()
            if not desc:
                continue
            codes.append(row["code_clean"])
            langs.append(lang)
            texts.append(desc)

    print(f"Total descriptions to embed: {len(texts):,}")

    print(f"Loading model {MODEL_NAME}…")
    model = SentenceTransformer(MODEL_NAME)

    print("Encoding (this takes a few minutes on CPU, seconds on GPU)…")
    matrix = model.encode(
        texts,
        batch_size=64,
        normalize_embeddings=True,  # so cosine == dot product later
        show_progress_bar=True,
        convert_to_numpy=True,
    ).astype(np.float32)

    print(f"Matrix shape: {matrix.shape}, dtype: {matrix.dtype}")
    print(f"Approx size on disk: {matrix.nbytes / 1024**2:.1f} MB")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        OUT_PATH,
        matrix=matrix,
        codes=np.array(codes),
        langs=np.array(langs),
    )
    print(f"Saved -> {OUT_PATH}")


if __name__ == "__main__":
    main()
