# Study: Art Nouveau Corner Markers (Tower Ban)

**Style:** art_nouveau  
**Version:** 0.1  
**Sources:** Horta townhouses (Brussels), Guimard Métro canopies, Mackintosh Glasgow School — street-facing civic walks without campanile spines

## Motifs

- Whiplash ironwork and ogee portals as primary vertical accents
- Fluted or vine-wrapped **pillars** at plot corners instead of bell towers
- Balcony + filigree rail as mid-height rhythm; facade bay as large mass

## Proportions

- Corner marker height ≈ piano-nobile + attic (pillar ~4 m), not campanile scale
- Horizontal facade walk dominates; verticality expressed in ogee swell, not tower shafts

## Rhythms

- Gate (ogee) → filigree panel → balcony → rail inset → facade bay → arabesque panel
- Corner markers bookend the walk as colonnette pairs, not free-standing towers

## Structural rules

- **No tower spines** — banned: TOWER, BELL_TOWER, WATCHTOWER, OBELISK, KEEP, TESSELLATION_TOWER
- Compose `corner_tower` role maps to `_lib_PILLAR` (classical column / capital)

## Ornament systems

- Filigree vine / geometric arabesque panels carry ornament density
- Pillar flutes echo ironwork density without adding banned arch types

## Extracted atoms

| Atom ID | Kit / part | Notes |
|---------|------------|-------|
| corner_pillar | PILLAR | Tower-ban corner marker |
| ogee_gate | OGEE_ARCH | Primary portal |
| filigree_panel | FILIGREE_PANEL | Ornament screen |

## OS hooks

- Genome: `art_nouveau_v1`
- Grammar graph: `ART_NOUVEAU`
- Compose style: `ART_NOUVEAU` (`corner_tower` → `_lib_PILLAR`)
