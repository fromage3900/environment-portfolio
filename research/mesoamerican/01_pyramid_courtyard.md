# Study: Mesoamerican Pyramid Courtyard

**Style:** mesoamerican  
**Version:** 0.1  
**Sources:** Teotihuacan Street of the Dead / Ciudadela plaza typology; Maya ceremonial court + processional stair; Aztec temple-platform batter walls

## Motifs

- Stepped battered retaining terraces (talud) framing a sunken or raised court
- Broad ceremonial stair block as the sacred ascent (not a tower spine)
- Processional ramp flanking the stair for horizontal civic flow
- Colonnade / arcade bays along the plaza edge
- Stone portal threshold into the upper platform
- Central sacred pool / basin as court monument

## Proportions

- Terrace batter ~0.08–0.12; wall thickness heavy relative to height
- Stair: many shallow risers (rise ~0.22, run ~0.32), wide frontage
- Ramp: long run, modest rise — horizontal civic chain preference
- Arcade bay width ~3.2 m; portal ~2.4 × 2.6 m

## Rhythms

- Terrace → stair → ramp → arcade → portal → pool (processional sequence)
- Bilateral symmetry along the court axis; ornament denser at portal and pool
- Horizontal layering over vertical monumentality

## Structural rules

- No tower / obelisk / keep spines — corner markers are pillars or battered piers
- Retaining walls carry terrain seams; stairs and ramps carry circulation
- Sacred role maps to the ceremonial stair block (ascent), not a vertical tower

## Ornament systems

- Recessed stone trim on arcade and portal
- Geometric batter steps read as ornament at distance
- Pool basin as reflective court centerpiece

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| meso_terrace_batter | RETAINING_WALL | Stepped talud terrace |
| meso_ceremonial_stair | GREYBOX_STAIR_BLOCK | Sacred ascent |
| meso_processional_ramp | GREYBOX_RAMP | Horizontal civic approach |
| meso_plaza_arcade | GB_ROMANESQUE_ARCADE | Court colonnade stand-in |
| meso_stone_portal | ARCHWAY_ADV | Upper-platform threshold |
| meso_sacred_pool | PUBLIC_FOUNTAIN | Court basin / cenote stand-in |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
- Transform: `axis_compression`
