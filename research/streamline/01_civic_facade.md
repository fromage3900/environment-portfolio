# Study: Streamline Moderne Civic Facade

**Style:** streamline / art deco civic  
**Version:** 0.1  
**Sources:** 1930s civic terminals, ocean-liner horizontality, WPA public works

## Motifs

- Long horizontal facade bands (piano nobile as continuous ribbon)
- Soft curved wall corners (ship prow / terminal curve)
- Arcade colonnade as civic porch
- Inclined ramp approach (no tower spine)
- Balcony ribbon as secondary horizontal register
- Round portal as ceremonial gate

## Proportions

- Facade height kept mid-rise (~8–10 m) with wide bay count (5–7)
- Ramp rise ~2.5–3.5 m over 8–10 m run
- Arcade bay width ~3.2 m; balcony depth shallow (~0.8 m)

## Rhythms

- Horizontal civic chain: facade → curve → arcade → ramp → balcony → portal
- Prefer lateral progression over vertical monument stacking
- Corner accents use pillars, never towers / obelisks / keeps

## Structural rules

- Banned arch types in this grammar: TOWER, TESSELLATION_TOWER, BELL_TOWER, WATCHTOWER, OBELISK, KEEP
- Compose `corner_tower` role maps to `_lib_PILLAR` (horizontal civic accent)
- Surreal transform: `axis_compression` (horizontal emphasis)

## Ornament systems

- Recessed trim (`gb_trim_mode: RECESS`) for panel banding
- Geometric filigree optional as secondary accent (not required in spine)
- Stone / AUTO materials; avoid vertical spire ornament

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| streamline_facade | BAROQUE_FACADE | Wide mid-rise civic front |
| streamline_curve | CURVED_WALL | Terminal / prow curve |
| civic_arcade | GB_ROMANESQUE_ARCADE | Porch colonnade |
| approach_ramp | GREYBOX_RAMP | Inclined public approach |
| ribbon_balcony | BALCONY | Horizontal register |
| round_portal | ARCHWAY_ADV | Ceremonial gate |

## OS hooks

- Genome: `streamline_moderne_v1`
- Grammar graph: `STREAMLINE_MODERNE`
- Compose style: `STREAMLINE_MODERNE`
