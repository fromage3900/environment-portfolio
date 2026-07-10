# Study: Mesoamerican pyramid courtyard

**Style:** mesoamerican  
**Version:** 1.0  
**Sources:** Teotihuacan Street of the Dead plaza rhythm; Maya ceremonial court + talud-tablero massing; Aztec sacred precinct approach

## Motifs

- Stepped battered retaining tiers (talud) framing a horizontal ceremonial court
- Broad processional stair as the primary axis — not a tower spine
- Colonnade / pier rhythm along the court edge
- Stone portal threshold into the sacred pool / plaza center

## Proportions

- Retaining batter ~0.08–0.12; 3–5 steps per terrace band
- Ceremonial stair: rise ~0.22 m, run ~0.32 m, width ≥2.4 m
- Arcade bay ~3.2 m wide × ~4.0 m high (stone recess trim)
- Portal clear opening ~2.4 × 2.6 m; fountain court radius ~1.5 m

## Rhythms

- Lower terrace wall → stair ascent → upper terrace → colonnade pier → arcade bay → portal → sacred pool
- Horizontal civic chain; height accumulates via terraces, not vertical tower modules
- Snap alignment along processional axis (WALL / path snaps)

## Structural rules

- Prefer `RETAINING_WALL` + `GREYBOX_STAIR_BLOCK` for massing; no TOWER / OBELISK / KEEP
- Colonnade uses `PILLAR` + `GB_ROMANESQUE_ARCADE` as stand-in stone arcade
- Gate role = `ARCHWAY_ADV` (ROUND); monument/sacred = `PUBLIC_FOUNTAIN` (cenote / pool stand-in)
- Genome `axis_compression` wraps the graph for terrace foreshortening

## Ornament systems

- Stone RECESS trim on arcade and portal
- Batter + step count as primary ornament (massing over filigree)
- Pool tiers as sacred terminus ornament

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| `meso_terrace_wall` | `RETAINING_WALL` | Battered stepped terrace |
| `meso_ceremonial_stair` | `GREYBOX_STAIR_BLOCK` | Processional ascent |
| `meso_colonnade_pier` | `PILLAR` | Court-edge pier |
| `meso_arcade_bay` | `GB_ROMANESQUE_ARCADE` | Stone arcade stand-in |
| `meso_stone_portal` | `ARCHWAY_ADV` | Round ceremonial gate |
| `meso_sacred_pool` | `PUBLIC_FOUNTAIN` | Court centerpiece |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
