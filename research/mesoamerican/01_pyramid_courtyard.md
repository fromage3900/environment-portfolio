# Study: Mesoamerican Pyramid Courtyard

**Style:** mesoamerican  
**Version:** 0.1  
**Sources:** Teotihuacan Avenue of the Dead processional courts; Maya plaza–pyramid compounds; Aztec ceremonial precinct typology

## Motifs

- Stepped battered retaining terraces (talud) framing a horizontal court
- Broad ceremonial stair block as the primary ascent — not a tower spine
- Processional ramp / side approach for secondary circulation
- Stone colonnade / arcade along the court edge
- Low stone portal (lintel / round arch) into the sacred precinct
- Sacred pool / fountain as court terminus (cenote / ritual basin stand-in)

## Proportions

- Horizontal civic chain preferred over vertical monument spines
- Stair rise ~0.20–0.24 m; run ~0.30–0.35 m; width ≥2.2 m for ceremonial reading
- Retaining batter 0.08–0.12; wall thickness 0.5–0.7 m
- Court modules spaced for plaza reading, not keep/tower stacking

## Rhythms

1. Retaining terrace (base platform)
2. Ceremonial stair block (ascent)
3. Processional ramp (side approach)
4. Colonnade / arcade (court edge)
5. Stone portal (threshold)
6. Sacred pool (terminus)

## Structural rules

- **No tower spines** — banned TOWER / TESSELLATION_TOWER / BELL_TOWER / WATCHTOWER / OBELISK / KEEP
- Corner markers resolve to pillars / colonnade posts, not watchtowers
- Compose style stamps `meso_pyramid_courtyard_v1` with `axis_compression`

## Ornament systems

- Stone material default; recess trim on arcade bays
- Minimal cosmic ornament — structural massing carries the style

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| `meso_retaining_terrace` | `RETAINING_WALL` | Battered talud terrace |
| `meso_ceremonial_stair` | `GREYBOX_STAIR_BLOCK` | Broad processional stair |
| `meso_processional_ramp` | `GREYBOX_RAMP` | Side approach ramp |
| `meso_court_colonnade` | `GB_ROMANESQUE_ARCADE` | Court-edge arcade stand-in |
| `meso_stone_portal` | `ARCHWAY_ADV` | ROMAN / lintel portal |
| `meso_sacred_pool` | `PUBLIC_FOUNTAIN` | Ritual basin terminus |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
