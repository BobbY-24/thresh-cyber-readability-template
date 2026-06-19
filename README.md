# Thresh Cybersecurity Reddit Readability Template

Public template files for a Thresh annotation interface.

Annotators can open the shared Thresh link and upload their own JSON annotation file.

## Cybersecurity Reddit Thresh Annotation Pilot

This repository includes a pilot Thresh annotation dataset built from a Reddit r/cybersecurity thread. The dataset contains 193 numbered Reddit comment body entries grouped into 40 balanced annotation hits and split into four JSON batches. It is intended for internal/pilot research on cybersecurity jargon, slang, technical terminology, and domain-specific comprehension.

The dataset lives in `data/reddit_cybersecurity_hehe_streams/`, with provenance documentation and a validation script at `scripts/validate_reddit_annotation_batches.py`.

Important: this repository contains raw Reddit comment text. Public redistribution should be reviewed with the advisor, lab policy, Reddit terms, and applicable research ethics expectations before broader release.

Expected JSON shape:

```json
[
  {
    "id": "comment-1",
    "source": "Comment text to annotate"
  }
]
```
