# Study: Mughal Charbagh Court

**Style:** mughal  
**Version:** 0.1  
**Sources:** Mughal garden typology (charbagh quadripartite plan); Shalamar / Humayun’s Tomb garden courts; Persian-Islamic water-axis gardens

## Motifs

- Four-fold garden (charbagh) with central hauz / fountain
- Ceremonial horseshoe or cusped portal as court threshold
- Water-channel walks as primary horizontal spine
- Arcade colonnades framing garden quadrants
- Terrace ramps and stair blocks for level changes (no vertical tower spines)

## Proportions

- Portal width ~2.4–2.8 m; arcade bay ~3.2 m
- Corridor / channel walk length 8–12 m between nodes
- Ramp rise modest (1.0–1.5 m) — horizontal civic, not monumental verticality
- Fountain radius ~1.4–1.8 m as court centerpiece

## Rhythms

- Gate → channel corridor → arcade bay → ramp/stair terrace → hauz terminus
- Alternating solid portal and open colonnade
- Bilateral symmetry along the water axis

## Structural rules

- Prefer facades, courts, arcades, stairs, ramps, colonnades
- Banned: TOWER, TESSELLATION_TOWER, BELL_TOWER, WATCHTOWER, OBELISK, KEEP
- Compose `corner_tower` maps to pillar colonnette, never a tower kit

## Ornament systems

- Stone / marble material language
- Recess trim on arcade and corridor greybox modules
- Horseshoe portal as primary gate ornament

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| charbagh_portal | ARCHWAY_ADV | Horseshoe ceremonial gate |
| water_channel_walk | GREYBOX_CORRIDOR | Axial channel corridor |
| garden_arcade | GB_ROMANESQUE_ARCADE | Colonnade bay |
| terrace_ramp | GREYBOX_RAMP | Level change without tower |
| court_stair | GREYBOX_STAIR_BLOCK | Ceremonial ascent |
| hauz_fountain | PUBLIC_FOUNTAIN | Central charbagh basin |

## OS hooks

- Genome: `mughal_charbagh_v1`
- Grammar graph: `MUGHAL_CHARBAGH`
- Compose style: `MUGHAL_CHARBAGH`
- Surreal transform: `axis_compression`
