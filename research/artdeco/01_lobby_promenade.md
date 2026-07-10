# Study: Art Deco Lobby Promenade (Horizontal Civic)

**Style:** artdeco  
**Version:** 0.2  
**Sources:** 1920s–30s cinema / hotel lobby typology; Chrysler Building lobby plan; Rockefeller Center promenades

## Motifs

- Stepped street facade with geometric setbacks (horizontal reading, not tower spine)
- Chevron / zig-zag filigree screens and metalwork panels
- Cusped or pointed portal as ceremonial threshold
- Balconette rhythm along the promenade wall
- Inclined ramp / grand stair as processional approach (no obelisk / tower terminus)

## Proportions

- Facade bay width ≈ 2.0–2.4 m; height 10–14 m (street wall, not skyscraper shaft)
- Panel wall modules ≈ 8–12 m long × 3.5–4 m high
- Ramp rise ≈ 2.5–3.5 m over 8–10 m run (gentle civic grade)
- Filigree panels ≈ 1.4–1.8 m wide × 2.0–2.4 m tall

## Rhythms

- Facade → panel wall → filigree → portal → balconette → ramp (horizontal civic chain)
- Ornament density peaks at portal and filigree; facade carries structural rhythm
- Avoid vertical monument spines; terminate with ramp / fountain court

## Structural rules

- No TOWER / TESSELLATION_TOWER / OBELISK / KEEP / WATCHTOWER / BELL_TOWER in grammar
- Corner role maps to PILLAR (colonnade pier), not tower
- Prefer `axis_compression` over `vertical_stretch` for lobby promenade genomes

## Ornament systems

- Geometric arabesque / chevron filigree (`FILIGREE_PANEL`, `GEOMETRIC_ARABESQUE`)
- Recessed trim on panel walls (`gb_trim_mode: RECESS`)
- Cusped arch portal as gate role

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| deco_street_facade | BAROQUE_FACADE | Stepped civic facade stand-in |
| deco_panel_wall | GB_BRUTALIST_PANEL_WALL | Geometric panel rhythm |
| deco_chevron_screen | FILIGREE_PANEL | Chevron / geometric arabesque |
| deco_cusped_portal | CUSPED_ARCH | Lobby threshold |
| deco_balconette | BALCONY | Wall rhythm |
| deco_promenade_ramp | GREYBOX_RAMP | Processional approach |

## OS hooks

- Genome: `art_deco_lobby_v1`
- Grammar graph: `ART_DECO`
- Compose style: `ART_DECO`
