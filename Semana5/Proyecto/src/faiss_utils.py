from __future__ import annotations
import numpy as np

def build_index(vectors: np.ndarray):
    import faiss
    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors.astype('float32'))
    return index

def search(index, query_vectors: np.ndarray, k: int = 5):
    scores, idxs = index.search(query_vectors.astype('float32'), k)
    return scores, idxs
