from __future__ import annotations

from typing import Dict, List, Optional

from src.retrieval import record_to_query, retrieve_neighbors_tfidf


def make_caption_baseline(record: dict) -> str:
    if record["source"] == "open_khipu":
        xs = record.get("x_s", {})
        return (
            f"Khipu con {xs.get('cord_count', 'N/A')} cordeles, "
            f"{xs.get('unique_colors', 'N/A')} colores registrados y procedencia {record.get('provenance') or 'desconocida'}."
        )
    if record["modality_type"] == "xrf_map":
        return "Visualización técnica de análisis XRF asociada a una muestra textil Paracas."
    return f"{record.get('object_type', 'Objeto')} de la cultura {record.get('culture', 'N/A')} con descripción catalográfica disponible."


def compute_plausibility(record: dict) -> dict:
    xs = record.get("x_s", {})
    score = 0.0
    if xs.get("material"):
        score += 0.25
    if xs.get("pattern_type"):
        score += 0.25
    if xs.get("analysis_type") or xs.get("cord_count"):
        score += 0.25
    if record.get("provenance"):
        score += 0.25
    label = "alta" if score >= 0.75 else "media" if score >= 0.5 else "baja"
    return {
        "plausibility_score": score,
        "plausibility_label": label,
    }


def build_evidence_bundle(record: dict, retriever: Dict[str, object], top_k: int = 3) -> dict:
    query = record_to_query(record)
    neighbors = [
        n for n in retrieve_neighbors_tfidf(query, retriever, top_k=top_k + 1)
        if n["canonical_id"] != record["canonical_id"]
    ][:top_k]
    return {
        "id": record["record_id"],
        "title": record["title"],
        "object_type": record["object_type"],
        "caption_base": make_caption_baseline(record),
        "x_s": record.get("x_s", {}),
        "x_t": record.get("x_t", {}),
        "x_c": record.get("x_c", {}),
        "plausibility": compute_plausibility(record),
        "neighbors": neighbors,
    }
