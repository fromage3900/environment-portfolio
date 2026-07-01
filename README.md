# BS_GodFile - Universal Environment Art Production Platform

BS_GodFile is a UE 5.8 environment-art production platform for building stylized portfolio work: reusable materials, look-dev stages, PCG scatter standards, procedural world-import contracts, render capture, and website/Figma/ArtStation handoff data.

The project is intentionally split between **platform work** and **art-direction work**. The platform should automate organization, audits, manifests, captures, and repeatable look-dev. Final scene composition, hero asset placement, and SakuraPath art direction remain human-owned.

## Current Focus

- Universal material/look-dev workflow centered on `M_Master_Toon_Universal`, `M_Master_Toon_Landscape_HeightBlend`, and `M_Water_Master_Grand_v6`.
- Generic `L_Template` look-dev stage for material, landscape, water, trimsheet, and PCG proof.
- Portfolio package generation from existing manifests and captures.
- Recursive agent support for documentation, QA, research, capture, and production-loop maintenance.

## Start Here

- [DOC_INDEX.md](DOC_INDEX.md) - documentation map and source-of-truth list.
- [CURRENT_STATE.md](CURRENT_STATE.md) - implemented, partial, broken, planned, and research systems.
- [UNIVERSAL_ENVIRONMENT_PIPELINE.md](UNIVERSAL_ENVIRONMENT_PIPELINE.md) - generic production flow.
- [MATERIAL_LOOKDEV_PIPELINE.md](MATERIAL_LOOKDEV_PIPELINE.md) - material and look-dev workflow.
- [AGENT_OPERATING_MODEL.md](AGENT_OPERATING_MODEL.md) - recursive agent roles and safety lanes.
- [PORTFOLIO_READINESS.md](PORTFOLIO_READINESS.md) - readiness checklist, excluding Sakura art-pass ownership.

## Key Systems

- Material architecture: [MATERIAL_PIPELINE.md](MATERIAL_PIPELINE.md)
- Material review: [MATERIAL_SYSTEM_REVIEW.md](MATERIAL_SYSTEM_REVIEW.md)
- Node tree review: [Docs/MATERIAL_NODE_TREE_REVIEW.md](Docs/MATERIAL_NODE_TREE_REVIEW.md)
- Material integration runbook: [Docs/MATERIAL_INTEGRATION.md](Docs/MATERIAL_INTEGRATION.md)
- Portfolio capture/package audit: [PORTFOLIO_PIPELINE_AUDIT.md](PORTFOLIO_PIPELINE_AUDIT.md)
- Agent ownership: [AGENTS.md](AGENTS.md), [AGENT_BOUNDARIES.md](AGENT_BOUNDARIES.md), [AGENT_OWNERSHIP.md](AGENT_OWNERSHIP.md)

## Generic Package Flow

```text
Material/PCG/world systems
  -> L_Template or neutral test map validation
  -> Saved/Portfolio render and metadata fragments
  -> renders_manifest.json
  -> portfolio_package.json
  -> website / Figma / ArtStation handoff metadata
```

## Hard Boundary

Do not automate final Sakura level art direction. `L_SakuraPath` is a human-owned art pass. The platform may provide capture tools, material manifests, PCG standards, and generic look-dev support, but it should not replace the human composition pass.
