# Next Actions - Universal Environment Platform

## Current Priority

Build the generic material/look-dev spine without touching `L_SakuraPath`.

## Queue

1. Generate material family manifest.
   - Command: `python Content/Python/material_family_manifest_full.py`
   - Output: `Saved/Portfolio/Materials/material_family_manifest.json`
   - Output: `Saved/Portfolio/MaterialPreviews/previews_manifest.json`

2. Aggregate portfolio package.
   - Command: `python Content/Python/portfolio_aggregator.py`
   - Check: `materials[]` is non-empty.

3. Produce generic look-dev capture pass.
   - Target: `L_Template`, not Sakura.
   - Capture: showcase material grid, landscape slab, water plane, trimsheet panel.

4. Add package-to-website handoff adapter.
   - Input: `portfolio_package.json`
   - Output: `_github_deploy/generated/*_config.json`

5. Add agent memory docs.
   - `Docs/AgentMemory/Decisions.md`
   - `Docs/AgentMemory/RejectedIdeas.md`
   - `Docs/AgentMemory/MaterialStandards.md`

## Red-Line Constraints

- Do not edit Sakura level content.
- Do not delete legacy material assets.
- Do not rewrite master material families.
- Do not publish externally without explicit approval.
