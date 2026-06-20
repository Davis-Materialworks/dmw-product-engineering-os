#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "adobe_xd_design_description",
    "expected_design_system",
    "expected_component_inventory",
    "expected_architecture",
    "expected_accessibility_findings",
    "expected_code_quality_metrics",
]

CATEGORY_WEIGHTS = {
    "adobe_xd_design_description": 15,
    "expected_design_system": 18,
    "expected_component_inventory": 20,
    "expected_architecture": 18,
    "expected_accessibility_findings": 14,
    "expected_code_quality_metrics": 15,
}


def flatten(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def field_completeness(benchmark: dict[str, Any], field: str) -> float:
    value = benchmark.get(field)
    if value in (None, "", [], {}):
        return 0.0
    text = flatten(value).strip()
    if len(text) < 80 and field != "expected_accessibility_findings":
        return 0.6
    if field == "expected_component_inventory":
        components = value if isinstance(value, list) else []
        if len(components) < 3:
            return 0.65
        required = {"component", "industry", "accessibility", "performance", "testing"}
        per_key_scores = []
        for component in components:
            matched_keys = sum(1 for key in required if key in component)
            per_key_scores.append(matched_keys / len(required))
        return sum(per_key_scores) / len(per_key_scores) if per_key_scores else 0.0
    return 1.0


def score_reference_benchmark(benchmark: dict[str, Any]) -> int:
    score = 0.0
    for field, weight in CATEGORY_WEIGHTS.items():
        score += weight * field_completeness(benchmark, field)
    return round(score)


def keyword_score(expected: Any, candidate: Any) -> float:
    expected_text = flatten(expected).lower()
    candidate_text = flatten(candidate).lower()
    terms = sorted({term.strip(".,:;()[]{}") for term in expected_text.split() if len(term.strip(".,:;()[]{}")) >= 4})
    if not terms:
        return 0.0  # empty terms: no keywords to match — return 0, not 1.0, to avoid conflating empty with perfect
    matched = sum(1 for term in terms if term in candidate_text)
    return matched / len(terms)


def score_candidate(benchmark: dict[str, Any], candidate: dict[str, Any]) -> int:
    score = 0.0
    for field, weight in CATEGORY_WEIGHTS.items():
        score += weight * keyword_score(benchmark.get(field), candidate.get(field, {}))
    return round(score)


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Score DMW Product Engineering OS benchmark outputs.")
    parser.add_argument("--benchmarks-dir", default="benchmarks", help="Directory containing */benchmark.json files.")
    parser.add_argument("--candidate-dir", help="Optional directory containing <benchmark-id>.json generated outputs to score.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    root = Path(args.benchmarks_dir)
    candidate_root = Path(args.candidate_dir) if args.candidate_dir else None
    results = []

    for benchmark_file in sorted(p for p in root.glob("*/benchmark.json") if not p.parent.name[:2].isdigit()):
        benchmark = load_json(benchmark_file)
        benchmark_id = benchmark.get("id", benchmark_file.parent.name)
        missing = [field for field in REQUIRED_TOP_LEVEL if field not in benchmark]
        if missing:
            print(f"WARNING: {benchmark_id} is missing required fields: {', '.join(missing)}", file=sys.stderr)
            score = 0
            mode = "invalid"
        elif candidate_root:
            candidate_file = candidate_root / f"{benchmark_id}.json"
            if candidate_file.exists():
                score = score_candidate(benchmark, load_json(candidate_file))
                mode = "candidate"
            else:
                score = 0
                mode = "missing-candidate"
        else:
            score = score_reference_benchmark(benchmark)
            mode = "benchmark-definition"
        results.append({"benchmark": benchmark_id, "score": score, "mode": mode})

    if args.json:
        print(json.dumps({"results": results}, indent=2))
    else:
        for result in results:
            print(f"{result['benchmark']}: {result['score']}/100 ({result['mode']})")
    return 0 if all(result["score"] >= 90 for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
