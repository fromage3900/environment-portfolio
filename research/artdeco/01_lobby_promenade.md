# Study: Art Deco Lobby Promenade (horizontal civic)

**Style:** artdeco  
**Version:** 0.2  
**Sources:** Chrysler Building lobby motifs, Miami Beach Streamline Deco plazas, setback-massing as facade rhythm (not tower spine)

## Motifs

- Stepped geometric facade bays (chevron / ziggurat silhouette in elevation, not a free-standing tower)
- Geometric arabesque filigree screens and metalwork
- Cusped / pointed portal as lobby threshold
- Inclined promenade ramp into the civic court
- Balconette rhythm along the facade wall
- Plaza fountain as monument (replaces obelisk spire)

## Proportions

- Facade height ~3–4× bay width; horizontal chain longer than tall
- Ramp rise modest (gb_rise ≈ 2.5–3.5 m over 8–12 m run)
- Filigree panels as mid-scale ornament, not structural mass

## Rhythms

- Facade → panel wall → filigree → portal → ramp → fountain
- Horizontal civic chain; axis compression preferred over vertical stretch

## Structural rules

- No TOWER / TESSELLATION_TOWER / OBELISK / KEEP / WATCHTOWER / BELL_TOWER in grammar or hero presets
- `corner_tower` compose role maps to `_lib_PILLAR`
- Monument role is fountain, not spire

## Ornament systems

- `FILIGREE_PANEL` with `GEOMETRIC_ARABESQUE`
- Recessed trim on panel walls (`gb_trim_mode: RECESS`)

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| deco_facade_bay | BAROQUE_FACADE | Civic lobby elevation stand-in |
| deco_panel_wall | GB_BRUTALIST_PANEL_WALL | Geometric setback wall |
| deco_filigree | FILIGREE_PANEL | Chevron / geometric screen |
| deco_portal | CUSPED_ARCH | Lobby threshold |
| deco_promenade | GREYBOX_RAMP | Inclined approach |
| deco_court_fountain | PUBLIC_FOUNTAIN | Plaza monument |

## OS hooks

- Genome: `art_deco_lobby_v1`
- Grammar graph: `ART_DECO`
- Compose style: `ART_DECO`
- Transform: `axis_compression`
