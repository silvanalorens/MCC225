from __future__ import annotations

from typing import Dict, Iterable, List


def attribute_coverage(record: dict, generated_text: str) -> float:
    xs = record.get("x_s", {})
    attrs = [
        str(xs.get("material") or "").lower(),
        str(xs.get("pattern_type") or "").lower(),
        str(record.get("provenance") or "").lower(),
        str(record.get("culture") or "").lower(),
    ]
    attrs = [a for a in attrs if a]
    if not attrs:
        return 0.0
    hits = sum(1 for attr in attrs if attr in generated_text.lower())
    return hits / len(attrs)


def retrieval_support(output: dict) -> float:
    trace = " ".join(output.get("traza_evidencia", []))
    return 1.0 if "neighbors:" in trace else 0.0


def hallucination_proxy(record: dict, generated_text: str) -> float:
    banned = [
        "exactamente",
        "sin duda",
        "con certeza absoluta",
    ]
    penalty = sum(1 for token in banned if token in generated_text.lower())
    return min(1.0, penalty / max(1, len(banned)))


def evaluate_outputs(records: List[dict], outputs: List[dict]) -> List[dict]:
    rows: List[dict] = []
    for record, output in zip(records, outputs):
        full_text = " ".join(
            [
                output.get("caption_factual", ""),
                output.get("nota_tecnico_curatorial", ""),
                output.get("nota_comparativa", ""),
                output.get("incertidumbre", ""),
            ]
        )
        rows.append({
            "record_id": record["record_id"],
            "attribute_coverage": attribute_coverage(record, full_text),
            "retrieval_support": retrieval_support(output),
            "hallucination_proxy": hallucination_proxy(record, full_text),
        })
    return rows
