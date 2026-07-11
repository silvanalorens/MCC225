from __future__ import annotations

from typing import Any, Dict


def normalize_open_khipu_record(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Normaliza un registro sin procesar de Open Khipu seleccionado según el esquema unificado."""

    source_record_id = raw["source_record_id"]
    canonical_id = source_record_id.lower()

    return {
        "record_id": f"okr_{canonical_id}_view_01",
        "canonical_id": canonical_id,
        "source": "open_khipu",
        "source_record_id": source_record_id,
        "modality_type": raw.get("modality_type", "no_image"),
        "title": raw.get("title"),
        "description": raw.get("description"),
        "object_type": raw.get("object_type", "Khipu"),
        "culture": raw.get("culture", "Andean"),
        "date_display": raw.get("date_display"),
        "date_begin": raw.get("date_begin"),
        "date_end": raw.get("date_end"),
        "medium": raw.get("medium", "fibra textil anudada"),
        "provenance": raw.get("provenance"),
        "institution": raw.get("institution"),
        "collection": raw.get("collection", "OKR"),
        "rights": raw.get("rights", "open metadata"),
        "language": raw.get("language", "es"),
        "tags": raw.get("tags", []),
        "image_path": raw.get("image_path"),
        "image_url": raw.get("image_url"),
        "thumbnail_path": raw.get("thumbnail_path"),
        "split": raw.get("split", "train"),
        "x_s": raw.get("x_s", {}),
        "x_t": raw.get("x_t", {}),
        "x_c": raw.get("x_c", {}),
        "qa_flags": raw.get("qa_flags", {}),
    }
