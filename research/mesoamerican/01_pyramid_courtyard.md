# Study: Mesoamerican Pyramid Courtyard

**Style:** mesoamerican  
**Version:** 0.1  
**Sources:** Teotihuacan Ciudadela / Avenue of the Dead plaza typology; Maya ceremonial plaza + talud-tablero terraces; Mixtec/Zapotec processional courts

## Motifs

- Stepped battered retaining tiers (talud) framing a sunken or raised plaza
- Broad ceremonial stair block as the primary vertical gesture (not a tower spine)
- Upper platform / terrace as sacred terminus
- Stone colonnade / arcade bays along the court edge
- Corbelled or round-headed stone portal into the precinct
- Ritual water basin / sacred pool at court center

## Proportions

- Horizontal civic chain dominates: wall → stair → terrace → colonnade → portal → pool
- Stair rise ~0.20–0.25 m per tread; run ~0.30–0.35 m; width ≥ 2.2 m
- Retaining batter 0.08–0.12; 3–5 terrace steps per wall segment
- Court colonnade bay ~3.0–3.4 m wide, ~4.0 m high

## Rhythms

- Processional approach along the long axis of the plaza
- Alternating solid terrace mass and open arcade bays
- Stair as mid-chain accent; pool as soft terminus (not a vertical monument)

## Structural rules

- No tower spines, obelisks, keeps, or watchtowers in the grammar chain
- Corner markers resolve to pillars / stelae-scale posts, not towers
- Prefer stone material language throughout
- Archway style must use valid Blender enum (`ROMAN`, not `ROUND`)

## Ornament systems

- Low ornament density; massing and batter carry the style
- Recessed greybox trim on arcade modules
- Optional later: talud-tablero panel relief as a dedicated kit

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| `retaining_terrace` | `RETAINING_WALL` | Stepped battered plaza edge |
| `ceremonial_stair` | `GREYBOX_STAIR_BLOCK` | Processional stair mass |
| `court_colonnade` | `GB_ROMANESQUE_ARCADE` | Court-edge arcade bays |
| `stone_portal` | `ARCHWAY_ADV` | Precinct gate (`ROMAN`) |
| `sacred_pool` | `PUBLIC_FOUNTAIN` | Ritual basin terminus |
| `stela_pillar` | `PILLAR` | Corner marker (tower-ban) |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
- Transform: `axis_compression`
