# GPT-5.2 Physics Analysis Prompt Templates

## Purpose

Structured prompts for GPT-5.2 to perform systematic physics document analysis without ad-hoc human decision-making.

---

## Prompt 1: Contradiction Detection

```markdown
You are a physics document analyst with expertise in mathematical physics and Yang-Mills theory.

### Task
Analyze the following synthesis document for internal contradictions.

### Instructions
1. Read the entire document carefully
2. For each claim, check if any other chapter makes a conflicting claim
3. For each contradiction found, provide:
   - Chapter A: [section reference]
   - Claim A: [exact quote]
   - Chapter B: [section reference]  
   - Claim B: [exact quote]
   - Nature of contradiction: [explain why these conflict]
   - Severity: [CRITICAL/MAJOR/MINOR]

### Document
{full_synthesis_document}

### Response Format
Return a structured JSON array of contradictions.
```

---

## Prompt 2: Gap Analysis

```markdown
You are a mathematical physicist reviewing a proof synthesis.

### Task
Identify logical gaps in the argument chain.

### Instructions
1. Trace the logical flow from Chapter 1 to the final conclusion
2. For each step that assumes an unproven claim, document:
   - Location: [chapter.section]
   - Claim being assumed: [quote]
   - What would be needed to prove it: [description]
   - Status: [FRONTIER/TRACTABLE/MISSING]

### Document
{full_synthesis_document}

### Response Format
Return a dependency graph in Mermaid format showing proven vs unproven nodes.
```

---

## Prompt 3: Source Verification

```markdown
You are a rigorous reviewer comparing synthesis claims to source documents.

### Task
Verify that each claim in the synthesis is supported by source documents.

### Instructions
For each major claim:
1. Extract the claim and its stated source
2. Query the RAG system for the source document
3. Compare the synthesis claim to the actual source
4. Rate: [SUPPORTED/EXAGGERATED/UNSUPPORTED/CONTRADICTED]

### Synthesis Document
{synthesis_document}

### Retrieved Sources
{rag_retrieved_chunks}

### Response Format
Verification report with citations.
```

---

## Prompt 4: Redundancy Detection

```markdown
You are a technical editor optimizing a physics document.

### Task
Identify redundant content that could be consolidated.

### Instructions
1. For each chapter, extract the key concepts covered
2. Find chapters with significant concept overlap (>50%)
3. Recommend consolidation strategy

### Document
{full_synthesis_document}

### Response Format
JSON mapping of redundant chapter pairs with overlap percentage.
```

---

## Prompt 5: Mathematical Consistency Check

```markdown
You are a mathematical physicist checking equation consistency.

### Task
Verify that mathematical expressions are used consistently.

### Instructions
1. Extract all named quantities (ρ*, σ_geom, λ*, etc.)
2. For each quantity, find all definitions/uses
3. Flag inconsistencies in:
   - Definition (same symbol, different meaning)
   - Units/dimensions
   - Sign conventions
   - Bounds (quantity claimed > 0 in one place, could be ≤ 0 elsewhere)

### Document
{full_synthesis_document}

### Response Format
Symbol consistency report.
```

---

## Usage

These prompts should be used with:
- **Model:** gpt-5.2-thinking (for complex reasoning)
- **Context:** Full document (up to 400k tokens)
- **Temperature:** 0.1 (for consistency)
- **Output:** Structured JSON or Markdown

---

*Created: 2026-01-18*
