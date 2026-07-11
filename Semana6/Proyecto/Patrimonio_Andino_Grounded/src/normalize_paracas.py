from __future__ import annotations

from typing import Any, Dict


def normalize_paracas_record(raw: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a curated Paracas raw record into the unified schema."""

    source_record_id = raw["source_record_id"]
    canonical_id = raw.get("canonical_id", source_record_id.lower().replace(".", "_"))

    return {
        "record_id": raw.get("record_id", f"par_{canonical_id}_{raw.get('modality_type', 'photo')}_01"),
        "canonical_id": canonical_id,
        "source": "paracas",
        "source_record_id": source_record_id,
        "modality_type": raw.get("modality_type", "photo"),
        "title": raw.get("title"),
        "description": raw.get("description"),
        "object_type": raw.get("object_type", "Textile"),
        "culture": raw.get("culture", "Paracas"),
        "date_display": raw.get("date_display"),
        "date_begin": raw.get("date_begin"),
        "date_end": raw.get("date_end"),
        "medium": raw.get("medium"),
        "provenance": raw.get("provenance"),
        "institution": raw.get("institution"),
        "collection": raw.get("collection"),
        "rights": raw.get("rights", "metadata public"),
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
