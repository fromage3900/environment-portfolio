# Study: Mesoamerican Pyramid Courtyard

**Style:** mesoamerican  
**Version:** 1.0  
**Sources:** Teotihuacan Ciudadela / plaza typology; Maya ceremonial court; stepped platform + talud-tablero massing

## Motifs

- Horizontal civic court framed by battered retaining tiers (not a tower spine)
- Ceremonial stair block as sacred ascent into the plaza
- Processional ramp linking lower court to upper platform
- Stone colonnade / arcade along the court edge
- Lintel portal as gate; sacred pool / fountain as court terminus

## Proportions

- Retaining batter ~0.08–0.12; wall thickness 0.55–0.65 m
- Stair block: 10–14 steps, rise ~0.22 m, run ~0.32 m, width ~2.4 m
- Ramp: length 6–8 m, rise ~1.2–1.8 m, width ~2.0 m
- Arcade bay ~3.2 m wide × 4.0 m high
- Portal: lintel / Roman archway ~2.4 × 2.6 m

## Rhythms

- Lower retaining tier → stair ascent → upper retaining platform
- Ramp offset as secondary processional path
- Arcade colonnade frames the court long edge
- Portal gate then sacred pool terminate the chain

## Structural rules

- Prefer `RETAINING_WALL`, `GREYBOX_STAIR_BLOCK`, `GREYBOX_RAMP`, `GB_ROMANESQUE_ARCADE`, `ARCHWAY_ADV`, `PUBLIC_FOUNTAIN`
- **No tower spines** — banned TOWER / TESSELLATION_TOWER / OBELISK / KEEP / WATCHTOWER / BELL_TOWER
- Compose `corner_tower` maps to `_lib_PILLAR` (stele / upright mass, not a tower kit)
- `axis_compression` surreal transform for horizontal civic massing

## Ornament systems

- Retaining: batter face, terrace tread, coping stone
- Stair: tread, riser, stringer, landing
- Arcade: column, arch soffit, entablature
- Portal: lintel, jamb, threshold
- Pool: basin rim, water plane

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| `talud_retaining_tier` | RETAINING_WALL | battered terrace wall |
| `ceremonial_stair` | GREYBOX_STAIR_BLOCK | sacred ascent |
| `processional_ramp` | GREYBOX_RAMP | secondary approach |
| `court_colonnade` | GB_ROMANESQUE_ARCADE | plaza edge arcade |
| `lintel_portal` | ARCHWAY_ADV | court gate |
| `sacred_pool` | PUBLIC_FOUNTAIN | court terminus |

## OS hooks

- Genome: `meso_pyramid_courtyard_v1`
- Grammar graph: `MESOAMERICAN_PYRAMID`
- Compose style: `MESOAMERICAN_PYRAMID`
