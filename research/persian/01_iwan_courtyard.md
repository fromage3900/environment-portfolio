# Study: Persian Iwan Courtyard (Chahar Bagh / Four-Iwan Plan)

**Style:** persian  
**Version:** 0.1  
**Sources:** Isfahan Masjed-e Jame‘ / Shah Mosque typology; Timurid–Safavid four-iwan madrasa plans; chahar-bagh garden axes

## Motifs

- Monumental **iwan** — deep pointed portal niche opening onto a sahn (courtyard)
- **Riwaq** arcade colonnade wrapping the court on one or more sides
- Geometric arabesque screens and muqarnas-adjacent filigree as surface ornament
- Axial processional approach (ramp / stair) into the court before the primary iwan
- Central **howz** (pool / fountain) as sacred terminus of the horizontal civic chain

## Proportions

- Iwan portal taller than wide (~1:1.4–1:1.6 height:width), deep enough to read as a room-scale niche
- Arcade bay module ~3.0–3.4 m; hypostyle hall behind iwan on a regular column grid
- Courtyard is the primary volume — horizontal civic, not vertical spine

## Rhythms

1. Processional ramp / approach
2. Pointed iwan portal (gate moment)
3. Arabesque screen bay
4. Riwaq arcade walk
5. Hypostyle / pillar hall depth
6. Fountain court terminus

## Structural rules

- Prefer facades, courts, arcades, stairs/ramps, colonnades — **no tower spines**
- Banned arch types for this grammar: TOWER, TESSELLATION_TOWER, BELL_TOWER, WATCHTOWER, OBELISK, KEEP
- Compose `corner_tower` role remaps to `_lib_PILLAR` (pilaster / free-standing column)

## Ornament systems

- `FILIGREE_PANEL` with `GEOMETRIC_ARABESQUE`
- Pointed `ARCHWAY_ADV` (`GOTHIC` style as Persian pointed-arch stand-in)
- Stone / marble material defaults; recess trim on greybox modules

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| `iwan_portal` | `ARCHWAY_ADV` | Pointed deep portal |
| `riwaq_arcade` | `GB_ROMANESQUE_ARCADE` | Court arcade |
| `arabesque_screen` | `FILIGREE_PANEL` | Geometric arabesque |
| `processional_ramp` | `GREYBOX_RAMP` | Approach axis |
| `hypostyle_hall` | `GREYBOX_PILLAR_HALL` | Behind-iwan hall |
| `howz_fountain` | `PUBLIC_FOUNTAIN` | Sahn terminus |

## OS hooks

- Genome: `persian_iwan_courtyard_v1`
- Grammar graph: `PERSIAN_IWAN`
- Compose style: `PERSIAN_IWAN`
- Transform: `axis_compression`
