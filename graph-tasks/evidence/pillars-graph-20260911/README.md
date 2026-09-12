# Pillars graph integration evidence

- [Task and mathematical consequence](../../2026-09-11-pillars-graph.md).
- [Corrected Gemini review](corrected-review.md).
- [Final validation](validation.json): full run plus three successful post-generation reruns.
- [Fresh mathematical verification](verification-final.json) and [complete output](verify-final.json).
- [Matched saved graph snapshot](end.json) and [registered result records](graph-result-records.json).
- [Conflict preservation](integration-preservation.json).
- `check-full.log` retains the original generated-view timing failures; `pytest-generated-final.log` retains their successful rerun. Interrupted runs are not passes.
- `SHA256SUMS` pins every retained evidence file other than itself.
