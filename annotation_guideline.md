# Cybersecurity Readability Annotation Guideline

## 1. Overview

This project studies why cybersecurity discussions are difficult for non-expert readers to understand. Many cybersecurity conversations rely on specialized technical language, insider slang, platform-specific references, legal terminology, abbreviations, and implicit background knowledge. These features can create comprehension barriers even when the surrounding sentence appears readable.

The annotation objective is to identify terms, phrases, or expressions that may make cybersecurity-related online discussions harder for a non-expert reader to understand.

This task is inspired by MedReadMe-style human understanding tasks. The goal is to:

- identify difficult terms or expressions;
- understand what makes them difficult;
- measure what kinds of external knowledge are required;
- estimate the comprehension burden created by each span.

Annotators will read Reddit cybersecurity discussion text segmented into annotation hits in Thresh. For each hit, annotators should highlight spans that may be difficult for a non-expert reader and assign labels describing the source and severity of the difficulty.

## 2. Annotation Workflow

Follow this workflow for each annotation hit:

1. Read the full annotation hit.
2. Identify any difficult term, phrase, acronym, abbreviation, platform reference, legal term, slang expression, or implicit knowledge reference.
3. Highlight the minimal meaningful span in Thresh.
4. Assign the appropriate term type, difficulty score, external knowledge labels, and comprehension burden.
5. Add notes if necessary, especially for ambiguous or borderline cases.

Annotate from the perspective of a generally literate internet user who does not have specialized cybersecurity training.

## 3. What Counts As A Difficult Span?

A difficult span is any word, phrase, acronym, abbreviation, shorthand, or expression that may require extra knowledge for a non-expert reader to understand in context.

Annotate spans that involve:

- cybersecurity technical terms;
- community slang;
- platform, software, service, or tool names;
- legal, law-enforcement, or compliance terminology;
- implicit knowledge references;
- abbreviations;
- acronyms;
- domain-specific shorthand.

Examples of spans to annotate:

| Span | Why It May Be Difficult |
|---|---|
| `CFAA` | Requires knowledge of U.S. cybercrime law. |
| `OPSEC` | Cybersecurity/hacker-culture acronym. |
| `RCE` | Technical security abbreviation. |
| `got flagged` | Requires context about detection, moderation, or security systems. |
| `burner` | Insider slang that can mean a disposable account, device, or identity. |
| `Metasploit` | Specific security tool. |

Do not annotate:

- common English words used in their ordinary sense;
- obvious expressions that do not create domain-specific difficulty;
- general internet language unless it has a cybersecurity-specific meaning;
- entire sentences when a shorter span is sufficient;
- words that are merely unusual but not important to understanding the cybersecurity discussion.

Examples of spans usually not to annotate:

| Span | Reason |
|---|---|
| `website` | Common internet term. |
| `password` | Generally understood unless used in a specialized way. |
| `download` | Common internet action. |
| `account` | Common internet term unless tied to a specialized platform or attack context. |

## 4. Term Type Labels

Choose the label that best explains why the span is difficult. If a span plausibly fits more than one category, select the most central reason for difficulty.

### TECHNICAL_JARGON

Specialized cybersecurity terminology, including attacks, vulnerabilities, defenses, security processes, and technical concepts.

Examples:

- `SQL injection`
- `RCE`
- `zero-day`
- `CVE`
- `credential stuffing`
- `hash cracking`

Use this label when understanding the span requires cybersecurity or computer security knowledge.

### COMMUNITY_SLANG

Informal insider slang used in cybersecurity, hacker, piracy, or internet subcultures.

Examples:

- `script kiddie`
- `burner`
- `pwned`
- `skid`
- `doxxed`

Use this label when the expression is informal, community-specific, or culturally loaded.

### TOOL_PLATFORM

Names of tools, software, protocols, services, websites, infrastructure providers, or platforms.

Examples:

- `Tor`
- `Metasploit`
- `Wireshark`
- `Cloudflare`
- `Akamai`
- `Fastly`

Use this label when the reader needs to know what a specific tool, service, or platform is.

### LEGAL_LAW

Legal, law-enforcement, criminal procedure, compliance, or prosecution terminology.

Examples:

- `subpoena`
- `CFAA`
- `indictment`
- `pleaded guilty`
- `wire fraud`
- `restitution`

Use this label when understanding the span requires legal or law-enforcement knowledge.

### IMPLICIT_KNOWLEDGE

References that require contextual background knowledge not explicitly stated in the text.

Examples:

- `got flagged`
- `got burned`
- `OPSEC failure`
- `feature-flagged the account`
- `on brand`

Use this label when the phrase is not simply a named term, but understanding it requires inference about cybersecurity practices, community norms, platform behavior, or prior context.

### Ambiguity Handling

Some spans may fit multiple labels. Use the following guidance:

| Case | Preferred Label |
|---|---|
| Technical acronym also used as legal term, such as `CFAA` | `LEGAL_LAW` |
| Tool name used in an attack context, such as `Metasploit` | `TOOL_PLATFORM` |
| Informal phrase with security meaning, such as `got burned` | `IMPLICIT_KNOWLEDGE` or `COMMUNITY_SLANG`, depending on context |
| Acronym for a security practice, such as `OPSEC` | `TECHNICAL_JARGON` if used technically; `IMPLICIT_KNOWLEDGE` if the difficulty is contextual |

When uncertain, choose the label that best captures what a non-expert would need to learn to understand the passage.

## 5. Difficulty Score

Assign a difficulty score based on how much specialized knowledge is needed to understand the span in context.

| Score | Definition |
|---|---|
| `EASY` | Understandable with general internet literacy. |
| `MEDIUM` | Requires some cybersecurity, legal, platform, or internet-culture knowledge. |
| `HARD` | Requires strong cybersecurity/domain expertise or specialized background knowledge. |

### EASY

Use `EASY` when most internet users could understand the span, even if it is somewhat technical.

Examples:

- `password`
- `VPN`
- `hacked`
- `streaming site`

### MEDIUM

Use `MEDIUM` when the span requires some domain knowledge but could be learned with a short explanation.

Examples:

- `credential stuffing`
- `burner account`
- `Cloudflare`
- `subpoena`
- `got flagged`

### HARD

Use `HARD` when understanding the span requires specialized cybersecurity, legal, platform, or hacker-culture expertise.

Examples:

- `RCE`
- `CVE`
- `OPSEC failure`
- `DRM and CDN abuse`
- `CFAA`
- `illicit digital transmission`

Annotate the difficulty of the span in context, not the difficulty of the entire sentence.

## 6. External Knowledge Requirement

External knowledge labels describe what kind of background knowledge a reader would need. Annotators may choose multiple labels when appropriate.

| Label | Definition | Examples |
|---|---|---|
| `GENERAL_INTERNET` | Basic internet literacy or online communication knowledge. | `account`, `DM`, `streaming`, `link` |
| `CYBERSECURITY` | Security concepts, attacks, defenses, vulnerabilities, or technical cyber knowledge. | `RCE`, `SQL injection`, `credential stuffing` |
| `HACKER_CULTURE` | Insider knowledge from hacking, piracy, security forums, or related internet subcultures. | `script kiddie`, `pwned`, `burner` |
| `LEGAL` | Cyber law, criminal procedure, law enforcement, prosecution, or compliance knowledge. | `CFAA`, `subpoena`, `indictment` |
| `PLATFORM_SPECIFIC` | Knowledge of specific tools, services, websites, software, protocols, or infrastructure providers. | `Tor`, `Metasploit`, `Cloudflare`, `Akamai` |

Examples:

- `CFAA`: `LEGAL`
- `Metasploit`: `CYBERSECURITY`, `PLATFORM_SPECIFIC`
- `script kiddie`: `HACKER_CULTURE`
- `credential stuffing`: `CYBERSECURITY`
- `got flagged`: `GENERAL_INTERNET`, `CYBERSECURITY`, or `PLATFORM_SPECIFIC`, depending on context

## 7. Comprehension Burden

Comprehension burden measures how much the annotated span contributes to the overall difficulty of understanding the passage.

| Burden | Definition |
|---|---|
| `LOW` | Minor disruption. The reader can still understand the main point. |
| `MEDIUM` | Noticeable difficulty. The reader may understand the sentence only partially. |
| `HIGH` | Major obstacle. The span is central to understanding the sentence or passage. |

Examples:

| Span | Context | Burden |
|---|---|---|
| `VPN` | Mentioned casually in a sentence about privacy. | `LOW` |
| `credential stuffing` | Explains how an account was attacked. | `MEDIUM` |
| `CFAA` | Central to explaining a criminal charge. | `HIGH` |
| `RCE` | Central to describing a vulnerability or exploit chain. | `HIGH` |
| `Cloudflare` | Mentioned as one provider among several. | `LOW` or `MEDIUM` |

Consider whether the reader could still understand the main claim without understanding the span.

## 8. Annotation Principles

Use these principles throughout the task:

- Annotate the minimal meaningful span.
- Prefer precision over over-labeling.
- Annotate based on non-expert understanding.
- Focus on comprehension difficulty, not rarity.
- Do not annotate entire sentences unless the whole phrase is necessary.
- Do not annotate a term only because it is interesting.
- When in doubt, ask whether a short definition would help a non-expert understand the passage.

Minimal-span examples:

| Better | Avoid |
|---|---|
| `credential stuffing` | `part of credential stuffing` |
| `CFAA` | `charged under CFAA` |
| `script kiddie` | `looks like a script kiddie` |

## 9. Edge Cases

### Multi-Word Expressions

Annotate the full expression when the phrase carries meaning as a unit.

Examples:

- `SQL injection`
- `credential stuffing`
- `wire fraud`
- `got flagged`
- `script kiddie`

### Nested Terms

If a phrase contains a smaller difficult term, annotate the span that best captures the comprehension barrier.

Example:

- In `CFAA wire fraud charge`, annotate `CFAA` and `wire fraud` separately if both create distinct difficulty.
- In `OPSEC failure`, annotate the full phrase if the meaning depends on the combination.

### Repeated Terms

Annotate repeated terms when they appear in a new context or remain important to understanding the passage. If the same term appears many times in the same hit with the same meaning, annotate the most relevant occurrence unless project instructions say otherwise.

### Sarcasm And Memes

Annotate sarcastic, meme-like, or joking expressions when understanding them requires insider knowledge.

Examples:

- `on brand`
- `skill issue`
- `script kiddie`

If the phrase is merely humorous but easy to understand, do not annotate it.

### Overlapping Spans

Avoid overlapping spans when possible. Prefer the span that best captures the difficulty.

Example:

- For `public PoC exploit`, annotate `PoC` and possibly `exploit` if each creates distinct difficulty.
- Do not annotate `public PoC exploit` as a single span unless the combined phrase is the difficult unit.

### Ambiguous Cases

If a span is borderline, annotate it if:

- a non-expert would likely need external knowledge;
- the term is central to understanding the sentence;
- the phrase has a domain-specific meaning beyond ordinary English.

If uncertainty remains, add a note explaining the ambiguity.

## 10. Quality Control

Annotators should:

- remain consistent across hits;
- use the same label for the same term when context is similar;
- review uncertain cases before final submission;
- document disagreements or borderline examples;
- avoid changing annotation strategy midway through the dataset;
- flag confusing instructions or schema issues for project leads.

Recommended quality-control questions:

- Would a non-expert likely pause at this span?
- What kind of outside knowledge would help?
- Is the selected span minimal but complete?
- Does the label explain the source of difficulty?
- Is the difficulty score based on the span, not the entire passage?

## 11. Final Notes

The purpose of this task is not to mark every unusual word. The purpose is to identify the language features that make cybersecurity discussions harder for non-experts to understand.

Good annotations should help researchers measure where comprehension breaks down, what background knowledge is required, and how much burden specific terms or expressions create. Annotate carefully, consistently, and from the perspective of a reader who is familiar with the internet but not trained in cybersecurity, law enforcement, hacker culture, or platform-specific systems.
