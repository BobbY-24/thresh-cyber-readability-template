# Thresh Cybersecurity Reddit Readability Template

Public template files for a Thresh annotation interface.

Annotators can open the shared Thresh link and upload their own JSON annotation file.

## Cybersecurity Reddit Dataset

The `data/reddit_cybersecurity_hehe_streams/` folder contains four Thresh-ready Reddit annotation batches from an r/cybersecurity thread about internet piracy, hacking, CFAA, platform abuse, and HeheStreams.

The source Reddit body entries were numbered [1] through [193], grouped into 40 balanced annotation hits by approximate character count, and split into four JSON files with 10 hits each. Each row includes `id`, `context`, `source`, and `metadata`.

Expected JSON shape:

```json
[
  {
    "id": "comment-1",
    "source": "Comment text to annotate"
  }
]
```
