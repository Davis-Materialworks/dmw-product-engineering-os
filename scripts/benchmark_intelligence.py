#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any


CATEGORIES = [
    "design_understanding",
    "ux_quality",
    "accessibility",
    "architecture",
    "design_system",
    "maintainability",
    "performance",
    "security",
    "testability",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def flatten(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(flatten(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(flatten(v) for v in value)
    return str(value)


def keyword_match_score(expected: Any, actual: Any) -> int:
    expected_text = flatten(expected).lower()
    actual_text = flatten(actual).lower()
    tokens = sorted({t.strip(".,:;()[]{}") for t in expected_text.split() if len(t.strip(".,:;()[]{}")) >= 4})
    if not tokens:
        return 0  # empty tokens: no keywords to match — return 0, not 100, to avoid conflating empty with perfect
    matched = sum(1 for token in tokens if token in actual_text)
    return round((matched / len(tokens)) * 100)


def score_project(project_dir: Path, actual_dir: Path | None = None) -> dict[str, Any]:
    benchmark = load_json(project_dir / "benchmark.json")

    # Schema B detection — this script only handles Schema A
    if "adobe_xd_design_description" in benchmark or "expected_design_system" in benchmark:
        print(f"WARNING: {project_dir.name} appears to be Schema B — skipping", file=sys.stderr)
        return {
            "project": project_dir.name,
            "title": benchmark.get("title", ""),
            "overall": 0,
            "scores": {},
            "status": "unscored-schema-b",
        }

    actual_path = actual_dir / f"{project_dir.name}.json" if actual_dir else None
    if not actual_path or not actual_path.exists():
        return {
            "project": project_dir.name,
            "title": benchmark.get("title", ""),
            "overall": 0,
            "scores": {},
            "status": "needs-actual-output",
            "previous_score": None,
            "delta": None,
            "trend": "new",
        }

    actual = load_json(actual_path)
    expected = benchmark.get("expected", {})

    category_scores = {}
    category_scores["design_understanding"] = keyword_match_score(
        benchmark.get("design_description", ""), actual
    )
    category_scores["ux_quality"] = keyword_match_score(
        expected.get("ux", {}), actual.get("ux", {})
    )
    category_scores["accessibility"] = keyword_match_score(
        expected.get("accessibility", {}), actual.get("accessibility", {})
    )
    category_scores["architecture"] = keyword_match_score(
        expected.get("architecture", {}), actual.get("architecture", {})
    )
    category_scores["design_system"] = keyword_match_score(
        expected.get("design_system", {}), actual.get("design_system", {})
    )
    code_quality = expected.get("code_quality", {})
    category_scores["maintainability"] = keyword_match_score(
        code_quality, actual.get("code_quality", {})
    )
    category_scores["performance"] = keyword_match_score(
        code_quality.get("performance", []), actual.get("code_quality", {})
    )
    category_scores["security"] = keyword_match_score(
        expected.get("security", {}), actual.get("security", {})
    )
    category_scores["testability"] = keyword_match_score(
        code_quality.get("tests", []), actual.get("code_quality", {})
    )
    overall = round(sum(category_scores.values()) / len(category_scores))

    return {
        "project": project_dir.name,
        "title": benchmark["title"],
        "overall": overall,
        "scores": category_scores,
        "status": "pass" if overall >= 90 else "needs-improvement",
    }


def previous_score(history_dir: Path, project: str) -> int | None:
    if not history_dir.exists():
        return None
    scores = []
    for result_file in sorted(history_dir.glob("*/scores.json")):
        data = load_json(result_file)
        for result in data.get("results", []):
            if result.get("project") == project:
                scores.append(result["overall"])
    return scores[-1] if scores else None


def write_report(results_dir: Path, report_dir: Path, results: list[dict[str, Any]]) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    average = round(sum(r["overall"] for r in results) / len(results)) if results else 0
    lines = [
        "# Benchmark Report",
        "",
        f"Average score: {average}/100",
        "",
        "| Project | Score | Status |",
        "| --- | ---: | --- |",
    ]
    for result in results:
        lines.append(f"| {result['project']} | {result['overall']} | {result['status']} |")
    lines.extend([
        "",
        "## Lessons Feed",
        "",
        "- Promote repeated score failures into `knowledge/evolution/`.",
        "- Add benchmark cases when new XD patterns or failures appear.",
        "- Treat regressions as failures until explained by intentional benchmark changes.",
    ])
    (report_dir / "benchmark-report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run DMW Product Engineering OS benchmark intelligence scoring.")
    parser.add_argument("--benchmarks-dir", default="benchmarks")
    parser.add_argument("--actual-dir", help="Directory containing actual output JSON files named <project>.json")
    parser.add_argument("--results-dir", default=None, help="Results directory. Defaults to results/<today>.")
    parser.add_argument("--reports-dir", default="reports")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    benchmarks_dir = Path(args.benchmarks_dir)
    actual_dir = Path(args.actual_dir) if args.actual_dir else None
    results_dir = Path(args.results_dir) if args.results_dir else Path("results") / date.today().isoformat()
    reports_dir = Path(args.reports_dir)

    projects = sorted(p for p in benchmarks_dir.iterdir() if p.is_dir() and p.name[:2].isdigit() and (p / "benchmark.json").exists())
    results = []
    for project in projects:
        result = score_project(project, actual_dir)
        prior = previous_score(Path("results"), result["project"])
        result["previous_score"] = prior
        result["delta"] = None if prior is None else result["overall"] - prior
        result["trend"] = "new" if prior is None else ("improved" if result["delta"] > 0 else "regressed" if result["delta"] < 0 else "unchanged")
        results.append(result)

    results_dir.mkdir(parents=True, exist_ok=True)
    output = {"results": results}
    (results_dir / "scores.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    write_report(results_dir, reports_dir, results)

    if args.json:
        print(json.dumps(output, indent=2))
    else:
        for result in results:
            print(f"{result['project']}: {result['overall']}/100 ({result['trend']})")
    return 0 if all(r["overall"] >= 90 for r in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
