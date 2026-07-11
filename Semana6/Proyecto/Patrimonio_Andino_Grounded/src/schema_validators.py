from __future__ import annotations

from typing import Any, Dict, Iterable, List


REQUIRED_TOP_LEVEL = [
    "record_id",
    "canonical_id",
    "source",
    "source_record_id",
    "modality_type",
    "title",
    "description",
    "object_type",
    "culture",
    "date_display",
    "x_s",
    "x_t",
    "x_c",
    "qa_flags",
]


def validate_record(record: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for key in REQUIRED_TOP_LEVEL:
        if key not in record:
            errors.append(f"Missing key: {key}")
    if record.get("source") not in {"open_khipu", "paracas"}:
        errors.append("Invalid source")
    if record.get("modality_type") not in {"photo", "xrf_map", "diagram", "no_image"}:
        errors.append("Invalid modality_type")
    return errors


def validate_records(records: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
    report: List[Dict[str, Any]] = []
    for record in records:
        report.append({
            "record_id": record.get("record_id"),
            "errors": validate_record(record),
            "is_valid": len(validate_record(record)) == 0,
        })
    return report
