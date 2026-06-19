#!/usr/bin/env python3
"""Validate Reddit cybersecurity Thresh annotation batch files."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data" / "reddit_cybersecurity_hehe_streams"
REPORT_PATH = DATA_DIR / "validation_report.json"

BATCH_FILES = [
    DATA_DIR / "reddit_body_part_1_10_hits.json",
    DATA_DIR / "reddit_body_part_2_10_hits.json",
    DATA_DIR / "reddit_body_part_3_10_hits.json",
    DATA_DIR / "reddit_body_part_4_10_hits.json",
]

EXPECTED_THREAD_ID = "1tp7mcv"
EXPECTED_TOTAL_HITS = 40
EXPECTED_HITS_PER_FILE = 10
EXPECTED_SENTENCE_NUMBERS = list(range(1, 194))
REQUIRED_ROW_FIELDS = {"id", "context", "source", "metadata"}
REQUIRED_METADATA_FIELDS = {
    "thread_id",
    "hit_index",
    "sentence_numbers",
    "sentence_range",
    "group_size",
    "character_count",
}
SENTENCE_NUMBER_RE = re.compile(r"\[(\d+)\]")


@dataclass
class ValidationState:
    errors: list[str]
    warnings: list[str]
    file_summaries: list[dict[str, Any]]
    sentence_numbers: list[int]
    total_hits: int = 0


def load_json_file(path: Path, errors: list[str]) -> Any | None:
    """Load one JSON file, recording parse errors instead of raising."""
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        errors.append(f"{path}: file is missing")
    except json.JSONDecodeError as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
    return None


def validate_hit(
    hit: Any,
    path: Path,
    row_index: int,
    state: ValidationState,
) -> None:
    """Validate one annotation hit and collect sentence numbers."""
    location = f"{path.name} row {row_index}"

    if not isinstance(hit, dict):
        state.errors.append(f"{location}: row is not an object")
        return

    missing_fields = sorted(REQUIRED_ROW_FIELDS - set(hit))
    if missing_fields:
        state.errors.append(f"{location}: missing required fields {missing_fields}")

    source = hit.get("source")
    if not isinstance(source, str) or not source.strip():
        state.errors.append(f"{location}: source must be a non-empty string")
        source_numbers: list[int] = []
    else:
        source_numbers = [int(match) for match in SENTENCE_NUMBER_RE.findall(source)]
        if not source_numbers:
            state.errors.append(f"{location}: source has no visible [n] numbering")
        state.sentence_numbers.extend(source_numbers)

    metadata = hit.get("metadata")
    if not isinstance(metadata, dict):
        state.errors.append(f"{location}: metadata must be an object")
        return

    missing_metadata = sorted(REQUIRED_METADATA_FIELDS - set(metadata))
    if missing_metadata:
        state.errors.append(
            f"{location}: missing metadata fields {missing_metadata}"
        )

    if metadata.get("thread_id") != EXPECTED_THREAD_ID:
        state.errors.append(
            f"{location}: metadata.thread_id is {metadata.get('thread_id')!r}, "
            f"expected {EXPECTED_THREAD_ID!r}"
        )

    metadata_numbers = metadata.get("sentence_numbers")
    if not isinstance(metadata_numbers, list) or not all(
        isinstance(number, int) for number in metadata_numbers
    ):
        state.errors.append(f"{location}: metadata.sentence_numbers must be a list of integers")
    elif source_numbers and metadata_numbers != source_numbers:
        state.errors.append(
            f"{location}: metadata.sentence_numbers does not match source numbering"
        )


def validate_batch_file(path: Path, state: ValidationState) -> None:
    """Validate one batch file."""
    data = load_json_file(path, state.errors)
    if data is None:
        return

    if not isinstance(data, list):
        state.errors.append(f"{path.name}: top-level JSON must be a list")
        return

    hit_count = len(data)
    state.total_hits += hit_count
    if hit_count != EXPECTED_HITS_PER_FILE:
        state.errors.append(
            f"{path.name}: has {hit_count} hits, expected {EXPECTED_HITS_PER_FILE}"
        )

    for row_index, hit in enumerate(data, start=1):
        validate_hit(hit, path, row_index, state)

    state.file_summaries.append(
        {
            "file": path.name,
            "hit_count": hit_count,
            "valid_json": True,
        }
    )


def validate_sentence_sequence(state: ValidationState) -> None:
    """Validate full sentence-number coverage across all files."""
    observed = state.sentence_numbers
    observed_set = set(observed)
    expected_set = set(EXPECTED_SENTENCE_NUMBERS)

    missing = sorted(expected_set - observed_set)
    duplicates = sorted(
        number for number in observed_set if observed.count(number) > 1
    )
    unexpected = sorted(observed_set - expected_set)

    if missing:
        state.errors.append(f"missing sentence numbers: {missing}")
    if duplicates:
        state.errors.append(f"duplicate sentence numbers: {duplicates}")
    if unexpected:
        state.errors.append(f"unexpected sentence numbers: {unexpected}")
    if sorted(observed_set) != EXPECTED_SENTENCE_NUMBERS:
        state.errors.append("sentence numbers are not continuous from 1 to 193")


def build_report(state: ValidationState) -> dict[str, Any]:
    """Build a machine-readable validation report."""
    observed_unique = sorted(set(state.sentence_numbers))
    return {
        "dataset": "reddit_cybersecurity_hehe_streams",
        "valid": not state.errors,
        "expected_thread_id": EXPECTED_THREAD_ID,
        "expected_total_hits": EXPECTED_TOTAL_HITS,
        "actual_total_hits": state.total_hits,
        "expected_hits_per_file": EXPECTED_HITS_PER_FILE,
        "file_summaries": state.file_summaries,
        "expected_sentence_number_min": EXPECTED_SENTENCE_NUMBERS[0],
        "expected_sentence_number_max": EXPECTED_SENTENCE_NUMBERS[-1],
        "actual_unique_sentence_count": len(observed_unique),
        "actual_sentence_number_min": observed_unique[0] if observed_unique else None,
        "actual_sentence_number_max": observed_unique[-1] if observed_unique else None,
        "missing_sentence_numbers": sorted(set(EXPECTED_SENTENCE_NUMBERS) - set(observed_unique)),
        "duplicate_sentence_numbers": sorted(
            number for number in set(state.sentence_numbers) if state.sentence_numbers.count(number) > 1
        ),
        "errors": state.errors,
        "warnings": state.warnings,
    }


def print_summary(report: dict[str, Any]) -> None:
    """Print a compact human-readable validation summary."""
    status = "PASSED" if report["valid"] else "FAILED"
    print(f"Validation {status}")
    print(f"Dataset: {report['dataset']}")
    print(f"Total hits: {report['actual_total_hits']} / {report['expected_total_hits']}")
    print(
        "Sentence numbers: "
        f"{report['actual_sentence_number_min']}-{report['actual_sentence_number_max']} "
        f"({report['actual_unique_sentence_count']} unique)"
    )
    print("Files:")
    for summary in report["file_summaries"]:
        print(f"  - {summary['file']}: {summary['hit_count']} hits")

    if report["errors"]:
        print("Errors:")
        for error in report["errors"]:
            print(f"  - {error}")


def main() -> int:
    """Run validation and write validation_report.json."""
    state = ValidationState(
        errors=[],
        warnings=[],
        file_summaries=[],
        sentence_numbers=[],
    )

    for path in BATCH_FILES:
        validate_batch_file(path, state)

    if state.total_hits != EXPECTED_TOTAL_HITS:
        state.errors.append(
            f"total hit count is {state.total_hits}, expected {EXPECTED_TOTAL_HITS}"
        )

    validate_sentence_sequence(state)

    report = build_report(state)
    REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print_summary(report)
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
