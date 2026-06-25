# Cybersecurity Readability Annotation Template

Span-level human-evaluation materials for studying why cybersecurity discussions are difficult for non-expert readers to understand.

This repository contains a Thresh annotation template, an annotation guideline, a pilot Reddit cybersecurity dataset, provenance notes, and validation tooling. The project is designed around a core research question: which words, phrases, acronyms, platform references, legal terms, and implicit knowledge references create comprehension barriers in cybersecurity discourse?

## Research Motivation

Cybersecurity discussions often combine technical concepts, hacker-culture slang, platform-specific references, legal terminology, and unstated background knowledge. Standard readability measures do not capture these domain-specific barriers well. This project defines a span-level annotation protocol for identifying the exact expressions that may block comprehension for a generally literate reader without cybersecurity training.

## What Is Included

- Thresh typology for span-level annotation
- detailed annotation guideline
- pilot Reddit cybersecurity annotation batches
- provenance metadata
- validation script for batch integrity
- validation report for the current pilot data

## Annotation Task

Annotators read cybersecurity discussion text and highlight the shortest meaningful span that may be difficult for a non-expert reader. Each span receives labels for:

- difficulty type
- difficulty level
- required background knowledge
- comprehension burden

The annotation schema targets five difficulty types:

- `technical_jargon`: cybersecurity terms, attacks, vulnerabilities, defenses, and technical concepts
- `community_slang`: informal hacker, piracy, security, or internet-subculture expressions
- `tool_platform`: specific tools, software, protocols, services, websites, or infrastructure providers
- `legal_law`: legal, law-enforcement, criminal procedure, compliance, or prosecution terminology
- `implicit_knowledge`: phrases requiring background inference about security practices, platform behavior, or community norms

## Pilot Dataset

The pilot dataset is derived from a Reddit r/cybersecurity thread discussing internet piracy, hacking, CFAA, platform abuse, and HeheStreams.

Current pilot contents:

- 193 extracted Reddit comment body entries
- 40 approximately character-balanced annotation hits
- 4 JSON batch files with 10 hits each
- stable hit IDs, visible numbering, metadata, and provenance

The data lives in:

```text
data/reddit_cybersecurity_hehe_streams/
```

## Validation

Run validation from the repository root:

```bash
python scripts/validate_reddit_annotation_batches.py
```

The validator checks:

- expected batch count
- expected hit count
- required fields
- metadata fields
- thread IDs
- visible sentence numbering
- continuous numbering from `[1]` through `[193]`

It writes a machine-readable validation report to:

```text
data/reddit_cybersecurity_hehe_streams/validation_report.json
```

## Repository Structure

```text
.
├── README.md
├── annotation_guideline.md
├── templates/
│   └── cyber/
│       └── cyber_reddit_readability_typology.yml
├── data/
│   └── reddit_cybersecurity_hehe_streams/
│       ├── README.md
│       ├── provenance.json
│       ├── reddit_body_part_1_10_hits.json
│       ├── reddit_body_part_2_10_hits.json
│       ├── reddit_body_part_3_10_hits.json
│       ├── reddit_body_part_4_10_hits.json
│       └── validation_report.json
└── scripts/
    └── validate_reddit_annotation_batches.py
```

## Research Use Cases

This repository can support:

- human evaluation of domain-specific readability
- dataset construction for LLM evaluation
- analysis of cybersecurity jargon and implicit knowledge
- comparison between human difficulty judgments and model explanations
- post-training data design for models that explain technical content to non-experts

## Ethics And Release Status

This repository contains raw Reddit comment text in the pilot data. Broader public redistribution should be reviewed against advisor expectations, lab policy, Reddit terms, and applicable research ethics requirements. A sanitized public release could preserve the annotation schema, examples, validation code, and aggregate statistics while keeping raw text private.

## Current Status

The project is a pilot annotation artifact. The next step is to run multi-annotator labeling, measure agreement, analyze disagreement cases, and produce a cleaned dataset card with release constraints.

## Roadmap

- add a dataset card
- add an ethics/release document
- add example completed annotations
- compute inter-annotator agreement
- add aggregate label distribution analysis
- compare human labels against LLM-predicted difficulty spans
- publish a sanitized public sample if raw-text release is restricted
