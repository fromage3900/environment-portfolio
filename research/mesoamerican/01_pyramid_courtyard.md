# Study: Mesoamerican Pyramid Courtyard

**Style:** mesoamerican  
**Version:** 0.1  
**Sources:** Teotihuacan Avenue of the Dead; Maya civic plazas; talud-tablero platform grammar

## Motifs

- Stepped talud retaining tiers framing a ceremonial court
- Processional stair + ramp approaches (no vertical tower spine)
- Lintel portals and colonnade bays along the plaza edge
- Sacred pool / cenote stand-in at court terminus

## Proportions

- Horizontal civic chain preferred over vertical monument spines
- Stair rise ~0.22 m / run ~0.32 m; ramp length ≥ stair width × 3
- Colonnade bays ~3.2 m; lintel portal ~2.4 × 2.6 m

## Rhythms

- Retain → ascend (stair) → process (ramp) → colonnade → lintel gate → sacred pool
- Bilateral symmetry along the processional axis

## Structural rules

- No TOWER / OBELISK / KEEP / WATCHTOWER modules
- Corner accents resolve to PILLAR (not corner towers)
- Stone material default; recess trim on arcade bays

## Ornament systems

- Batter on retaining faces; plain lintel heads; arcade colonettes

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| talud_tier | RETAINING_WALL | Batter + stepped face |
| ceremonial_stair | GREYBOX_STAIR_BLOCK | Processional ascent |
| processional_ramp | GREYBOX_RAMP | Horizontal civic climb |
| court_colonnade | GB_ROMANESQUE_ARCADE | Plaza edge arcade |
| lintel_portal | ARCHWAY_ADV (LINTEL) | Maya-style flat head |
| sacred_pool | PUBLIC_FOUNTAIN | Court terminus |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
