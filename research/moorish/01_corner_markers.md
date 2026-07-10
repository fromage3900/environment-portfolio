# Study: Moorish Courtyard Corner Markers (Tower Ban)

**Style:** moorish  
**Version:** 0.1  
**Sources:** Alhambra Court of the Lions, Alcázar Seville patios, Maghrebi riads — colonnade courts without minaret / campanile spines in the compose role map

## Motifs

- Horseshoe portal as gate; arcade bays as medium mass
- Arabesque filigree screens; fountain as court terminus
- **Pillar** corner markers (engaged columns / colonnettes) instead of bell towers

## Proportions

- Court is horizontal: arcade height ~4 m, fountain radius ~1.4 m
- Corner pillars match arcade impost height — civic colonnade, not vertical monument

## Rhythms

- Horseshoe gate → arabesque screen → arcade → offset corridor → arcade → fountain
- Corner pillars frame the riad without introducing banned tower arch types

## Structural rules

- **No tower spines** — banned: TOWER, BELL_TOWER, WATCHTOWER, OBELISK, KEEP, TESSELLATION_TOWER
- Compose `corner_tower` role maps to `_lib_PILLAR`

## Ornament systems

- Geometric arabesque filigree carries density; horseshoe arch carries sacred geometry
- Pillar capitals stay simple stone — ornament lives on screens and portals

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| corner_pillar | PILLAR | Tower-ban corner marker |
| horseshoe_gate | ARCHWAY_ADV (HORSESHOE) | Primary portal |
| arcade_bay | GB_ROMANESQUE_ARCADE | Colonnade medium |

## OS hooks

- Genome: `moorish_courtyard_v1`
- Grammar graph: `MOORISH_COURTYARD`
- Compose style: `MOORISH_COURTYARD` (`corner_tower` → `_lib_PILLAR`)
