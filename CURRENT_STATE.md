# Current State - Universal Environment Platform

Status labels: `Implemented`, `Partial`, `Broken`, `Planned`, `Research`, `Deprecated`.

## Ownership Boundary

`L_SakuraPath` art direction, hero composition, set dressing, and final scene polish are human-owned. Japanese/Sakura-themed materials and instances are allowed as reusable platform/look-dev work. This state file tracks the reusable platform around that work.

## Platform Systems

| System | Status | Current Truth | Next Platform Action |
|---|---|---|---|
| Universal master material | Implemented | `M_Master_Toon_Universal` is the central mesh/prop/trimsheet master with many style families. | Keep architecture; audit latest update, parameter metadata, duplicate params, stale refs. |
| Landscape height blend | Implemented | `M_Master_Toon_Landscape_HeightBlend` supports reusable terrain look-dev. | Document generic usage presets and capture requirements. |
| Grand water | Implemented | `M_Water_Master_Grand_v6` is canonical reusable water. | Treat as platform pillar; capture generic pond/shoreline examples in template context. |
| Material instances | Implemented | `MI_Show_*`, `MI_Landscape_*`, `MI_GrandWater_*`, trimsheet, Zen, Baroque families exist. | Generate material family manifest and preview readiness report. |
| Material manifest | Partial | Portfolio schema expects material metadata, but no stable producer existed. | Use `Content/Python/material_family_manifest.py` as the thin contract producer. |
| L_Template look-dev stage | Partial | Template stage exists and is referenced by setup scripts. | Promote as generic look-dev validation stage; avoid Sakura dependency. |
| PCG universal stack | Implemented | Universal and style wrapper PCG graphs are documented and audited. | Keep generic scatter contracts separate from Sakura art pass. |
| Capture/package stack | Implemented | Render exporter, plate compiler, output layout, and aggregator exist. | Add completeness reports and generic material preview inputs. |
| Website deploy lane | Implemented | `_github_deploy/generated` contains generated web artifacts. | Add package-to-website metadata handoff map. |
| Figma/design system | Implemented | Design system and Figma guide are mature. | Connect package schema to design tokens via adapter docs. |
| Recursive agents | Partial | Agent roles, boundaries, and loops exist. | Add Producer, Material TD, Look-Dev Capture roles and autonomy lanes. |

## Known Technical Debt

| Area | Status | Detail |
|---|---|---|
| Universal inline vs MF duplication | Partial | `MATERIAL_SYSTEM_REVIEW.md` flags Nikki/Parallax duplication. |
| Duplicate material params | Partial | Duplicate declarations are tracked in audits; should be reduced cautiously. |
| Archive instance duplication | Partial | `_Archive` mirrors active instance trees in places. Do not delete without explicit approval. |
| Material preview producer | Partial | Existing preview capture was under-wired; manifest producer now supplies metadata, not images. |
| Figma API sync | Planned | Design contract exists; automatic package consumption is not the priority until generic package is stable. |

## Out Of Scope For Automation

- Editing `L_SakuraPath` composition.
- Replacing Sakura hero props.
- Publishing external portfolio updates without approval.
- Broad shader-family redesign.
- Destructive cleanup of legacy assets.
