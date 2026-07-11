from __future__ import annotations

import json
from typing import Dict

from src.evidence_bundle import build_evidence_bundle


def grounded_prompt(record: Dict, retriever: Dict, top_k: int = 3) -> str:
    ev = build_evidence_bundle(record, retriever, top_k=top_k)
    prompt = f"""
Usa solo la evidencia disponible.
No inventes cronología, procedencia, materialidad ni significado.
Separa observación, metadatos e inferencia.
Explicita incertidumbre.

[OBJETO]
id: {ev["id"]}
title: {ev["title"]}
object_type: {ev["object_type"]}

[BASELINE]
{ev["caption_base"]}

[ESTRUCTURA]
{json.dumps(ev["x_s"], ensure_ascii=False)}

[TEXTO]
{json.dumps(ev["x_t"], ensure_ascii=False)}

[CONTEXTO]
{json.dumps(ev["x_c"], ensure_ascii=False)}

[PLAUDIBILIDAD]
{json.dumps(ev["plausibility"], ensure_ascii=False)}

[VECINOS RECUPERADOS]
{json.dumps(ev["neighbors"], ensure_ascii=False)}

Escribe:
1) caption factual
2) nota técnico-curatorial
3) nota comparativa
4) línea de incertidumbre
5) traza de evidencia
""".strip()
    return prompt


def grounded_generate_template(record: Dict, retriever: Dict, top_k: int = 3) -> Dict:
    ev = build_evidence_bundle(record, retriever, top_k=top_k)
    xs = ev["x_s"] or {}
    xc = ev["x_c"] or {}
    neighbors = ev["neighbors"] or []
    neighbor_titles = "; ".join([n["title"] for n in neighbors[:2]]) or "sin vecinos suficientemente cercanos"

    caption = ev["caption_base"]

    note = (
        f"{record['title']} se documenta como {record['object_type'].lower()} "
        f"asociado a {record['culture']}. "
        f"La ficha disponible sitúa la procedencia en {record.get('provenance') or 'un contexto no especificado'} "
        f"y aporta como soporte material {record.get('medium') or 'material no especificado'}. "
        f"Los atributos estructurales disponibles incluyen patrón={xs.get('pattern_type')}, "
        f"material={xs.get('material')}, análisis={xs.get('analysis_type')}, "
        f"jerarquía={xs.get('hierarchy')}, cordeles={xs.get('cord_count')}."
    )

    comparative = (
        f"La recuperación sugiere afinidad parcial con {neighbor_titles}. "
        f"Esa proximidad es útil para comparación curatorial, pero no demuestra identidad de origen, función o cronología."
    )

    uncertainty = (
        "La evidencia actual no permite afirmar una lectura funcional o simbólica cerrada, y cualquier interpretación debe mantenerse provisional."
    )

    evidence_trace = [
        f"baseline: {ev['caption_base']}",
        f"provenance: {record.get('provenance')}",
        f"material: {record.get('medium')}",
        f"plausibility: {ev['plausibility']['plausibility_label']} ({ev['plausibility']['plausibility_score']:.2f})",
        f"neighbors: {neighbor_titles}",
    ]

    return {
        "caption_factual": caption,
        "nota_tecnico_curatorial": note,
        "nota_comparativa": comparative,
        "incertidumbre": uncertainty,
        "traza_evidencia": evidence_trace,
    }
