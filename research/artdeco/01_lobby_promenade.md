# Study: Art Deco Lobby Promenade

**Style:** artdeco  
**Version:** 0.2  
**Sources:** 1920s–30s civic lobbies, setback-era street fronts, horizontal promenade sequences (not tower spines)

## Motifs

- Stepped facade bays and geometric panel walls
- Chevron / arabesque filigree screens
- Cusped portals as ceremonial thresholds
- Balconettes and colonnade rhythm along the walk
- Inclined ceremonial ramps instead of vertical monuments

## Proportions

- Facade bay height ~2–3× door clear; panel wall runs longer than tall
- Ramp rise modest (civic grade), length >> rise
- Filigree panels as secondary ornament, not structural mass

## Rhythms

- Facade → panel wall → filigree → portal → balcony → ramp
- Horizontal civic chain; avoid tower / obelisk termini

## Structural rules

- No TOWER / TESSELLATION_TOWER / OBELISK / KEEP spines
- Compose `corner_tower` maps to pillar colonnade markers
- Prefer `axis_compression` over `vertical_stretch`

## Ornament systems

- Geometric arabesque filigree density mid–high
- Recessed trim on panel walls

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| deco_facade_bay | BAROQUE_FACADE | Stepped civic front |
| deco_panel_wall | GB_BRUTALIST_PANEL_WALL | Geometric cladding run |
| deco_chevron_screen | FILIGREE_PANEL | Chevron / arabesque |
| deco_cusped_portal | CUSPED_ARCH | Lobby threshold |
| deco_balconette | BALCONY | Mid-level overlook |
| deco_ceremonial_ramp | GREYBOX_RAMP | Horizontal ascent |

## OS hooks

- Genome: `art_deco_lobby_v1`
- Grammar graph: `ART_DECO`
- Compose style: `ART_DECO`
